from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def get_hashed_user(email,password):
  master_key = key_derivation_function(password, email)
  hashed_user = key_derivation_function(master_key, password)
  del password
  del master_key
  return hashed_user
  
def key_derivation_function(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=256,
        salt=salt,
        iterations=600000,
    )

    return kdf.derive(password)