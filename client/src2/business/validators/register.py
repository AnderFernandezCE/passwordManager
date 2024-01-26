from ..validators.email import check_email_valid
from ..exceptions.validation import FormInvalid

class RegisterValidator:
  def __init__(self):
    pass

  def validate(self, user, email, password, confirmpassword):
    if not user or not password:
      raise FormInvalid("Fill all the fields")
    elif not check_email_valid(email):
       raise FormInvalid("Invalid email")
    elif not password == confirmpassword:
       raise FormInvalid("Passwords are not equal")