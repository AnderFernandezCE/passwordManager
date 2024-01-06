from src.config import settings
import resend

resend.api_key = settings.RESEND_API

def send_verification_mail(email, token):
  link = f"https://192.168.1.37:8000/api/auth/new-register?token={token}"
  params = {
      "from": "PassMan <passwordmanager@resend.dev>",
      "to": [email],
      "subject": "Account verification",
      "html": f"verify your account <a href='{link}'><strong>here</strong></a>",
  }

  resend.Emails.send(params)
