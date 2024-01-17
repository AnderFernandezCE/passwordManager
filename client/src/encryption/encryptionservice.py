from src.encryption import lowencryption

def obtain_hash_master_password(payload:str, salt:str):
  """payload = password 
     salt = email    
  """
  payload_bytes = payload.encode('UTF-8')
  del payload
  salt_bytes = salt.encode('UTF-8')
  master_key = lowencryption.kdf(payload_bytes,salt_bytes)
  hash_master_password = lowencryption.kdf(master_key,payload_bytes)
  del master_key
  del payload_bytes
  return lowencryption.bin_to_b64(hash_master_password).decode('UTF-8')
