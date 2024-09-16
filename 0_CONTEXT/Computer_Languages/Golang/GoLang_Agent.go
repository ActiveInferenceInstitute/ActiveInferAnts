// Start of Selection
package main

import (
	"errors"
	"fmt"
	"math/rand"
	"sync"
	"time"
)

// State represents the possible states of the agent.
type State string

// Observation represents the possible observations an agent can make.
type Observation string

// Constants defining agent states for type safety and clarity.
const (
	StateSearching State = "searching"
	StateForaging  State = "foraging"
	StateReturning State = "returning"

	ObservationFood Observation = "food_found"
	ObservationNest Observation = "nest_sighted"
	ObservationNone Observation = "nothing"
)

// StateTransition encapsulates the transition and observation probabilities for a state.
type StateTransition struct {
	Transitions  map[State]float64
	Observations map[Observation]float64
}

// Probabilities defines the state transitions and observations for each state.
var probabilities = map[State]StateTransition{
	StateSearching: {
		Transitions: map[State]float64{
			StateForaging:  0.3,
			StateReturning: 0.1,
			StateSearching: 0.6,
		},
		Observations: map[Observation]float64{
			ObservationFood: 0.2,
			ObservationNest: 0.1,
			ObservationNone: 0.7,
		},
	},
	StateForaging: {
		Transitions: map[State]float64{
			StateForaging:  State(0.5),
			StateReturning: State(0.4),
			StateSearching: State(0.1),
		},
		Observations: map[Observation]float64{
			ObservationFood: 0.6,
			ObservationNest: 0.1,
			ObservationNone: 0.3,
		},
	},
	StateReturning: {
		Transitions: map[State]float64{
			StateForaging:  0.2,
			StateReturning: 0.7,
			StateSearching: 0.1,
		},
		Observations: map[Observation]float64{
			ObservationFood: 0.1,
			ObservationNest: 0.8,
			ObservationNone: 0.1,
		},
	},
}

// ActiveInferenceAgent represents an agent with a current state.
type ActiveInferenceAgent struct {
	currentState State
}

// NewActiveInferenceAgent initializes an ActiveInferenceAgent with a valid initial state.
func NewActiveInferenceAgent(initialState State) (*ActiveInferenceAgent, error) {
	if _, exists := probabilities[initialState]; !exists {
		return nil, fmt.Errorf("invalid initial state: %s", initialState)
	}
	return &ActiveInferenceAgent{currentState: initialState}, nil
}

// UpdateState transitions the agent to a new state based on transition probabilities.
func (a *ActiveInferenceAgent) UpdateState() error {
	transitionProbs, exists := probabilities[a.currentState]
	if !exists {
		return errors.New("current state not found in probabilities map")
	}

	nextState, err := weightedChoiceState(transitionProbs.Transitions)
	if err != nil {
		return fmt.Errorf("failed to update state: %w", err)
	}

	a.currentState = nextState
	return nil
}

// Observe generates an observation based on the current state's observation probabilities.
func (a *ActiveInferenceAgent) Observe() (Observation, error) {
	observationProbs, exists := probabilities[a.currentState].Observations
	if !exists {
		return ObservationNone, errors.New("current state not found in observations map")
	}

	observation, err := weightedChoiceObservation(observationProbs)
	if err != nil {
		return ObservationNone, fmt.Errorf("failed to generate observation: %w", err)
	}

	return observation, nil
}

// weightedChoiceState selects a state based on provided probabilities using a cumulative distribution.
func weightedChoiceState(probs map[State]float64) (State, error) {
	cumulative := toCumulative(probs)
	r := rand.Float64()
	for _, entry := range cumulative {
		if r <= entry.CumulativeProb {
			return entry.State, nil
		}
	}
	return "", errors.New("invalid transition probabilities")
}

// weightedChoiceObservation selects an observation based on provided probabilities using a cumulative distribution.
func weightedChoiceObservation(probs map[Observation]float64) (Observation, error) {
	cumulative := toCumulative(probs)
	r := rand.Float64()
	for _, entry := range cumulative {
		if r <= entry.CumulativeProb {
			return entry.Observation, nil
		}
	}
	return ObservationNone, nil
}

// CumulativeProbability represents a state or observation with its cumulative probability.
type CumulativeProbability struct {
	State          State
	Observation    Observation
	CumulativeProb float64
}

// toCumulative converts a probability map to a slice of CumulativeProbability, sorted for selection.
func toCumulative[T comparable](probs map[T]float64) []CumulativeProbability {
	var cumulative []CumulativeProbability
	var sum float64
	for _, prob := range probs {
		sum += prob
	}

	var runningTotal float64
	for key, prob := range probs {
		runningTotal += prob / sum
		if any, ok := interface{}(key).(State); ok {
			cumulative = append(cumulative, CumulativeProbability{
				State:          any,
				CumulativeProb: runningTotal,
			})
		} else if any, ok := interface{}(key).(Observation); ok {
			cumulative = append(cumulative, CumulativeProbability{
				Observation:    any,
				CumulativeProb: runningTotal,
			})
		}
	}
	return cumulative
}

// simulateAntBehavior simulates the ant's behavior by observing and updating its state in a loop.
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
		behaviorChannel <- string(behavior)

		if err := agent.UpdateState(); err != nil {
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
