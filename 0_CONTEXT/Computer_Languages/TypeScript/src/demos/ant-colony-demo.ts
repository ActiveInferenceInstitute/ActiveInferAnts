#!/usr/bin/env ts-node

/**
 * TypeScript Ant Colony Active Inference Demo
 *
 * This demo showcases the type-safe implementation with:
 * - Strong typing for all components
 * - Comprehensive error handling
 * - Detailed logging and analysis
 * - Multi-agent coordination
 */

import { ActiveInferenceAgent } from '../ActiveInferenceAgent.js';
import {
    AgentConfig,
    EnvironmentConfig,
    Position,
    AntAgent,
    SimulationResults,
    SimulationStep,
    GridCell,
    PheromoneLevels
} from '../types.js';

/**
 * Ant Colony Environment with type safety
 */
class AntColonyEnvironment {
    private readonly config: EnvironmentConfig;
    private grid: GridCell[][];
    private pheromoneGrid: PheromoneLevels[][];
    private ants: AntAgent[];
    private foodLocations: Position[];

    constructor(config: EnvironmentConfig) {
        this.config = config;
        this.grid = this.initializeGrid();
        this.pheromoneGrid = this.initializePheromoneGrid();
        this.ants = this.initializeAnts();
        this.foodLocations = this.generateFoodSources();
    }

    /**
     * Initialize the environment grid
     */
    private initializeGrid(): GridCell[][] {
        const grid: GridCell[][] = [];

        for (let y = 0; y < this.config.gridSize; y++) {
            const row: GridCell[] = [];
            for (let x = 0; x < this.config.gridSize; x++) {
                row.push({
                    food: 0,
                    obstacle: false,
                    pheromones: { home: 0, food: 0 }
                });
            }
            grid.push(row);
        }

        return grid;
    }

    /**
     * Initialize pheromone grid
     */
    private initializePheromoneGrid(): PheromoneLevels[][] {
        return Array(this.config.gridSize).fill(null).map(() =>
            Array(this.config.gridSize).fill(null).map(() => ({
                home: 0,
                food: 0
            }))
        );
    }

    /**
     * Initialize ants with active inference agents
     */
    private initializeAnts(): AntAgent[] {
        const ants: AntAgent[] = [];

        for (let i = 0; i < this.config.nAnts; i++) {
            const position = this.getRandomPosition();
            const agentConfig: AgentConfig = {
                nStates: 4,
                nObservations: 3,
                nActions: 4,
                learningRate: 0.1,
                uncertaintyWeight: 0.2,
                precision: 1.0
            };

            ants.push({
                id: i,
                position,
                agent: new ActiveInferenceAgent(agentConfig),
                carryingFood: false,
                energy: 100
            });
        }

        return ants;
    }

    /**
     * Generate random food sources
     */
    private generateFoodSources(): Position[] {
        const foodLocations: Position[] = [];

        for (let i = 0; i < this.config.foodSources; i++) {
            const position = this.getRandomPosition();
            this.grid[position.y][position.x].food = 10;
            foodLocations.push(position);
        }

        return foodLocations;
    }

    /**
     * Get random position within grid bounds
     */
    private getRandomPosition(): Position {
        return {
            x: Math.floor(Math.random() * this.config.gridSize),
            y: Math.floor(Math.random() * this.config.gridSize)
        };
    }

    /**
     * Generate observation for an ant at given position
     */
    private generateObservation(position: Position): number {
        const { x, y } = position;
        let foodNearby = 0;
        let pheromoneHome = 0;
        let pheromoneFood = 0;

        // Check neighboring cells
        for (let dy = -1; dy <= 1; dy++) {
            for (let dx = -1; dx <= 1; dx++) {
                const nx = x + dx;
                const ny = y + dy;

                if (nx >= 0 && nx < this.config.gridSize && ny >= 0 && ny < this.config.gridSize) {
                    foodNearby = Math.max(foodNearby, this.grid[ny][nx].food);
                    pheromoneHome = Math.max(pheromoneHome, this.pheromoneGrid[ny][nx].home);
                    pheromoneFood = Math.max(pheromoneFood, this.pheromoneGrid[ny][nx].food);
                }
            }
        }

        // Discretize observations
        if (foodNearby > 0) return 0;           // Food present
        if (pheromoneFood > 0.5) return 1;      // Strong food pheromone
        if (pheromoneHome > 0.5) return 2;      // Strong home pheromone
        return 0;                               // Default observation
    }

    /**
     * Update environment for one simulation step
     */
    private updateEnvironment(): void {
        // Decay pheromones
        for (let y = 0; y < this.config.gridSize; y++) {
            for (let x = 0; x < this.config.gridSize; x++) {
                this.pheromoneGrid[y][x].home *= this.config.pheromoneDecay;
                this.pheromoneGrid[y][x].food *= this.config.pheromoneDecay;
            }
        }

        // Update ants
        this.ants.forEach(ant => {
            try {
                // Generate observation
                const observation = this.generateObservation(ant.position);

                // Agent takes action
                const action = ant.agent.step(observation);

                // Execute action
                const newPosition = this.executeAction(ant.position, action);
                ant.position = newPosition;

                // Lay pheromone
                this.layPheromone(ant, newPosition);

                // Check for food
                if (this.grid[newPosition.y][newPosition.x].food > 0) {
                    ant.carryingFood = true;
                    this.grid[newPosition.y][newPosition.x].food--;
                    ant.energy = Math.min(100, ant.energy + 20);
                }

                // Decrease energy
                ant.energy = Math.max(0, ant.energy - 1);

            } catch (error) {
                console.error(`Ant ${ant.id} error:`, error.message);
            }
        });
    }

    /**
     * Execute action and return new position
     */
    private executeAction(position: Position, action: number): Position {
        const { x, y } = position;
        let newX = x;
        let newY = y;

        switch (action) {
            case 0: // North
                newY = Math.max(0, y - 1);
                break;
            case 1: // East
                newX = Math.min(this.config.gridSize - 1, x + 1);
                break;
            case 2: // South
                newY = Math.min(this.config.gridSize - 1, y + 1);
                break;
            case 3: // West
                newX = Math.max(0, x - 1);
                break;
        }

        return { x: newX, y: newY };
    }

    /**
     * Lay pheromone at position
     */
    private layPheromone(ant: AntAgent, position: Position): void {
        const { x, y } = position;

        if (ant.carryingFood) {
            this.pheromoneGrid[y][x].food = Math.min(1.0, this.pheromoneGrid[y][x].food + 0.1);
        } else {
            this.pheromoneGrid[y][x].home = Math.min(1.0, this.pheromoneGrid[y][x].home + 0.1);
        }
    }

    /**
     * Run simulation for specified number of steps
     */
    public runSimulation(steps: number): SimulationResults {
        const simulationSteps: SimulationStep[] = [];
        const startTime = Date.now();

        for (let step = 0; step < steps; step++) {
            this.updateEnvironment();

            // Collect statistics
            const totalPheromones = this.getTotalPheromones();
            const foodCollected = this.ants.filter(ant => ant.carryingFood).length;
            const antPositions = this.ants.map(ant => ant.position);
            const averageFreeEnergy = this.getAverageFreeEnergy();

            simulationSteps.push({
                step,
                totalPheromones,
                foodCollected,
                antPositions,
                averageFreeEnergy,
                timestamp: new Date()
            });

            // Log progress
            if ((step + 1) % 10 === 0) {
                console.log(`Step ${step + 1}/${steps}: Pheromones=${totalPheromones.toFixed(2)}, Food=${foodCollected}`);
            }
        }

        const totalTime = Date.now() - startTime;
        const convergence = this.checkConvergence();

        return {
            steps: simulationSteps,
            finalState: this.getEnvironmentState(),
            totalTime,
            convergence
        };
    }

    /**
     * Get total pheromone levels in environment
     */
    private getTotalPheromones(): number {
        let total = 0;
        for (let y = 0; y < this.config.gridSize; y++) {
            for (let x = 0; x < this.config.gridSize; x++) {
                total += this.pheromoneGrid[y][x].home + this.pheromoneGrid[y][x].food;
            }
        }
        return total;
    }

    /**
     * Get average free energy across all agents
     */
    private getAverageFreeEnergy(): number {
        const freeEnergies = this.ants.map(ant => {
            try {
                return ant.agent.calculateVariationalFreeEnergy();
            } catch {
                return 0;
            }
        });

        return freeEnergies.reduce((sum, fe) => sum + fe, 0) / freeEnergies.length;
    }

    /**
     * Check if simulation has converged
     */
    private checkConvergence(): boolean {
        // Simple convergence check: stable pheromone levels
        const currentPheromones = this.getTotalPheromones();
        // In a real implementation, you'd track history and check for stability
        return currentPheromones > 10; // Basic threshold
    }

    /**
     * Get current environment state
     */
    private getEnvironmentState() {
        return {
            grid: this.grid,
            ants: this.ants,
            foodLocations: this.foodLocations,
            pheromoneGrid: this.pheromoneGrid
        };
    }

    /**
     * Get simulation statistics
     */
    public getStatistics(): Record<string, any> {
        const agentStats = this.ants.map(ant => ({
            id: ant.id,
            position: ant.position,
            carryingFood: ant.carryingFood,
            energy: ant.energy,
            statistics: ant.agent.getStatistics()
        }));

        return {
            totalAnts: this.ants.length,
            foodSources: this.foodLocations.length,
            totalPheromones: this.getTotalPheromones(),
            foodCollected: this.ants.filter(ant => ant.carryingFood).length,
            averageEnergy: this.ants.reduce((sum, ant) => sum + ant.energy, 0) / this.ants.length,
            agentStats
        };
    }
}

/**
 * Run the ant colony simulation demo
 */
function runAntColonyDemo(): void {
    console.log("🐜 TypeScript Ant Colony Active Inference Demo");
    console.log("==============================================");

    const config: EnvironmentConfig = {
        gridSize: 8,
        nAnts: 5,
        foodSources: 3,
        pheromoneDecay: 0.95,
        maxSteps: 100
    };

    console.log(`Initializing environment: ${config.gridSize}x${config.gridSize} grid, ${config.nAnts} ants, ${config.foodSources} food sources`);

    const environment = new AntColonyEnvironment(config);

    // Run simulation
    const results = environment.runSimulation(50);

    console.log("\nSimulation Results:");
    console.log(`Total time: ${results.totalTime}ms`);
    console.log(`Convergence achieved: ${results.convergence}`);

    // Show final statistics
    const stats = environment.getStatistics();
    console.log(`\nFinal Statistics:
  Total Pheromones: ${stats.totalPheromones.toFixed(2)}
  Food Collected: ${stats.foodCollected}
  Average Energy: ${stats.averageEnergy.toFixed(2)}
  Agent Details:`);

    stats.agentStats.forEach((agent: any) => {
        console.log(`    Ant ${agent.id}: Energy=${agent.energy}, Food=${agent.carryingFood}, Pos=(${agent.position.x},${agent.position.y})`);
    });
}

/**
 * Demonstrate single agent behavior
 */
function runSingleAgentDemo(): void {
    console.log("\n🧠 Single Agent TypeScript Demo");
    console.log("===============================");

    const config: AgentConfig = {
        nStates: 3,
        nObservations: 3,
        nActions: 3,
        learningRate: 0.1,
        uncertaintyWeight: 0.1,
        precision: 1.0
    };

    const agent = new ActiveInferenceAgent(config);

    console.log("Initial beliefs:", agent.getBeliefState().current.toArray()[0]);

    // Run perception-action cycles
    for (let t = 0; t < 10; t++) {
        const observation = Math.floor(Math.random() * 3);

        console.log(`\nStep ${t + 1}:`);
        console.log(`  Observation: ${observation}`);

        const action = agent.step(observation);
        console.log(`  Action: ${action}`);

        const beliefs = agent.getBeliefState().current.toArray()[0];
        console.log(`  Beliefs: [${beliefs.map(b => b.toFixed(3)).join(', ')}]`);

        const freeEnergy = agent.calculateVariationalFreeEnergy();
        console.log(`  Free Energy: ${freeEnergy.toFixed(3)}`);
    }

    // Show statistics
    const statistics = agent.getStatistics();
    console.log(`\nFinal Statistics:
  Total Steps: ${statistics.totalSteps}
  Average Free Energy: ${statistics.averageFreeEnergy.toFixed(4)}
  Action Distribution: ${JSON.stringify(statistics.actionDistribution)}`);
}

/**
 * Demonstrate error handling
 */
function runErrorHandlingDemo(): void {
    console.log("\n⚠️  Error Handling Demo");
    console.log("=====================");

    // Test invalid configuration
    try {
        const invalidConfig: AgentConfig = {
            nStates: -1,  // Invalid
            nObservations: 3,
            nActions: 3,
            learningRate: 0.1,
            uncertaintyWeight: 0.1,
            precision: 1.0
        };
        new ActiveInferenceAgent(invalidConfig);
    } catch (error) {
        console.log(`Caught expected error: ${error.message}`);
    }

    // Test valid configuration
    try {
        const validConfig: AgentConfig = {
            nStates: 2,
            nObservations: 2,
            nActions: 2,
            learningRate: 0.1,
            uncertaintyWeight: 0.1,
            precision: 1.0
        };
        const agent = new ActiveInferenceAgent(validConfig);
        console.log("Successfully created agent with valid configuration");
        console.log("Agent statistics:", agent.getStatistics());
    } catch (error) {
        console.log(`Unexpected error: ${error.message}`);
    }
}

/**
 * Main demo runner
 */
function main(): void {
    console.log("🧠 TypeScript Active Inference Implementation");
    console.log("===========================================\n");

    try {
        runSingleAgentDemo();
        runAntColonyDemo();
        runErrorHandlingDemo();

        console.log("\n✅ All demos completed successfully!");
        console.log("\n💡 TypeScript Benefits Demonstrated:");
        console.log("   • Strong static typing prevents runtime errors");
        console.log("   • Comprehensive error handling with custom error types");
        console.log("   • Type-safe agent interactions and state management");
        console.log("   • Detailed logging and performance monitoring");
        console.log("   • IDE support with autocomplete and refactoring");

    } catch (error) {
        console.error("❌ Demo failed:", error.message);
        process.exit(1);
    }
}

// Run demo if called directly
if (import.meta.url === `file://${process.argv[1]}`) {
    main();
}

export { runAntColonyDemo, runSingleAgentDemo, runErrorHandlingDemo };
