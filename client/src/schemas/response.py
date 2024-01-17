from abc import ABC, abstractmethod

class Response(ABC):
  
  def __init__(self, message=None):
    self.message= message

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

class ServerErrorResponse(Response):
  def get_message(self):
    return "Server has encountered an error"