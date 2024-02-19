from src.business.encryption import lowencryption

def obtain_hash_master_password_and_master_key(payload:str, salt:str):
  """payload = password 
     salt = email    
  """
  payload_bytes = payload.encode('UTF-8')
  del payload
  salt_bytes = salt.encode('UTF-8')
  master_key = lowencryption.kdf(payload_bytes,salt_bytes)
  hash_master_password = lowencryption.kdf(master_key,payload_bytes)
  del payload_bytes
  return lowencryption.bin_to_b64(hash_master_password).decode('UTF-8') , master_key

def generate_protected_sym_key(master_key:bytes):
  iv = lowencryption.generate_salt()
  symkey = lowencryption.generate_symmetric_key()
  protected_key = lowencryption.aes_encryption(symkey, iv, master_key)
  utf8_iv = lowencryption.bin_to_b64(iv).decode('UTF-8')
  utf8_protected_key = lowencryption.bin_to_b64(protected_key).decode('UTF-8')
  return utf8_protected_key + "|" + utf8_iv

def decypher_protected_sym_key(protected_key:str, master_key:bytes):
  key, iv = lowencryption.get_protected_key_data(protected_key) 
  key_bytes = lowencryption.b64_to_bin(key.encode('UTF-8'))
  iv_bytes = lowencryption.b64_to_bin(iv.encode('UTF-8'))
  fsymkey = lowencryption.aes_decryption(key_bytes, iv_bytes,master_key)
  return fsymkey[:32] #fsymkey is compound of symkey + symkeymac
  
def vault_encrypt(symkey, name, username, password, extra):
  item_name = lowencryption.encrypt_vault_item_name(symkey, name)
  item_data = lowencryption.encrypt_vault_item_data(symkey, username, password, extra)
  return item_name, item_data

def vault_decrypt(symkey, name, data):
  name = lowencryption.decrypt_vault_item_name(symkey, name)
  username, password, extra = lowencryption.decrypt_vault_item_data(symkey, data)
  
  return name, username, password, extra