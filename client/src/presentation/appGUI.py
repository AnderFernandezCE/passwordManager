import tkinter as tk
from tkinter import ttk

class AppInterface(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.logoutbutton = tk.Button(self, text="LOGOUT")
        self.logoutbutton.grid(row=0, column=2, sticky="e", padx=5, pady=5)
        self.welcome = tk.Label(self, text="Hello: User")
        self.welcome.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.title = tk.Label(self, text= "APP", pady=20)
        self.title.config(font=("Italic", 44))
        self.title.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)

        self.label_name = tk.Label(self, text="NAME")
        self.label_name.config(font=('Arial',12,'bold'))
        self.label_name.grid(row=2, column=0, sticky="w", padx=5, pady=5)

        self.name = tk.StringVar()
        self.entry_name = tk.Entry(self, textvariable=self.name, state="disabled")
        self.entry_name.config(width=50, font=('Arial',  12))
        self.entry_name.grid(row=2, column=1, columnspan=2, sticky="ew", padx=5, pady=5)

        self.label_username = tk.Label(self, text="USERNAME")
        self.label_username.config(font=('Arial',12,'bold'))
        self.label_username.grid(row=3, column=0, sticky="w", padx=5, pady=5)

        self.username = tk.StringVar()
        self.entry_username = tk.Entry(self, textvariable=self.username, state="disabled")
        self.entry_username.config(width=50, font=('Arial',  12))
        self.entry_username.grid(row=3, column=1, columnspan=2, sticky="ew", padx=5, pady=5)

        self.label_password = tk.Label(self, text="PASSWORD")
        self.label_password.config(font=('Arial',12,'bold'))
        self.label_password.grid(row=4, column=0, sticky="w", padx=5, pady=5)

        self.password = tk.StringVar()
        self.entry_password = tk.Entry(self, textvariable=self.password, state="disabled")
        self.entry_password.config( font=('Arial',  12))
        self.entry_password.grid(row=4, column=1, columnspan=2, sticky="ew", padx=5, pady=5)

        self.label_extra = tk.Label(self, text="EXTRA")
        self.label_extra.config(font=('Arial',12,'bold'))
        self.label_extra.grid(row=5, column=0, sticky="w", padx=5, pady=5)

        self.extra = tk.StringVar()
        self.entry_extra = tk.Entry(self, textvariable=self.extra, state="disabled")
        self.entry_extra.config(width=50, font=('Arial',  12))
        self.entry_extra.grid(row=5, column=1, columnspan=2, sticky="ew", padx=5, pady=5)

        self.add_button = tk.Button(self, text="Add", bg="blue", fg="white", width=30)
        self.add_button.grid(row=6, column=0, sticky="w", padx=5, pady=5)

        self.save_button = tk.Button(self, text="Save", bg="green", fg="white", width=30, state="disabled")
        self.save_button.grid(row=6, column=1, sticky="w", padx=5, pady=5)

        self.cancel_button = tk.Button(self, text="Cancel", bg="red", fg="white", width=30, state="disabled")
        self.cancel_button.grid(row=6, column=2, sticky="w", padx=5, pady=5)

        self.table_frame = ttk.Frame(self)
        self.table_frame.grid(row=7, column=0, columnspan=3, pady=20, sticky="nsew")

        self.verticalscrollbar = ttk.Scrollbar(self.table_frame)
        self.verticalscrollbar.grid(row=0, column=1, sticky='ns')
        self.horizontalscrollbar = ttk.Scrollbar(self.table_frame, orient="horizontal")
        self.horizontalscrollbar.grid(row=1, column=0, sticky='ew')

        self.table = ttk.Treeview(self.table_frame, columns=("Id","Username","Password", "Extra"),selectmode='browse', yscrollcommand=self.verticalscrollbar.set, xscrollcommand=self.horizontalscrollbar.set)
        self.table.grid(row=0, column=0,sticky="nsew")

        self.verticalscrollbar.config(command=self.table.yview)
        self.horizontalscrollbar.config(command=self.table.xview)

        self.table.heading("#0", text='NAME')
        self.table.heading("Username", text='USERNAME')
        self.table.heading("Password", text='PASSWORD')
        self.table.heading("Extra", text='EXTRA')

        self.table["displaycolumns"] = ['Username', 'Password']

        self.modifybutton = tk.Button(self, text="Modify", bg="green", fg="white", width=30)
        self.modifybutton.grid(row=8, column=0, sticky="w", padx=5, pady=5)

        self.deletebutton = tk.Button(self, text="Delete", bg="red", fg="white", width=30)
        self.deletebutton.grid(row=8, column=1, sticky="w", padx=5, pady=5)
