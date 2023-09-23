import tomlkit
from os.path import isfile

class PasswordManager:

    def __init__(self, database = "PasswordManager.toml"):
        self.database = database
        self._create_database()

    def create_user(self, username, password, userdata):
        value = {
            "password" : password,
            "data" : userdata
        }
        self._create_database_entry(key = username, value = value)

    def authenticate_user(self, username, password):
        pass

    def get_user_data(self, username, password):
        login = self.authenticate_user( username, password)
        if login:
             user_data = self.get_user_record(username)
             return user_data["data"]

    def verify_password(self, username, input_password, original_password, **kwargs):
        if input_password == original_password:
            print(f"Password Verification Successful for user '{username}'.")
            return True
        else:
            if kwargs.get("debug"):
                print(f"'{input_password}' is not the correct Password for user '{username}'.")
            return False

    def get_user_record(self, username):
        user_details = self._get_database_entry(key=username)
        if not user_details:
            print(f"'{username}' does not have an account.")
        return user_details


    # Utility Methods.

    def _create_database(self):
        if not isfile(self.database):
            with open(self.database, "w") as f:
                f.write('')

    def _create_database_entry(self, key, value):
        data = self._read_from_database()
        data[key] = value
        self._write_to_database(data)

    def _get_database_entry(self, key):
        data = self._read_from_database()
        return data.get(key)

    def _write_to_database(self, data):
        with open(self.database, "w") as f:
            tomlkit.dump(data, f)

    def _read_from_database(self):
        with open(self.database, "r") as f:
            return tomlkit.load(f)
