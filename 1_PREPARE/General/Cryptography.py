import hashlib
import hmac
import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

class CryptographyUtils:
    """
    A collection of cryptographic utilities supporting advanced operations such as RSA key generation,
    RSA encryption/decryption, Fernet symmetric encryption/decryption, and secure hashing mechanisms.
    """

    RSA_KEY_SIZE = 2048
    RSA_PUBLIC_EXPONENT = 65537
    HASH_ALGORITHM = hashes.SHA256()

    @classmethod
    def generate_rsa_keys(cls):
        """
        Generates and returns a pair of RSA keys (private and public).
        """
        private_key = rsa.generate_private_key(
            public_exponent=cls.RSA_PUBLIC_EXPONENT,
            key_size=cls.RSA_KEY_SIZE,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def rsa_encrypt(public_key, message):
        """
        Encrypts a message using the provided RSA public key.
        """
        return public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=EnhancedCryptographyUtils.HASH_ALGORITHM),
                algorithm=EnhancedCryptographyUtils.HASH_ALGORITHM,
                label=None
            )
        )

    @staticmethod
    def rsa_decrypt(private_key, encrypted_message):
        """
        Decrypts an encrypted message using the provided RSA private key.
        """
        return private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=EnhancedCryptographyUtils.HASH_ALGORITHM),
                algorithm=EnhancedCryptographyUtils.HASH_ALGORITHM,
                label=None
            )
        )

    @staticmethod
    def generate_fernet_key():
        """
        Generates a Fernet key for symmetric encryption and returns it.
        """
        return Fernet.generate_key()

    @staticmethod
    def fernet_encrypt(key, message):
        """
        Encrypts a message using the provided Fernet key.
        """
        f = Fernet(key)
        return f.encrypt(message)

    @staticmethod
    def fernet_decrypt(key, encrypted_message):
        """
        Decrypts an encrypted message using the provided Fernet key.
        """
        f = Fernet(key)
        return f.decrypt(encrypted_message)

    @staticmethod
    def hash_message(message):
        """
        Hashes a message using SHA-256 and returns the hash.
        """
        digest = hashes.Hash(EnhancedCryptographyUtils.HASH_ALGORITHM, backend=default_backend())
        digest.update(message)
        return digest.finalize()

    @staticmethod
    def hmac_message(key, message):
        """
        Generates an HMAC for a message using SHA-256 and returns it.
        """
        return hmac.new(key, message, hashlib.sha256).digest()
