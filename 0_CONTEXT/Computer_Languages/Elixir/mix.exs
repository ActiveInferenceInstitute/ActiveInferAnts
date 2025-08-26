defmodule ActiveInference.MixProject do
  use Mix.Project

  def project do
    [
      app: :active_inference,
      version: "1.0.0",
      elixir: "~> 1.14",
      start_permanent: Mix.env() == :prod,
      deps: deps()
    ]
  end

  def application do
    [
      extra_applications: [:logger],
      mod: {ActiveInference.Application, []}
    ]
  end

  defp deps do
    [
      # Add matrix library if needed
      # {:matrix, "~> 0.3.0"}
    ]
  end
end
