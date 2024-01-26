from src2.presentation.main import View
from src2.business.controllers.home import HomeController

view = View()
view.switch("home")
HomeController(view)
view.start_mainloop()