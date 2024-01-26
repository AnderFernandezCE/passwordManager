from ..validators.email import check_email_valid

class RegisterValidator:
  def __init__(self):
    pass

  def validate(self, user, email, password, confirmpassword):
    if not user or not password:
      raise Exception("Fill all the fields")
    elif not check_email_valid(email):
       raise Exception("Invalid email")
    elif not password == confirmpassword:
       raise Exception("Passwords are not equal")