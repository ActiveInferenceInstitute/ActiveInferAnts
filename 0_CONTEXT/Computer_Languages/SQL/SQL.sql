# Create the Agent table to store agent information
CREATE TABLE dbo.Agent (
    AgentID INT IDENTITY(1,1) PRIMARY KEY, # Unique identifier for each agent
    Name NVARCHAR(100) NOT NULL, # Name of the agent
    CurrentState NVARCHAR(50) NOT NULL, # Current state of the agent
    LastUpdated DATETIME2 DEFAULT SYSDATETIME(), # Timestamp of the last update
    CreatedAt DATETIME2 DEFAULT SYSDATETIME() # Timestamp of creation
);

# Create the BayesianGraph table to store the Bayesian network
CREATE TABLE dbo.BayesianGraph (
    GraphID INT IDENTITY(1,1) PRIMARY KEY, # Unique identifier for each graph entry
    State NVARCHAR(50) NOT NULL, # Current state
    ExternalState NVARCHAR(50) NOT NULL, # External perception state
    ExternalProb DECIMAL(5,4) NOT NULL, # Probability of the external state
    ActionState NVARCHAR(50) NOT NULL, # Action state
    ActionProb DECIMAL(5,4) NOT NULL, # Probability of the action
    SenseState NVARCHAR(50) NOT NULL, # Sense state
    SenseProb DECIMAL(5,4) NOT NULL, # Probability of the sense
    InternalState NVARCHAR(50) NOT NULL, # Internal state transition
    InternalProb DECIMAL(5,4) NOT NULL, # Probability of the internal state
    CreatedAt DATETIME2 DEFAULT SYSDATETIME(), # Timestamp of creation
    UpdatedAt DATETIME2 DEFAULT SYSDATETIME(), # Timestamp of last update
    CONSTRAINT CHK_BayesianGraph_Probabilities CHECK (
        ExternalProb BETWEEN 0 AND 1 AND
        ActionProb BETWEEN 0 AND 1 AND
        SenseProb BETWEEN 0 AND 1 AND
        InternalProb BETWEEN 0 AND 1
    )
);

# Create an index on the State column for faster lookups
CREATE INDEX IX_BayesianGraph_State ON dbo.BayesianGraph (State);

# Insert sample data into the BayesianGraph table
INSERT INTO dbo.BayesianGraph (State, ExternalState, ExternalProb, ActionState, ActionProb, SenseState, SenseProb, InternalState, InternalProb)
VALUES
    ('idle', 'signal_detected', 0.2000, 'wait', 0.7000, 'processing', 0.3000, 'idle', 0.9000),
    ('idle', 'obstacle_detected', 0.1000, 'move', 0.2000, 'acting', 0.1000, 'processing', 0.1000),
    ('idle', 'path_clear', 0.7000, 'interact', 0.1000, 'idle', 0.6000, 'idle', 0.9000),
    ('processing', 'signal_detected', 0.6000, 'wait', 0.1000, 'processing', 0.5000, 'processing', 0.8000),
    ('processing', 'obstacle_detected', 0.1000, 'move', 0.4000, 'acting', 0.4000, 'acting', 0.2000),
    ('processing', 'path_clear', 0.3000, 'interact', 0.5000, 'idle', 0.1000, 'processing', 0.8000);

# Create a function to generate a random probability value
CREATE FUNCTION dbo.GetRandomProb()
RETURNS DECIMAL(5,4)
WITH SCHEMABINDING
AS
BEGIN
    RETURN CAST(RAND(CHECKSUM(NEWID())) AS DECIMAL(5,4)); # Generate a random probability between 0 and 1
END;

# Create a stored procedure to update the agent's state based on the Bayesian graph
CREATE PROCEDURE dbo.UpdateAgentState
    @AgentID INT
AS
BEGIN
    SET NOCOUNT ON;
    BEGIN TRY
        DECLARE @CurrentState NVARCHAR(50);
        DECLARE @RandomProb DECIMAL(5,4);
        DECLARE @NewState NVARCHAR(50);
        
        SELECT @CurrentState = CurrentState FROM dbo.Agent WHERE AgentID = @AgentID;
        
        IF @CurrentState IS NULL
            THROW 50001, 'Agent not found.', 1;
        
        SET @RandomProb = dbo.GetRandomProb();
        
        SELECT TOP 1 @NewState = InternalState
        FROM dbo.BayesianGraph
        WHERE State = @CurrentState
          AND @RandomProb <= InternalProb
        ORDER BY InternalProb DESC;
    
        IF @NewState IS NULL
            SET @NewState = @CurrentState;
    
        UPDATE dbo.Agent
        SET 
            CurrentState = @NewState,
            LastUpdated = SYSDATETIME()
        WHERE AgentID = @AgentID;
        
    END TRY
    BEGIN CATCH
        THROW;
    END CATCH
END;

# Create a stored procedure to perceive an event based on the Bayesian graph
CREATE PROCEDURE dbo.PerceiveEvent
    @AgentID INT,
    @Perception NVARCHAR(50) OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    BEGIN TRY
        DECLARE @CurrentState NVARCHAR(50);
        DECLARE @RandomProb DECIMAL(5,4);
        
        SELECT @CurrentState = CurrentState FROM dbo.Agent WHERE AgentID = @AgentID;
        
        IF @CurrentState IS NULL
            THROW 50001, 'Agent not found.', 1;
    
        SET @RandomProb = dbo.GetRandomProb();
        
        SELECT TOP 1 @Perception = ExternalState
        FROM dbo.BayesianGraph
        WHERE State = @CurrentState
          AND @RandomProb <= ExternalProb
        ORDER BY ExternalProb DESC;
        
        IF @Perception IS NULL
            SET @Perception = 'path_clear';
    END TRY
    BEGIN CATCH
        THROW;
    END CATCH
END;

# Create a stored procedure to decide an action based on the Bayesian graph
CREATE PROCEDURE dbo.DecideAction
    @AgentID INT,
    @Action NVARCHAR(50) OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    BEGIN TRY
        DECLARE @CurrentState NVARCHAR(50);
        DECLARE @RandomProb DECIMAL(5,4);
        
        SELECT @CurrentState = CurrentState FROM dbo.Agent WHERE AgentID = @AgentID;
        
        IF @CurrentState IS NULL
            THROW 50001, 'Agent not found.', 1;
    
        SET @RandomProb = dbo.GetRandomProb();
        
        SELECT TOP 1 @Action = ActionState
        FROM dbo.BayesianGraph
        WHERE State = @CurrentState
          AND @RandomProb <= ActionProb
        ORDER BY ActionProb DESC;
        
        IF @Action IS NULL
            SET @Action = 'wait';
    END TRY
    BEGIN CATCH
        THROW;
    END CATCH
END;

# Create a stored procedure to simulate agent behavior
CREATE PROCEDURE dbo.SimulateAgentBehavior
    @AgentID INT,
    @NumIterations INT
AS
BEGIN
    SET NOCOUNT ON;
    BEGIN TRY
        DECLARE @Perception NVARCHAR(50);
        DECLARE @Action NVARCHAR(50);
        DECLARE @Counter INT = 0;
        DECLARE @CurrentState NVARCHAR(50);
        
        # Create a temporary table to store simulation results
        CREATE TABLE #SimulationResults (
            IterationNumber INT PRIMARY KEY,
            AgentState NVARCHAR(50),
            Perception NVARCHAR(50),
            Action NVARCHAR(50)
        );
    
        WHILE @Counter < @NumIterations
        BEGIN
            SELECT @CurrentState = CurrentState FROM dbo.Agent WHERE AgentID = @AgentID;
    
            EXEC dbo.PerceiveEvent @AgentID, @Perception OUTPUT;
            EXEC dbo.DecideAction @AgentID, @Action OUTPUT;
            
            INSERT INTO #SimulationResults (IterationNumber, AgentState, Perception, Action)
            VALUES (@Counter, @CurrentState, @Perception, @Action);
            
            EXEC dbo.UpdateAgentState @AgentID;
            
            SET @Counter = @Counter + 1;
        END;
    
        # Output simulation results
        SELECT * FROM #SimulationResults ORDER BY IterationNumber;
    
        # Clean up
        DROP TABLE #SimulationResults;
    END TRY
    BEGIN CATCH
        DROP TABLE IF EXISTS #SimulationResults;
        THROW;
    END CATCH
END;

# Insert an agent into the Agent table
INSERT INTO dbo.Agent (Name, CurrentState)
VALUES ('Agent001', 'idle');

# Simulate agent behavior for 10 iterations
EXEC dbo.SimulateAgentBehavior @AgentID = 1, @NumIterations = 10;

# Create a view to analyze agent behavior patterns
CREATE VIEW dbo.AgentBehaviorAnalysis AS
SELECT 
    a.AgentID,
    a.Name,
    a.CurrentState,
    bg.ExternalState,
    bg.ActionState,
    bg.SenseState,
    bg.InternalState
FROM 
    dbo.Agent a
CROSS APPLY (
    SELECT TOP 1 *
    FROM dbo.BayesianGraph bg
    WHERE bg.State = a.CurrentState
    ORDER BY bg.InternalProb DESC
) bg;

# Create a stored procedure to update the Bayesian graph based on observed behavior
CREATE PROCEDURE dbo.UpdateBayesianGraph
    @State NVARCHAR(50),
    @ExternalState NVARCHAR(50),
    @ActionState NVARCHAR(50),
    @SenseState NVARCHAR(50),
    @InternalState NVARCHAR(50)
AS
BEGIN
    SET NOCOUNT ON;
    BEGIN TRY
        DECLARE @ExistingGraphID INT;
    
        SELECT @ExistingGraphID = GraphID
        FROM dbo.BayesianGraph
        WHERE State = @State
          AND ExternalState = @ExternalState
          AND ActionState = @ActionState
          AND SenseState = @SenseState
          AND InternalState = @InternalState;
    
        IF @ExistingGraphID IS NULL
        BEGIN
            INSERT INTO dbo.BayesianGraph (
                State, ExternalState, ExternalProb, 
                ActionState, ActionProb, SenseState, SenseProb, 
                InternalState, InternalProb
            )
            VALUES (
                @State, @ExternalState, 0.1000, 
                @ActionState, 0.1000, @SenseState, 0.1000, 
                @InternalState, 0.1000
            );
        END
        ELSE
        BEGIN
            UPDATE dbo.BayesianGraph
            SET 
                ExternalProb = ExternalProb + 0.0100,
                ActionProb = ActionProb + 0.0100,
                SenseProb = SenseProb + 0.0100,
                InternalProb = InternalProb + 0.0100,
                UpdatedAt = SYSDATETIME()
            WHERE GraphID = @ExistingGraphID;
        END
    END TRY
    BEGIN CATCH
        THROW;
    END CATCH
END;