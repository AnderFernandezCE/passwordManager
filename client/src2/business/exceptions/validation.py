class FormInvalid(Exception):
  "Raised when the form is invalid"
  def __init__(self, message="Invalid input."):
    self.message = message
    super().__init__(self.message)