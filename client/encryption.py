from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

import base64

def get_hashed_user(email,password):
  email_bytes = email.encode('UTF-8')
  password_bytes = password.encode('UTF-8')
  master_key = key_derivation_function(password_bytes, email_bytes)
  hashed_user = key_derivation_function(master_key, password_bytes)
  del password
  del password_bytes
  del master_key
  return bin_to_b64(hashed_user)

def get_master_key(email,password):
  email_bytes = email.encode('UTF-8')
  password_bytes = password.encode('UTF-8')
  master_key = key_derivation_function(password_bytes, email_bytes)
  del password
  del password_bytes
  return master_key
  
def get_sym_key(response):
  return b64_to_bin(response.get_message())

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

def b64_to_bin(data):
  return  base64.b64decode(data)

# server =  Server()
# # response = server.register("email@gmail.com",bin_to_b64(hash_master_key),bin_to_b64(os.urandom(32)))  -- IT WORKS, will do in client
# # print(response.get_message())