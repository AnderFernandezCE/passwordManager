from src.vault.schemas import PasswordsResponse, CipherData
from src.vault.vaultDBmanager import VaultDBmanager
from datetime import date

vault_manager = VaultDBmanager()

async def get_passwords(user_token):

  return {user_token: {}}

async def create_item(item, user_token):
  item = await vault_manager.create_item(item.name, item.data, user_token)
  item = CipherData(name=item.name,
                    id=item.id,
                    created_at=item.created_at.date(),
                    updated_at=item.updated_at.date(),
                    data=item.data)
  return item