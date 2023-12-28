from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional, List
from enum import Enum


    
class UserRequest(BaseModel):
  username : str
  email : EmailStr
  hash_master_password : str
  key : str
  
class RegisterRequest(BaseModel):
  user : UserRequest

class RegisterResponse(BaseModel):
  username : str
  email : EmailStr
  hash_master_password : str
  key : str