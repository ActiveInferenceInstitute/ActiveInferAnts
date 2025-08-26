#!/usr/bin/env node

/**
 * Ant Colony Active Inference Demo
 *
 * This demo shows multiple active inference agents working together
 * in an ant colony environment, demonstrating collective intelligence
 * through pheromone communication and coordinated behavior.
 */

import { ActiveInferenceAgent, AntColonyEnvironment } from './active_inference.js';

/**
 * Run a single agent simulation
 */
function runSingleAgentDemo() {
    console.log("🧠 Single Agent Active Inference Demo");
    console.log("=====================================");

    const agent = new ActiveInferenceAgent({
        nStates: 3,
        nObservations: 3,
        nActions: 3,
        uncertaintyWeight: 0.1
    });

    console.log("Initial beliefs:", agent.getBeliefs().toArray());

    // Simulate perception-action cycles
    for (let t = 0; t < 10; t++) {
        // Generate random observation
        const observation = Math.floor(Math.random() * 3);

        console.log(`\nStep ${t + 1}:`);
        console.log(`  Observation: ${observation}`);

        const action = agent.step(observation);
        console.log(`  Action: ${action}`);
        console.log(`  Beliefs: [${agent.getBeliefs().toArray()[0].map(b => b.toFixed(3)).join(', ')}]`);

        const freeEnergy = agent.history.freeEnergy[agent.history.freeEnergy.length - 1];
        console.log(`  Free Energy: ${freeEnergy.toFixed(3)}`);
    }

    const history = agent.getHistory();
    console.log(`\nFinal Statistics:
  Total Actions: ${history.actions.length}
  Average Free Energy: ${history.freeEnergy.reduce((a, b) => a + b, 0) / history.freeEnergy.length}
  Action Distribution: ${JSON.stringify(getActionDistribution(history.actions))}`);
}

/**
 * Run multi-agent ant colony simulation
 */
function runAntColonyDemo() {
    console.log("\n🐜 Ant Colony Active Inference Demo");
    console.log("===================================");

    const environment = new AntColonyEnvironment({
        nAnts: 5,
        gridSize: 8,
        foodSources: 3
    });

    console.log(`Created ant colony with ${environment.nAnts} ants on ${environment.gridSize}x${environment.gridSize} grid`);

    // Run simulation
    const results = environment.runSimulation(20);

    console.log("\nSimulation Results:");
    results.forEach(result => {
        console.log(`Step ${result.step}: Pheromones=${result.totalPheromones.toFixed(2)}, Food Collected=${result.foodCollected}`);
    });

    // Show final state
    const finalState = environment.getState();
    console.log(`\nFinal State:
  Ants: ${finalState.ants.length}
  Food Sources: ${finalState.foodLocations.length}
  Total Pheromones: ${environment.getTotalPheromones().toFixed(2)}
  Food Collected: ${environment.getFoodCollected()}`);
}

/**
 * Analyze agent behavior patterns
 */
function analyzeAgentBehavior() {
    console.log("\n📊 Agent Behavior Analysis");
    console.log("==========================");

    const agent = new ActiveInferenceAgent({
        nStates: 4,
        nObservations: 3,
        nActions: 4,
        uncertaintyWeight: 0.2
    });

    // Run multiple episodes
    const episodes = 5;
    const episodeResults = [];

    for (let episode = 0; episode < episodes; episode++) {
        agent.reset();

        for (let t = 0; t < 15; t++) {
            const observation = Math.floor(Math.random() * 3);
            agent.step(observation);
        }

        const history = agent.getHistory();
        episodeResults.push({
            episode,
            totalActions: history.actions.length,
            avgFreeEnergy: history.freeEnergy.reduce((a, b) => a + b, 0) / history.freeEnergy.length,
            actionDistribution: getActionDistribution(history.actions),
            finalBeliefs: history.beliefs[history.beliefs.length - 1][0]
        });
    }

    console.log("Episode Results:");
    episodeResults.forEach(result => {
        console.log(`  Episode ${result.episode + 1}:
    Actions: ${result.totalActions}
    Avg Free Energy: ${result.avgFreeEnergy.toFixed(4)}
    Action Distribution: ${JSON.stringify(result.actionDistribution)}
    Final Beliefs: [${result.finalBeliefs.map(b => b.toFixed(3)).join(', ')}]`);
    });
}

/**
 * Helper function to get action distribution
 */
function getActionDistribution(actions) {
    const distribution = {};
    actions.forEach(action => {
        distribution[action] = (distribution[action] || 0) + 1;
    });
    return distribution;
}

/**
 * Demonstrate belief updating
 */
function demonstrateBeliefUpdating() {
    console.log("\n🎯 Belief Updating Demo");
    console.log("======================");

    const agent = new ActiveInferenceAgent({
        nStates: 2,
        nObservations: 2,
        nActions: 2
    });

    console.log("Initial beliefs:", agent.getBeliefs().toArray()[0]);

    // Provide consistent observations
    for (let i = 0; i < 5; i++) {
        console.log(`\nObservation ${i + 1}: 0`);
        agent.updateBeliefs(0);
        console.log("Updated beliefs:", agent.getBeliefs().toArray()[0].map(b => b.toFixed(3)));
    }

    // Introduce conflicting observation
    console.log(`\nObservation 6: 1 (conflicting)`);
    agent.updateBeliefs(1);
    console.log("Updated beliefs:", agent.getBeliefs().toArray()[0].map(b => b.toFixed(3)));
}

/**
 * Main demo runner
 */
function main() {
    console.log("🧠 Active Inference JavaScript Implementation");
    console.log("============================================\n");

    try {
        runSingleAgentDemo();
        runAntColonyDemo();
        analyzeAgentBehavior();
        demonstrateBeliefUpdating();

        console.log("\n✅ All demos completed successfully!");
        console.log("\n💡 Key Takeaways:");
        console.log("   • Active inference agents minimize free energy through belief updating");
        console.log("   • Multi-agent systems can exhibit collective intelligence");
        console.log("   • Belief updating follows Bayesian principles");
        console.log("   • Actions are selected to minimize expected free energy");

    } catch (error) {
        console.error("❌ Demo failed:", error.message);
        process.exit(1);
    }
}

// Run demo if called directly
if (import.meta.url === `file://${process.argv[1]}`) {
    main();
}

export { runSingleAgentDemo, runAntColonyDemo, analyzeAgentBehavior, demonstrateBeliefUpdating };
