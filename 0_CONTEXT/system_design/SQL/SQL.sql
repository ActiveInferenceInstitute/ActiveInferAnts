-- Create the Agent table to store agent information
CREATE TABLE Agent (
    AgentID INT PRIMARY KEY,
    CurrentState VARCHAR(50) NOT NULL
);

-- Create the BayesianGraph table to store the Bayesian network
CREATE TABLE BayesianGraph (
    GraphID INT PRIMARY KEY,
    State VARCHAR(50) NOT NULL,
    ExternalState VARCHAR(50) NOT NULL,
    ExternalProb DECIMAL(5, 4) NOT NULL,
    ActionState VARCHAR(50) NOT NULL,
    ActionProb DECIMAL(5, 4) NOT NULL,
    SenseState VARCHAR(50) NOT NULL,
    SenseProb DECIMAL(5, 4) NOT NULL,
    InternalState VARCHAR(50) NOT NULL,
    InternalProb DECIMAL(5, 4) NOT NULL
);

-- Insert sample data into the BayesianGraph table
INSERT INTO BayesianGraph (GraphID, State, ExternalState, ExternalProb, ActionState, ActionProb, SenseState, SenseProb, InternalState, InternalProb)
VALUES
    (1, 'idle', 'signal_detected', 0.2, 'wait', 0.7, 'processing', 0.3, 'idle', 0.9),
    (2, 'idle', 'obstacle_detected', 0.1, 'move', 0.2, 'acting', 0.1, 'processing', 0.1),
    (3, 'idle', 'path_clear', 0.7, 'interact', 0.1, 'idle', 0.6, 'idle', 0.9),
    (4, 'processing', 'signal_detected', 0.6, 'wait', 0.1, 'processing', 0.5, 'processing', 0.8),
    (5, 'processing', 'obstacle_detected', 0.1, 'move', 0.4, 'acting', 0.4, 'acting', 0.2),
    (6, 'processing', 'path_clear', 0.3, 'interact', 0.5, 'idle', 0.1, 'processing', 0.8);

-- Create a function to generate a random probability value
CREATE FUNCTION dbo.GetRandomProb()
RETURNS DECIMAL(5, 4)
AS
BEGIN
    RETURN RAND();
END;

-- Create a stored procedure to update the agent's state based on the Bayesian graph
CREATE PROCEDURE UpdateAgentState
    @AgentID INT
AS
BEGIN
    DECLARE @CurrentState VARCHAR(50);
    DECLARE @RandomProb DECIMAL(5, 4);
    
    SELECT @CurrentState = CurrentState FROM Agent WHERE AgentID = @AgentID;
    
    SELECT @RandomProb = dbo.GetRandomProb();
    
    UPDATE Agent
    SET CurrentState = (
        SELECT TOP 1 InternalState
        FROM BayesianGraph
        WHERE State = @CurrentState
        AND @RandomProb <= InternalProb
        ORDER BY InternalProb DESC
    )
    WHERE AgentID = @AgentID;
END;

-- Create a stored procedure to perceive an event based on the Bayesian graph
CREATE PROCEDURE PerceiveEvent
    @AgentID INT,
    @Perception VARCHAR(50) OUTPUT
AS
BEGIN
    DECLARE @CurrentState VARCHAR(50);
    DECLARE @RandomProb DECIMAL(5, 4);
    
    SELECT @CurrentState = CurrentState FROM Agent WHERE AgentID = @AgentID;
    
    SELECT @RandomProb = dbo.GetRandomProb();
    
    SELECT TOP 1 @Perception = ExternalState
    FROM BayesianGraph
    WHERE State = @CurrentState
    AND @RandomProb <= ExternalProb
    ORDER BY ExternalProb DESC;
    
    IF @Perception IS NULL
        SET @Perception = 'path_clear';
END;

-- Create a stored procedure to decide an action based on the Bayesian graph
CREATE PROCEDURE DecideAction
    @AgentID INT,
    @Action VARCHAR(50) OUTPUT
AS
BEGIN
    DECLARE @CurrentState VARCHAR(50);
    DECLARE @RandomProb DECIMAL(5, 4);
    
    SELECT @CurrentState = CurrentState FROM Agent WHERE AgentID = @AgentID;
    
    SELECT @RandomProb = dbo.GetRandomProb();
    
    SELECT TOP 1 @Action = ActionState
    FROM BayesianGraph
    WHERE State = @CurrentState
    AND @RandomProb <= ActionProb
    ORDER BY ActionProb DESC;
    
    IF @Action IS NULL
        SET @Action = 'wait';
END;

-- Create a stored procedure to simulate agent behavior
CREATE PROCEDURE SimulateAgentBehavior
    @AgentID INT,
    @NumIterations INT
AS
BEGIN
    DECLARE @Perception VARCHAR(50);
    DECLARE @Action VARCHAR(50);
    DECLARE @Counter INT = 0;
    
    WHILE @Counter < @NumIterations
    BEGIN
        EXEC PerceiveEvent @AgentID, @Perception OUTPUT;
        EXEC DecideAction @AgentID, @Action OUTPUT;
        
        PRINT 'Iteration: ' + CAST(@Counter AS VARCHAR(10));
        PRINT 'Perception: ' + @Perception;
        PRINT 'Action: ' + @Action;
        
        EXEC UpdateAgentState @AgentID;
        
        SET @Counter = @Counter + 1;
    END;
END;

-- Insert an agent into the Agent table
INSERT INTO Agent (AgentID, CurrentState)
VALUES (1, 'idle');

-- Simulate agent behavior for 10 iterations
EXEC SimulateAgentBehavior 1, 10;