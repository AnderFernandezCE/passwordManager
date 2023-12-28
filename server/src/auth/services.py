from src.auth.authDBmanager import AuthDBmanager

authmanager = AuthDBmanager()

async def user_exists(email):
  return await authmanager.user_exists(email)