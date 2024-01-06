from typing import Mapping
from src.auth import services
import src.auth.verification_token as verificate_token_manager
from src.auth.schemas import RegisterRequest
from src.auth.exceptions import UserExists, InvalidToken, ExpiredVerificationToken, UserNotExists, AccountVerified
import datetime

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
  
  expired = True if token.expires_at < datetime.datetime.utcnow() else False
  if expired:
    raise ExpiredVerificationToken()
  
  existingUser = await services.get_user_by_email(token.email)
  if existingUser is None:
    raise UserNotExists()
  return existingUser.UUID