import requests
from src.schemas import response

BASE_API_URL = "https://192.168.1.37:8000/"
AUTH_API_URL = BASE_API_URL + "api/auth/"

def register_user(user, email, hmp, psk) -> response.Response:
  url = AUTH_API_URL + "register"
  user = {
          "user" : {
              "username" : user,
              "email" : email,
              "hash_master_password" : hmp,
              "key" : psk
            }
          }
  x = requests.post(url, json = user, verify=False)
  if x.status_code == 409:# user exists
    return response.EmailInUseResponse()
  if x.status_code == 500:# server error
    return response.ServerErrorResponse()
  if x.status_code == 201:# created
    return response.OkResponse()