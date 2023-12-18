import re
import server.server as server
from client.encryption import get_hashed_user

from utils.utils import check_email_valid

def welcome():
  print("Welcome to the password manager.")
  print("Do you want to register or to log in?")
  msg = "Press (r) for register, (l) for login or (e) to exit: "
  decision = str(input(msg)).lower()
  while not decision in ("r", "l", "e"):
    print("Unknown command.")
    decision = str(input(msg)).lower()
  return decision

def register():
  print("Register option checked.")
  email = str(input("Please enter your email: ")).lower().strip()
  while not check_email_valid(email):
    email = str(input("Please enter your email: ")).lower().strip()
  password = str(input("Please enter a password: "))
  return email, password

def login():
  print("Login option checked.")
  email = str(input("Please enter your email: ")).lower().strip()
  while not check_email_valid(email):
    email = str(input("Please enter your email: ")).lower().strip()
  password = str(input("Please enter a password: ")) # todo check strong password
  return email, password

def main_menu():
  print("You are in the main menu.")
  print("What do you want to do now?:")
  print("1. Create item")
  print("2. Modify item")
  print("3. List items")
  print("4. Log out")

  while True:
    try:
      decision = int(input("Type 1 to 4 for a decision:"))
      if decision in range(1,6):
        return decision
      else:
        print("Unknown command.")
    except ValueError:
      print("Invalid input. Please enter a valid integer.")

def logout():
  print("LEAVING PASSWORD MANAGER")

def new_item():
  print("New Item selected.")
  return get_item_data()


def get_item_data():
  while True:
    name = input("Enter the item name: ").strip()
    email = input("Enter desired email: ").strip()
    password = input("Enter desired password: ").strip()

    if name and email and password:
        return name, email, password
    else:
        print("Error: Please make sure all fields are non-empty.")
        print("Try again.")

def modify_item():
  print("Modify Item selected.")
  while True:
    file_name = input("Enter Item name: format(text1-text2-text3-text4-text5)   ").strip()
    if re.fullmatch("\w+(?:-\w+){4}", file_name):
      return file_name
    else:
      print("Invalid file name.")

def list_items():
  print("List Items selected.")

def item_created():
  print("ITEM CREATED SUCCESFULLY")

def item_modified():
  print("ITEM MODIFIED SUCCESSFULLY")
