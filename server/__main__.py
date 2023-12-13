import os
from server.paths import ACCOUNTS, DB

class Server:

  def __init__(self):
    self.users = {}
    self.load_user_from_file()

  def load_user_from_file(self):
    try:
      with open(ACCOUNTS, "r") as users_file:
        emails = users_file.readlines()
        for email in emails:
          hash_email = os.path.join(DB / email, "hash")
          if os.path.exists(hash_email):
            with open(hash_email, "rb") as hash_email_file:
              self.users[email] = hash_email_file.readline()

    except FIleNotFoundError:
      print("Users file not found")
    except Exception as e:
      print(e)
    
  def print_users(self):
    print(self.users)



server =  Server()

server.print_users() 

# def register(email, hashed_user):
#   if check_user_exists(email):
#     return("Email exists")
#   creation = create_user(email, hashed_user)
#   if creation:
#     return ("Account created succesfully")
#   return ("Error creating account")

# def check_user_exists(email):
#   with open(ACCOUNTS, 'r') as f:
#     for line in f.readlines():
#       if line == email:
#         return True
#     return False
  
# def create_user(email, hashed_user):
#   try:
#     user = DB / email
#     os.makedirs(user)
#     with open(user/"hash", "wb") as f:
#       f.write(hashed_user)
#     return True
#   except Exception as e:
#     print(e)
#     return False