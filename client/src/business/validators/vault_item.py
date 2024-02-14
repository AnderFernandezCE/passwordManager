from ..exceptions.validation import FormInvalid

class ItemValidator:
  def __init__(self):
    pass

  def validate(self, name, username, password, extra):
    if not name or not username or not password:
      raise FormInvalid("Fill all the fields")