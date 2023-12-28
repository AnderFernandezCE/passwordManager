from typing import Mapping
from src.auth import services
from src.auth.schemas import RegisterRequest
from src.auth.exceptions import UserExists

async def valid_register_user(user_request: RegisterRequest) -> RegisterRequest:
  #check email exists
  if await services.user_exists(user_request.user.email):
    raise UserExists()
  #check email valid? NO IN THE SCHEMA
  #check anything more?
  return user_request