from src.auth.authDBmanager import AuthDBmanager
from src.auth.mail import send_verification_mail

authmanager = AuthDBmanager()

async def get_verificationtoken_by_email(email):
  token = await authmanager.get_verification_token_by_email(email)
  return token

async def get_verificationtoken_by_token(token):
  token = await authmanager.get_verification_token_by_token(token)
  return token

async def send_verification_token(email):
  token = await get_verificationtoken_by_email(email)
  if token is not None:
    send_verification_mail(email , token.verification_token)