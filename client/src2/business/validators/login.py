from ..validators.email import check_email_valid

class LoginValidator:
  def __init__(self):
    pass

  def validate(self, email, password):
    if not email or not password:
      raise Exception ("Fill all the fields")
    elif not check_email_valid(email):
      raise Exception("Invalid email")