package main

import (
	"errors"
	"fmt"
	"math/rand"
	"sync"
	"time"
)

// StateTransition encapsulates the probabilities of transitioning between states and observing events.
type StateTransition struct {
	Transitions  map[string]float64 // Probability of transitioning to other states
	Observations map[string]float64 // Probability of observing certain events in the current state
}

// Agent states and observations are defined as constants for improved type safety and readability.
const (
	StateSearching  = "searching"
	StateForaging   = "foraging"
	StateReturning  = "returning"
	ObservationFood = "food_found"
	ObservationNest = "nest_sighted"
	ObservationNone = "nothing"
)

var (
	states       = []string{StateSearching, StateForaging, StateReturning}
	observations = []string{ObservationFood, ObservationNest, ObservationNone}

	// Mapping each state to its corresponding transition and observation probabilities.
	probabilities = map[string]StateTransition{
		StateSearching: {
			Transitions:  map[string]float64{StateForaging: 0.3, StateReturning: 0.1, StateSearching: 0.6},
			Observations: map[string]float64{ObservationFood: 0.2, ObservationNest: 0.1, ObservationNone: 0.7},
		},
		StateForaging: {
			Transitions:  map[string]float64{StateForaging: 0.5, StateReturning: 0.4, StateSearching: 0.1},
			Observations: map[string]float64{ObservationFood: 0.6, ObservationNest: 0.1, ObservationNone: 0.3},
		},
		StateReturning: {
			Transitions:  map[string]float64{StateForaging: 0.2, StateReturning: 0.7, StateSearching: 0.1},
			Observations: map[string]float64{ObservationFood: 0.1, ObservationNest: 0.8, ObservationNone: 0.1},
		},
	}
)

// ActiveInferenceAgent models an agent with a current state and provides methods for state transitions and observations.
type ActiveInferenceAgent struct {
	currentState string
}

// NewActiveInferenceAgent initializes a new agent with a specified initial state, ensuring it's valid.
func NewActiveInferenceAgent(initialState string) (*ActiveInferenceAgent, error) {
	if _, exists := probabilities[initialState]; !exists {
		return nil, fmt.Errorf("invalid initial state: %s", initialState)
	}
	return &ActiveInferenceAgent{currentState: initialState}, nil
}

// UpdateState transitions the agent to a new state based on the defined probabilities, using a cumulative probability approach.
func (a *ActiveInferenceAgent) UpdateState() error {
	transitionProbabilities, ok := probabilities[a.currentState].Transitions
	if !ok {
		return errors.New("current state not found in probabilities map")
	}
	r := rand.Float64()
	for state, prob := range toCumulative(transitionProbabilities) {
		if r <= prob {
			a.currentState = state
			return nil
		}
	}
	return errors.New("failed to update state due to invalid probability distribution")
}

// Observe generates an observation based on the current state and defined probabilities, defaulting to ObservationNone if no match is found.
func (a *ActiveInferenceAgent) Observe() (string, error) {
	observationProbabilities, ok := probabilities[a.currentState].Observations
	if !ok {
		return "", errors.New("current state not found in observations map")
	}
	r := rand.Float64()
	for observation, prob := range toCumulative(observationProbabilities) {
		if r <= prob {
			return observation, nil
		}
	}
	return ObservationNone, nil
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

// simulateAntBehavior simulates the behavior of an ant agent, observing the environment and updating its state in a loop.
func simulateAntBehavior(behaviorChannel chan<- string, wg *sync.WaitGroup) {
	defer wg.Done()
	agent, err := NewActiveInferenceAgent(StateSearching)
	if err != nil {
		fmt.Println("Error initializing agent:", err)
		return
	}
	for i := 0; i < 10; i++ {
		behavior, err := agent.Observe()
		if err != nil {
			fmt.Println("Error observing environment:", err)
			return
		}
		behaviorChannel <- behavior
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
	go simulateAntBehavior(behaviorChannel, &wg)

	go func() {
		for behavior := range behaviorChannel {
			fmt.Printf("Ant behavior: %s\n", behavior)
		}
	}()
	wg.Wait()
	close(behaviorChannel)
}
