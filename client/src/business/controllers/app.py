from src.persistance.authAPI import LogoutAPI
from src.persistance.vaultAPI import VaultAPI
from ..validators.vault_item import ItemValidator
from ..exceptions.validation import FormInvalid
from ..encryption import encryptionservice

class AppController:
  def __init__(self, view, model):
    self.model = model
    self.view = view
    self.frame = self.view.frames["app"]
    self.validator = ItemValidator()
    self._bind()

    self.current_item_id = None
    self.current_action = None

  def _bind(self):
    # self.frame.table.bind('<ButtonRelease-1>', self.on_select)
    self.frame.modifybutton.config(command=self.modify_item)
    self.frame.deletebutton.config(command=self.delete_item)
    self.frame.add_button.config(command=self.add_item)
    self.frame.cancel_button.config(command=self.cancel_operation)
    self.frame.save_button.config(command=self.save_operation)
  
  def disable_buttons(self):
    self.frame.modifybutton["state"] = "disabled"
    self.frame.deletebutton["state"] = "disabled"
    self.frame.add_button["state"] = "disabled"

    self.frame.save_button["state"] = "normal"
    self.frame.cancel_button["state"] = "normal"
    self.frame.entry_name["state"] = "normal"
    self.frame.entry_username["state"] = "normal"
    self.frame.entry_password["state"] = "normal"
    self.frame.entry_extra["state"] = "normal"

  def unable_buttons(self):
    self.frame.modifybutton["state"] = "normal"
    self.frame.deletebutton["state"] = "normal"
    self.frame.add_button["state"] = "normal"

    self.frame.save_button["state"] = "disabled"
    self.frame.cancel_button["state"] = "disabled"
    self.frame.entry_name["state"] = "disabled"
    self.frame.entry_username["state"] = "disabled"
    self.frame.entry_password["state"] = "disabled"
    self.frame.entry_extra["state"] = "disabled"

  def clear_input(self):
    self.frame.name.set('')
    self.frame.username.set('')
    self.frame.password.set('')
    self.frame.extra.set('')

  def cancel_operation(self):
    self.frame.table.selection_remove(self.frame.table.selection())
    self.clear_input()
    self.current_item_id = None
    self.current_action = None
    self.unable_buttons()

  def modify_item(self):
    curItem = self.frame.table.focus()
    if bool(curItem):
      self.disable_buttons()
      item = self.frame.table.item(curItem)
      self.frame.name.set(item.get("text", "nada"))
      item_values = item.get('values')
      self.current_action = "modify"
      self.current_item_id = item_values[0]
      self.frame.username.set(item_values[1])
      self.frame.password.set(item_values[2])
      self.frame.extra.set(item_values[3])

  def delete_item(self):
    curItem = self.frame.table.focus()
    if bool(curItem):# and self.current_item_id is not None:
      item = self.frame.table.item(curItem)
      item_id = item.get('values')[0]
      refresh_token = self.model.account_data.get_access_token()
      vaultAPI = VaultAPI(refresh_token) #should do try except
      vaultAPI.delete_item(item_id)
      self.frame.table.delete(curItem)

  def add_item(self):
    self.frame.table.selection_remove(self.frame.table.selection())
    self.disable_buttons()
    self.current_action = "add"

  def save_operation(self):
    name = self.frame.name.get()
    username = self.frame.username.get()
    password = self.frame.password.get()
    extra = self.frame.extra.get()
    print(extra)
    try:
      self.validator.validate(name, username, password, extra)
    except FormInvalid as e:
      print(e)
      return
    item_name = name # encrypt
    item_data = "|".join([username,password,extra])
    refresh_token = self.model.account_data.get_access_token()
    vaultAPI = VaultAPI(refresh_token) #should do try except
    if self.current_action == "add":
      response = vaultAPI.add_item(item_name, item_data)
      item_id = response.get('id')
      self.model.account_data.add_item(item_id, response)
      self.frame.table.insert('','end', text=name, values=(item_id,username, password, extra))
      self.cancel_operation()
    elif self.current_action == "modify":
      response = vaultAPI.modify_item(self.current_item_id, item_name, item_data)
      self.model.account_data.update_item(self.current_item_id, response)
      selected_item = self.frame.table.selection()[0]
      self.frame.table.item(selected_item, text=item_name, values=(self.current_item_id,username,password,extra))
      self.cancel_operation()

  def get_user_data(self):
    access_token = self.model.account_data.get_access_token()
    tokenAPI = VaultAPI(access_token)
    user_data = tokenAPI.get_user_data()
    self.model.account_data.set_user_data(user_data.get("user_data"))

  def update_table_data(self):
    protected_key = self.model.account_data.get_protected_key()
    master_key = self.model.account_data.get_master_key()
    sym_key = encryptionservice.decypher_protected_sym_key(protected_key, master_key)
    del protected_key
    del master_key
    print(sym_key)
    user_data = self.model.account_data.get_user_data()
    for count, value in enumerate(user_data):
      name = user_data[value]["name"]
      data = user_data[value]["data"].split("|")
      username = data[0]
      password = data[1]
      extra = data[2]
      # decipher data and insert into table
      self.frame.table.insert('',count, text=name, values=(value,username, password, extra))

  def update_view(self):
    if self.model.account_data:
      self.get_user_data()
      self.frame.welcome["text"] = "Welcome " + self.model.account_data.get_username()
      self.update_table_data()
      self.view.root.geometry("900x900")
      
    else:
      self.frame.welcome["text"] = ""
      self.frame.table.delete(*self.frame.table.get_children())

  def bind_logout(self):
    self.frame.logoutbutton.config(command = self.logout)

  def logout(self):
    token = self.model.account_data.get_refresh_token()
    logoutservice = LogoutAPI(token)
    logoutservice.logout()
    self.model.logout()