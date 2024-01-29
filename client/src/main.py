from src.presentation.main import View
from src.business.controllers.main import Controller
from src.business.models.account.account  import UserAccount

def main():
  view = View()
  model = UserAccount()
  controller = Controller(view, model)
  controller.start()

if __name__ == "__main__":
  main()