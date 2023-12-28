from src.exceptions import Conflict

class UserExists(Conflict):
  DETAIL = "User already exists"