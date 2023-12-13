from abc import ABC, abstractmethod

class Response(ABC):
  @abstractmethod
  def get_message(self):
    pass

class EmailInUseResponse(Response):
  def get_message(self):
    return "Email is already in use."

class IncorrectCredentialsResponse(Response):
  def get_message(self):
    return "Incorrect email or password."
  
class InvalidEmailResponse(Response):
  def get_message(self):
    return "Invalid email."

class OkResponse(Response):
  def get_message(self):
    return "Ok"

class ServerError(Response):
  def get_message(self):
    return "Server has encountered an error"