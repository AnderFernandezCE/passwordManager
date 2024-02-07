from src.vault.schemas import PasswordsResponse, CipherData
from src.vault.vaultDBmanager import VaultDBmanager
from datetime import date, datetime

vault_manager = VaultDBmanager()

async def get_passwords(user_token):
  items = await vault_manager.get_all_items(user_token)
  print(items)
  response = {"user_id": user_token,
              "user_data": {}}
  if items is None:
    return response
  for item in items:
    data = CipherData.from_dict(item)
    response["user_data"][item.get("id")] = data
  return response  

async def create_item(item, user_token):
  item = await vault_manager.create_item(item.name, item.data, user_token)
  item = CipherData(name=item.name,
                    id=item.id,
                    created_at=item.created_at.date(),
                    updated_at=item.updated_at.date(),
                    data=item.data)
  return item

async def update_item(item):
  updated_data = {key: value for key, value in item.dict().items() if value is not None}
  item = await vault_manager.update_item(item.id, updated_data, datetime.now())
  item = CipherData(name=item.name,
                    id=item.id,
                    created_at=item.created_at.date(),
                    updated_at=item.updated_at.date(),
                    data=item.data)
  return item