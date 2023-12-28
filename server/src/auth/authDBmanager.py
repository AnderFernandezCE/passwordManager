from src.database import fetch_one, insert_one
from sqlalchemy import select, insert
from sqlalchemy import UUID
from src.models import Users

class AuthDBmanager():
  def __init__(self) -> None:
    pass

  async def user_exists(self, email) -> bool:
    user = await fetch_one(select(Users).where(Users.email == email))
    if user:
      return True
    return False
  
  async def register_user(self, user):
    try:
      inserted = await insert_one(insert(Users).values(UUID=UUID(as_uuid=True), username=user.username, email = user.email, userhash=user.hash_master_password, key=user.key))
      return True
    except Exception as e:
      print(e)
      return False