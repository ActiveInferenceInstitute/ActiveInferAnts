/**
 * Serialization utilities for Active Inference JavaScript implementation
 */

export class Serializer {
    constructor(config = {}) {
        this.format = config.format || 'json'; // 'json', 'binary', 'compressed'
        this.enableCompression = config.enableCompression || false;
        this.checkpointPath = config.checkpointPath || './checkpoints/';
        this.maxCheckpoints = config.maxCheckpoints || 10;
        this.enableVersioning = config.enableVersioning || true;
        this.version = '1.0.0';
    }

    /**
     * Serialize agent state
     */
    serialize(agent, options = {}) {
        const state = {
            version: this.version,
            timestamp: new Date().toISOString(),
            config: agent.config || {},
            beliefs: agent.getBeliefs(),
            history: agent.getHistory ? agent.getHistory() : {},
            statistics: agent.getStatistics ? agent.getStatistics() : {},
            metadata: {
                serializedBy: 'ActiveInferenceJavaScript',
                format: this.format,
                compressed: this.enableCompression,
                ...options.metadata
            }
        };

        switch (this.format) {
            case 'json':
                return this.serializeToJSON(state);
            case 'binary':
                return this.serializeToBinary(state);
            case 'compressed':
                return this.serializeToCompressed(state);
            default:
                throw new Error(`Unsupported serialization format: ${this.format}`);
        }
    }

    /**
     * Deserialize agent state
     */
    deserialize(data, agentClass = null) {
        let state;

        // Detect format and deserialize
        if (typeof data === 'string') {
            // JSON format
            state = JSON.parse(data);
        } else if (data instanceof ArrayBuffer || data instanceof Uint8Array) {
            // Binary format
            state = this.deserializeFromBinary(data);
        } else if (typeof data === 'object' && data.compressed) {
            // Compressed format
            state = this.deserializeFromCompressed(data);
        } else {
            throw new Error('Unknown serialization format');
        }

        // Validate version compatibility
        if (this.enableVersioning && state.version !== this.version) {
            console.warn(`Version mismatch: expected ${this.version}, got ${state.version}`);
        }

        // Create agent if class provided
        if (agentClass) {
            const agent = new agentClass(state.config);
            agent.setBeliefs(state.beliefs);
            if (agent.setHistory && state.history) {
                agent.setHistory(state.history);
            }
            return agent;
        }

        return state;
    }

    /**
     * Serialize to JSON
     */
    serializeToJSON(state) {
        return JSON.stringify(state, null, 2);
    }

    /**
     * Serialize to binary format
     */
    serializeToBinary(state) {
        const encoder = new TextEncoder();
        const jsonString = JSON.stringify(state);
        return encoder.encode(jsonString);
    }

    /**
     * Serialize to compressed format
     */
    async serializeToCompressed(state) {
        const jsonString = JSON.stringify(state);
        const encoder = new TextEncoder();
        const data = encoder.encode(jsonString);

        if (typeof CompressionStream !== 'undefined') {
            // Use built-in compression if available
            const stream = new CompressionStream('gzip');
            const writer = stream.writable.getWriter();
            const reader = stream.readable.getReader();

            writer.write(data);
            writer.close();

            const chunks = [];
            let done = false;
            while (!done) {
                const { value, done: readerDone } = await reader.read();
                if (!readerDone) {
                    chunks.push(value);
                }
                done = readerDone;
            }

            return {
                compressed: true,
                data: new Uint8Array(chunks.reduce((acc, chunk) => acc + chunk.length, 0)),
                originalSize: data.length
            };
        } else {
            // Fallback to basic encoding
            return {
                compressed: true,
                data: data,
                originalSize: data.length,
                note: 'Compression not supported, using uncompressed data'
            };
        }
    }

    /**
     * Deserialize from binary format
     */
    deserializeFromBinary(data) {
        const decoder = new TextDecoder();
        const jsonString = decoder.decode(data);
        return JSON.parse(jsonString);
    }

    /**
     * Deserialize from compressed format
     */
    async deserializeFromCompressed(data) {
        if (typeof DecompressionStream !== 'undefined') {
            const stream = new DecompressionStream('gzip');
            const writer = stream.writable.getWriter();
            const reader = stream.readable.getReader();

            writer.write(data.data);
            writer.close();

            const chunks = [];
            let done = false;
            while (!done) {
                const { value, done: readerDone } = await reader.read();
                if (!readerDone) {
                    chunks.push(value);
                }
                done = readerDone;
            }

            const decompressedData = new Uint8Array(chunks.reduce((acc, chunk) => acc + chunk.length, 0));
            const decoder = new TextDecoder();
            return JSON.parse(decoder.decode(decompressedData));
        } else {
            // Fallback
            const decoder = new TextDecoder();
            return JSON.parse(decoder.decode(data.data));
        }
    }

    /**
     * Save agent state to file
     */
    async saveToFile(agent, filename = null) {
        if (typeof window !== 'undefined') {
            throw new Error('File operations not supported in browser environment');
        }

        const fs = await import('fs');
        const path = await import('path');

        // Create checkpoint directory if it doesn't exist
        if (!fs.existsSync(this.checkpointPath)) {
            fs.mkdirSync(this.checkpointPath, { recursive: true });
        }

        // Generate filename with timestamp
        const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
        const actualFilename = filename || `checkpoint_${timestamp}.${this.getFileExtension()}`;

        const filePath = path.join(this.checkpointPath, actualFilename);

        // Serialize agent
        const serializedData = this.serialize(agent);

        // Write to file
        if (this.format === 'binary') {
            fs.writeFileSync(filePath, Buffer.from(serializedData));
        } else {
            fs.writeFileSync(filePath, serializedData);
        }

        // Manage checkpoint rotation
        await this.rotateCheckpoints();

        return filePath;
    }

    /**
     * Load agent state from file
     */
    async loadFromFile(filePath, agentClass = null) {
        if (typeof window !== 'undefined') {
            throw new Error('File operations not supported in browser environment');
        }

        const fs = await import('fs');
        const path = await import('path');

        const fullPath = path.resolve(filePath);

        if (!fs.existsSync(fullPath)) {
            throw new Error(`Checkpoint file not found: ${fullPath}`);
        }

        let data;
        if (this.format === 'binary') {
            data = fs.readFileSync(fullPath);
        } else {
            data = fs.readFileSync(fullPath, 'utf8');
        }

        return this.deserialize(data, agentClass);
    }

    /**
     * List available checkpoints
     */
    async listCheckpoints() {
        if (typeof window !== 'undefined') {
            throw new Error('File operations not supported in browser environment');
        }

        const fs = await import('fs');
        const path = await import('path');

        if (!fs.existsSync(this.checkpointPath)) {
            return [];
        }

        const files = fs.readdirSync(this.checkpointPath);
        const extension = this.getFileExtension();

        return files
            .filter(file => file.endsWith(`.${extension}`))
            .map(file => ({
                filename: file,
                path: path.join(this.checkpointPath, file),
                stats: fs.statSync(path.join(this.checkpointPath, file))
            }))
            .sort((a, b) => b.stats.mtime.getTime() - a.stats.mtime.getTime());
    }

    /**
     * Rotate checkpoints (remove old ones)
     */
    async rotateCheckpoints() {
        const checkpoints = await this.listCheckpoints();

        if (checkpoints.length > this.maxCheckpoints) {
            const fs = await import('fs');

            // Remove oldest checkpoints
            const toRemove = checkpoints.slice(this.maxCheckpoints);
            for (const checkpoint of toRemove) {
                fs.unlinkSync(checkpoint.path);
            }
        }
    }

    /**
     * Save to browser localStorage
     */
    saveToLocalStorage(agent, key = 'activeInferenceAgent') {
        if (typeof window === 'undefined') {
            throw new Error('localStorage only available in browser environment');
        }

        try {
            const serializedData = this.serialize(agent);
            const dataToStore = {
                data: serializedData,
                format: this.format,
                timestamp: new Date().toISOString()
            };
            localStorage.setItem(key, JSON.stringify(dataToStore));
            return true;
        } catch (error) {
            console.error('Failed to save to localStorage:', error.message);
            return false;
        }
    }

    /**
     * Load from browser localStorage
     */
    loadFromLocalStorage(key = 'activeInferenceAgent', agentClass = null) {
        if (typeof window === 'undefined') {
            throw new Error('localStorage only available in browser environment');
        }

        try {
            const stored = localStorage.getItem(key);
            if (!stored) {
                throw new Error(`No data found for key: ${key}`);
            }

            const data = JSON.parse(stored);
            return this.deserialize(data.data, agentClass);
        } catch (error) {
            console.error('Failed to load from localStorage:', error.message);
            return null;
        }
    }

    /**
     * Export agent state for sharing
     */
    exportForSharing(agent) {
        const state = this.serialize(agent);
        return btoa(JSON.stringify({
            version: this.version,
            format: this.format,
            data: state,
            timestamp: new Date().toISOString()
        }));
    }

    /**
     * Import agent state from shared data
     */
    importFromShared(sharedData, agentClass = null) {
        try {
            const decoded = JSON.parse(atob(sharedData));
            return this.deserialize(decoded.data, agentClass);
        } catch (error) {
            console.error('Failed to import shared data:', error.message);
            return null;
        }
    }

    /**
     * Get file extension for current format
     */
    getFileExtension() {
        switch (this.format) {
            case 'json': return 'json';
            case 'binary': return 'bin';
            case 'compressed': return 'gz';
            default: return 'dat';
        }
    }

    /**
     * Validate serialized data
     */
    validateSerializedData(data) {
        try {
            const state = typeof data === 'string' ? JSON.parse(data) : this.deserialize(data);

            // Check required fields
            const required = ['version', 'config', 'beliefs'];
            for (const field of required) {
                if (!(field in state)) {
                    throw new Error(`Missing required field: ${field}`);
                }
            }

            // Validate beliefs
            if (!Array.isArray(state.beliefs) || state.beliefs.length === 0) {
                throw new Error('Invalid beliefs format');
            }

            // Check belief normalization
            const sum = state.beliefs.reduce((a, b) => a + b, 0);
            if (Math.abs(sum - 1.0) > 1e-6) {
                console.warn('Beliefs are not normalized');
            }

            return true;
        } catch (error) {
            console.error('Validation failed:', error.message);
            return false;
        }
    }

    /**
     * Create a snapshot with metadata
     */
    createSnapshot(agent, metadata = {}) {
        return this.serialize(agent, {
            metadata: {
                snapshot: true,
                description: metadata.description || '',
                tags: metadata.tags || [],
                userDefined: metadata.userDefined || {},
                ...metadata
            }
        });
    }

    /**
     * Compare two serialized states
     */
    compareStates(state1, state2) {
        const s1 = typeof state1 === 'string' ? JSON.parse(state1) : state1;
        const s2 = typeof state2 === 'string' ? JSON.parse(state2) : state2;

        return {
            beliefsDifference: this.arrayDifference(s1.beliefs, s2.beliefs),
            configDifference: this.objectDifference(s1.config, s2.config),
            timestampDifference: new Date(s1.timestamp) - new Date(s2.timestamp),
            versionCompatible: s1.version === s2.version
        };
    }

    /**
     * Helper: Calculate difference between arrays
     */
    arrayDifference(arr1, arr2) {
        if (arr1.length !== arr2.length) {
            return { different: true, reason: 'different lengths' };
        }

        const differences = arr1.map((val, i) => Math.abs(val - arr2[i]));
        const maxDifference = Math.max(...differences);

        return {
            different: maxDifference > 1e-6,
            maxDifference,
            meanDifference: differences.reduce((a, b) => a + b, 0) / differences.length
        };
    }

    /**
     * Helper: Calculate difference between objects
     */
    objectDifference(obj1, obj2) {
        const keys1 = Object.keys(obj1);
        const keys2 = Object.keys(obj2);
        const allKeys = [...new Set([...keys1, ...keys2])];

        const differences = {};
        for (const key of allKeys) {
            if (!(key in obj1)) {
                differences[key] = { type: 'missing_in_first', value: obj2[key] };
            } else if (!(key in obj2)) {
                differences[key] = { type: 'missing_in_second', value: obj1[key] };
            } else if (obj1[key] !== obj2[key]) {
                differences[key] = { type: 'different', value1: obj1[key], value2: obj2[key] };
            }
        }

        return differences;
    }
}

// Create default serializer instance
export const serializer = new Serializer();
