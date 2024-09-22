import hashlib
from typing import Callable

class HashingService:
    # Initialize with a specific hash function, default to SHA-256
    def __init__(self, hash_function: Callable[[bytes], str] = None):
        self.hash_function = hash_function or self.compute_sha256

    # Compute SHA-256 hash
    def compute_sha256(self, data: bytes) -> str:
        return hashlib.sha256(data).hexdigest()

    # Compute hash using the configured hash function
    def compute_hash(self, data: bytes) -> str:
        if not isinstance(data, bytes):
            raise TypeError("Data must be bytes.")
        return self.hash_function(data)