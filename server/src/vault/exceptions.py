from src.exceptions import NotFound

class ItemNotFound(NotFound):
  DETAIL = "Item not found"