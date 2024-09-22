import zlib
import json
import logging
from typing import Dict, Any

class CompressionService:
    """Service for compressing and decompressing JSON-compatible data."""

    def __init__(self, level: int = 9):
        """
        Initialize the CompressionService with a specified compression level.

        :param level: Compression level (1-9), where 9 is the highest compression.
        """
        self.level = level
        self.logger = logging.getLogger(self.__class__.__name__)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

    def compress(self, data: Dict[str, Any]) -> bytes:
        """
        Compress a dictionary into a bytes object using JSON serialization and zlib.

        :param data: The data to compress.
        :return: Compressed data as bytes.
        :raises ValueError: If serialization or compression fails.
        """
        try:
            json_data = json.dumps(data).encode('utf-8')
            self.logger.debug(f"Serializing data: {data}")
            compressed_data = zlib.compress(json_data, level=self.level)
            self.logger.info("Data compressed successfully.")
            return compressed_data
        except (TypeError, zlib.error) as e:
            self.logger.error(f"Compression failed: {e}")
            raise ValueError("Failed to compress data.") from e

    def decompress(self, compressed_data: bytes) -> Dict[str, Any]:
        """
        Decompress bytes back into a dictionary using zlib and JSON deserialization.

        :param compressed_data: The data to decompress.
        :return: Decompressed data as a dictionary.
        :raises ValueError: If decompression or deserialization fails.
        """
        try:
            decompressed_bytes = zlib.decompress(compressed_data)
            self.logger.debug(f"Decompressed bytes: {decompressed_bytes}")
            data = json.loads(decompressed_bytes.decode('utf-8'))
            self.logger.info("Data decompressed successfully.")
            return data
        except (zlib.error, json.JSONDecodeError) as e:
            self.logger.error(f"Decompression failed: {e}")
            raise ValueError("Failed to decompress data.") from e