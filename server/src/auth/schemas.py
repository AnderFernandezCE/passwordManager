from pydantic import BaseModel, EmailStr, constr
from datetime import date
from typing import Optional, List
from enum import Enum

class UserEntity(BaseModel):
    username: str
    email: str
    userhash: str
    key: str
    # publicKey: str
    # privateKey: str
    salt: bytes
    
class UserRequest(BaseModel):
  username : constr(strip_whitespace=True, min_length=1, max_length=50)
  email : EmailStr
  hash_master_password : constr(min_length=44, max_length=44)
  key : constr(min_length=1)
  
class RegisterRequest(BaseModel):
  user : UserRequest

class RegisterResponse(BaseModel):
  username : str
  email : EmailStr
  hash_master_password : str
  key : str