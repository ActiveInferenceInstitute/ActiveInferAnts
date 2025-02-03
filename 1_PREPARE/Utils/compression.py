import zlib
import json
import logging
from typing import Dict, Any, Optional
from .security_base import SecurityServiceBase, SecurityConfigurationError
import clamd
import re

class CompressionService(SecurityServiceBase):
    """Security-hardened compression service with resource limits"""

    def __init__(
        self,
        service_name: str = "DefaultCompressor",
        level: int = 9,
        logger: Optional[logging.Logger] = None,
        max_ratio: Optional[float] = None,
        av_scanner: str = None
    ):
        super().__init__(service_name, logger)
        self.level = self._validate_compression_level(level)
        self.max_ratio = max_ratio or self._config.max_compression_ratio
        self.av_scanner = clamd.ClamdNetworkSocket() if av_scanner else None
        self.logger.info(f"Initialized with compression level {self.level}")

    def _validate_compression_level(self, level: int) -> int:
        if not 1 <= level <= 9:
            raise SecurityConfigurationError(
                f"Invalid compression level {level} - must be 1-9"
            )
        return level

    def compress(self, data: Dict[str, Any]) -> bytes:
        """Compress with size validation and audit logging"""
        self._pre_operation_check('compress', data)
        try:
            json_data = json.dumps(data).encode('utf-8')
            compressed = zlib.compress(json_data, level=self.level)
            ratio = len(json_data) / len(compressed)
            
            if ratio > self.max_ratio:
                self.log_audit_event("COMPRESSION_RATIO_EXCEEDED", {
                    "ratio": ratio,
                    "max_allowed": self.max_ratio
                })
                raise SecurityConfigurationError(
                    f"Compression ratio {ratio:.1f}x exceeds safety limit"
                )
                
            self.log_audit_event("COMPRESSION_SUCCESS", {
                "original_size": len(json_data),
                "compressed_size": len(compressed)
            })
            return compressed
        except Exception as e:
            self.log_audit_event("COMPRESSION_FAILURE", {"error": str(e)})
            raise

    def decompress(self, compressed_data: bytes) -> Dict[str, Any]:
        """Decompress with anti-bomb protection and malware scanning"""
        self._pre_operation_check('decompress', compressed_data)
        try:
            # Create decompression object with size limits
            decompressor = zlib.decompressobj()
            max_output = len(compressed_data) * self.max_ratio
            output = decompressor.decompress(compressed_data, max_output)
            
            if decompressor.unconsumed_tail:
                self.log_audit_event("DECOMPRESSION_BOMB_ATTEMPT", {
                    "received_size": len(compressed_data),
                    "processed_size": len(output)
                })
                raise SecurityConfigurationError(
                    "Potential decompression bomb detected"
                )
                
            if self.av_scanner:
                scan_result = self.av_scanner.instream(compressed_data)
                if scan_result['stream'][0] == 'FOUND':
                    self.log_audit_event("MALWARE_DETECTED", scan_result)
                    raise SecurityConfigurationError("Malicious content detected")
                
            return json.loads(output.decode('utf-8'))
        except Exception as e:
            self.log_audit_event("DECOMPRESSION_FAILURE", {"error": str(e)})
            raise

    def _pre_operation_check(self, operation: str, data: Any):
        """Common security checks for all operations"""
        self.operation_counter += 1
        if not data:
            self.log_audit_event("EMPTY_INPUT", {"operation": operation})
            raise ValueError("Input data cannot be empty")
            
        if isinstance(data, dict) and operation == 'compress':
            self._validate_json_content(data)

    def _validate_json_content(self, data: dict):
        """Prevent serialization of dangerous objects"""
        if any(isinstance(v, (bytes, bytearray)) for v in data.values()):
            self.log_audit_event("UNSAFE_JSON_CONTENT", {"data_types": str(type(v) for v in data.values())})
            raise SecurityConfigurationError("JSON data contains binary content")

    def validate_content_policy(self, data: dict) -> bool:
        """GDPR-aware content validation"""
        if self._config.data_anonymization:
            return self._check_pii_absence(data)
        return True

    def _check_pii_absence(self, data: dict) -> bool:
        """Pattern-based PII detection"""
        pii_patterns = [
            r'\b\d{3}-\d{2}-\d{4}\b',  # SSN
            r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  # Email
        ]
        data_str = str(data)
        return not any(re.search(p, data_str) for p in pii_patterns)