from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes

def hash():
    pass

def key_derivation_function(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=256,
        salt=salt,
        iterations=600000,
    )

    return kdf.derive(password)

def hmac_based_extract_expand_key_derivation_function_hkdf(password, salt):
    info = b"hkdf-example"
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=512,
        salt=salt,
        info=info,
    )
    return  hkdf.derive(password)

def symmetric_key_generation():
    pass

def initial_vector_generation():
    pass

def aes_encryption():
    pass

master_password = b"password"
email = b"email@gmail.com"
master_key = key_derivation_function(master_password,email)
print("derived key is: ",master_key)
print("-"*15)
master_password_hash= key_derivation_function(master_key, master_password)
print("master password hash is: ",master_password_hash)
print("-"*15)
streched_master_key = hmac_based_extract_expand_key_derivation_function_hkdf(master_key, email)
print("streched master key is: ",streched_master_key)
