from src.config import settings
import resend

resend.api_key = settings.RESEND_API

def send_verification_mail(email, token):

  params = {
      "from": "PassMan <passwordmanager@resend.dev>",
      "to": [email],
      "subject": "Account verification",
      "html": f"<strong>{token}</strong>",
  }

  resend.Emails.send(params)
