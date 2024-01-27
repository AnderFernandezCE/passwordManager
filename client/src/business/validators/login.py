from ..validators.email import check_email_valid
from ..exceptions.validation import FormInvalid

class LoginValidator:
  def __init__(self):
    pass

  def validate(self, email, password):
    if not email or not password:
      raise FormInvalid ("Fill all the fields")
    elif not check_email_valid(email):
      raise FormInvalid("Invalid email")