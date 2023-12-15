from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
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
  
def get_protected_sym_key(response):
  return b64_to_bin(response.get_message())

def decrypt_protected_sym_key(protected_key, master_key, iv):
  fskey = aes_decryption(protected_key, iv, master_key)
  return fskey

def generate_symmetric_key():
  skey = os.urandom(32)
  h = hmac.HMAC(skey, hashes.SHA256())
  h.update(skey)
  smac = h.finalize()
  return skey, smac

def get_protected_key(sym_key, master_key, iv):
  protected_key = aes_encryption(sym_key, iv, master_key)
  return bin_to_b64(protected_key)

def generate_iv():
  return os.urandom(16)

def aes_decryption(payload,iv, key):
  cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
  decryptor = cipher.decryptor()
  ct = decryptor.update(payload) + decryptor.finalize()
  return ct

def aes_encryption(payload, iv, key):
  cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
  encryptor = cipher.encryptor()
  ct = encryptor.update(payload) + encryptor.finalize()
  return ct

def check_correct_sym_key(sym_key: bytes):
  skey = sym_key[:32]
  smac = sym_key[32:]
  h = hmac.HMAC(skey, hashes.SHA256())
  h.update(skey)
  smac_received = h.finalize()
  return smac_received == smac
  
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