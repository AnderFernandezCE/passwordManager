from src.auth.authDBmanager import AuthDBmanager
from src.auth.schemas import RegisterRequest, UserRequest

authmanager = AuthDBmanager()

async def user_exists(email):
  return await authmanager.user_exists(email)

async def register_user(user: UserRequest):
  #todo - fulfill user data with publickey - privateKey - salt...
  return await authmanager.register_user(user)