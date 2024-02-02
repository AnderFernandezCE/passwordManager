from pydantic import BaseModel
from datetime import date
from typing import Optional, List, Dict
from enum import Enum

class CipherData(BaseModel):
  id:str
  created_at: date
  updated_at: date
  name: str
  data: str

class PasswordsResponse(BaseModel):
  user_id: Dict[str, Dict[str, CipherData]] = {}

class CreateItemRequest(BaseModel):
  name: str
  data: str