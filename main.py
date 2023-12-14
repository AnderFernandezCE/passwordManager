#import client.prompts as prompts
from client.client import Client
from server.server import Server

if __name__== "__main__":
  server = Server()
  client = Client(server)
  client.start()