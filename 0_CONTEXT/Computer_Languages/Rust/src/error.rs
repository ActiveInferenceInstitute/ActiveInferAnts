//! Error types and handling for the Active Inference library

use std::fmt;

/// Custom error types for the active inference agent
#[derive(thiserror::Error, Debug)]
pub enum AgentError {
    #[error("Invalid probability distribution: sum = {sum}")]
    InvalidProbability { sum: f64 },
    #[error("Numerical computation error: {message}")]
    NumericalError { message: String },
    #[error("Dimension mismatch: expected {expected}, got {actual}")]
    DimensionMismatch { expected: usize, actual: usize },
    #[error("Simulation error: {message}")]
    SimulationError { message: String },
    #[error("Configuration error: {message}")]
    ConfigError { message: String },
    #[error("I/O error: {0}")]
    Io(#[from] std::io::Error),
    #[error("Serialization error: {0}")]
    Serde(#[from] serde_json::Error),
}

/// Result type alias for convenience
pub type Result<T> = std::result::Result<T, AgentError>;

/// Error handling utilities
pub struct ErrorHandler;

impl ErrorHandler {
    /// Check if a probability distribution is valid
    pub fn validate_probability_distribution(distribution: &[f64]) -> Result<()> {
        let sum: f64 = distribution.iter().sum();

        if !(0.99..=1.01).contains(&sum) {
            return Err(AgentError::InvalidProbability { sum });
        }

        // Check for negative probabilities
        for (i, &prob) in distribution.iter().enumerate() {
            if prob < 0.0 {
                return Err(AgentError::NumericalError {
                    message: format!("Negative probability at index {}: {}", i, prob),
                });
            }
        }

        Ok(())
    }

    /// Handle numerical errors gracefully
    pub fn handle_numerical_error(operation: &str, value: f64) -> Result<f64> {
        if !value.is_finite() {
            return Err(AgentError::NumericalError {
                message: format!("Non-finite value in {}: {}", operation, value),
            });
        }

        if value.is_nan() {
            return Err(AgentError::NumericalError {
                message: format!("NaN value in {}", operation),
            });
        }

        Ok(value)
    }

    /// Check array dimensions
    pub fn check_dimensions(actual: usize, expected: usize, context: &str) -> Result<()> {
        if actual != expected {
            return Err(AgentError::DimensionMismatch {
                expected,
                actual,
            });
        }
        Ok(())
    }

    /// Create a simulation error
    pub fn simulation_error(message: impl Into<String>) -> AgentError {
        AgentError::SimulationError {
            message: message.into(),
        }
    }

    /// Create a configuration error
    pub fn config_error(message: impl Into<String>) -> AgentError {
        AgentError::ConfigError {
            message: message.into(),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_valid_probability_distribution() {
        let valid_dist = vec![0.3, 0.4, 0.3];
        assert!(ErrorHandler::validate_probability_distribution(&valid_dist).is_ok());
    }

    #[test]
    fn test_invalid_probability_distribution() {
        let invalid_dist = vec![0.5, 0.6, 0.1]; // Sum = 1.2
        assert!(ErrorHandler::validate_probability_distribution(&invalid_dist).is_err());
    }

    #[test]
    fn test_negative_probability() {
        let negative_dist = vec![0.5, -0.1, 0.6];
        assert!(ErrorHandler::validate_probability_distribution(&negative_dist).is_err());
    }

    #[test]
    fn test_numerical_error_handling() {
        assert!(ErrorHandler::handle_numerical_error("test", f64::NAN).is_err());
        assert!(ErrorHandler::handle_numerical_error("test", f64::INFINITY).is_err());
        assert!(ErrorHandler::handle_numerical_error("test", 1.0).is_ok());
    }

    #[test]
    fn test_dimension_checking() {
        assert!(ErrorHandler::check_dimensions(5, 5, "test").is_ok());
        assert!(ErrorHandler::check_dimensions(5, 3, "test").is_err());
    }
}
