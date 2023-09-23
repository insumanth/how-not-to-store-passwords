import sys
from pathlib import Path
sys.path.append(str(Path(f"{__file__}").parent.parent))
# import my_module

from cryptography.fernet import Fernet
from password_manager import PasswordManager
import base64

class EncryptionPasswordManager(PasswordManager):

    def __init__(self, database = "EncryptionPasswordManager.toml"):
        super().__init__(database)
        key = Fernet.generate_key()
        self.fernet = Fernet(key)



    def create_user(self, username, password, userdata):
        # Encrypting and Storing Passwords.
        encrypted_password = self.encrypt_text(password)
        super().create_user(username, encrypted_password, userdata)


    def authenticate_user(self, username, input_password):
        user_data = self.get_user_record(username)
        if user_data:
            # Decrypting Stored Password to verify if the entered password is correct or not.
            original_password = self.decrypt_text(user_data["password"])
            return self.verify_password(username, input_password, original_password)



    def encrypt_text(self, text):
        text_bytes = bytes(text, 'ascii')
        encrypted_bytes = self.fernet.encrypt(text_bytes)
        return encrypted_bytes.decode("ascii")



    def decrypt_text(self, text):
        text_bytes = bytes(text, 'ascii')
        decrypted_bytes = self.fernet.decrypt(text_bytes)
        return decrypted_bytes.decode("ascii")





