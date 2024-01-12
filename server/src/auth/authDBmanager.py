from src.database import fetch_one,fetch_one_columns, insert_update_delete_one
from sqlalchemy import select, insert, update, delete
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
  
  async def get_user_by_email(self, email) -> Users:
    return await fetch_one(select(Users).where(Users.email == email))
  
  async def register_user(self, user:UserEntity) -> None:
    try:
      await insert_update_delete_one(insert(Users).values(
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
  
  async def unregister_user(self, user:UserEntity) -> None:
    try:
      await insert_update_delete_one(delete(Users).where(Users.email == user.email)
      )
      return True
    except Exception as e:
      raise e
    
  async def get_verification_token_by_email(self, email):
    try:
      token = await fetch_one_columns(select(
        Users.email,
        Users.verification_token,
        Users.expires_at,
        Users.verified).where(Users.email == email))
      return token
    except Exception as e:
      print(e)
      raise e
    
  async def get_verification_token_by_token(self, token):
    try:
      token = await fetch_one_columns(select(
        Users.email,
        Users.verification_token,
        Users.expires_at,
        Users.verified).where(Users.verification_token == token))
      return token
    except Exception as e:
      print(e)
      raise e
    
  async def verificate_user_account(self, uuid):
    try:
      await insert_update_delete_one(update(Users).where(Users.UUID == uuid).values(verified=True))
    except Exception as e:
      print(e)
      raise e