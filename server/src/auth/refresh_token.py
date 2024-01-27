from jose import jwt
from src.auth.authDBmanager import AuthDBmanager
import datetime
from pathlib import Path

private_key_path = Path(__file__).resolve().parent / "auth_server_keys" / "private.pem"
private_key = open(private_key_path).read()
authmanager = AuthDBmanager()

# public_key = open('public.pem').read()
ALGORITHM = "RS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def generate_refresh_token(uuid):
  to_encode ={"exp": new_expire_time(),
              "sub": uuid}  
  encoded_jwt = jwt.encode(to_encode, private_key, algorithm=ALGORITHM)
  return encoded_jwt

def new_expire_time():
  return datetime.datetime.now() + datetime.timedelta(days=1, hours=0)

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