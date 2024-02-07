from src.vault.vaultDBmanager import VaultDBmanager
from fastapi import  Depends
from fastapi.security import OAuth2PasswordBearer
from src.exceptions import Unauthorized
from src.vault.exceptions import ItemNotFound
from src.auth.refresh_token import  is_access_token_valid
from src.vault.schemas import UpdateDataRequest , DeleteRequest

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
vault_manager = VaultDBmanager()

async def valid_user_token(token: str = Depends(oauth2_scheme)):
  # Replace this with your actual token validation logic
  sub_token = is_access_token_valid(token)
  if not sub_token:
      raise Unauthorized()
  return sub_token

async def valid_item(item: UpdateDataRequest | DeleteRequest ) :
  # Replace this with your actual token validation logic
  exists = await vault_manager.exists_item(item.id)
  if not exists:
      raise ItemNotFound()
  return item