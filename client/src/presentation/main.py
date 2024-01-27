from .root import Root
from .homeGUI import HomeInterface
from .loginGUI import LoginInterface
from .registerGUI import RegisterInterface

class View:
    def __init__(self):
        self.root = Root()
        self.frames = {}

        self._add_frame(HomeInterface, "home")
        self._add_frame(LoginInterface, "login")
        self._add_frame(RegisterInterface, "register")

    def _add_frame(self, Frame, name):
        self.frames[name] = Frame(self.root)
        self.frames[name].place(x=0, y=0, relwidth=1, relheight=1)

    def switch(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self):
        self.root.mainloop()