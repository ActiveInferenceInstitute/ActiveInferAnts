/**
 * Logging and debugging utilities for Active Inference JavaScript implementation
 */

export class Logger {
    constructor(config = {}) {
        this.logLevel = config.logLevel || 'info';
        this.enableFileLogging = config.enableFileLogging || false;
        this.logFilePath = config.logFilePath || './logs/active_inference.log';
        this.maxLogSize = config.maxLogSize || 1024 * 1024; // 1MB
        this.logBuffer = [];
        this.maxBufferSize = config.maxBufferSize || 1000;

        // Log level hierarchy
        this.levels = {
            'debug': 0,
            'info': 1,
            'warn': 2,
            'error': 3
        };

        // Performance tracking
        this.performanceMetrics = {
            startTime: Date.now(),
            operationCount: 0,
            totalExecutionTime: 0,
            memoryUsage: [],
            beliefUpdates: 0,
            actionSelections: 0,
            freeEnergyCalculations: 0
        };

        // Initialize file logging if enabled
        if (this.enableFileLogging) {
            this.initializeFileLogging();
        }
    }

    /**
     * Initialize file logging
     */
    async initializeFileLogging() {
        try {
            // Create logs directory if it doesn't exist
            const logDir = this.logFilePath.substring(0, this.logFilePath.lastIndexOf('/'));
            if (typeof window === 'undefined') {
                // Node.js environment
                const fs = await import('fs');
                if (!fs.existsSync(logDir)) {
                    fs.mkdirSync(logDir, { recursive: true });
                }
            }
        } catch (error) {
            console.warn('Could not initialize file logging:', error.message);
            this.enableFileLogging = false;
        }
    }

    /**
     * Log a message at the specified level
     */
    log(level, message, data = null) {
        if (this.levels[level] < this.levels[this.logLevel]) {
            return;
        }

        const logEntry = {
            timestamp: new Date().toISOString(),
            level: level.toUpperCase(),
            message: message,
            data: data,
            performance: this.getCurrentPerformanceMetrics()
        };

        // Add to buffer
        this.logBuffer.push(logEntry);
        if (this.logBuffer.length > this.maxBufferSize) {
            this.logBuffer.shift();
        }

        // Console logging
        const consoleMessage = `[${logEntry.timestamp}] ${logEntry.level}: ${message}`;
        switch (level) {
            case 'debug':
                console.debug(consoleMessage, data);
                break;
            case 'info':
                console.info(consoleMessage, data);
                break;
            case 'warn':
                console.warn(consoleMessage, data);
                break;
            case 'error':
                console.error(consoleMessage, data);
                break;
        }

        // File logging
        if (this.enableFileLogging) {
            this.writeToFile(logEntry);
        }

        // Update performance metrics
        this.performanceMetrics.operationCount++;
    }

    /**
     * Debug level logging
     */
    debug(message, data = null) {
        this.log('debug', message, data);
    }

    /**
     * Info level logging
     */
    info(message, data = null) {
        this.log('info', message, data);
    }

    /**
     * Warning level logging
     */
    warn(message, data = null) {
        this.log('warn', message, data);
    }

    /**
     * Error level logging
     */
    error(message, data = null) {
        this.log('error', message, data);
    }

    /**
     * Write log entry to file
     */
    async writeToFile(logEntry) {
        if (typeof window !== 'undefined') {
            // Browser environment - use localStorage or IndexedDB
            try {
                const logs = JSON.parse(localStorage.getItem('activeInferenceLogs') || '[]');
                logs.push(logEntry);
                // Keep only last 1000 entries
                if (logs.length > 1000) {
                    logs.splice(0, logs.length - 1000);
                }
                localStorage.setItem('activeInferenceLogs', JSON.stringify(logs));
            } catch (error) {
                console.warn('Could not write to localStorage:', error.message);
            }
            return;
        }

        // Node.js environment
        try {
            const fs = await import('fs');
            const logLine = JSON.stringify(logEntry) + '\n';
            fs.appendFileSync(this.logFilePath, logLine);

            // Rotate log file if it gets too large
            const stats = fs.statSync(this.logFilePath);
            if (stats.size > this.maxLogSize) {
                const backupPath = `${this.logFilePath}.${Date.now()}.bak`;
                fs.renameSync(this.logFilePath, backupPath);
            }
        } catch (error) {
            console.warn('Could not write to log file:', error.message);
        }
    }

    /**
     * Get current performance metrics
     */
    getCurrentPerformanceMetrics() {
        const memoryUsage = typeof performance !== 'undefined' && performance.memory
            ? {
                used: performance.memory.usedJSHeapSize,
                total: performance.memory.totalJSHeapSize,
                limit: performance.memory.jsHeapSizeLimit
            }
            : null;

        if (memoryUsage) {
            this.performanceMetrics.memoryUsage.push(memoryUsage);
            // Keep only last 100 memory measurements
            if (this.performanceMetrics.memoryUsage.length > 100) {
                this.performanceMetrics.memoryUsage.shift();
            }
        }

        return {
            operationCount: this.performanceMetrics.operationCount,
            memoryUsage: memoryUsage,
            beliefUpdates: this.performanceMetrics.beliefUpdates,
            actionSelections: this.performanceMetrics.actionSelections,
            freeEnergyCalculations: this.performanceMetrics.freeEnergyCalculations
        };
    }

    /**
     * Start performance profiling
     */
    startProfile(operationName) {
        if (!this.profilingEnabled) return null;

        const startTime = performance.now();
        this.debug(`Started profiling: ${operationName}`);

        return {
            operationName,
            startTime,
            stop: () => {
                const endTime = performance.now();
                const duration = endTime - startTime;
                this.performanceMetrics.totalExecutionTime += duration;

                this.debug(`Completed profiling: ${operationName}`, {
                    duration: `${duration.toFixed(2)}ms`,
                    totalOperations: this.performanceMetrics.operationCount
                });

                return duration;
            }
        };
    }

    /**
     * Track specific operation
     */
    trackOperation(operationType, data = null) {
        switch (operationType) {
            case 'beliefUpdate':
                this.performanceMetrics.beliefUpdates++;
                this.debug('Belief update performed', data);
                break;
            case 'actionSelection':
                this.performanceMetrics.actionSelections++;
                this.debug('Action selection performed', data);
                break;
            case 'freeEnergyCalculation':
                this.performanceMetrics.freeEnergyCalculations++;
                this.debug('Free energy calculation performed', data);
                break;
        }
    }

    /**
     * Get performance summary
     */
    getPerformanceSummary() {
        const uptime = Date.now() - this.performanceMetrics.startTime;
        const avgMemoryUsage = this.performanceMetrics.memoryUsage.length > 0
            ? this.performanceMetrics.memoryUsage.reduce((sum, mem) => sum + mem.used, 0) / this.performanceMetrics.memoryUsage.length
            : 0;

        return {
            uptime: `${(uptime / 1000).toFixed(1)}s`,
            totalOperations: this.performanceMetrics.operationCount,
            totalExecutionTime: `${this.performanceMetrics.totalExecutionTime.toFixed(2)}ms`,
            averageMemoryUsage: `${(avgMemoryUsage / 1024 / 1024).toFixed(2)}MB`,
            operationsPerSecond: (this.performanceMetrics.operationCount / (uptime / 1000)).toFixed(1),
            beliefUpdates: this.performanceMetrics.beliefUpdates,
            actionSelections: this.performanceMetrics.actionSelections,
            freeEnergyCalculations: this.performanceMetrics.freeEnergyCalculations
        };
    }

    /**
     * Export logs
     */
    exportLogs(format = 'json') {
        switch (format) {
            case 'json':
                return JSON.stringify(this.logBuffer, null, 2);
            case 'csv':
                if (this.logBuffer.length === 0) return '';

                const headers = Object.keys(this.logBuffer[0]).join(',');
                const rows = this.logBuffer.map(entry =>
                    Object.values(entry).map(val =>
                        typeof val === 'object' ? JSON.stringify(val) : val
                    ).join(',')
                ).join('\n');

                return `${headers}\n${rows}`;
            default:
                return this.logBuffer.map(entry =>
                    `[${entry.timestamp}] ${entry.level}: ${entry.message}`
                ).join('\n');
        }
    }

    /**
     * Clear logs
     */
    clearLogs() {
        this.logBuffer = [];
        if (this.enableFileLogging && typeof window === 'undefined') {
            // Clear file in Node.js
            try {
                const fs = require('fs');
                fs.writeFileSync(this.logFilePath, '');
            } catch (error) {
                console.warn('Could not clear log file:', error.message);
            }
        } else if (this.enableFileLogging) {
            // Clear localStorage in browser
            try {
                localStorage.removeItem('activeInferenceLogs');
            } catch (error) {
                console.warn('Could not clear localStorage logs:', error.message);
            }
        }
    }

    /**
     * Set log level
     */
    setLogLevel(level) {
        if (this.levels.hasOwnProperty(level)) {
            this.logLevel = level;
            this.info(`Log level changed to: ${level}`);
        } else {
            this.warn(`Invalid log level: ${level}`);
        }
    }

    /**
     * Enable or disable profiling
     */
    setProfilingEnabled(enabled) {
        this.profilingEnabled = enabled;
        this.info(`Performance profiling ${enabled ? 'enabled' : 'disabled'}`);
    }

    /**
     * Create a child logger with context
     */
    createChildLogger(context) {
        const childLogger = Object.create(this);
        childLogger.context = context;

        // Override log method to include context
        const originalLog = childLogger.log.bind(childLogger);
        childLogger.log = (level, message, data = null) => {
            const contextualMessage = `[${context}] ${message}`;
            originalLog(level, contextualMessage, data);
        };

        return childLogger;
    }
}

// Create default logger instance
export const logger = new Logger();
