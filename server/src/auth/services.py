from src.auth.authDBmanager import AuthDBmanager
from src.auth import encryptionmanager
from src.auth.schemas import RegisterRequest, UserRequest, UserEntity

authmanager = AuthDBmanager()

async def user_exists(email):
  return await authmanager.user_exists(email)

async def register_user(user: UserRequest):
  user = complete_user_data(user)
  return await authmanager.register_user(user)

def complete_user_data(user: UserRequest):
  new_user = format_register_user(user)
  #todo - fulfill user data with publickey - privateKey - salt...
  #step 1 generate salt
  print(new_user)
  new_user = add_salt_register_user(new_user)
  print(new_user)
  #step 2 kdf - new hash master password 
  new_user = update_userhash_register_user(new_user, user.hash_master_password )
  return UserEntity(**new_user)

def format_register_user(user: UserRequest):
  new_user = user.dict()
  new_user.pop('hash_master_password')
  return new_user

def add_salt_register_user(user: UserEntity):
  salt = encryptionmanager.generate_salt()
  user['salt'] = salt
  return user

def update_userhash_register_user(user: UserEntity, old_hash):
  new_userhash = encryptionmanager.derive_userhash(old_hash, user.salt)
  user['userhash'] = new_userhash
  return user