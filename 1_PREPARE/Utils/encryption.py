import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend


class EncryptionService:
    """
    A service that provides encryption and decryption functionalities using Fernet symmetric encryption.
    """

    def __init__(
        self,
        password: bytes = b"this_is_a_secure_password",
        salt: bytes = b"secure_salt",
        iterations: int = 100_000,
        algorithm=hashes.SHA256(),
    ):
        """
        Initializes the EncryptionService with a derived key and Fernet instance.

        :param password: The password used for key derivation.
        :param salt: The salt used for key derivation.
        :param iterations: Number of iterations for the key derivation function.
        :param algorithm: The hash algorithm to use for key derivation.
        """
        self.key = self._derive_key(password, salt, iterations, algorithm)
        self.fernet = Fernet(self.key)

    def _derive_key(
        self, password: bytes, salt: bytes, iterations: int, algorithm
    ) -> bytes:
        """
        Derives a cryptographic key from the given password and salt using PBKDF2HMAC.

        :param password: The password to derive the key from.
        :param salt: The salt to use in key derivation.
        :param iterations: Number of iterations for the key derivation function.
        :param algorithm: The hash algorithm to use.
        :return: A base64-url encoded derived key.
        """
        kdf = PBKDF2HMAC(
            algorithm=algorithm,
            length=32,
            salt=salt,
            iterations=iterations,
            backend=default_backend(),
        )
        derived_key = kdf.derive(password)
        return base64.urlsafe_b64encode(derived_key)

    def encrypt(self, data: bytes) -> bytes:
        """
        Encrypts the given data using Fernet encryption.

        :param data: Data to encrypt.
        :return: Encrypted data as bytes.
        """
        return self.fernet.encrypt(data)

    def decrypt(self, token: bytes) -> bytes:
        """
        Decrypts the given token using Fernet decryption.

        :param token: Encrypted data to decrypt.
        :return: Decrypted data as bytes.
        :raises: cryptography.fernet.InvalidToken if the token is invalid.
        """
        return self.fernet.decrypt(token)