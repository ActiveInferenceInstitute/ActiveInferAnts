package main

import (
	"errors"
	"fmt"
	"math/rand"
	"sync"
	"time"
)

// BayesianGraph represents the Bayesian network of perception-action cycles, encapsulating the Markov Blanket components.
type BayesianGraph struct {
	ExternalStates map[string]float64 // External states probabilities
	ActionStates   map[string]float64 // Action states probabilities
	SenseStates    map[string]float64 // Sense states probabilities
	InternalStates map[string]float64 // Internal states probabilities
}

// Agent states, perceptions, and actions are defined as constants for improved type safety and readability.
const (
	StateIdle          = "idle"
	StateProcessing    = "processing"
	StateActing        = "acting"
	PerceptionSignal   = "signal_detected"
	PerceptionObstacle = "obstacle_detected"
	PerceptionClear    = "path_clear"
	ActionWait         = "wait"
	ActionMove         = "move"
	ActionInteract     = "interact"
)

var (
	states      = []string{StateIdle, StateProcessing, StateActing}
	perceptions = []string{PerceptionSignal, PerceptionObstacle, PerceptionClear}
	actions     = []string{ActionWait, ActionMove, ActionInteract}

	// Mapping each state to its corresponding Bayesian graph components.
	agentGraphs = map[string]BayesianGraph{
		StateIdle: {
			ExternalStates: map[string]float64{PerceptionSignal: 0.2, PerceptionObstacle: 0.1, PerceptionClear: 0.7},
			ActionStates:   map[string]float64{ActionWait: 0.7, ActionMove: 0.2, ActionInteract: 0.1},
			SenseStates:    map[string]float64{StateProcessing: 0.3, StateActing: 0.1, StateIdle: 0.6},
			InternalStates: map[string]float64{StateIdle: 0.9, StateProcessing: 0.1},
		},
		StateProcessing: {
			ExternalStates: map[string]float64{PerceptionSignal: 0.6, PerceptionObstacle: 0.1, PerceptionClear: 0.3},
			ActionStates:   map[string]float64{ActionWait: 0.1, ActionMove: 0.4, ActionInteract: 0.5},
			SenseStates:    map[string]float64{StateProcessing: 0.5, StateActing: 0.4, StateIdle: 0.1},
			InternalStates: map[string]float64{StateProcessing: 0.8, StateActing: 0.2},
		},
		StateActing: {
			ExternalStates: map[string]float64{PerceptionSignal: 0.1, PerceptionObstacle: 0.8, PerceptionClear: 0.1},
			ActionStates:   map[string]float64{ActionWait: 0.1, ActionMove: 0.7, ActionInteract: 0.2},
			SenseStates:    map[string]float64{StateProcessing: 0.2, StateActing: 0.7, StateIdle: 0.1},
			InternalStates: map[string]float64{StateActing: 0.9, StateIdle: 0.1},
		},
	}
)

// ActiveInferenceAgent models an agent with a current state and provides methods for state transitions, event perceptions, and actions based on Bayesian graphs.
type ActiveInferenceAgent struct {
	currentState string
}

// NewActiveInferenceAgent initializes a new agent with a specified initial state, ensuring it's valid.
func NewActiveInferenceAgent(initialState string) (*ActiveInferenceAgent, error) {
	if _, exists := agentGraphs[initialState]; !exists {
		return nil, errors.New("invalid initial state: " + initialState)
	}
	return &ActiveInferenceAgent{currentState: initialState}, nil
}

// UpdateState transitions the agent to a new state based on the Bayesian graph, using a cumulative probability approach.
func (a *ActiveInferenceAgent) UpdateState() error {
	internalProbabilities, ok := agentGraphs[a.currentState].InternalStates
	if !ok {
		return errors.New("current state not found in Bayesian graph")
	}
	r := rand.Float64()
	for state, prob := range toCumulative(internalProbabilities) {
		if r <= prob {
			a.currentState = state
			return nil
		}
	}
	return errors.New("failed to update state due to invalid probability distribution")
}

// PerceiveEvent generates a perception based on the Bayesian graph, defaulting to PerceptionClear if no match is found.
func (a *ActiveInferenceAgent) PerceiveEvent() (string, error) {
	externalProbabilities, ok := agentGraphs[a.currentState].ExternalStates
	if !ok {
		return "", errors.New("current state not found in Bayesian graph")
	}
	r := rand.Float64()
	for perception, prob := range toCumulative(externalProbabilities) {
		if r <= prob {
			return perception, nil
		}
	}
	return PerceptionClear, nil
}

// DecideAction determines the next action based on the Bayesian graph, defaulting to ActionWait if no match is found.
func (a *ActiveInferenceAgent) DecideAction() (string, error) {
	actionProbabilities, ok := agentGraphs[a.currentState].ActionStates
	if !ok {
		return "", errors.New("current state not found in Bayesian graph")
	}
	r := rand.Float64()
	for action, prob := range toCumulative(actionProbabilities) {
		if r <= prob {
			return action, nil
		}
	}
	return ActionWait, nil
}

// toCumulative transforms a map of probabilities into a cumulative map to facilitate weighted random selection.
func toCumulative(probabilities map[string]float64) map[string]float64 {
	cumulative := make(map[string]float64)
	var sum float64
	for _, prob := range probabilities {
		sum += prob
	}
	currentSum := 0.0
	for key, prob := range probabilities {
		currentSum += prob / sum
		cumulative[key] = currentSum
	}
	return cumulative
}

// simulateAgentBehavior simulates the behavior of an active inference agent, perceiving events, deciding actions, and updating its state in a loop.
func simulateAgentBehavior(behaviorChannel chan<- string, wg *sync.WaitGroup) {
	defer wg.Done()
	agent, err := NewActiveInferenceAgent(StateIdle)
	if err != nil {
		fmt.Println("Error initializing active inference agent:", err)
		return
	}
	for i := 0; i < 10; i++ {
		perception, err := agent.PerceiveEvent()
		if err != nil {
			fmt.Println("Error perceiving event:", err)
			return
		}
		action, err := agent.DecideAction()
		if err != nil {
			fmt.Println("Error deciding action:", err)
			return
		}
		behaviorChannel <- fmt.Sprintf("Perception: %s, Action: %s", perception, action)
		err = agent.UpdateState()
		if err != nil {
			fmt.Println("Error updating agent state:", err)
			return
		}
	}
}

func main() {
	rand.Seed(time.Now().UnixNano())
	behaviorChannel := make(chan string, 10)
	var wg sync.WaitGroup

	wg.Add(1)
	go simulateAgentBehavior(behaviorChannel, &wg)

	go func() {
		for behavior := range behaviorChannel {
			fmt.Printf("Agent behavior: %s\n", behavior)
		}
	}()
	wg.Wait()
	close(behaviorChannel)
}
