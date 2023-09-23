from hash_password_manager import HashPasswordManager


class SimpleHashPasswordManager(HashPasswordManager):

    def __init__(self, database = "HashPasswordManager.toml", hash_algorithm = "md5"):
        super().__init__(database)
        self.hash_algorithm = hash_algorithm



    def create_user(self, username, password, userdata):
        # Storing only Hash of the Password and not the Password at all.
        password_hash = self.get_hash_of_text(text=password)
        super().create_user(username=username, password=password_hash, userdata=userdata)


    def authenticate_user(self, username, input_password):
        user_data = self.get_user_record(username)
        if user_data:
            # Hashing input_password and comparing against the saved hash.
            input_password_hash = self.get_hash_of_text(text=input_password)
            original_password_hash = user_data["password"]
            return self.verify_password(username, input_password = input_password_hash, original_password = original_password_hash)


