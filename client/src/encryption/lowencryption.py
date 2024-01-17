from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
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
  return os.urandom(16)

def generate_symmetric_key():
  skey = os.urandom(32)
  h = hmac.HMAC(skey, hashes.SHA256())
  h.update(skey)
  smac = h.finalize()
  return skey + smac


def aes_encryption(payload:bytes, iv:bytes, key:bytes):
  cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
  encryptor = cipher.encryptor()
  ct = encryptor.update(payload) + encryptor.finalize()
  return ct

def aes_decryption(payload:bytes, iv:bytes, key:bytes):
  cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
  decryptor = cipher.decryptor()
  ct = decryptor.update(payload) + decryptor.finalize()
  return ct