from src.auth.authDBmanager import AuthDBmanager
from src.auth import encryptionmanager
from src.auth.schemas import RegisterRequest, UserRequest, UserEntity

authmanager = AuthDBmanager()

async def user_exists(email):
  return await authmanager.user_exists(email)


############# REGISTER FUNCTIONS ####################
async def register_user(user: UserRequest):
  user:UserEntity = complete_user_data(user)
  return await authmanager.register_user(user)

def complete_user_data(user: UserRequest) -> UserEntity: 
  """Fulfills user data with publickey - privateKey - salt..."""
  user_formated = format_register_user(user)
  
  #step 1 generate salt and 
  user_formated = add_salt_register_user(user_formated)
  #step 2 kdf - new hash master password 
  user_formated = update_userhash_register_user(user_formated, user.hash_master_password )
  return UserEntity(**user_formated)

def format_register_user(user: UserRequest):
  new_user = user.dict()
  new_user.pop('hash_master_password')
  return new_user

def add_salt_register_user(user: UserEntity):
  salt = encryptionmanager.generate_salt()
  user['salt'] = salt
  return user

def update_userhash_register_user(user: UserEntity, old_hash):
  new_userhash = encryptionmanager.derive_userhash(old_hash, user['salt'])
  user['userhash'] = new_userhash
  return user

############# LOGIN FUNCTIONS ####################