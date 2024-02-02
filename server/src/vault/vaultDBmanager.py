from src.database import fetch_one,fetch_one_columns, insert_update_delete_one
from sqlalchemy import select, insert, update, delete, desc
from src.models import Users, Vault
from src.auth.schemas import UserEntity

class VaultDBmanager():
  def __init__(self) -> None:
    pass

  async def create_item(self, name, data, user_uuid) -> Vault:
    await insert_update_delete_one(insert(Vault).values(user_id = user_uuid, name=name, data = data))
    item = await fetch_one(select(Vault).order_by(desc(Vault.created_at)))
    if item:
      return item
    return None