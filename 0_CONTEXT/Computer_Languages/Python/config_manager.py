#!/usr/bin/env python3
"""
Configuration management for Active Inference Python implementation
"""

import json
import os
import logging
from typing import Dict, Any, Optional
from dataclasses import dataclass, asdict
import yaml

@dataclass
class AgentConfig:
    """Configuration for Active Inference Agent"""
    n_states: int = 4
    n_observations: int = 3
    n_actions: int = 2
    precision: float = 1.0
    learning_rate: float = 0.1
    uncertainty_weight: float = 0.1

    # Advanced parameters
    max_iterations: int = 1000
    convergence_threshold: float = 1e-6
    temperature: float = 1.0
    exploration_rate: float = 0.1

    # Learning parameters
    use_adaptive_learning: bool = True
    learning_decay_rate: float = 0.99
    min_learning_rate: float = 0.001

    # Logging and debugging
    enable_logging: bool = False
    log_level: str = 'INFO'  # 'DEBUG', 'INFO', 'WARNING', 'ERROR'
    log_to_file: bool = False
    log_file_path: str = './logs/active_inference.log'

    # Performance monitoring
    enable_profiling: bool = False
    profile_memory_usage: bool = False
    profile_execution_time: bool = True

    # Visualization
    enable_visualization: bool = True
    visualization_update_interval: int = 100
    plot_belief_history: bool = True
    plot_free_energy: bool = True
    save_plots: bool = True
    plot_format: str = 'png'

    # Serialization
    save_history: bool = True
    save_interval: int = 100
    checkpoint_path: str = './checkpoints/'

    # Multi-agent parameters
    enable_multi_agent: bool = False
    num_agents: int = 1
    communication_range: float = 1.0
    cooperation_weight: float = 0.5

    # Environment parameters
    environment_type: str = 'grid'  # 'grid', 'continuous', 'discrete'
    environment_size: list = None
    obstacle_density: float = 0.1
    resource_density: float = 0.2

    # Advanced features
    use_gpu_acceleration: bool = False
    enable_parallel_processing: bool = False
    num_threads: int = 4
    use_multiprocessing: bool = False

    def __post_init__(self):
        if self.environment_size is None:
            self.environment_size = [10, 10]

        self._validate_config()

    def _validate_config(self):
        """Validate configuration parameters"""
        # Validate core parameters
        assert self.n_states > 0, "Number of states must be positive"
        assert self.n_observations > 0, "Number of observations must be positive"
        assert self.n_actions > 0, "Number of actions must be positive"
        assert self.precision > 0, "Precision must be positive"
        assert 0 < self.learning_rate <= 1, "Learning rate must be in (0, 1]"
        assert 0 <= self.uncertainty_weight <= 1, "Uncertainty weight must be in [0, 1]"

        # Validate advanced parameters
        assert self.max_iterations > 0, "Max iterations must be positive"
        assert self.convergence_threshold > 0, "Convergence threshold must be positive"
        assert self.temperature > 0, "Temperature must be positive"
        assert 0 <= self.exploration_rate <= 1, "Exploration rate must be in [0, 1]"

        # Validate learning parameters
        assert 0 < self.learning_decay_rate <= 1, "Learning decay rate must be in (0, 1]"
        assert self.min_learning_rate >= 0, "Minimum learning rate must be non-negative"

        # Validate performance parameters
        assert self.num_threads > 0, "Number of threads must be positive"
        assert self.visualization_update_interval > 0, "Visualization update interval must be positive"
        assert self.save_interval > 0, "Save interval must be positive"

        # Validate multi-agent parameters
        assert self.num_agents > 0, "Number of agents must be positive"
        assert self.communication_range > 0, "Communication range must be positive"
        assert 0 <= self.cooperation_weight <= 1, "Cooperation weight must be in [0, 1]"

        # Validate environment parameters
        assert len(self.environment_size) == 2, "Environment size must be 2D"
        assert all(dim > 0 for dim in self.environment_size), "Environment dimensions must be positive"
        assert 0 <= self.obstacle_density <= 1, "Obstacle density must be in [0, 1]"
        assert 0 <= self.resource_density <= 1, "Resource density must be in [0, 1]"


class ConfigManager:
    """Configuration manager for Active Inference"""

    def __init__(self):
        self.config_file = './config/active_inference_config.json'
        self.backup_dir = './config/backups/'
        self.config = AgentConfig()
        self.logger = logging.getLogger(__name__)

    def load_config(self, config_file: Optional[str] = None) -> bool:
        """Load configuration from file"""
        if config_file:
            self.config_file = config_file

        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)

            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    if self.config_file.endswith('.json'):
                        config_dict = json.load(f)
                    elif self.config_file.endswith(('.yml', '.yaml')):
                        import yaml
                        config_dict = yaml.safe_load(f)
                    else:
                        raise ValueError(f"Unsupported config file format: {self.config_file}")

                # Create config object from dictionary
                self.config = AgentConfig(**config_dict)
                self.logger.info(f"Configuration loaded from {self.config_file}")
                return True
            else:
                self.logger.warning(f"Config file not found: {self.config_file}. Using defaults.")
                return False

        except Exception as e:
            self.logger.error(f"Failed to load configuration: {e}")
            return False

    def save_config(self, config_file: Optional[str] = None) -> bool:
        """Save current configuration to file"""
        if config_file:
            self.config_file = config_file

        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            os.makedirs(self.backup_dir, exist_ok=True)

            # Create backup if file exists
            if os.path.exists(self.config_file):
                import shutil
                from datetime import datetime
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                backup_file = os.path.join(self.backup_dir, f'config_backup_{timestamp}.json')
                shutil.copy2(self.config_file, backup_file)

            # Save current configuration
            config_dict = asdict(self.config)

            with open(self.config_file, 'w') as f:
                if self.config_file.endswith('.json'):
                    json.dump(config_dict, f, indent=2)
                elif self.config_file.endswith(('.yml', '.yaml')):
                    import yaml
                    yaml.dump(config_dict, f, default_flow_style=False)
                else:
                    raise ValueError(f"Unsupported config file format: {self.config_file}")

            self.logger.info(f"Configuration saved to {self.config_file}")
            return True

        except Exception as e:
            self.logger.error(f"Failed to save configuration: {e}")
            return False

    def update_config(self, updates: Dict[str, Any]) -> bool:
        """Update configuration with new values"""
        try:
            # Create new config with updates
            current_dict = asdict(self.config)
            current_dict.update(updates)
            self.config = AgentConfig(**current_dict)
            self.logger.info("Configuration updated successfully")
            return True
        except Exception as e:
            self.logger.error(f"Failed to update configuration: {e}")
            return False

    def get_config(self) -> AgentConfig:
        """Get current configuration"""
        return self.config

    def reset_to_defaults(self):
        """Reset configuration to defaults"""
        self.config = AgentConfig()
        self.logger.info("Configuration reset to defaults")

    def create_default_config(self) -> Dict[str, Any]:
        """Create default configuration dictionary"""
        return asdict(AgentConfig())

    def validate_config(self) -> bool:
        """Validate current configuration"""
        try:
            # Create a new instance to trigger validation
            test_config = AgentConfig(**asdict(self.config))
            return True
        except Exception as e:
            self.logger.error(f"Configuration validation failed: {e}")
            return False

    def export_config(self, format: str = 'json') -> str:
        """Export configuration as string"""
        config_dict = asdict(self.config)

        if format.lower() == 'json':
            return json.dumps(config_dict, indent=2)
        elif format.lower() in ['yml', 'yaml']:
            try:
                import yaml
                return yaml.dump(config_dict, default_flow_style=False)
            except ImportError:
                raise ImportError("PyYAML is required for YAML export")
        else:
            raise ValueError(f"Unsupported export format: {format}")

    def import_config(self, config_str: str, format: str = 'json') -> bool:
        """Import configuration from string"""
        try:
            if format.lower() == 'json':
                config_dict = json.loads(config_str)
            elif format.lower() in ['yml', 'yaml']:
                import yaml
                config_dict = yaml.safe_load(config_str)
            else:
                raise ValueError(f"Unsupported import format: {format}")

            self.config = AgentConfig(**config_dict)
            self.logger.info("Configuration imported successfully")
            return True

        except Exception as e:
            self.logger.error(f"Failed to import configuration: {e}")
            return False

    def get_config_summary(self) -> Dict[str, Any]:
        """Get configuration summary"""
        config_dict = asdict(self.config)

        return {
            'core': {
                'states': config_dict['n_states'],
                'observations': config_dict['n_observations'],
                'actions': config_dict['n_actions'],
                'precision': config_dict['precision'],
                'learning_rate': config_dict['learning_rate']
            },
            'advanced': {
                'max_iterations': config_dict['max_iterations'],
                'convergence_threshold': config_dict['convergence_threshold'],
                'temperature': config_dict['temperature'],
                'exploration_rate': config_dict['exploration_rate']
            },
            'features': {
                'logging': config_dict['enable_logging'],
                'profiling': config_dict['enable_profiling'],
                'visualization': config_dict['enable_visualization'],
                'multi_agent': config_dict['enable_multi_agent'],
                'gpu_acceleration': config_dict['use_gpu_acceleration']
            },
            'environment': {
                'type': config_dict['environment_type'],
                'size': config_dict['environment_size'],
                'obstacle_density': config_dict['obstacle_density'],
                'resource_density': config_dict['resource_density']
            }
        }

    def list_config_files(self) -> list:
        """List available configuration files"""
        config_dir = os.path.dirname(self.config_file)
        if not os.path.exists(config_dir):
            return []

        files = []
        for filename in os.listdir(config_dir):
            if filename.endswith(('.json', '.yml', '.yaml')):
                files.append(os.path.join(config_dir, filename))

        return sorted(files)

    def load_config_from_name(self, name: str) -> bool:
        """Load configuration by name"""
        config_dir = os.path.dirname(self.config_file)

        for ext in ['.json', '.yml', '.yaml']:
            config_path = os.path.join(config_dir, f"{name}{ext}")
            if os.path.exists(config_path):
                return self.load_config(config_path)

        self.logger.error(f"Configuration '{name}' not found")
        return False

    def create_config_template(self, filename: str = 'config_template.json') -> bool:
        """Create a configuration template file"""
        try:
            template_path = os.path.join(os.path.dirname(self.config_file), filename)
            os.makedirs(os.path.dirname(template_path), exist_ok=True)

            template = self.create_default_config()

            # Add comments to template
            template_with_comments = {
                "_comment": "Active Inference Configuration Template",
                "_description": "This file contains all available configuration options",
                **template
            }

            with open(template_path, 'w') as f:
                json.dump(template_with_comments, f, indent=2)

            self.logger.info(f"Configuration template created: {template_path}")
            return True

        except Exception as e:
            self.logger.error(f"Failed to create configuration template: {e}")
            return False


# Create default instance
config_manager = ConfigManager()
