import os
from server.paths import ACCOUNTS, DB

def register(email, hashed_user):
  if check_user_exists(email):
    return("Email exists")
  creation = create_user(email, hashed_user)
  if creation:
    return ("Account created succesfully")
  return ("Error creating account")

def check_user_exists(email):
  with open(ACCOUNTS, 'r') as f:
    for line in f.readlines():
      if line == email:
        return True
    return False
  
def create_user(email, hashed_user):
  try:
    user = DB / email
    os.makedirs(user)
    with open(user/"hash", "wb") as f:
      f.write(hashed_user)
    return True
  except Exception as e:
    print(e)
    return False
