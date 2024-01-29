from ..encryption import encryptionservice
from ..models.api.userlogin import User
from ..exceptions.validation import FormInvalid
from src.persistance.authAPI import LoginAPI

class AppController:
  def __init__(self, view, model):
    self.model = model
    self.view = view
    self.frame = self.view.frames["app"]
    self._bind()

  def _bind(self):
    if self.model.account_data:
      self.frame.welcome["text"] = "Welcome " + self.model.account_data.get_username()
    # finally:
      # Clear sensitive data from memory
      # password = " " * len(password)
      # hmp = " " * len(hmp) if hmp else ""
      # del password, hmp, user