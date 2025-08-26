#include "ActiveInferenceAgent.h"
#include <iostream>
#include <iomanip>
#include <random>
#include <chrono>
#include <vector>

/**
 * Ant Colony Environment for multi-agent simulation
 */
class AntColonyEnvironment {
public:
    struct Position {
        int x, y;
        Position(int x = 0, int y = 0) : x(x), y(y) {}
    };

    struct PheromoneLevels {
        double home = 0.0;
        double food = 0.0;
    };

    struct AntAgent {
        int id;
        Position position;
        ActiveInferenceAgent agent;
        bool carryingFood = false;
        double energy = 100.0;

        AntAgent(int id, const Position& pos, const AgentConfig& config)
            : id(id), position(pos), agent(config) {}
    };

    struct EnvironmentConfig {
        int gridSize = 8;
        int nAnts = 5;
        int foodSources = 3;
        double pheromoneDecay = 0.95;
        int maxSteps = 100;

        void validate() const {
            if (gridSize <= 0 || nAnts <= 0 || foodSources < 0) {
                throw std::invalid_argument("Invalid environment configuration");
            }
        }
    };

private:
    EnvironmentConfig config;
    std::vector<std::vector<PheromoneLevels>> pheromoneGrid;
    std::vector<std::vector<double>> foodGrid;
    std::vector<AntAgent> ants;
    std::vector<Position> foodLocations;
    std::mt19937 rng;

public:
    AntColonyEnvironment(const EnvironmentConfig& config)
        : config(config), rng(std::random_device{}()) {
        config.validate();
        initializeEnvironment();
        initializeAnts();
    }

    void runSimulation(int steps) {
        auto startTime = std::chrono::high_resolution_clock::now();

        for (int step = 0; step < steps; ++step) {
            updateEnvironment();

            if ((step + 1) % 10 == 0) {
                std::cout << "Step " << (step + 1) << "/" << steps
                         << ": Pheromones=" << std::fixed << std::setprecision(2) << getTotalPheromones()
                         << ", Food Collected=" << getFoodCollected() << std::endl;
            }
        }

        auto endTime = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(endTime - startTime);

        std::cout << "\nSimulation completed in " << duration.count() << "ms" << std::endl;
        printStatistics();
    }

private:
    void initializeEnvironment() {
        // Initialize grids
        pheromoneGrid.resize(config.gridSize);
        foodGrid.resize(config.gridSize);

        for (int y = 0; y < config.gridSize; ++y) {
            pheromoneGrid[y].resize(config.gridSize);
            foodGrid[y].resize(config.gridSize);
        }

        // Place food sources
        std::uniform_int_distribution<int> dist(0, config.gridSize - 1);
        for (int i = 0; i < config.foodSources; ++i) {
            Position pos(dist(rng), dist(rng));
            foodGrid[pos.y][pos.x] = 10.0;
            foodLocations.push_back(pos);
        }
    }

    void initializeAnts() {
        AgentConfig agentConfig;
        agentConfig.nStates = 4;
        agentConfig.nObservations = 3;
        agentConfig.nActions = 4;
        agentConfig.uncertaintyWeight = 0.2;
        agentConfig.verbose = false;

        std::uniform_int_distribution<int> dist(0, config.gridSize - 1);
        for (int i = 0; i < config.nAnts; ++i) {
            Position pos(dist(rng), dist(rng));
            ants.emplace_back(i, pos, agentConfig);
        }
    }

    void updateEnvironment() {
        // Decay pheromones
        for (int y = 0; y < config.gridSize; ++y) {
            for (int x = 0; x < config.gridSize; ++x) {
                pheromoneGrid[y][x].home *= config.pheromoneDecay;
                pheromoneGrid[y][x].food *= config.pheromoneDecay;
            }
        }

        // Update ants
        for (auto& ant : ants) {
            try {
                // Generate observation
                int observation = generateObservation(ant.position);

                // Agent takes action
                int action = ant.agent.step(observation);

                // Execute action
                Position newPosition = executeAction(ant.position, action);
                ant.position = newPosition;

                // Lay pheromone
                layPheromone(ant, newPosition);

                // Check for food
                if (foodGrid[newPosition.y][newPosition.x] > 0.0) {
                    ant.carryingFood = true;
                    foodGrid[newPosition.y][newPosition.x]--;
                    ant.energy = std::min(100.0, ant.energy + 20.0);
                }

                // Decrease energy
                ant.energy = std::max(0.0, ant.energy - 1.0);

            } catch (const std::exception& e) {
                std::cerr << "Ant " << ant.id << " error: " << e.what() << std::endl;
            }
        }
    }

    int generateObservation(const Position& position) const {
        const int x = position.x;
        const int y = position.y;
        double foodNearby = 0.0;
        double pheromoneHome = 0.0;
        double pheromoneFood = 0.0;

        // Check neighboring cells
        for (int dy = -1; dy <= 1; ++dy) {
            for (int dx = -1; dx <= 1; ++dx) {
                const int nx = x + dx;
                const int ny = y + dy;

                if (nx >= 0 && nx < config.gridSize && ny >= 0 && ny < config.gridSize) {
                    foodNearby = std::max(foodNearby, foodGrid[ny][nx]);
                    pheromoneHome = std::max(pheromoneHome, pheromoneGrid[ny][nx].home);
                    pheromoneFood = std::max(pheromoneFood, pheromoneGrid[ny][nx].food);
                }
            }
        }

        // Discretize observations
        if (foodNearby > 0.0) return 0;           // Food present
        if (pheromoneFood > 0.5) return 1;      // Strong food pheromone
        if (pheromoneHome > 0.5) return 2;      // Strong home pheromone
        return 0;                               // Default observation
    }

    Position executeAction(const Position& position, int action) const {
        int x = position.x;
        int y = position.y;

        switch (action) {
            case 0: // North
                y = std::max(0, y - 1);
                break;
            case 1: // East
                x = std::min(config.gridSize - 1, x + 1);
                break;
            case 2: // South
                y = std::min(config.gridSize - 1, y + 1);
                break;
            case 3: // West
                x = std::max(0, x - 1);
                break;
        }

        return Position(x, y);
    }

    void layPheromone(const AntAgent& ant, const Position& position) {
        if (ant.carryingFood) {
            pheromoneGrid[position.y][position.x].food =
                std::min(1.0, pheromoneGrid[position.y][position.x].food + 0.1);
        } else {
            pheromoneGrid[position.y][position.x].home =
                std::min(1.0, pheromoneGrid[position.y][position.x].home + 0.1);
        }
    }

    double getTotalPheromones() const {
        double total = 0.0;
        for (const auto& row : pheromoneGrid) {
            for (const auto& cell : row) {
                total += cell.home + cell.food;
            }
        }
        return total;
    }

    int getFoodCollected() const {
        return std::count_if(ants.begin(), ants.end(),
            [](const AntAgent& ant) { return ant.carryingFood; });
    }

    void printStatistics() const {
        const int foodCollected = getFoodCollected();
        const double totalPheromones = getTotalPheromones();
        const double averageEnergy = std::accumulate(ants.begin(), ants.end(), 0.0,
            [](double sum, const AntAgent& ant) { return sum + ant.energy; }) / ants.size();

        std::cout << "\n=== Simulation Statistics ===" << std::endl;
        std::cout << "Total Pheromones: " << std::fixed << std::setprecision(2) << totalPheromones << std::endl;
        std::cout << "Food Collected: " << foodCollected << std::endl;
        std::cout << "Average Energy: " << std::fixed << std::setprecision(2) << averageEnergy << std::endl;
        std::cout << "Ant Details:" << std::endl;

        for (const auto& ant : ants) {
            std::cout << "  Ant " << ant.id << ": Energy=" << std::fixed << std::setprecision(1) << ant.energy
                     << ", Food=" << (ant.carryingFood ? "Yes" : "No")
                     << ", Pos=(" << ant.position.x << "," << ant.position.y << ")" << std::endl;
        }
    }
};

/**
 * Run single agent demonstration
 */
void runSingleAgentDemo() {
    std::cout << "\n🧠 Single Agent C++ Demo" << std::endl;
    std::cout << "========================" << std::endl;

    AgentConfig config;
    config.nStates = 3;
    config.nObservations = 3;
    config.nActions = 3;
    config.uncertaintyWeight = 0.1;
    config.verbose = true;

    ActiveInferenceAgent agent(config);

    std::cout << "Initial beliefs: [";
    Eigen::VectorXd beliefs = agent.getBeliefs();
    for (int i = 0; i < beliefs.size(); ++i) {
        std::cout << std::fixed << std::setprecision(3) << beliefs(i);
        if (i < beliefs.size() - 1) std::cout << ", ";
    }
    std::cout << "]" << std::endl;

    // Run perception-action cycles
    std::random_device rd;
    std::mt19937 rng(rd());
    std::uniform_int_distribution<int> dist(0, 2);

    for (int t = 0; t < 10; ++t) {
        int observation = dist(rng);

        std::cout << "\nStep " << (t + 1) << ":" << std::endl;
        std::cout << "  Observation: " << observation << std::endl;

        int action = agent.step(observation);
        std::cout << "  Action: " << action << std::endl;

        beliefs = agent.getBeliefs();
        std::cout << "  Beliefs: [";
        for (int i = 0; i < beliefs.size(); ++i) {
            std::cout << std::fixed << std::setprecision(3) << beliefs(i);
            if (i < beliefs.size() - 1) std::cout << ", ";
        }
        std::cout << "]" << std::endl;

        double freeEnergy = agent.calculateVariationalFreeEnergy();
        std::cout << "  Free Energy: " << std::fixed << std::setprecision(3) << freeEnergy << std::endl;
    }

    // Show statistics
    auto statistics = agent.getStatistics();
    std::cout << "\nFinal Statistics:" << std::endl;
    std::cout << "  Total Steps: " << statistics["totalSteps"] << std::endl;
    std::cout << "  Average Free Energy: " << std::fixed << std::setprecision(4) << statistics["averageFreeEnergy"] << std::endl;
    std::cout << "  Action Distribution:" << std::endl;
    for (int i = 0; i < config.nActions; ++i) {
        std::cout << "    Action " << i << ": " << statistics["action" + std::to_string(i) + "Count"]
                 << " (" << std::fixed << std::setprecision(2) << statistics["action" + std::to_string(i) + "Frequency"] * 100 << "%)" << std::endl;
    }
}

/**
 * Run ant colony simulation
 */
void runAntColonyDemo() {
    std::cout << "\n🐜 Ant Colony C++ Demo" << std::endl;
    std::cout << "======================" << std::endl;

    AntColonyEnvironment::EnvironmentConfig config;
    config.gridSize = 8;
    config.nAnts = 5;
    config.foodSources = 3;
    config.pheromoneDecay = 0.95;

    std::cout << "Creating environment: " << config.gridSize << "x" << config.gridSize << " grid, "
             << config.nAnts << " ants, " << config.foodSources << " food sources" << std::endl;

    AntColonyEnvironment environment(config);
    environment.runSimulation(50);
}

/**
 * Demonstrate error handling
 */
void runErrorHandlingDemo() {
    std::cout << "\n⚠️  Error Handling Demo" << std::endl;
    std::cout << "=====================" << std::endl;

    // Test invalid configuration
    try {
        AgentConfig invalidConfig;
        invalidConfig.nStates = -1;  // Invalid
        ActiveInferenceAgent agent(invalidConfig);
    } catch (const std::exception& e) {
        std::cout << "Caught expected error: " << e.what() << std::endl;
    }

    // Test valid configuration
    try {
        AgentConfig validConfig;
        validConfig.nStates = 2;
        validConfig.nObservations = 2;
        validConfig.nActions = 2;

        ActiveInferenceAgent agent(validConfig);
        std::cout << "Successfully created agent with valid configuration" << std::endl;

        // Test invalid observation
        try {
            agent.updateBeliefs(-1);  // Invalid observation
        } catch (const BeliefUpdateError& e) {
            std::cout << "Caught belief update error: " << e.what() << std::endl;
        }

        auto statistics = agent.getStatistics();
        std::cout << "Agent statistics: Total steps = " << statistics["totalSteps"] << std::endl;

    } catch (const std::exception& e) {
        std::cout << "Unexpected error: " << e.what() << std::endl;
    }
}

/**
 * Main demonstration function
 */
void main() {
    std::cout << "🧠 Active Inference C++ Implementation" << std::endl;
    std::cout << "=====================================" << std::endl;

    try {
        runSingleAgentDemo();
        runAntColonyDemo();
        runErrorHandlingDemo();

        std::cout << "\n✅ All demos completed successfully!" << std::endl;
        std::cout << "\n💡 C++ Benefits Demonstrated:" << std::endl;
        std::cout << "   • High performance with Eigen matrix operations" << std::endl;
        std::cout << "   • Strong type safety and compile-time error checking" << std::endl;
        std::cout << "   • Comprehensive error handling with custom exceptions" << std::endl;
        std::cout << "   • Memory efficiency and RAII resource management" << std::endl;
        std::cout << "   • Template metaprogramming for generic operations" << std::endl;

    } catch (const std::exception& e) {
        std::cerr << "❌ Demo failed: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}

int main() {
    return main();
}
