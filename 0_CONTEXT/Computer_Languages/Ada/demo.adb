with Active_Inference;
with Ada.Text_IO;

procedure Demo is
    Selected_Action : Active_Inference.Action_Type;
    Observation : Active_Inference.Observation_Type := 1;
begin
    Ada.Text_IO.Put_Line("Ada Active Inference Demo");
    Ada.Text_IO.Put_Line("==========================");

    -- Initialize agent
    Active_Inference.Agent.Initialize;

    -- Display initial beliefs
    Ada.Text_IO.Put("Initial ");
    Active_Inference.Agent.Print_Beliefs;

    -- Run several perception-action cycles
    for Cycle in 1..10 loop
        Ada.Text_IO.Put_Line("Cycle" & Integer'Image(Cycle) & ":");

        -- Perception and action selection
        Active_Inference.Agent.Step(Observation, Selected_Action);

        -- Display results
        Active_Inference.Agent.Print_Beliefs;
        Ada.Text_IO.Put_Line("Selected Action:" & Active_Inference.Action_Type'Image(Selected_Action));

        -- Simulate environment response (simple random observation)
        Observation := (Observation mod Active_Inference.Num_Observations) + 1;

        Ada.Text_IO.New_Line;
    end loop;

    Ada.Text_IO.Put_Line("Demo completed successfully!");
end Demo;
