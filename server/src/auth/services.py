from src.auth.authDBmanager import AuthDBmanager
from src.auth import encryptionmanager
from src.auth import usermanager
from src.auth import refresh_token as refresh_token_service
import src.auth.verification_token as verification_token
from src.auth.schemas import RegisterRequest, UserRequest, UserEntity
from src.exceptions import ServerError

authmanager = AuthDBmanager()

async def get_user_by_email(email):
  return await authmanager.get_user_by_email(email)


############# REGISTER FUNCTIONS ####################
async def register_user(user: UserRequest):
  user_registered = False
  try: # rollback registered user in case token email failed
    #format user
    user:UserEntity = usermanager.complete_user_data(user)
    
    #insert user in db
    await authmanager.register_user(user)
    user_registered = True

    # send verification token to email
    await verification_token.send_verification_token(user.email)
    return #new user registered response
  except Exception as e:
    print(e)
    if user_registered:
      # Rollback user registration
      await authmanager.unregister_user(user)
    raise ServerError()

############# LOGIN FUNCTIONS ####################
async def generate_refresh_token(uuid):
  # await authmanager.verificate_user_account(uuid)
  try:
    await refresh_token_service.delete_existing_refreshtoken(uuid)
    refresh_token = refresh_token_service.generate_refresh_token(uuid)
    await refresh_token_service.update_db(refresh_token)
    return refresh_token
  except Exception as e:
    print(e)
    raise ServerError()

############# ACCOUNT VERIFICATION TOKEN FUNCTIONS ####################
async def verificate_user_account(uuid):
  await authmanager.verificate_user_account(uuid)

#############  TOKEN FUNCTIONS ####################
async def  revoke_token(token):
  await refresh_token_service.revoke_token(token)

def generate_access_token(token):
  return refresh_token_service.generate_access_token(token)