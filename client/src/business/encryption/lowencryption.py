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

def get_protected_key_data(protected_key:str):
  protected_key_data = protected_key.split("|")
  key = protected_key_data[0]
  iv = protected_key_data[1]
  return key,iv

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

def encrypt_vault_item_data(symkey:bytes, username:str, password:str, extra:str):
  iv = generate_salt()
  item_data = []
  for i in [username,password, extra]:
    padder = padding.PKCS7(128).padder()
    i_bytes = i.encode('UTF-8')
    padded_data = padder.update(i_bytes) + padder.finalize()
    encrypted_data = bin_to_b64(aes_encryption(padded_data, iv, symkey)).decode('UTF-8')
    item_data.append(encrypted_data)
  iv_utf8 = bin_to_b64(iv).decode('UTF-8')
  return "|".join(item_data) + "|" + iv_utf8

def decrypt_vault_item_data(symkey:bytes, data:str):
  vault_data = data.split("|")
  username = vault_data[0]
  password = vault_data[1]
  extra = vault_data[2]
  iv = vault_data[3]
  iv_bytes = b64_to_bin(iv.encode('UTF-8'))
  
  item_data_decrypted = []
  for i in [username, password, extra]:
    i_bytes = b64_to_bin(i.encode('UTF-8'))
    decrypted_value = aes_decryption(i_bytes, iv_bytes, symkey)
    padder = padding.PKCS7(128).unpadder()
    padded_data = padder.update(decrypted_value) + padder.finalize()
    item_data_decrypted.append(padded_data.decode('UTF-8'))
  
  username, password, extra = item_data_decrypted[:3]
  return username, password, extra

def encrypt_vault_item_name(symkey:bytes, name:str):
  padder = padding.PKCS7(128).padder()
  name_bytes = name.encode('UTF-8')
  padded_data = padder.update(name_bytes) + padder.finalize()
  iv = generate_salt()
  iv_utf8 = bin_to_b64(iv).decode('UTF-8')
  encrypted_name = bin_to_b64(aes_encryption(padded_data, iv, symkey)).decode('UTF-8')
  return encrypted_name + "|" + iv_utf8

def decrypt_vault_item_name(symkey:bytes, name:str):
  name_data = name.split("|")
  name = name_data[0]
  name_iv = name_data[1]
  iv_bytes = b64_to_bin(name_iv.encode('UTF-8'))
  
  name_bytes =  b64_to_bin(name.encode('UTF-8'))
  decrypted_name = aes_decryption(name_bytes, iv_bytes, symkey)
  padder = padding.PKCS7(128).unpadder()
  padded_data = padder.update(decrypted_name) + padder.finalize()
  return padded_data.decode('UTF-8')