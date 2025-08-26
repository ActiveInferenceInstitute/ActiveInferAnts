# Active Inference Implementation in SQL

This directory contains a database-driven SQL implementation of active inference demonstrating declarative programming and data persistence.

## Overview

The SQL implementation provides:
- Declarative active inference modeling
- Database-driven belief state management
- Set-based operations for belief updates
- Stored procedures for complex algorithms

## Core Components

- **SQL.sql**: Complete active inference database schema and procedures

## Architecture

### Database Schema
The implementation uses a comprehensive relational database design:

```sql
-- Core tables for active inference
CREATE TABLE states (
    state_id INTEGER PRIMARY KEY,
    state_name VARCHAR(50),
    prior_probability DECIMAL(10,6)
);

CREATE TABLE observations (
    observation_id INTEGER PRIMARY KEY,
    observation_name VARCHAR(50),
    preference_value DECIMAL(10,6)
);

CREATE TABLE beliefs (
    time_step INTEGER,
    state_id INTEGER,
    belief_value DECIMAL(10,6),
    PRIMARY KEY (time_step, state_id)
);

CREATE TABLE generative_model (
    from_state INTEGER,
    action_id INTEGER,
    to_state INTEGER,
    transition_probability DECIMAL(10,6),
    observation_likelihood DECIMAL(10,6)
);
```

## Dependencies

- SQL Database Engine (PostgreSQL, MySQL, SQLite, SQL Server)
- SQL Client for execution and analysis

## Database Setup

```sql
-- PostgreSQL setup
psql -d active_inference -f SQL.sql

-- SQLite setup
sqlite3 active_inference.db < SQL.sql

-- MySQL setup
mysql -u user -p active_inference < SQL.sql
```

## Core Algorithms

### Belief Update Stored Procedure
```sql
CREATE PROCEDURE update_beliefs(
    IN p_observation_id INT,
    IN p_time_step INT
)
BEGIN
    -- Bayesian belief updating using SQL
    INSERT INTO beliefs (time_step, state_id, belief_value)
    SELECT
        p_time_step + 1,
        s.state_id,
        -- P(s|o) ∝ P(o|s) * P(s)
        (gm.observation_likelihood * b.belief_value) /
        SUM(gm.observation_likelihood * b.belief_value) OVER ()
    FROM states s
    JOIN generative_model gm ON s.state_id = gm.from_state
    JOIN beliefs b ON s.state_id = b.state_id
    WHERE gm.observation_id = p_observation_id
    AND b.time_step = p_time_step;
END
```

### Free Energy Calculation
```sql
CREATE FUNCTION calculate_free_energy(p_time_step INT)
RETURNS DECIMAL(10,6)
BEGIN
    DECLARE vfe DECIMAL(10,6);

    -- Variational free energy: E_q[ln q(s) - ln p(o|s)]
    SELECT SUM(b.belief_value * LOG(b.belief_value / gm.observation_likelihood))
    INTO vfe
    FROM beliefs b
    JOIN generative_model gm ON b.state_id = gm.from_state
    WHERE b.time_step = p_time_step;

    RETURN vfe;
END
```

### Action Selection Query
```sql
CREATE VIEW optimal_actions AS
SELECT
    a.action_id,
    a.action_name,
    -- Expected free energy calculation
    SUM(b.belief_value * (
        LOG(b.belief_value) -
        LOG(gm.transition_probability)
    )) AS expected_free_energy
FROM actions a
CROSS JOIN beliefs b
JOIN generative_model gm ON b.state_id = gm.from_state
    AND gm.action_id = a.action_id
GROUP BY a.action_id, a.action_name
ORDER BY expected_free_energy;
```

## Running the Implementation

```sql
-- Initialize simulation
CALL initialize_simulation(4, 3, 2, 100);

-- Run single time step
CALL run_time_step(1);

-- Run complete simulation
CALL run_simulation();

-- Analyze results
SELECT * FROM simulation_results;
SELECT * FROM optimal_actions LIMIT 1;
```

## Data Management

### Belief State Persistence
```sql
-- Store belief evolution over time
CREATE TABLE belief_history (
    time_step INTEGER,
    state_id INTEGER,
    belief_value DECIMAL(10,6),
    free_energy DECIMAL(10,6),
    selected_action INTEGER,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Automated belief tracking
CREATE TRIGGER track_beliefs
AFTER INSERT ON beliefs
FOR EACH ROW
INSERT INTO belief_history (time_step, state_id, belief_value)
VALUES (NEW.time_step, NEW.state_id, NEW.belief_value);
```

### Performance Optimization
```sql
-- Indexes for efficient queries
CREATE INDEX idx_beliefs_time_step ON beliefs(time_step);
CREATE INDEX idx_generative_model_state ON generative_model(from_state, action_id);

-- Materialized view for complex calculations
CREATE MATERIALIZED VIEW belief_statistics AS
SELECT
    time_step,
    AVG(belief_value) as mean_belief,
    STDDEV(belief_value) as belief_stddev,
    MAX(belief_value) as max_belief,
    MIN(belief_value) as min_belief
FROM beliefs
GROUP BY time_step;
```

## Analysis and Reporting

### Simulation Results
```sql
-- Comprehensive simulation analysis
SELECT
    sr.time_step,
    sr.total_free_energy,
    oa.action_name as selected_action,
    COUNT(*) as active_states,
    AVG(bh.belief_value) as avg_belief
FROM simulation_results sr
JOIN optimal_actions oa ON sr.selected_action = oa.action_id
JOIN belief_history bh ON sr.time_step = bh.time_step
GROUP BY sr.time_step, sr.total_free_energy, oa.action_name
ORDER BY sr.time_step;
```

### Performance Metrics
```sql
-- Query performance analysis
SELECT
    query_type,
    AVG(execution_time) as avg_time,
    MAX(execution_time) as max_time,
    MIN(execution_time) as min_time,
    COUNT(*) as execution_count
FROM query_performance_log
GROUP BY query_type
ORDER BY avg_time DESC;
```

## Advanced Features

### Temporal Analysis
```sql
-- Belief evolution analysis
SELECT
    state_id,
    time_step,
    belief_value,
    -- Moving average
    AVG(belief_value) OVER (
        PARTITION BY state_id
        ORDER BY time_step
        ROWS 5 PRECEDING
    ) as moving_avg,
    -- Trend analysis
    belief_value - LAG(belief_value) OVER (
        PARTITION BY state_id
        ORDER BY time_step
    ) as belief_change
FROM belief_history
ORDER BY state_id, time_step;
```

### Statistical Analysis
```sql
-- Belief distribution statistics
SELECT
    time_step,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY belief_value) as median_belief,
    MODE() WITHIN GROUP (ORDER BY state_id) as most_likely_state,
    CORR(time_step, belief_value) as time_belief_correlation
FROM belief_history
GROUP BY time_step
ORDER BY time_step;
```

## Integration Capabilities

### ETL Processing
```sql
-- Data import/export
CREATE TABLE simulation_import (
    time_step INTEGER,
    state_data JSON,
    observation_data JSON,
    action_data JSON
);

-- JSON processing for complex data
SELECT
    time_step,
    JSON_EXTRACT(state_data, '$.beliefs') as beliefs,
    JSON_EXTRACT(observation_data, '$.likelihood') as observation_likelihood
FROM simulation_import;
```

### External Connectivity
```sql
-- Foreign data wrapper for external data sources
CREATE EXTENSION postgres_fdw;

-- Connect to external analysis tools
CREATE SERVER analysis_server
FOREIGN DATA WRAPPER postgres_fdw
OPTIONS (host 'analysis.example.com', dbname 'analytics');

-- Import external belief data
CREATE FOREIGN TABLE external_beliefs (
    time_step INTEGER,
    state_id INTEGER,
    external_belief DECIMAL(10,6)
) SERVER analysis_server;
```

## References

### Key Papers
1. **Friston, K. (2010)**: The free-energy principle: a unified brain theory?
2. **Da Costa, L., et al. (2020)**: Active inference on discrete state-spaces
3. **Parr, T., & Friston, K. (2019)**: Generalised free energy and active inference

### SQL Resources
1. **SQL Performance Explained**: Query optimization and indexing
2. **Database Design for Mere Mortals**: Relational database design
3. **SQL Antipatterns**: Best practices and common mistakes
