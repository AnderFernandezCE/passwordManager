from src.exceptions import Conflict, BadRequest, Gone, NotFound

class UserExists(Conflict):
  DETAIL = "User already exists"

class AccountVerified(Conflict):
  DETAIL = "Account already verified"

class InvalidToken(BadRequest):
  DETAIL = "Invalid Token"

class ExpiredVerificationToken(Gone):
  DETAIL = "Expired verification Token"

class UserNotExists(NotFound):
  DETAIL = "User not found"