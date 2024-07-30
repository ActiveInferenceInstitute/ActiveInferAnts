-- Create the Agent table to store agent information
CREATE TABLE Agent (
    AgentID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    CurrentState VARCHAR(50) NOT NULL,
    LastUpdated DATETIME DEFAULT GETDATE(),
    CreatedAt DATETIME DEFAULT GETDATE()
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
    InternalProb DECIMAL(5, 4) NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE(),
    UpdatedAt DATETIME DEFAULT GETDATE(),
    CONSTRAINT CHK_Probabilities CHECK (ExternalProb >= 0 AND ExternalProb <= 1 AND
                                        ActionProb >= 0 AND ActionProb <= 1 AND
                                        SenseProb >= 0 AND SenseProb <= 1 AND
                                        InternalProb >= 0 AND InternalProb <= 1)
);

-- Create an index on the State column for faster lookups
CREATE INDEX IX_BayesianGraph_State ON BayesianGraph (State);

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
WITH SCHEMABINDING
AS
BEGIN
    RETURN CAST(RAND() AS DECIMAL(5, 4));
END;

-- Create a stored procedure to update the agent's state based on the Bayesian graph
CREATE PROCEDURE UpdateAgentState
    @AgentID INT
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @CurrentState VARCHAR(50);
    DECLARE @RandomProb DECIMAL(5, 4);
    DECLARE @NewState VARCHAR(50);
    
    SELECT @CurrentState = CurrentState FROM Agent WHERE AgentID = @AgentID;
    
    SET @RandomProb = dbo.GetRandomProb();
    
    SELECT TOP 1 @NewState = InternalState
    FROM BayesianGraph
    WHERE State = @CurrentState
    AND @RandomProb <= InternalProb
    ORDER BY InternalProb DESC;

    IF @NewState IS NULL
        SET @NewState = @CurrentState;

    UPDATE Agent
    SET CurrentState = @NewState,
        LastUpdated = GETDATE()
    WHERE AgentID = @AgentID;

    IF @@ROWCOUNT = 0
        THROW 50001, 'Agent not found', 1;
END;

-- Create a stored procedure to perceive an event based on the Bayesian graph
CREATE PROCEDURE PerceiveEvent
    @AgentID INT,
    @Perception VARCHAR(50) OUTPUT
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @CurrentState VARCHAR(50);
    DECLARE @RandomProb DECIMAL(5, 4);
    
    SELECT @CurrentState = CurrentState FROM Agent WHERE AgentID = @AgentID;
    
    IF @CurrentState IS NULL
        THROW 50001, 'Agent not found', 1;

    SET @RandomProb = dbo.GetRandomProb();
    
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
    SET NOCOUNT ON;

    DECLARE @CurrentState VARCHAR(50);
    DECLARE @RandomProb DECIMAL(5, 4);
    
    SELECT @CurrentState = CurrentState FROM Agent WHERE AgentID = @AgentID;
    
    IF @CurrentState IS NULL
        THROW 50001, 'Agent not found', 1;

    SET @RandomProb = dbo.GetRandomProb();
    
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
    SET NOCOUNT ON;

    DECLARE @Perception VARCHAR(50);
    DECLARE @Action VARCHAR(50);
    DECLARE @Counter INT = 0;
    DECLARE @CurrentState VARCHAR(50);
    
    -- Create a temporary table to store simulation results
    CREATE TABLE #SimulationResults (
        IterationNumber INT,
        AgentState VARCHAR(50),
        Perception VARCHAR(50),
        Action VARCHAR(50)
    );

    WHILE @Counter < @NumIterations
    BEGIN
        SELECT @CurrentState = CurrentState FROM Agent WHERE AgentID = @AgentID;

        EXEC PerceiveEvent @AgentID, @Perception OUTPUT;
        EXEC DecideAction @AgentID, @Action OUTPUT;
        
        INSERT INTO #SimulationResults (IterationNumber, AgentState, Perception, Action)
        VALUES (@Counter, @CurrentState, @Perception, @Action);
        
        EXEC UpdateAgentState @AgentID;
        
        SET @Counter = @Counter + 1;
    END;

    -- Output simulation results
    SELECT * FROM #SimulationResults ORDER BY IterationNumber;

    -- Clean up
    DROP TABLE #SimulationResults;
END;

-- Insert an agent into the Agent table
INSERT INTO Agent (AgentID, Name, CurrentState)
VALUES (1, 'Agent001', 'idle');

-- Simulate agent behavior for 10 iterations
EXEC SimulateAgentBehavior 1, 10;

-- Create a view to analyze agent behavior patterns
CREATE VIEW AgentBehaviorAnalysis AS
SELECT 
    a.AgentID,
    a.Name,
    a.CurrentState,
    bg.ExternalState,
    bg.ActionState,
    bg.SenseState,
    bg.InternalState
FROM 
    Agent a
CROSS APPLY (
    SELECT TOP 1 *
    FROM BayesianGraph bg
    WHERE bg.State = a.CurrentState
    ORDER BY bg.InternalProb DESC
) bg;

-- Create a stored procedure to update the Bayesian graph based on observed behavior
CREATE PROCEDURE UpdateBayesianGraph
    @State VARCHAR(50),
    @ExternalState VARCHAR(50),
    @ActionState VARCHAR(50),
    @SenseState VARCHAR(50),
    @InternalState VARCHAR(50)
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @ExistingGraphID INT;

    SELECT @ExistingGraphID = GraphID
    FROM BayesianGraph
    WHERE State = @State
      AND ExternalState = @ExternalState
      AND ActionState = @ActionState
      AND SenseState = @SenseState
      AND InternalState = @InternalState;

    IF @ExistingGraphID IS NULL
    BEGIN
        INSERT INTO BayesianGraph (State, ExternalState, ExternalProb, ActionState, ActionProb, SenseState, SenseProb, InternalState, InternalProb)
        VALUES (@State, @ExternalState, 0.1, @ActionState, 0.1, @SenseState, 0.1, @InternalState, 0.1);
    END
    ELSE
    BEGIN
        UPDATE BayesianGraph
        SET ExternalProb = ExternalProb + 0.01,
            ActionProb = ActionProb + 0.01,
            SenseProb = SenseProb + 0.01,
            InternalProb = InternalProb + 0.01,
            UpdatedAt = GETDATE()
        WHERE GraphID = @ExistingGraphID;
    END
END;