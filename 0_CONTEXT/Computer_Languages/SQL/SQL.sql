-- Active Inference Implementation in SQLite
-- Demonstrating active inference concepts using SQL database operations

-- Create the Agent table to store agent information
CREATE TABLE IF NOT EXISTS Agent (
    agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    current_state TEXT NOT NULL,
    precision REAL DEFAULT 1.0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create the BeliefState table to store probability distributions
CREATE TABLE IF NOT EXISTS BeliefState (
    belief_id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_id INTEGER NOT NULL,
    state_name TEXT NOT NULL,
    probability REAL NOT NULL,
    step_number INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (agent_id) REFERENCES Agent(agent_id)
);

-- Create the GenerativeModel table to store A, B, C, D matrices
CREATE TABLE IF NOT EXISTS GenerativeModel (
    model_id INTEGER PRIMARY KEY AUTOINCREMENT,
    matrix_type TEXT NOT NULL, -- 'A', 'B', 'C', 'D'
    from_state TEXT,
    to_state TEXT,
    action TEXT, -- for B matrix
    observation TEXT, -- for A and C matrices
    probability REAL NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create the SimulationResults table
CREATE TABLE IF NOT EXISTS SimulationResults (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_id INTEGER NOT NULL,
    step_number INTEGER NOT NULL,
    observation TEXT NOT NULL,
    action_taken TEXT NOT NULL,
    free_energy REAL NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (agent_id) REFERENCES Agent(agent_id)
);

-- Insert initial generative model data (A, B, C, D matrices)
INSERT OR IGNORE INTO GenerativeModel (matrix_type, from_state, to_state, observation, probability) VALUES
-- A matrix: P(o|s) - observation likelihood
('A', 'S1', NULL, 'O1', 0.8), ('A', 'S1', NULL, 'O2', 0.1), ('A', 'S1', NULL, 'O3', 0.1),
('A', 'S2', NULL, 'O1', 0.1), ('A', 'S2', NULL, 'O2', 0.8), ('A', 'S2', NULL, 'O3', 0.1),
('A', 'S3', NULL, 'O1', 0.1), ('A', 'S3', NULL, 'O2', 0.1), ('A', 'S3', NULL, 'O3', 0.8),
-- C vector: P(o) - observation preferences
('C', NULL, NULL, 'O1', 0.0), ('C', NULL, NULL, 'O2', 0.5), ('C', NULL, NULL, 'O3', 0.5),
-- D vector: P(s) - prior beliefs
('D', NULL, 'S1', NULL, 0.33), ('D', NULL, 'S2', NULL, 0.33), ('D', NULL, 'S3', NULL, 0.34);

-- Insert B matrix: P(s'|s,a) - state transition probabilities
INSERT OR IGNORE INTO GenerativeModel (matrix_type, from_state, to_state, action, probability) VALUES
('B', 'S1', 'S1', 'A1', 0.2), ('B', 'S1', 'S2', 'A1', 0.7), ('B', 'S1', 'S3', 'A1', 0.1),
('B', 'S2', 'S2', 'A1', 0.2), ('B', 'S2', 'S3', 'A1', 0.7), ('B', 'S2', 'S1', 'A1', 0.1),
('B', 'S3', 'S3', 'A1', 0.2), ('B', 'S3', 'S1', 'A1', 0.7), ('B', 'S3', 'S2', 'A1', 0.1),
('B', 'S1', 'S1', 'A2', 0.1), ('B', 'S1', 'S2', 'A2', 0.1), ('B', 'S1', 'S3', 'A2', 0.8),
('B', 'S2', 'S2', 'A2', 0.1), ('B', 'S2', 'S3', 'A2', 0.1), ('B', 'S2', 'S1', 'A2', 0.8),
('B', 'S3', 'S3', 'A2', 0.1), ('B', 'S3', 'S1', 'A2', 0.1), ('B', 'S3', 'S2', 'A2', 0.8),
('B', 'S1', 'S1', 'A3', 0.4), ('B', 'S1', 'S2', 'A3', 0.3), ('B', 'S1', 'S3', 'A3', 0.3),
('B', 'S2', 'S2', 'A3', 0.4), ('B', 'S2', 'S3', 'A3', 0.3), ('B', 'S2', 'S1', 'A3', 0.3),
('B', 'S3', 'S3', 'A3', 0.4), ('B', 'S3', 'S1', 'A3', 0.3), ('B', 'S3', 'S2', 'A3', 0.3);

-- Create an agent and initialize beliefs
INSERT OR IGNORE INTO Agent (name, current_state) VALUES ('ActiveInferenceAgent', 'S1');

-- Initialize belief state for the agent
INSERT OR IGNORE INTO BeliefState (agent_id, state_name, probability, step_number)
SELECT 1, 'S1', 0.33, 0
UNION ALL SELECT 1, 'S2', 0.33, 0
UNION ALL SELECT 1, 'S3', 0.34, 0;

-- Function to update beliefs based on observation
CREATE VIEW IF NOT EXISTS UpdateBeliefs AS
WITH likelihood AS (
    SELECT gm.from_state, gm.observation, gm.probability
    FROM GenerativeModel gm
    WHERE gm.matrix_type = 'A'
),
current_beliefs AS (
    SELECT bs.state_name, bs.probability
    FROM BeliefState bs
    WHERE bs.agent_id = 1 AND bs.step_number = (SELECT MAX(step_number) FROM BeliefState WHERE agent_id = 1)
),
posterior AS (
    SELECT l.from_state, l.observation, l.probability * cb.probability AS prob
    FROM likelihood l
    JOIN current_beliefs cb ON l.from_state = cb.state_name
),
normalized AS (
    SELECT from_state, observation, prob / (SELECT SUM(prob) FROM posterior WHERE observation = p.observation) AS norm_prob
    FROM posterior p
)
SELECT * FROM normalized;

-- Function to calculate expected free energy for action selection
CREATE VIEW IF NOT EXISTS ExpectedFreeEnergy AS
WITH transitions AS (
    SELECT gm.from_state, gm.to_state, gm.action, gm.probability
    FROM GenerativeModel gm
    WHERE gm.matrix_type = 'B'
),
current_beliefs AS (
    SELECT bs.state_name, bs.probability
    FROM BeliefState bs
    WHERE bs.agent_id = 1 AND bs.step_number = (SELECT MAX(step_number) FROM BeliefState WHERE agent_id = 1)
),
predicted_beliefs AS (
    SELECT t.to_state, t.action, SUM(t.probability * cb.probability) AS prob
    FROM transitions t
    JOIN current_beliefs cb ON t.from_state = cb.state_name
    GROUP BY t.to_state, t.action
),
efe_calc AS (
    SELECT pb.action,
           SUM(CASE WHEN pb.prob > 0 THEN pb.prob * LOG(pb.prob / 0.33) ELSE 0 END) AS efe
    FROM predicted_beliefs pb
    GROUP BY pb.action
)
SELECT * FROM efe_calc;

-- Simulation demonstration
.headers on
.mode column

-- Show initial beliefs
.print "\n🧠 Active Inference SQL Implementation"
.print "=====================================\n"

.print "Initial Beliefs:"
SELECT state_name, printf("%.3f", probability) as probability
FROM BeliefState
WHERE agent_id = 1 AND step_number = 0;

.print "\nExpected Free Energy for each action:"
SELECT action, printf("%.4f", efe) as expected_free_energy
FROM ExpectedFreeEnergy
ORDER BY efe;

.print "\nBest action (minimum EFE):"
SELECT action, printf("%.4f", efe) as expected_free_energy
FROM ExpectedFreeEnergy
ORDER BY efe
LIMIT 1;

.print "\n✅ SQL Active Inference simulation completed successfully!"
