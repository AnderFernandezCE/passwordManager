from src.database import fetch_one,fetch_one_columns, insert_update_delete_one
from sqlalchemy import select, insert, update, delete
from src.models import Users, AuthRequests
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
      await insert_update_delete_one(insert(Users).values(**user.dict()
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
    
  async def renew_verification_token(self, email, token,expiration_time ):
    try:
      await insert_update_delete_one(update(Users).where(Users.email == email).values(verification_token=token, expires_at=expiration_time))
    except Exception as e:
      print(e)
      raise e
    
  async def renew_refresh_token(self, token, uuid, expiration_datetime):
    try:
      await insert_update_delete_one(insert(AuthRequests).values(jwt=token, userID = uuid ,expires_at=expiration_datetime, valid=True))
    except Exception as e:
      print(e)
      raise e
    
  async def delete_existing_refreshtoken(self, uuid):
    try:
      await insert_update_delete_one(delete(AuthRequests).where(AuthRequests.userID == uuid))
    except Exception as e:
      print(e)
      raise e
    
  async def delete_refreshtoken(self, jwt):
    try:
      await insert_update_delete_one(delete(AuthRequests).where(AuthRequests.jwt == jwt))
    except Exception as e:
      print(e)
      raise e
    
  async def get_refreshtoken_by_token(self, jwt) -> AuthRequests:
    try:
      token = await fetch_one(select(AuthRequests).where(AuthRequests.jwt == jwt))
      return  token
    except Exception as e:
      print(e)
      raise e