from src.auth.authDBmanager import AuthDBmanager
from src.auth import encryptionmanager
import src.auth.verification_token as verification_token
from src.auth.schemas import RegisterRequest, UserRequest, UserEntity

authmanager = AuthDBmanager()

async def get_user_by_email(email):
  return await authmanager.get_user_by_email(email)


############# REGISTER FUNCTIONS ####################
async def register_user(user: UserRequest):
  try:
    #format user
    user:UserEntity = complete_user_data(user)
    #insert user in db
    await authmanager.register_user(user)
    # send verification token to email
    await verification_token.send_verification_token(user.email)
    return #new user registered response
  except Exception as e:
    print(e)
    raise e

def complete_user_data(user: UserRequest) -> UserEntity: 
  """Fulfills user data with publickey - privateKey - salt..."""
  user_formatted = format_register_user(user)
  
  #step 1 generate salt 
  user_formatted = add_salt_register_user(user_formatted)
  #step 2 kdf - new hash master password 
  user_formatted = update_userhash_register_user(user_formatted, user.hash_master_password )
  return UserEntity(**user_formatted)

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

############# ACCOUNT VERIFICATION TOKEN FUNCTIONS ####################
async def verificate_user_account(uuid):
  await authmanager.verificate_user_account(uuid)
