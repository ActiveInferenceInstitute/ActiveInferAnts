/**
 * Active Inference Agent Implementation in JavaScript
 *
 * This implementation demonstrates core active inference concepts:
 * - Belief updating through Bayesian inference
 * - Expected free energy calculation
 * - Policy selection through EFE minimization
 * - Perception-action loops
 */

import { Matrix, math } from 'mathjs';

/**
 * Active Inference Agent class
 */
export class ActiveInferenceAgent {
    constructor(config = {}) {
        this.nStates = config.nStates || 3;
        this.nObservations = config.nObservations || 3;
        this.nActions = config.nActions || 3;
        this.learningRate = config.learningRate || 0.1;
        this.uncertaintyWeight = config.uncertaintyWeight || 0.1;

        // Initialize generative model matrices
        this.A = this.initializeMatrix(this.nObservations, this.nStates); // Likelihood
        this.B = this.initializeTransitionMatrix(); // Transition model
        this.C = new Matrix([0, 0.5, 0]); // Preferences over observations
        this.D = this.initializeVector(this.nStates); // Prior beliefs

        // Current beliefs
        this.currentBeliefs = math.clone(this.D);

        // History for analysis
        this.history = {
            beliefs: [],
            actions: [],
            observations: [],
            freeEnergy: []
        };
    }

    /**
     * Initialize a random matrix with proper normalization
     */
    initializeMatrix(rows, cols) {
        const data = [];
        for (let i = 0; i < rows; i++) {
            const row = [];
            for (let j = 0; j < cols; j++) {
                row.push(Math.random());
            }
            // Normalize row to sum to 1
            const sum = row.reduce((a, b) => a + b, 0);
            data.push(row.map(x => x / sum));
        }
        return new Matrix(data);
    }

    /**
     * Initialize transition matrix (B) - state transitions given actions
     */
    initializeTransitionMatrix() {
        const matrices = [];
        for (let action = 0; action < this.nActions; action++) {
            const matrix = [];
            for (let fromState = 0; fromState < this.nStates; fromState++) {
                const row = [];
                for (let toState = 0; toState < this.nStates; toState++) {
                    // Simple transition: prefer staying in same state or moving to adjacent
                    let prob = 0.1; // Base probability
                    if (fromState === toState) prob = 0.6; // Stay in same state
                    else if (Math.abs(fromState - toState) === 1) prob = 0.2; // Move to adjacent
                    row.push(prob);
                }
                // Normalize row
                const sum = row.reduce((a, b) => a + b, 0);
                matrix.push(row.map(x => x / sum));
            }
            matrices.push(new Matrix(matrix));
        }
        return matrices;
    }

    /**
     * Initialize a normalized probability vector
     */
    initializeVector(size) {
        const data = [];
        for (let i = 0; i < size; i++) {
            data.push(Math.random());
        }
        const sum = data.reduce((a, b) => a + b, 0);
        return new Matrix([data.map(x => x / sum)]);
    }

    /**
     * Update beliefs given an observation using Bayesian inference
     */
    updateBeliefs(observation) {
        // Get likelihood for this observation
        const likelihood = this.A.subset(math.index(observation, math.range(0, this.nStates)));

        // Update beliefs: posterior = prior * likelihood
        const posterior = math.dotMultiply(this.currentBeliefs, likelihood);

        // Normalize
        const sum = math.sum(posterior);
        this.currentBeliefs = math.divide(posterior, sum);

        // Store in history
        this.history.beliefs.push(math.clone(this.currentBeliefs));

        return math.clone(this.currentBeliefs);
    }

    /**
     * Calculate variational free energy
     */
    calculateVariationalFreeEnergy() {
        // F = E_q[ln q(s) - ln p(o,s)] = -E_q[ln p(o|s)] + E_q[ln q(s)]
        const expectedLikelihood = math.sum(math.dotMultiply(
            this.currentBeliefs,
            this.A.subset(math.index(math.range(0, this.nObservations), 0))
        ));

        const entropy = this.calculateEntropy(this.currentBeliefs);

        return -expectedLikelihood - entropy;
    }

    /**
     * Calculate expected free energy for a given action
     */
    calculateExpectedFreeEnergy(action) {
        const B_action = this.B[action];

        // Calculate predicted next beliefs
        const predictedBeliefs = math.multiply(this.currentBeliefs, B_action);

        // Pragmatic value: expected surprise about preferred observations
        const pragmaticValue = this.calculatePragmaticValue(predictedBeliefs);

        // Epistemic value: information gain
        const epistemicValue = this.calculateEpistemicValue(predictedBeliefs);

        // Total EFE
        const efe = pragmaticValue - this.uncertaintyWeight * epistemicValue;

        return efe;
    }

    /**
     * Calculate pragmatic value (expected surprise about preferred observations)
     */
    calculatePragmaticValue(predictedBeliefs) {
        // For each predicted state, calculate expected surprise about preferred observations
        let pragmaticValue = 0;

        for (let state = 0; state < this.nStates; state++) {
            const stateProb = predictedBeliefs.get([0, state]);
            if (stateProb > 0) {
                // Get observation probabilities for this state
                const obsProbs = this.A.subset(math.index(math.range(0, this.nObservations), state));

                // Calculate expected surprise under preferred observations
                for (let obs = 0; obs < this.nObservations; obs++) {
                    const obsProb = obsProbs.get([obs]);
                    const preference = this.C.get([obs]);
                    if (obsProb > 0) {
                        pragmaticValue += stateProb * obsProb * preference;
                    }
                }
            }
        }

        return pragmaticValue;
    }

    /**
     * Calculate epistemic value (information gain)
     */
    calculateEpistemicValue(predictedBeliefs) {
        // Epistemic value is the entropy of predicted beliefs
        return this.calculateEntropy(predictedBeliefs);
    }

    /**
     * Calculate Shannon entropy of a probability distribution
     */
    calculateEntropy(probabilities) {
        let entropy = 0;
        for (let i = 0; i < probabilities.size()[1]; i++) {
            const p = probabilities.get([0, i]);
            if (p > 0) {
                entropy -= p * Math.log2(p);
            }
        }
        return entropy;
    }

    /**
     * Select the best action by minimizing expected free energy
     */
    selectAction() {
        const efes = [];

        // Calculate EFE for each action
        for (let action = 0; action < this.nActions; action++) {
            const efe = this.calculateExpectedFreeEnergy(action);
            efes.push(efe);
        }

        // Select action with minimum EFE
        const bestAction = efes.indexOf(Math.min(...efes));

        this.history.actions.push(bestAction);
        return bestAction;
    }

    /**
     * Execute one step of the perception-action loop
     */
    step(observation) {
        // Update beliefs based on observation
        this.updateBeliefs(observation);

        // Calculate free energy
        const fe = this.calculateVariationalFreeEnergy();
        this.history.freeEnergy.push(fe);

        // Select and return action
        const action = this.selectAction();

        this.history.observations.push(observation);

        return action;
    }

    /**
     * Get current beliefs
     */
    getBeliefs() {
        return math.clone(this.currentBeliefs);
    }

    /**
     * Get history for analysis
     */
    getHistory() {
        return {
            beliefs: this.history.beliefs.map(b => b.toArray()),
            actions: this.history.actions,
            observations: this.history.observations,
            freeEnergy: this.history.freeEnergy
        };
    }

    /**
     * Reset agent state
     */
    reset() {
        this.currentBeliefs = math.clone(this.D);
        this.history = {
            beliefs: [],
            actions: [],
            observations: [],
            freeEnergy: []
        };
    }
}

/**
 * Ant Colony Environment for multi-agent simulation
 */
export class AntColonyEnvironment {
    constructor(config = {}) {
        this.nAnts = config.nAnts || 5;
        this.gridSize = config.gridSize || 10;
        this.foodSources = config.foodSources || 3;
        this.pheromoneDecay = config.pheromoneDecay || 0.95;

        // Initialize environment
        this.grid = this.initializeGrid();
        this.pheromones = this.initializePheromones();
        this.ants = [];
        this.foodLocations = this.generateFoodSources();

        // Initialize ants with active inference agents
        for (let i = 0; i < this.nAnts; i++) {
            const position = this.getRandomPosition();
            const agent = new ActiveInferenceAgent();
            this.ants.push({
                id: i,
                position: position,
                agent: agent,
                carryingFood: false
            });
        }
    }

    initializeGrid() {
        return Array(this.gridSize).fill().map(() =>
            Array(this.gridSize).fill().map(() => ({ food: 0, obstacle: false }))
        );
    }

    initializePheromones() {
        return Array(this.gridSize).fill().map(() =>
            Array(this.gridSize).fill().map(() => ({ home: 0, food: 0 }))
        );
    }

    generateFoodSources() {
        const foodLocations = [];
        for (let i = 0; i < this.foodSources; i++) {
            const position = this.getRandomPosition();
            this.grid[position.y][position.x].food = 10; // Food amount
            foodLocations.push(position);
        }
        return foodLocations;
    }

    getRandomPosition() {
        return {
            x: Math.floor(Math.random() * this.gridSize),
            y: Math.floor(Math.random() * this.gridSize)
        };
    }

    /**
     * Generate observation for an ant at given position
     */
    generateObservation(position) {
        const { x, y } = position;

        // Simple observation: nearby food, pheromones, and obstacles
        let foodNearby = 0;
        let pheromoneHome = 0;
        let pheromoneFood = 0;

        // Check neighboring cells
        for (let dy = -1; dy <= 1; dy++) {
            for (let dx = -1; dx <= 1; dx++) {
                const nx = x + dx;
                const ny = y + dy;

                if (nx >= 0 && nx < this.gridSize && ny >= 0 && ny < this.gridSize) {
                    foodNearby = Math.max(foodNearby, this.grid[ny][nx].food);
                    pheromoneHome = Math.max(pheromoneHome, this.pheromones[ny][nx].home);
                    pheromoneFood = Math.max(pheromoneFood, this.pheromones[ny][nx].food);
                }
            }
        }

        // Discretize observations
        const obs = [
            foodNearby > 0 ? 1 : 0,           // Food present
            pheromoneHome > 0.5 ? 1 : 0,      // Strong home pheromone
            pheromoneFood > 0.5 ? 1 : 0       // Strong food pheromone
        ];

        return obs.indexOf(Math.max(...obs)); // Return index of strongest signal
    }

    /**
     * Update environment based on ant actions
     */
    updateEnvironment() {
        // Decay pheromones
        for (let y = 0; y < this.gridSize; y++) {
            for (let x = 0; x < this.gridSize; x++) {
                this.pheromones[y][x].home *= this.pheromoneDecay;
                this.pheromones[y][x].food *= this.pheromoneDecay;
            }
        }

        // Update ant positions and lay pheromones
        this.ants.forEach(ant => {
            const observation = this.generateObservation(ant.position);
            const action = ant.agent.step(observation);

            // Execute action (simplified movement)
            const { x, y } = ant.position;
            let newX = x, newY = y;

            switch (action) {
                case 0: newX = Math.max(0, x - 1); break;           // Left
                case 1: newX = Math.min(this.gridSize - 1, x + 1); break; // Right
                case 2: newY = Math.max(0, y - 1); break;           // Up
            }

            ant.position = { x: newX, y: newY };

            // Lay pheromone based on state
            if (ant.carryingFood) {
                this.pheromones[y][x].food = Math.min(1.0, this.pheromones[y][x].food + 0.1);
            } else {
                this.pheromones[y][x].home = Math.min(1.0, this.pheromones[y][x].home + 0.1);
            }

            // Check if ant found food
            if (this.grid[ant.position.y][ant.position.x].food > 0) {
                ant.carryingFood = true;
                this.grid[ant.position.y][ant.position.x].food--;
            }
        });
    }

    /**
     * Run simulation for specified number of steps
     */
    runSimulation(steps) {
        const results = [];

        for (let step = 0; step < steps; step++) {
            this.updateEnvironment();

            // Collect statistics
            const stats = {
                step: step,
                totalPheromones: this.getTotalPheromones(),
                foodCollected: this.getFoodCollected(),
                antPositions: this.ants.map(ant => ({ ...ant.position }))
            };

            results.push(stats);
        }

        return results;
    }

    getTotalPheromones() {
        let total = 0;
        for (let y = 0; y < this.gridSize; y++) {
            for (let x = 0; x < this.gridSize; x++) {
                total += this.pheromones[y][x].home + this.pheromones[y][x].food;
            }
        }
        return total;
    }

    getFoodCollected() {
        return this.ants.filter(ant => ant.carryingFood).length;
    }

    /**
     * Get current state for visualization
     */
    getState() {
        return {
            grid: this.grid,
            pheromones: this.pheromones,
            ants: this.ants.map(ant => ({
                position: ant.position,
                carryingFood: ant.carryingFood
            })),
            foodLocations: this.foodLocations
        };
    }
}

// Export for Node.js
export default { ActiveInferenceAgent, AntColonyEnvironment };
