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