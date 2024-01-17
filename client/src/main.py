import tkinter as tk
from src.user_interface.register import RegisterInterface
from src.user_interface.login import LoginInterface
from src.user_interface.home import HomeInterface

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        register = RegisterInterface(self)
        login = LoginInterface(self)
        home = HomeInterface(self, go_login=login.show, go_register=register.show)
        # p3 = Page3(self)  this is for ciphers form
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        home.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        register.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        login.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # register.show()
        home.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("PassMan")
    root.geometry("400x400")
    root.minsize(400, 400)
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    # root.wm_geometry("400x400")
    root.mainloop()