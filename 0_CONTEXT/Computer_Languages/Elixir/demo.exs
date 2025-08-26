#!/usr/bin/env elixir

# Active Inference Demo in Elixir

IO.puts("Elixir Active Inference Demo")
IO.puts("============================")

# Start the agent
{:ok, _pid} = ActiveInference.Agent.start_link()

# Initialize
:ok = ActiveInference.Agent.initialize()

# Display initial beliefs
beliefs = ActiveInference.Agent.get_beliefs()
IO.puts("Initial Beliefs: #{inspect(beliefs)}")

# Run simulation
Enum.each(1..10, fn cycle ->
  IO.puts("\nCycle #{cycle}:")

  # Simulate observation (cycle through different observations)
  observation = rem(cycle - 1, 3) + 1

  # Perform perception-action cycle
  {new_beliefs, action} = ActiveInference.Agent.step(observation)

  IO.puts("  Observation: #{observation}")
  IO.puts("  Updated Beliefs: #{inspect(new_beliefs)}")
  IO.puts("  Selected Action: #{action}")
end)

IO.puts("\nDemo completed successfully!")
