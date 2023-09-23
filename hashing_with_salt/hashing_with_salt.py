import sys
import os
from uuid import uuid4
from hash_password_manager import HashPasswordManager


class HashWithSaltPasswordManager(HashPasswordManager):

    def __init__(self, database = "HashWithSaltPasswordManager.toml", hash_algorithm = "md5"):
        super().__init__(database, hash_algorithm)
        self.hash_algorithm = hash_algorithm


    def create_user(self, username, password, userdata):
        # Storing only the salted Hash of the Password and not the Password itself.
        # Also Storing the salt used in the hash.
        random_salt = str(uuid4())
        userdata["salt"] = random_salt
        password_hash = self.get_hash_of_text_with_salt(text=password, salt=random_salt)
        super().create_user(username=username, password=password_hash, userdata=userdata)


    def authenticate_user(self, username, input_password):
        user_data = self.get_user_record(username)
        if user_data:
            # Hashing input_password with the original salt and comparing against the saved hash.
            salt_used_in_hash = user_data["data"]["salt"]
            input_password_hash = self.get_hash_of_text_with_salt(text=input_password, salt=salt_used_in_hash)
            original_password_hash = user_data["password"]
            return self.verify_password(username, input_password = input_password_hash, original_password = original_password_hash)


    def get_hash_of_text_with_salt(self, text, salt):
        salted_text = f"{text}{salt}"
        return self.get_hash_of_text(salted_text)

