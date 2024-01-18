from src.exceptions import Conflict, BadRequest, Gone, NotFound, Unauthorized, Forbidden

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

class InvalidCredentials(Unauthorized):
  DETAIL = "Invalid credentials"

class EmailNotVerified(Forbidden):
  DETAIL = "Your email address is not verified"