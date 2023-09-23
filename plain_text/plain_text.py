import tomlkit
from password_manager import PasswordManager

class PlainTextPasswordManager(PasswordManager):

    def __init__(self, database = "PlainTextPasswordManager.toml"):
        super().__init__(database)


    def create_user(self, username, password, userdata):
        # Storing password as it is in plain text.
        password_to_store = password
        super().create_user(username, password_to_store, userdata)


    def authenticate_user(self, username, input_password):
        user_data = self.get_user_record(username)
        if user_data:
            # Password is in Plain Text and it should match exactly.
            original_password = user_data["password"]
            return self.verify_password(username, input_password, original_password)

