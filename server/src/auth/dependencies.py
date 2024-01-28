from typing import Mapping
from src.auth import services
from src.auth import encryptionmanager
import src.auth.refresh_token as refresh_token_service
import src.auth.verification_token as verificate_token_manager
from src.auth.schemas import RegisterRequest, LoginRequest, UserLoginResponse
from src.auth.exceptions import UserExists, InvalidToken, ExpiredVerificationToken, UserNotExists, AccountVerified, InvalidCredentials, EmailNotVerified, InvalidRefreshToken
import datetime
from fastapi import  Depends
from fastapi.security import OAuth2PasswordBearer

async def valid_register_user(user_request: RegisterRequest) -> RegisterRequest:
  #check email exists
  user = await services.get_user_by_email(user_request.user.email)
  if user is not None:
    raise UserExists()
  #check anything more?
  return user_request

async def valid_verification_token(token):
  token = await verificate_token_manager.get_verificationtoken_by_token(token)
  if token is None:
    raise InvalidToken()
  
  if token.verified:
    raise AccountVerified()
  
  expired = True if token.expires_at < datetime.datetime.now() else False
  if expired:
    raise ExpiredVerificationToken()
  
  existingUser = await services.get_user_by_email(token.email)
  if existingUser is None:
    raise UserNotExists()
  return existingUser.UUID

async def valid_login_user(user_request: LoginRequest) -> UserLoginResponse:
  user = await services.get_user_by_email(user_request.email)
  if user is None:
    raise UserNotExists()
  
  if not user.verified:
    if user.expires_at < datetime.datetime.utcnow():
      await verificate_token_manager.send_verification_token(user.email)
    raise EmailNotVerified()
  
  derived_hash = encryptionmanager.derive_userhash(user_request.userhash, user.salt)
  if not derived_hash  == user.userhash:
    raise InvalidCredentials()
  
  return UserLoginResponse(
        uuid = user.UUID,
        username= user.username,
        email= user.email,
        # userhash: str  maybe for token auth?
        protectedkey= user.key,
        refresh_token=""
    )

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def is_token_valid(token: str = Depends(oauth2_scheme)):
  valid = refresh_token_service.is_token_valid(token)
  if valid:
    return token
  else:
    raise InvalidRefreshToken()
  
async def is_token_valid_db(token: str = Depends(oauth2_scheme)):
  valid = refresh_token_service.is_token_valid(token)
  if not valid:
    raise InvalidRefreshToken()
  active = refresh_token_service.is_active_token(token)
  if not active:
    raise InvalidRefreshToken()
  return token
