from pydantic import BaseModel
from datetime import date
from typing import Optional, List
from enum import Enum


    
class UserRequest(BaseModel):
  username : str
  email : str
  hash_master_password : str
  key : str
  
class RegisterRequest(BaseModel):
  user : UserRequest

class RegisterResponse(BaseModel):
  status : bool