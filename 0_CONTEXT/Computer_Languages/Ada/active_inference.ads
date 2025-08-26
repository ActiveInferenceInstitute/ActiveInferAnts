with Ada.Numerics.Elementary_Functions;

package Active_Inference is

    -- Configuration constants
    Num_States : constant := 4;
    Num_Observations : constant := 3;
    Num_Actions : constant := 2;

    -- Type definitions
    subtype State_Type is Positive range 1..Num_States;
    subtype Observation_Type is Positive range 1..Num_Observations;
    subtype Action_Type is Positive range 1..Num_Actions;

    type Float_Array is array(Positive range <>) of Float;
    type Matrix_2D is array(Positive range <>, Positive range <>) of Float;
    type Matrix_3D is array(Positive range <>, Positive range <>, Positive range <>) of Float;

    -- Active Inference Agent
    protected Agent is

        procedure Initialize;
        -- Initialize the agent's generative model and belief state

        procedure Update_Beliefs(Observation : Observation_Type);
        -- Update beliefs based on observation using Bayesian inference

        function Calculate_Expected_Free_Energy(Action : Action_Type) return Float;
        -- Calculate expected free energy for a given action

        procedure Select_Action(Selected_Action : out Action_Type);
        -- Select action that minimizes expected free energy

        procedure Step(Observation : Observation_Type; Selected_Action : out Action_Type);
        -- Complete perception-action cycle

        procedure Print_Beliefs;
        -- Display current belief state

    private
        A_Matrix : Matrix_2D(1..Num_Observations, 1..Num_States);  -- P(o|s)
        B_Matrix : Matrix_3D(1..Num_States, 1..Num_Actions, 1..Num_States);  -- P(s'|s,a)
        C_Vector : Float_Array(1..Num_Observations);  -- Preferred observations
        D_Vector : Float_Array(1..Num_States);        -- Prior preferences
        Belief_State : Float_Array(1..Num_States);    -- Current beliefs P(s)

    end Agent;

end Active_Inference;
