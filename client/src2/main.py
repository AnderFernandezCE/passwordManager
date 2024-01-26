from src2.presentation.main import View
from src2.business.controllers.home import HomeController
from src2.business.controllers.login import LoginController
from src2.business.controllers.register import RegisterController

view = View()
view.switch("home")
HomeController(view)
LoginController(view)
RegisterController(view)
view.start_mainloop()