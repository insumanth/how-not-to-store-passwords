import hashlib
from password_manager import PasswordManager

class HashPasswordManager(PasswordManager):

    def __init__(self, database = "HashPasswordManager.toml", hash_algorithm = "md5"):
        super().__init__(database)
        self.hash_algorithm = hash_algorithm

    def get_hash_of_text(self, text):
        text_bytes = bytes(text, 'ascii')
        if self.hash_algorithm == "md5":
            hash = hashlib.md5(text_bytes).hexdigest()
        elif self.hash_algorithm == "sha1":
            hash = hashlib.sha1(text_bytes).hexdigest()
        elif self.hash_algorithm == "sha224":
            hash = hashlib.sha224(text_bytes).hexdigest()
        elif self.hash_algorithm == "sha256":
            hash = hashlib.sha256(text_bytes).hexdigest()
        elif self.hash_algorithm == "sha384":
            hash = hashlib.sha384(text_bytes).hexdigest()
        elif self.hash_algorithm == "sha512":
            hash = hashlib.sha512(text_bytes).hexdigest()
        elif self.hash_algorithm == "sha3_224":
            hash = hashlib.sha3_224(text_bytes).hexdigest()
        elif self.hash_algorithm == "sha3_256":
            hash = hashlib.sha3_256(text_bytes).hexdigest()
        elif self.hash_algorithm == "sha3_384":
            hash = hashlib.sha3_384(text_bytes).hexdigest()
        elif self.hash_algorithm == "sha3_512":
            hash = hashlib.sha3_512(text_bytes).hexdigest()
        elif self.hash_algorithm == "shake_128":
            hash = hashlib.shake_128(text_bytes).hexdigest(128)
        elif self.hash_algorithm == "shake_256":
            hash = hashlib.shake_256(text_bytes).hexdigest(256)
        elif self.hash_algorithm == "blake2b":
            hash = hashlib.blake2b(text_bytes).hexdigest()
        elif self.hash_algorithm == "blake2s":
            hash = hashlib.blake2s(text_bytes).hexdigest()
        else:
            print("Invalid Hashing Algorithm Specified. Using 'md5'")
            hash = hashlib.md5(text_bytes).hexdigest()

        return hash
