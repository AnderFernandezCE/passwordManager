from jose import jwt
from src.auth.authDBmanager import AuthDBmanager
import datetime
from pathlib import Path
import pytz

#refresh token 
private_key_path = Path(__file__).resolve().parent / "auth_server_keys" / "private.pem"
public_key_path = Path(__file__).resolve().parent / "auth_server_keys" / "public.pem"
private_key = open(private_key_path).read()
public_key = open(public_key_path).read()
#access token
access_private_key_path = Path(__file__).resolve().parent / "auth_server_keys" / "access_token_private.pem"
access_public_key_path = Path(__file__).resolve().parent / "auth_server_keys" / "access_token_public.pem"
access_private_key = open(access_private_key_path).read()
access_public_key = open(access_public_key_path).read()
authmanager = AuthDBmanager()


ALGORITHM = "RS256"


def generate_refresh_token(uuid):
  to_encode ={"exp": new_expire_time(),
              "sub": uuid}  
  encoded_jwt = jwt.encode(to_encode, private_key, algorithm=ALGORITHM)
  return encoded_jwt

def new_expire_time():
  current_time = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
  expiration_time = current_time + datetime.timedelta(days=1)
  return expiration_time

def new_access_expire_time():
  current_time = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
  expiration_time = current_time + datetime.timedelta(minutes=5)
  return expiration_time

def get_expiration_datetime(token):
  expiration_datetime = jwt.get_unverified_claims(token).get('exp')
  return datetime.datetime.fromtimestamp(expiration_datetime)

def get_uuid_token(token):
  uuid = jwt.get_unverified_claims(token).get('sub')
  return uuid

async def update_db(token):
  expiration_datetime = get_expiration_datetime(token)
  uuid = get_uuid_token(token)
  await authmanager.renew_refresh_token(token, uuid, expiration_datetime)

async def delete_existing_refreshtoken(uuid):
  await authmanager.delete_existing_refreshtoken(uuid)

async def revoke_token(token):
  await authmanager.delete_refreshtoken(token)

def is_token_valid(token):
  try:
    decoded_token = jwt.decode(token, public_key, algorithms=ALGORITHM)
    token_expiration = decoded_token.get('exp')
    time = datetime.datetime.fromtimestamp(token_expiration)
    if datetime.datetime.now() < time:
      return True  
    return False
  except Exception as e:
    return False  # Token has expired
  
async def is_active_token(token):
  db_token = await authmanager.get_refreshtoken_by_token(token)
  if not db_token:
    return False
  if not db_token.valid:
    return False
  return True

def generate_access_token(token):
  sub = jwt.get_unverified_claims(token).get('sub')
  to_encode ={"exp": new_access_expire_time(),
              "sub": sub}  
  encoded_jwt = jwt.encode(to_encode, access_private_key, algorithm=ALGORITHM)
  return encoded_jwt


def is_access_token_valid(token):
  try:
    decoded_token = jwt.decode(token, access_public_key, algorithms=ALGORITHM)
    token_expiration = decoded_token.get('exp')
    time = datetime.datetime.fromtimestamp(token_expiration)
    if datetime.datetime.now() < time:
      return decoded_token.get('sub')  
    return False
  except Exception as e:
    return False  # Token has expired
