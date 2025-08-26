with Ada.Text_IO;
with Ada.Numerics.Float_Random;
with Ada.Containers.Vectors;

package body Active_Inference is

    package Float_IO is new Ada.Text_IO.Float_IO(Float);
    package Random renames Ada.Numerics.Float_Random;
    package Float_Vectors is new Ada.Containers.Vectors(Natural, Float);

    -- Active Inference Agent Implementation
    protected body Agent is

        procedure Initialize is
        begin
            -- Initialize generative model parameters
            A_Matrix := (others => (others => 0.5));
            B_Matrix := (others => (others => (others => 0.5)));
            C_Vector := (others => 0.0);
            D_Vector := (others => 0.0);

            -- Initialize belief state
            Belief_State := (others => 1.0 / Float(Num_States));
        end Initialize;

        procedure Update_Beliefs(Observation : Observation_Type) is
            Likelihood : Float_Array(1..Num_States);
            Prior : Float_Array(1..Num_States) := Belief_State;
            Total : Float := 0.0;
        begin
            -- Calculate likelihood P(o|s)
            for S in 1..Num_States loop
                Likelihood(S) := A_Matrix(Observation, S);
            end loop;

            -- Update beliefs P(s|o) ∝ P(o|s) * P(s)
            for S in 1..Num_States loop
                Belief_State(S) := Likelihood(S) * Prior(S);
                Total := Total + Belief_State(S);
            end loop;

            -- Normalize
            if Total > 0.0 then
                for S in 1..Num_States loop
                    Belief_State(S) := Belief_State(S) / Total;
                end loop;
            end if;
        end Update_Beliefs;

        function Calculate_Expected_Free_Energy(Action : Action_Type) return Float is
            G : Float := 0.0;
            Future_Belief : Float_Array(1..Num_States);
            Total : Float := 0.0;
        begin
            -- Calculate expected free energy for given action
            -- G(π) = Σ_s P(s) * [ln P(s) - ln Q(s|π)] + extrinsic terms

            for S in 1..Num_States loop
                Future_Belief(S) := 0.0;
                for S_Prime in 1..Num_States loop
                    Future_Belief(S) := Future_Belief(S) +
                        B_Matrix(S_Prime, Action, S) * Belief_State(S_Prime);
                end loop;
                Total := Total + Future_Belief(S);
            end loop;

            -- Normalize future beliefs
            if Total > 0.0 then
                for S in 1..Num_States loop
                    Future_Belief(S) := Future_Belief(S) / Total;
                end loop;
            end if;

            -- Calculate EFE
            for S in 1..Num_States loop
                if Future_Belief(S) > 0.0 then
                    G := G + Belief_State(S) * (Ada.Numerics.Elementary_Functions.Log(Belief_State(S)) -
                        Ada.Numerics.Elementary_Functions.Log(Future_Belief(S)));
                end if;
            end loop;

            return G;
        end Calculate_Expected_Free_Energy;

        procedure Select_Action(Selected_Action : out Action_Type) is
            Min_EFE : Float := Float'Last;
            EFE : Float;
        begin
            Selected_Action := 1;

            -- Select action with minimum expected free energy
            for A in Action_Type'Range loop
                EFE := Calculate_Expected_Free_Energy(A);
                if EFE < Min_EFE then
                    Min_EFE := EFE;
                    Selected_Action := A;
                end if;
            end loop;
        end Select_Action;

        procedure Step(Observation : Observation_Type; Selected_Action : out Action_Type) is
        begin
            Update_Beliefs(Observation);
            Select_Action(Selected_Action);
        end Step;

        procedure Print_Beliefs is
        begin
            Ada.Text_IO.Put("Current Beliefs: ");
            for S in 1..Num_States loop
                Float_IO.Put(Belief_State(S), 3, 2, 0);
                Ada.Text_IO.Put(" ");
            end loop;
            Ada.Text_IO.New_Line;
        end Print_Beliefs;

    end Agent;

end Active_Inference;
