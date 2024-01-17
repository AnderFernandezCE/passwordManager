from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64
import os

def bin_to_b64(data):
  return  base64.b64encode(data)

def b64_to_bin(data):
  return base64.b64decode(data)


def kdf(payload:bytes, salt:bytes):
  kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=600000,
    )

  return kdf.derive(payload)


def generate_salt():
  return os.urandom(32)