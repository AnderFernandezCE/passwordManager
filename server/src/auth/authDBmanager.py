from src.database import fetch_one,fetch_one_columns, insert_one
from sqlalchemy import select, insert
from src.models import Users
from src.auth.schemas import UserEntity

class AuthDBmanager():
  def __init__(self) -> None:
    pass

  async def user_exists(self, email) -> bool:
    user = await fetch_one(select(Users).where(Users.email == email))
    if user:
      return True
    return False
  
  async def register_user(self, user:UserEntity):
    try:
      await insert_one(insert(Users).values(
        username=user.username, 
        email = user.email, 
        userhash=user.userhash, 
        key=user.key, 
        publicKey="",
        salt= user.salt
        )
      )
      return True
    except Exception as e:
      raise e
    
  async def get_verification_token(self, email):
    try:
      token = await fetch_one_columns(select(
        Users.verification_token,
        Users.expires_at).where(Users.email == email))
      return token
    except Exception as e:
      print(e)
      raise e