from Utils.security_base import SecurityConfigSchema
from enum import Enum

class EnvironmentTier(Enum):
    PRODUCTION = "prod"
    STAGING = "stage"
    DEVELOPMENT = "dev"

class ProductionSecurityPolicy(SecurityConfigSchema):
    """Tiered security policy with environment-specific rules"""
    
    def __init__(self, tier: EnvironmentTier = EnvironmentTier.PRODUCTION):
        super().__init__()
        self.tier = tier
        self._apply_tier_settings()
        
    def _apply_tier_settings(self):
        """Dynamic policy configuration based on environment tier"""
        tier_configs = {
            EnvironmentTier.PRODUCTION: {
                'min_password_length': 16,
                'hash_iterations': 1_200_000,
                'key_rotation_interval': 30,
                'allowed_algorithms': {
                    'encryption': ['AES-256-GCM', 'ChaCha20-Poly1305'],
                    'hashing': ['argon2', 'scrypt']
                },
                'audit_log_retention': 365  # Days
            },
            EnvironmentTier.STAGING: {
                'hash_iterations': 600_000,
                'key_rotation_interval': 60
            },
            EnvironmentTier.DEVELOPMENT: {
                'min_password_length': 8,
                'hash_iterations': 100_000,
                'audit_log_retention': 7
            }
        }
        self.update(tier_configs[self.tier])

class CompliancePreset:
    """Pre-configured compliance templates"""
    
    @classmethod
    def hipaa_compliant(cls):
        policy = ProductionSecurityPolicy()
        policy.update({
            'audit_log_retention': 6 * 365,  # 6 years
            'encryption_required': True,
            'allowed_algorithms': {
                'encryption': ['AES-256-GCM'],
                'hashing': ['argon2']
            }
        })
        return policy
    
    @classmethod
    def gdpr_compliant(cls):
        policy = ProductionSecurityPolicy()
        policy.update({
            'data_anonymization': True,
            'right_to_be_forgotten': True,
            'audit_log_encryption': True
        })
        return policy 