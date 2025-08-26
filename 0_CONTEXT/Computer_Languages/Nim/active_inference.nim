# Active Inference Implementation in Nim

import math, sequtils, sugar

type
  ActiveInferenceAgent = object
    numStates: int = 4
    numObservations: int = 3
    numActions: int = 2
    beliefs: seq[float]
    aMatrix: seq[seq[float]]
    bMatrix: seq[seq[float]]
    cVector: seq[float]
    dVector: seq[float]

proc newActiveInferenceAgent(): ActiveInferenceAgent =
  result = ActiveInferenceAgent()
  result.beliefs = @[0.25, 0.25, 0.25, 0.25]
  result.aMatrix = @[
    @[0.8, 0.1, 0.1],
    @[0.1, 0.8, 0.1],
    @[0.1, 0.1, 0.8]
  ]
  result.bMatrix = @[
    @[0.9, 0.1],
    @[0.1, 0.9]
  ]
  result.cVector = @[0.0, 0.5, 0.0]
  result.dVector = @[0.5, 0.5]

proc updateBeliefs(agent: var ActiveInferenceAgent, observation: int) =
  let likelihood = agent.aMatrix[observation - 1]
  var posterior = zip(likelihood, agent.beliefs).mapIt(it[0] * it[1])
  let total = posterior.foldl(a + b, 0.0)
  
  if total > 0.0:
    agent.beliefs = posterior.mapIt(it / total)

proc calculateExpectedFreeEnergy(agent: ActiveInferenceAgent, action: int): float =
  result = 0.0
  for belief in agent.beliefs:
    if belief > 0.0:
      result -= belief * ln(belief)

proc selectAction(agent: ActiveInferenceAgent): int =
  var minEFE = Inf
  result = 1
  
  for action in 1..agent.numActions:
    let efe = agent.calculateExpectedFreeEnergy(action)
    if efe < minEFE:
      minEFE = efe
      result = action

proc step(agent: var ActiveInferenceAgent, observation: int): int =
  agent.updateBeliefs(observation)
  result = agent.selectAction()

proc printBeliefs(agent: ActiveInferenceAgent) =
  stdout.write "Beliefs: "
  for i, belief in agent.beliefs:
    stdout.write formatFloat(belief, ffDecimal, 3)
    if i < agent.beliefs.high:
      stdout.write ", "
  echo ""

# Demo
var agent = newActiveInferenceAgent()
echo "Nim Active Inference Demo"
echo "Initial beliefs:"
agent.printBeliefs()

for cycle in 1..5:
  let observation = (cycle - 1) mod 3 + 1
  let action = agent.step(observation)
  echo "Cycle ", cycle, ": Observation=", observation, ", Action=", action
  agent.printBeliefs()
