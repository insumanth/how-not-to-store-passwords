from uuid import uuid4
import random


from hash_password_manager import HashPasswordManager


class HashWithSaltAndPepperPasswordManager(HashPasswordManager):

    def __init__(self, database = "HashWithSaltPasswordManager.toml", hash_algorithm = "md5"):
        super().__init__(database, hash_algorithm)
        self.hash_algorithm = hash_algorithm
        self.pepper_number_range = range(100,1000)


    def create_user(self, username, password, userdata):
        # Storing only the Slated Hash of the Password and not the Password at all.
        # Also Storing the salt used in the hash. Pepper is not saved.

        # Salt
        random_salt = str(uuid4())
        userdata["salt"] = random_salt

        # Pepper
        random_pepper = random.choice(self.pepper_number_range)


        password_hash = self.get_hash_of_text_with_salt_and_pepper(text=password, salt=random_salt, pepper=random_pepper)
        super(HashPasswordManager, self).create_user(username=username, password=password_hash, userdata=userdata)


    def authenticate_user(self, username, input_password):
        user_data = self.get_user_record(username)
        if user_data:
            # Hashing input_password and comparing against the saved hash.
            salt_used_in_hash = user_data["data"]["salt"]

            hash_match = False
            for number in self.pepper_number_range:

                input_password_hash = self.get_hash_of_text_with_salt_and_pepper(text=input_password, salt=salt_used_in_hash, pepper=number)
                original_password_hash = user_data["password"]
                is_valid = self.verify_password(username, input_password = input_password_hash, original_password = original_password_hash, debug=False)
                if is_valid:
                    hash_match = True
                    break

            if hash_match:
                return True


    def get_hash_of_text_with_salt_and_pepper(self, text, salt, pepper):
        salted_peppered_text = f"{text}{salt}{pepper}"
        return self.get_hash_of_text(salted_peppered_text)
