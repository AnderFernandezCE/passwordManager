from src.presentation.main import View
from src.business.controllers.home import HomeController
from src.business.controllers.login import LoginController
from src.business.controllers.register import RegisterController

view = View()
view.switch("home")
HomeController(view)
LoginController(view)
RegisterController(view)
view.start_mainloop()