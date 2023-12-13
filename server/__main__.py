import os
import re

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64

from server.paths import ACCOUNTS, DB

from models.response import OkResponse, IncorrectCredentialsResponse, EmailInUseResponse, ServerError, InvalidEmailResponse

class Server:

  def __init__(self):
    self.users = {}
    self.load_users_from_file()

  def load_users_from_file(self):
    try:
      with open(ACCOUNTS, "r") as users_file:
        emails = users_file.readlines()
        for email in emails:
          email = email.strip()
          hash_email = os.path.join(DB / email, "hash")
          if os.path.exists(hash_email):
            with open(hash_email, "rb") as hash_email_file:
              self.users[email] = hash_email_file.readline()

    except FileNotFoundError:
      print("Users file not found")
    except Exception as e:
      print(e)
    
  def register(self, email: str, hashed_master_password: bytes, protected_sym_key: bytes):
    if not self.check_email_valid(email):
      return InvalidEmailResponse()
    if email in self.users:
      return EmailInUseResponse()

    try:
      user_dir = DB / email
      self.create_user_directory(user_dir)
      self.save_user_data(user_dir, hashed_master_password, protected_sym_key)
      self.update_accounts_registered(email)
      self.users[email] = hashed_master_password
    except Exception as e:
      print(e)
      return ServerError()

    return OkResponse()

  def create_user_directory(self,user_directory):
    try:
      os.makedirs(user_directory)
    except FileExistsError:
      pass
    except Exception as e:
      raise e

  def save_user_data(self, user_dir, hash_user, psk):
    with open(user_dir / "hash", "wb") as f:
      f.write(hash_user)
    with open(user_dir / "psk", "wb") as f:
      f.write(psk)
  
  def update_accounts_registered(self, email):
    with open(ACCOUNTS, "a") as f:
      f.write(f'{email}\n')

  def check_email_valid(self, email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, email):
      return True
    return False
  
  def login(self, email: str, hashed_master_password: bytes):
    if not self.check_email_valid(email):
      return InvalidEmailResponse()
    
    if not email in self.users:
      return IncorrectCredentialsResponse()
    if not self.users[email] == hashed_master_password:
      return IncorrectCredentialsResponse()
    
    user_dir = DB / email
    with open( user_dir / "hash", "rb") as f:
      protected_key = f.readline()
    
    return OkResponse(), protected_key

# ---------------------------
def key_derivation_function(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=600000,
    )

    return kdf.derive(password)

def bin_to_b64(data):
  return  base64.b64encode(data)
 
# -------------------

email = "correoinventado@gmail.com".encode('UTF-8')
password = "password123".encode('UTF-8')
master_key =  key_derivation_function(password, email)
hash_master_key = key_derivation_function(master_key, password)

server =  Server()
# response = server.register("email@gmail.com",bin_to_b64(hash_master_key),bin_to_b64(os.urandom(32)))  -- IT WORKS, will do in client
# print(response.get_message())
response, key = server.login("correoinventado@gmail.com", bin_to_b64(hash_master_key))
if isinstance(response, OkResponse):
    print("Login Succesful")
    print("Protected Key:", key)
else:
    print("Login failed. Incorrect credentials.")