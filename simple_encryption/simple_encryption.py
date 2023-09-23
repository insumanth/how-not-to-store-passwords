from password_manager import PasswordManager

class SimpleEncryptionPasswordManager(PasswordManager):

    def __init__(self, database = "SimpleEncryptionPasswordManager.toml"):
        super().__init__(database)
        self.password_shift = 5



    def create_user(self, username, password, userdata):
        # Encrypting and Storing Passwords.
        encrypted_password = self.encrypt_with_ceaser_encryption(text=password, shift=self.password_shift)
        super().create_user(username, encrypted_password, userdata)


    def authenticate_user(self, username, input_password):
        user_data = self.get_user_record(username)
        if user_data:
            # Decrypting Stored Password to verify if the entered password is correct or not.
            original_password = self.decrypt_ceaser_encryption(text=user_data["password"], shift=self.password_shift)
            return self.verify_password(username, input_password, original_password)


    @staticmethod
    def encrypt_with_ceaser_encryption(text, shift):
        result = ""
        for char in text:

            if char.isupper():
                result += chr((ord(char) - 65 + shift ) % 26 + 65)

            elif char.islower() :
                result += chr((ord(char) - 97 + shift ) % 26 + 97)

        return result


    @staticmethod
    def decrypt_ceaser_encryption(text, shift):
        result = ""
        for char in text:

            if char.isupper():
                result += chr((ord(char) - 65 - shift ) % 26 + 65)

            elif char.islower() :
                result += chr((ord(char) - 97 - shift ) % 26 + 97)

        return result

