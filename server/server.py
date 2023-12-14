import os
import re

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64

from server.paths import ACCOUNTS, DB
from server.constants import HASH_FILE, PROTECTED_KEY_FILE

from models.response import OkResponse, IncorrectCredentialsResponse, EmailInUseResponse, ServerError, InvalidEmailResponse, LoginResponse
from utils.utils import check_email_valid

class Server:

  def __init__(self):
    self.start_server()
    self.users = {}
    self.load_users_from_file()

  def start_server(self):
    try:
      if not ACCOUNTS.exists():
        ACCOUNTS.touch()
      if not DB.exists():
        DB.mkdir()
    except Exception as e:
      print(e)

  def load_users_from_file(self):
    try:
      with open(ACCOUNTS, "r") as users_file:
        emails = users_file.readlines()
        for email in emails:
          email = email.strip()
          hash_email = os.path.join(DB / email, HASH_FILE)
          if os.path.exists(hash_email):
            with open(hash_email, "rb") as hash_email_file:
              self.users[email] = hash_email_file.readline()

    except FileNotFoundError:
      print("Users file not found")
    except Exception as e:
      print(e)
    
  def register(self, email: str, hashed_master_password: bytes, protected_sym_key: bytes):
    if not check_email_valid(email):
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
    with open(user_dir / HASH_FILE, "wb") as f:
      f.write(hash_user)
    with open(user_dir / PROTECTED_KEY_FILE, "wb") as f:
      f.write(psk)
  
  def update_accounts_registered(self, email):
    with open(ACCOUNTS, "a") as f:
      f.write(f'{email}\n')
  
  def login(self, email: str, hashed_master_password: bytes):
    if not check_email_valid(email):
      return InvalidEmailResponse()
    
    if not email in self.users:
      return IncorrectCredentialsResponse()
    if not self.users[email] == hashed_master_password:
      return IncorrectCredentialsResponse()
    
    try:
      user_dir = DB / email
      with open( user_dir / PROTECTED_KEY_FILE, "rb") as f:
        protected_key = f.readline()
    except Exception as e:
      return ServerError()
    
    return LoginResponse(protected_key)