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
from src.exceptions import Unauthorized
from src.auth.refresh_token import  is_access_token_valid

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def valid_user_token(token: str = Depends(oauth2_scheme)):
  # Replace this with your actual token validation logic
  sub_token = is_access_token_valid(token)
  if not sub_token:
      raise Unauthorized()
  return sub_token
