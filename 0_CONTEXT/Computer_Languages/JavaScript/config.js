/**
 * Configuration management for Active Inference JavaScript implementation
 */

export class ConfigManager {
    constructor() {
        this.defaultConfig = {
            // Core parameters
            nStates: 4,
            nObservations: 3,
            nActions: 2,
            precision: 1.0,
            learningRate: 0.1,
            uncertaintyWeight: 0.1,

            // Advanced parameters
            maxIterations: 1000,
            convergenceThreshold: 1e-6,
            temperature: 1.0,
            explorationRate: 0.1,

            // Learning parameters
            useAdaptiveLearning: true,
            learningDecayRate: 0.99,
            minLearningRate: 0.001,

            // Logging and debugging
            enableLogging: false,
            logLevel: 'info', // 'debug', 'info', 'warn', 'error'
            logToFile: false,
            logFilePath: './logs/active_inference.log',

            // Performance monitoring
            enableProfiling: false,
            profileMemoryUsage: false,
            profileExecutionTime: true,

            // Visualization
            enableVisualization: false,
            visualizationUpdateInterval: 100,
            plotBeliefHistory: true,
            plotFreeEnergy: true,

            // Serialization
            saveHistory: true,
            saveInterval: 100,
            checkpointPath: './checkpoints/',

            // Multi-agent parameters
            enableMultiAgent: false,
            numAgents: 1,
            communicationRange: 1.0,
            cooperationWeight: 0.5,

            // Environment parameters
            environmentType: 'grid', // 'grid', 'continuous', 'discrete'
            environmentSize: [10, 10],
            obstacleDensity: 0.1,
            resourceDensity: 0.2,

            // Advanced features
            useGPUAcceleration: false,
            enableParallelProcessing: false,
            numThreads: 4,
            useWebWorkers: false
        };

        this.userConfig = {};
        this.loadedConfig = {};
    }

    /**
     * Load configuration from JSON file
     */
    async loadFromFile(filePath) {
        try {
            const response = await fetch(filePath);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const fileConfig = await response.json();
            this.userConfig = fileConfig;
            this.validateConfig();
            this.mergeConfigs();
            return true;
        } catch (error) {
            console.warn(`Could not load config from ${filePath}:`, error.message);
            this.mergeConfigs(); // Use defaults
            return false;
        }
    }

    /**
     * Save current configuration to file
     */
    async saveToFile(filePath) {
        try {
            const configToSave = { ...this.loadedConfig };
            const blob = new Blob([JSON.stringify(configToSave, null, 2)], {
                type: 'application/json'
            });

            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filePath.split('/').pop() || 'config.json';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);

            return true;
        } catch (error) {
            console.error('Could not save config:', error.message);
            return false;
        }
    }

    /**
     * Update configuration at runtime
     */
    updateConfig(newConfig) {
        this.userConfig = { ...this.userConfig, ...newConfig };
        this.validateConfig();
        this.mergeConfigs();
    }

    /**
     * Get configuration value
     */
    get(key, defaultValue = null) {
        return this.loadedConfig[key] !== undefined ? this.loadedConfig[key] : defaultValue;
    }

    /**
     * Get all configuration
     */
    getAll() {
        return { ...this.loadedConfig };
    }

    /**
     * Validate configuration
     */
    validateConfig() {
        const config = { ...this.defaultConfig, ...this.userConfig };

        // Validate core parameters
        if (config.nStates < 1) throw new Error('nStates must be positive');
        if (config.nObservations < 1) throw new Error('nObservations must be positive');
        if (config.nActions < 1) throw new Error('nActions must be positive');
        if (config.precision <= 0) throw new Error('precision must be positive');
        if (config.learningRate <= 0 || config.learningRate > 1) {
            throw new Error('learningRate must be in (0, 1]');
        }

        // Validate advanced parameters
        if (config.maxIterations < 1) throw new Error('maxIterations must be positive');
        if (config.convergenceThreshold <= 0) throw new Error('convergenceThreshold must be positive');
        if (config.temperature <= 0) throw new Error('temperature must be positive');
        if (config.explorationRate < 0 || config.explorationRate > 1) {
            throw new Error('explorationRate must be in [0, 1]');
        }

        // Validate learning parameters
        if (config.learningDecayRate <= 0 || config.learningDecayRate > 1) {
            throw new Error('learningDecayRate must be in (0, 1]');
        }
        if (config.minLearningRate < 0) throw new Error('minLearningRate must be non-negative');

        // Validate performance parameters
        if (config.numThreads < 1) throw new Error('numThreads must be positive');
        if (config.visualizationUpdateInterval < 1) {
            throw new Error('visualizationUpdateInterval must be positive');
        }
        if (config.saveInterval < 1) throw new Error('saveInterval must be positive');

        // Validate multi-agent parameters
        if (config.numAgents < 1) throw new Error('numAgents must be positive');
        if (config.communicationRange <= 0) throw new Error('communicationRange must be positive');
        if (config.cooperationWeight < 0 || config.cooperationWeight > 1) {
            throw new Error('cooperationWeight must be in [0, 1]');
        }

        // Validate environment parameters
        if (config.environmentSize.length !== 2) {
            throw new Error('environmentSize must be a 2-element array');
        }
        if (config.environmentSize[0] < 1 || config.environmentSize[1] < 1) {
            throw new Error('environment dimensions must be positive');
        }
        if (config.obstacleDensity < 0 || config.obstacleDensity > 1) {
            throw new Error('obstacleDensity must be in [0, 1]');
        }
        if (config.resourceDensity < 0 || config.resourceDensity > 1) {
            throw new Error('resourceDensity must be in [0, 1]');
        }
    }

    /**
     * Merge default and user configurations
     */
    mergeConfigs() {
        this.loadedConfig = { ...this.defaultConfig, ...this.userConfig };
    }

    /**
     * Reset to default configuration
     */
    reset() {
        this.userConfig = {};
        this.mergeConfigs();
    }

    /**
     * Create default configuration file
     */
    createDefaultConfig() {
        return { ...this.defaultConfig };
    }

    /**
     * Export configuration as JSON string
     */
    toJSON() {
        return JSON.stringify(this.loadedConfig, null, 2);
    }

    /**
     * Import configuration from JSON string
     */
    fromJSON(jsonString) {
        try {
            const config = JSON.parse(jsonString);
            this.userConfig = config;
            this.validateConfig();
            this.mergeConfigs();
            return true;
        } catch (error) {
            console.error('Invalid JSON configuration:', error.message);
            return false;
        }
    }

    /**
     * Get configuration summary
     */
    getSummary() {
        return {
            core: {
                states: this.loadedConfig.nStates,
                observations: this.loadedConfig.nObservations,
                actions: this.loadedConfig.nActions,
                precision: this.loadedConfig.precision,
                learningRate: this.loadedConfig.learningRate
            },
            advanced: {
                maxIterations: this.loadedConfig.maxIterations,
                convergenceThreshold: this.loadedConfig.convergenceThreshold,
                temperature: this.loadedConfig.temperature,
                explorationRate: this.loadedConfig.explorationRate
            },
            features: {
                logging: this.loadedConfig.enableLogging,
                profiling: this.loadedConfig.enableProfiling,
                visualization: this.loadedConfig.enableVisualization,
                multiAgent: this.loadedConfig.enableMultiAgent,
                gpuAcceleration: this.loadedConfig.useGPUAcceleration
            },
            environment: {
                type: this.loadedConfig.environmentType,
                size: this.loadedConfig.environmentSize,
                obstacleDensity: this.loadedConfig.obstacleDensity,
                resourceDensity: this.loadedConfig.resourceDensity
            }
        };
    }
}

// Create default instance
export const configManager = new ConfigManager();
