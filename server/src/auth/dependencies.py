from typing import Mapping
from src.auth import services
from src.auth.schemas import RegisterRequest
from src.auth.exceptions import UserExists

async def valid_register_user(user_request: RegisterRequest) -> bool:
  #check email exists
  if await user_exists(user_request.user.email):
    raise UserExists()
  #check email valid? NO IN THE SCHEMA
  #check

async def user_exists(user_request: RegisterRequest) -> bool:
  user =  await services.user_exists(user_request.user.email)
  if user:
      # raise UserExists()
      return True

  return False