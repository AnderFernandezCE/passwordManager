import sys
import server.server as server
from client.encryption import get_hashed_user

def welcome():
  print("Welcome to the password manager.")
  print("Do you want to register or to log in?")
  msg = "Press (r) for register, (l) for login or (e) to exit: "
  decision = str(input(msg)).lower()
  while not decision in ("r", "l", "e"):
    print("Unknown command.")
    decision = str(input(msg)).lower()
  if decision == "r":
    register()
  if decision == "l":
    login()
  else:
    sys.exit(0)

def register():
  print("Register option checked.")
  email = str(input("Please enter your email: ")).lower().strip()
  password = str(input("Please enter a password: "))
  hashed_user = get_hashed_user(email.encode(), password.encode())
  print(hashed_user.decode())
  response = server.register(email, hashed_user)
  print(response)

def login():
  print("Login option checked.")
