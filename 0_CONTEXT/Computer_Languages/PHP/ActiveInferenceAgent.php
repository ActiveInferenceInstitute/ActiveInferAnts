<?php

/**
 * Active Inference Agent Implementation in PHP
 *
 * This class implements the core active inference algorithm using PHP's
 * object-oriented capabilities and array operations.
 */

class ActiveInferenceAgent {
    private int $nStates;
    private int $nObservations;
    private int $nActions;
    private array $beliefs;
    private array $priorBeliefs;
    private array $aMatrix;  // P(o|s) - observation likelihood
    private array $bMatrix;  // P(s'|s,a) - state transitions
    private array $cVector;  // P(o) - observation preferences
    private float $precision;
    private float $learningRate;

    // History for analysis
    private array $beliefHistory = [];
    private array $actionHistory = [];
    private array $observationHistory = [];
    private array $freeEnergyHistory = [];

    /**
     * Constructor
     */
    public function __construct(int $nStates, int $nObservations, int $nActions,
                               float $precision = 1.0, float $learningRate = 0.1) {
        $this->nStates = $nStates;
        $this->nObservations = $nObservations;
        $this->nActions = $nActions;
        $this->precision = $precision;
        $this->learningRate = $learningRate;

        $this->initializeGenerativeModel();
        $this->beliefs = $this->priorBeliefs;
        $this->beliefHistory[] = $this->beliefs;
    }

    /**
     * Initialize the generative model matrices
     */
    private function initializeGenerativeModel(): void {
        // Initialize A matrix (observation likelihood)
        $this->aMatrix = [];
        for ($o = 0; $o < $this->nObservations; $o++) {
            $this->aMatrix[$o] = [];
            for ($s = 0; $s < $this->nStates; $s++) {
                // Diagonal structure with some noise
                if (($s % $this->nObservations) === $o) {
                    $this->aMatrix[$o][$s] = 0.8;
                } else {
                    $this->aMatrix[$o][$s] = 0.2 / ($this->nObservations - 1);
                }
            }
        }

        // Initialize B matrix (state transitions)
        $this->bMatrix = [];
        for ($a = 0; $a < $this->nActions; $a++) {
            $this->bMatrix[$a] = [];
            for ($s = 0; $s < $this->nStates; $s++) {
                $this->bMatrix[$a][$s] = [];
                for ($sNext = 0; $sNext < $this->nStates; $sNext++) {
                    // Action-specific transition patterns
                    if ($sNext === (($s + $a + 1) % $this->nStates)) {
                        $this->bMatrix[$a][$s][$sNext] = 0.7;
                    } elseif ($sNext === $s) {
                        $this->bMatrix[$a][$s][$sNext] = 0.2;
                    } else {
                        $this->bMatrix[$a][$s][$sNext] = 0.1 / ($this->nStates - 2);
                    }
                }
            }
        }

        // Initialize C vector (observation preferences)
        $this->cVector = [];
        for ($o = 0; $o < $this->nObservations; $o++) {
            $this->cVector[$o] = ($o === 0) ? 0.0 : 0.5;
        }

        // Initialize D vector (prior beliefs)
        $this->priorBeliefs = [];
        for ($s = 0; $s < $this->nStates; $s++) {
            $this->priorBeliefs[$s] = 1.0 / $this->nStates;
        }
    }

    /**
     * Update beliefs based on observation using Bayesian inference
     */
    public function updateBeliefs(int $observation): void {
        // Get likelihood for this observation
        $likelihood = $this->aMatrix[$observation];

        // Compute posterior: P(s|o) ∝ P(o|s) * P(s)
        $posterior = [];
        for ($s = 0; $s < $this->nStates; $s++) {
            $posterior[$s] = $likelihood[$s] * $this->beliefs[$s];
        }

        // Normalize
        $sum = array_sum($posterior);
        if ($sum > 0) {
            for ($s = 0; $s < $this->nStates; $s++) {
                $this->beliefs[$s] = $posterior[$s] / $sum;
            }
        }

        // Store in history
        $this->beliefHistory[] = $this->beliefs;
        $this->observationHistory[] = $observation;
    }

    /**
     * Select action by minimizing expected free energy
     */
    public function selectAction(): int {
        $minEfe = PHP_FLOAT_MAX;
        $bestAction = 0;

        for ($action = 0; $action < $this->nActions; $action++) {
            $predictedBeliefs = $this->predictBeliefs($action);
            $efe = $this->calculateExpectedFreeEnergy($predictedBeliefs);

            if ($efe < $minEfe) {
                $minEfe = $efe;
                $bestAction = $action;
            }
        }

        $this->actionHistory[] = $bestAction;
        return $bestAction;
    }

    /**
     * Predict beliefs after taking an action
     */
    private function predictBeliefs(int $action): array {
        $predictedBeliefs = array_fill(0, $this->nStates, 0.0);

        for ($sNext = 0; $sNext < $this->nStates; $sNext++) {
            for ($s = 0; $s < $this->nStates; $s++) {
                $predictedBeliefs[$sNext] += $this->bMatrix[$action][$s][$sNext] * $this->beliefs[$s];
            }
        }

        return $predictedBeliefs;
    }

    /**
     * Calculate expected free energy for predicted beliefs
     */
    private function calculateExpectedFreeEnergy(array $predictedBeliefs): float {
        $efe = 0.0;

        for ($s = 0; $s < $this->nStates; $s++) {
            if ($predictedBeliefs[$s] > 0) {
                // KL divergence between predicted beliefs and prior
                $efe += $predictedBeliefs[$s] * log($predictedBeliefs[$s] / $this->priorBeliefs[$s]);
            }
        }

        return $efe * $this->precision;
    }

    /**
     * Calculate current variational free energy
     */
    public function calculateFreeEnergy(): float {
        $fe = 0.0;

        for ($s = 0; $s < $this->nStates; $s++) {
            if ($this->beliefs[$s] > 0) {
                $fe += $this->beliefs[$s] * log($this->beliefs[$s] / $this->priorBeliefs[$s]);
            }
        }

        $this->freeEnergyHistory[] = $fe;
        return $fe;
    }

    /**
     * Execute one perception-action cycle
     */
    public function step(int $observation): int {
        $this->updateBeliefs($observation);
        $action = $this->selectAction();
        $this->calculateFreeEnergy();
        return $action;
    }

    /**
     * Learn from experience
     */
    public function learn(int $observation, int $action, int $nextObservation): void {
        // Simple learning: reinforce the most likely state
        $maxState = array_keys($this->beliefs, max($this->beliefs))[0];

        // Update A matrix
        $this->aMatrix[$observation][$maxState] += $this->learningRate;

        // Renormalize row
        $rowSum = array_sum($this->aMatrix[$observation]);
        for ($s = 0; $s < $this->nStates; $s++) {
            $this->aMatrix[$observation][$s] /= $rowSum;
        }
    }

    /**
     * Calculate belief entropy
     */
    public function calculateBeliefEntropy(): float {
        $entropy = 0.0;
        for ($s = 0; $s < $this->nStates; $s++) {
            if ($this->beliefs[$s] > 0) {
                $entropy -= $this->beliefs[$s] * log($this->beliefs[$s]);
            }
        }
        return $entropy;
    }

    /**
     * Get current beliefs
     */
    public function getBeliefs(): array {
        return $this->beliefs;
    }

    /**
     * Get belief history
     */
    public function getBeliefHistory(): array {
        return $this->beliefHistory;
    }

    /**
     * Print agent statistics
     */
    public function printStatistics(): void {
        echo "Active Inference Agent Statistics:\n";
        echo "=====================================\n";
        echo "States: {$this->nStates}, Observations: {$this->nObservations}, Actions: {$this->nActions}\n";
        echo "Precision: {$this->precision}, Learning Rate: {$this->learningRate}\n";

        if (!empty($this->actionHistory)) {
            echo "Total steps: " . count($this->actionHistory) . "\n";
            echo "Final beliefs: [";
            for ($s = 0; $s < $this->nStates; $s++) {
                echo number_format($this->beliefs[$s], 3);
                if ($s < $this->nStates - 1) {
                    echo ", ";
                }
            }
            echo "]\n";

            if (!empty($this->freeEnergyHistory)) {
                $finalFe = end($this->freeEnergyHistory);
                echo "Final free energy: " . number_format($finalFe, 4) . "\n";
            }

            $entropy = $this->calculateBeliefEntropy();
            echo "Belief entropy: " . number_format($entropy, 4) . "\n";
        } else {
            echo "No steps taken yet.\n";
        }
    }

    /**
     * Get comprehensive statistics
     */
    public function getStatistics(): array {
        $stats = [
            'n_states' => $this->nStates,
            'n_observations' => $this->nObservations,
            'n_actions' => $this->nActions,
            'precision' => $this->precision,
            'learning_rate' => $this->learningRate,
            'current_beliefs' => $this->beliefs,
            'total_steps' => count($this->actionHistory),
            'belief_history_length' => count($this->beliefHistory)
        ];

        if (!empty($this->freeEnergyHistory)) {
            $stats['final_free_energy'] = end($this->freeEnergyHistory);
            $stats['free_energy_history'] = $this->freeEnergyHistory;
        }

        if (!empty($this->actionHistory)) {
            $stats['action_history'] = $this->actionHistory;
            $stats['observation_history'] = $this->observationHistory;
        }

        $stats['belief_entropy'] = $this->calculateBeliefEntropy();

        return $stats;
    }
}

/**
 * Demonstration class
 */
class ActiveInferenceDemo {
    public static function run(): void {
        echo "🧠 Active Inference PHP Implementation\n";
        echo "=====================================\n\n";

        // Create agent
        $nStates = 3;
        $nObservations = 3;
        $nActions = 2;

        echo "Creating agent with {$nStates} states, {$nObservations} observations, {$nActions} actions...\n\n";

        $agent = new ActiveInferenceAgent($nStates, $nObservations, $nActions, 1.0, 0.1);

        // Print initial beliefs
        echo "Initial beliefs: [";
        $beliefs = $agent->getBeliefs();
        for ($s = 0; $s < count($beliefs); $s++) {
            echo number_format($beliefs[$s], 3);
            if ($s < count($beliefs) - 1) {
                echo ", ";
            }
        }
        echo "]\n\n";

        // Run simulation
        $nSteps = 10;
        echo "Running simulation for {$nSteps} steps...\n\n";

        for ($step = 1; $step <= $nSteps; $step++) {
            // Generate random observation
            $observation = random_int(1, $nObservations);

            echo "Step {$step}:\n";
            echo "  Observation: {$observation}\n";

            // Execute perception-action cycle
            $action = $agent->step($observation);

            echo "  Selected action: {$action}\n";

            // Print current beliefs
            $currentBeliefs = $agent->getBeliefs();
            echo "  Updated beliefs: [";
            for ($s = 0; $s < count($currentBeliefs); $s++) {
                echo number_format($currentBeliefs[$s], 3);
                if ($s < count($currentBeliefs) - 1) {
                    echo ", ";
                }
            }
            echo "]\n";

            // Print free energy
            $stats = $agent->getStatistics();
            if (isset($stats['final_free_energy'])) {
                echo "  Free energy: " . number_format($stats['final_free_energy'], 4) . "\n";
            }

            echo "\n";
        }

        // Print final statistics
        echo "\n";
        $agent->printStatistics();

        echo "\n✅ PHP Active Inference simulation completed!\n";
    }

    /**
     * Multi-agent simulation demo
     */
    public static function runMultiAgentDemo(): void {
        echo "\n🐜 Multi-Agent PHP Demo\n";
        echo "======================\n\n";

        $nAgents = 3;
        $agents = [];

        // Create multiple agents
        for ($i = 0; $i < $nAgents; $i++) {
            $agents[] = new ActiveInferenceAgent(3, 3, 2, 1.0, 0.1);
        }

        // Run multi-agent simulation
        for ($step = 1; $step <= 5; $step++) {
            echo "Multi-agent Step {$step}:\n";

            for ($i = 0; $i < $nAgents; $i++) {
                $observation = random_int(1, 3);
                $action = $agents[$i]->step($observation);

                $beliefs = $agents[$i]->getBeliefs();
                $maxBelief = max($beliefs);

                echo "  Agent " . ($i + 1) . ": Obs={$observation}, Action={$action}, ";
                echo "Best Belief=" . number_format($maxBelief, 3) . "\n";
            }
            echo "\n";
        }

        echo "✅ Multi-agent simulation completed!\n";
    }
}

// Run the demo if this file is executed directly
if (basename(__FILE__) === basename($_SERVER['PHP_SELF'] ?? __FILE__)) {
    ActiveInferenceDemo::run();
    ActiveInferenceDemo::runMultiAgentDemo();
}
?>
