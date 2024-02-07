from src.database import fetch_one,fetch_one_columns, insert_update_delete_one, fetch_all, fetch_all_columns
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
  
  async def update_item(self, id, updated_data, updated_at) -> Vault:
    await insert_update_delete_one(update(Vault).where(Vault.id == id).values(updated_at = updated_at,**updated_data))
    item = await fetch_one(select(Vault).where(Vault.id == id))
    if item:
      return item
    return None
  
  async def get_all_items(self, user_uuid) -> Vault:
    item = await fetch_all_columns(select(Vault.id, Vault.created_at, Vault.updated_at, Vault.name, Vault.data).where(Vault.user_id == user_uuid))
    if item:
      return item
    return None
  
