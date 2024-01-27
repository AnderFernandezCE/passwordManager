from pydantic import BaseModel, EmailStr, constr
from datetime import date
from typing import Optional, List
from enum import Enum

# Used in authDBmanager
class UserEntity(BaseModel):
  username: str
  email: str
  userhash: str
  key: str
  # publicKey: str
  # privateKey: str
  salt: bytes

class UserLoginResponse(BaseModel):
  uuid: str
  username: str
  email: str
  # userhash: str  maybe for token auth?
  protectedkey: str
  refresh_token : str

class LoginRequest(BaseModel):
  email: str
  userhash: str
  # auth token, todo
    
class UserRequest(BaseModel):
  username : constr(strip_whitespace=True, min_length=1, max_length=50)
  email : EmailStr
  hash_master_password : constr(min_length=44, max_length=44)
  key : constr(min_length=113, max_length=113)
  
class RegisterRequest(BaseModel):
  user : UserRequest

class RegisterResponse(BaseModel):
  username : str
  email : EmailStr
  hash_master_password : str
  key : str