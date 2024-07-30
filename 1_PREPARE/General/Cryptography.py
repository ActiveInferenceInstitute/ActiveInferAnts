import hashlib
import hmac
import base64
import os
from typing import Tuple, Union

from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding, utils
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
from cryptography.exceptions import InvalidSignature

class CryptographyUtils:
    """
    A comprehensive collection of cryptographic utilities supporting advanced operations such as:
    - RSA key generation, encryption, decryption, and signing
    - Fernet symmetric encryption and decryption
    - Secure hashing mechanisms
    - HMAC generation and verification
    - Key derivation functions
    - Base64 encoding and decoding
    """

    RSA_KEY_SIZE = 2048
    RSA_PUBLIC_EXPONENT = 65537
    HASH_ALGORITHM = hashes.SHA256()
    SALT_SIZE = 16
    ITERATIONS = 100000

    @classmethod
    def generate_rsa_keys(cls) -> Tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
        """
        Generates and returns a pair of RSA keys (private and public).

        Returns:
            Tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]: A tuple containing the private and public RSA keys.
        """
        private_key = rsa.generate_private_key(
            public_exponent=cls.RSA_PUBLIC_EXPONENT,
            key_size=cls.RSA_KEY_SIZE,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def rsa_encrypt(public_key: rsa.RSAPublicKey, message: bytes) -> bytes:
        """
        Encrypts a message using the provided RSA public key.

        Args:
            public_key (rsa.RSAPublicKey): The RSA public key for encryption.
            message (bytes): The message to encrypt.

        Returns:
            bytes: The encrypted message.
        """
        return public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=CryptographyUtils.HASH_ALGORITHM),
                algorithm=CryptographyUtils.HASH_ALGORITHM,
                label=None
            )
        )

    @staticmethod
    def rsa_decrypt(private_key: rsa.RSAPrivateKey, encrypted_message: bytes) -> bytes:
        """
        Decrypts an encrypted message using the provided RSA private key.

        Args:
            private_key (rsa.RSAPrivateKey): The RSA private key for decryption.
            encrypted_message (bytes): The encrypted message to decrypt.

        Returns:
            bytes: The decrypted message.
        """
        return private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=CryptographyUtils.HASH_ALGORITHM),
                algorithm=CryptographyUtils.HASH_ALGORITHM,
                label=None
            )
        )

    @staticmethod
    def rsa_sign(private_key: rsa.RSAPrivateKey, message: bytes) -> bytes:
        """
        Signs a message using the provided RSA private key.

        Args:
            private_key (rsa.RSAPrivateKey): The RSA private key for signing.
            message (bytes): The message to sign.

        Returns:
            bytes: The signature.
        """
        return private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(CryptographyUtils.HASH_ALGORITHM),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            CryptographyUtils.HASH_ALGORITHM
        )

    @staticmethod
    def rsa_verify(public_key: rsa.RSAPublicKey, message: bytes, signature: bytes) -> bool:
        """
        Verifies a signature using the provided RSA public key.

        Args:
            public_key (rsa.RSAPublicKey): The RSA public key for verification.
            message (bytes): The original message.
            signature (bytes): The signature to verify.

        Returns:
            bool: True if the signature is valid, False otherwise.
        """
        try:
            public_key.verify(
                signature,
                message,
                padding.PSS(
                    mgf=padding.MGF1(CryptographyUtils.HASH_ALGORITHM),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                CryptographyUtils.HASH_ALGORITHM
            )
            return True
        except InvalidSignature:
            return False

    @staticmethod
    def generate_fernet_key() -> bytes:
        """
        Generates a Fernet key for symmetric encryption.

        Returns:
            bytes: The generated Fernet key.
        """
        return Fernet.generate_key()

    @staticmethod
    def fernet_encrypt(key: bytes, message: bytes) -> bytes:
        """
        Encrypts a message using the provided Fernet key.

        Args:
            key (bytes): The Fernet key for encryption.
            message (bytes): The message to encrypt.

        Returns:
            bytes: The encrypted message.
        """
        f = Fernet(key)
        return f.encrypt(message)

    @staticmethod
    def fernet_decrypt(key: bytes, encrypted_message: bytes) -> bytes:
        """
        Decrypts an encrypted message using the provided Fernet key.

        Args:
            key (bytes): The Fernet key for decryption.
            encrypted_message (bytes): The encrypted message to decrypt.

        Returns:
            bytes: The decrypted message.
        """
        f = Fernet(key)
        return f.decrypt(encrypted_message)

    @staticmethod
    def hash_message(message: Union[str, bytes]) -> bytes:
        """
        Hashes a message using SHA-256.

        Args:
            message (Union[str, bytes]): The message to hash.

        Returns:
            bytes: The hash of the message.
        """
        if isinstance(message, str):
            message = message.encode()
        digest = hashes.Hash(CryptographyUtils.HASH_ALGORITHM, backend=default_backend())
        digest.update(message)
        return digest.finalize()

    @staticmethod
    def hmac_message(key: bytes, message: Union[str, bytes]) -> bytes:
        """
        Generates an HMAC for a message using SHA-256.

        Args:
            key (bytes): The key for HMAC generation.
            message (Union[str, bytes]): The message to generate HMAC for.

        Returns:
            bytes: The HMAC of the message.
        """
        if isinstance(message, str):
            message = message.encode()
        return hmac.new(key, message, hashlib.sha256).digest()

    @staticmethod
    def verify_hmac(key: bytes, message: Union[str, bytes], hmac_value: bytes) -> bool:
        """
        Verifies an HMAC for a given message.

        Args:
            key (bytes): The key used for HMAC generation.
            message (Union[str, bytes]): The original message.
            hmac_value (bytes): The HMAC to verify.

        Returns:
            bool: True if the HMAC is valid, False otherwise.
        """
        if isinstance(message, str):
            message = message.encode()
        expected_hmac = CryptographyUtils.hmac_message(key, message)
        return hmac.compare_digest(expected_hmac, hmac_value)

    @classmethod
    def derive_key(cls, password: str, salt: bytes = None) -> Tuple[bytes, bytes]:
        """
        Derives a key from a password using PBKDF2.

        Args:
            password (str): The password to derive the key from.
            salt (bytes, optional): The salt for key derivation. If not provided, a random salt will be generated.

        Returns:
            Tuple[bytes, bytes]: A tuple containing the derived key and the salt used.
        """
        if salt is None:
            salt = os.urandom(cls.SALT_SIZE)
        kdf = PBKDF2HMAC(
            algorithm=cls.HASH_ALGORITHM,
            length=32,
            salt=salt,
            iterations=cls.ITERATIONS,
            backend=default_backend()
        )
        key = kdf.derive(password.encode())
        return key, salt

    @staticmethod
    def base64_encode(data: bytes) -> str:
        """
        Encodes bytes to a base64 string.

        Args:
            data (bytes): The data to encode.

        Returns:
            str: The base64 encoded string.
        """
        return base64.b64encode(data).decode()

    @staticmethod
    def base64_decode(data: str) -> bytes:
        """
        Decodes a base64 string to bytes.

        Args:
            data (str): The base64 encoded string to decode.

        Returns:
            bytes: The decoded data.
        """
        return base64.b64decode(data)
