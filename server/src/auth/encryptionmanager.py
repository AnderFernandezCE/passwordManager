from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64
import os

def generate_salt():
  return os.urandom(32)

def derive_userhash(userhash:str, salt:bytes):
  user_bytes = userhash.encode('UTF-8')
  new_userhash = kdf(user_bytes, salt)
  return bin_to_b64(new_userhash).decode('UTF-8')

def bin_to_b64(data):
  return  base64.b64encode(data)

def b64_to_bin(data):
  return base64.b64decode(data)


def kdf(password, salt):
  kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=600000,
    )

  return kdf.derive(password)