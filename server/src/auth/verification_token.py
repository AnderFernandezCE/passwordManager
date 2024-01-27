from src.auth.authDBmanager import AuthDBmanager
from src.auth import mail
from src.exceptions import ServerError, DatabaseDown
import uuid
import datetime

authmanager = AuthDBmanager()

async def get_verificationtoken_by_email(email):
  token = await authmanager.get_verification_token_by_email(email)
  return token

async def get_verificationtoken_by_token(token):
  token = await authmanager.get_verification_token_by_token(token)
  return token

async def send_verification_token(email):
  token = await get_verificationtoken_by_email(email)
  if token is None:
    raise ServerError()

  if token.expires_at < datetime.datetime.now():
    new_token = await renew_verification_token(email)
  else:
    new_token = token.verification_token
  
  mail.send_verification_mail(email , new_token)


async def renew_verification_token(email:str):
  token = str(uuid.uuid4())
  expiration_time = datetime.datetime.now() + datetime.timedelta(hours=1)
  try:
    await authmanager.renew_verification_token(email, token, expiration_time)
    return token
  except Exception as e:
    print(e)
    raise DatabaseDown()