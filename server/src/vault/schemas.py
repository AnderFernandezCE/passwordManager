from pydantic import BaseModel , constr
from datetime import date, datetime
from typing import Optional, List, Dict
from enum import Enum

class CipherData(BaseModel):
  id:str
  created_at: date
  updated_at: date
  name: str
  data: str

  @classmethod
  def from_dict(cls, item: dict):
    # Convert datetime objects to date objects
    item['created_at'] = item['created_at'].date()
    item['updated_at'] = item['updated_at'].date()
    return cls(**item)

class PasswordsResponse(BaseModel):
  user_id: str
  user_data : Dict[str, CipherData] = {}

class CreateItemRequest(BaseModel):
  name: str
  data: str

class UpdateDataRequest(BaseModel):
    id: str
    name: Optional[str] = None
    data: Optional[str] = None

    _validate_at_least_one: classmethod = constr(strip_whitespace=True, min_length=1)

    class Config:
      arbitrary_types_allowed = True
      validate_assignment = True

    def __init__(self, **data):
      super().__init__(**data)
      if self.name is None and self.data is None:
        raise ValueError("At least one of 'name' or 'data' must be provided")