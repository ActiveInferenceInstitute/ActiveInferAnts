import java.util.*;
import java.util.stream.Collectors;

class Ant {
    private double freeEnergy;
    private Map<String, Double> beliefs;
    private Map<String, Double> observations;
    private Map<String, Double> priors;
    private double precision;

    public Ant() {
        this.freeEnergy = 0;
        this.beliefs = new HashMap<>();
        this.observations = new HashMap<>();
        this.priors = initializePriors();
        this.precision = 1.0;
    }

    private Map<String, Double> initializePriors() {
        Map<String, Double> priors = new HashMap<>();
        priors.put("food", 0.5);
        priors.put("pheromone", 0.5);
        priors.put("danger", 0.1);
        return priors;
    }

    public void updateBeliefs(Map<String, Double> newObservations) {
        // Bayesian belief update
        for (Map.Entry<String, Double> entry : newObservations.entrySet()) {
            String key = entry.getKey();
            double observedValue = entry.getValue();
            double currentBelief = beliefs.getOrDefault(key, priors.get(key));
            double prior = priors.get(key);
            
            // Calculate posterior using Bayes' rule
            double likelihood = calculateLikelihood(observedValue, currentBelief);
            double posterior = (likelihood * currentBelief) / 
                               ((likelihood * currentBelief) + (likelihood * (1 - currentBelief)));
            
            beliefs.put(key, posterior);
        }
        this.observations = newObservations;
    }

    private double calculateLikelihood(double observation, double belief) {
        // Simplified likelihood calculation using Gaussian distribution
        return Math.exp(-Math.pow(observation - belief, 2) / (2 * Math.pow(precision, 2))) /
               (Math.sqrt(2 * Math.PI) * precision);
    }

    public void minimizeFreeEnergy() {
        double accuracy = calculateAccuracy();
        double complexity = calculateComplexity();
        this.freeEnergy = complexity - accuracy;
    }

    private double calculateAccuracy() {
        // Calculate accuracy term (negative log-likelihood)
        return -observations.entrySet().stream()
            .mapToDouble(entry -> {
                String key = entry.getKey();
                double observedValue = entry.getValue();
                double belief = beliefs.get(key);
                return Math.log(calculateLikelihood(observedValue, belief));
            })
            .sum();
    }

    private double calculateComplexity() {
        // Calculate complexity term (KL divergence between posterior and prior)
        return beliefs.entrySet().stream()
            .mapToDouble(entry -> {
                String key = entry.getKey();
                double posterior = entry.getValue();
                double prior = priors.get(key);
                return posterior * Math.log(posterior / prior);
            })
            .sum();
    }

    public String selectAction() {
        // Select action that minimizes expected free energy
        Map<String, Double> expectedFreeEnergies = new HashMap<>();
        String[] actions = {"forage", "return", "communicate", "explore"};
        
        for (String action : actions) {
            double expectedFreeEnergy = calculateExpectedFreeEnergy(action);
            expectedFreeEnergies.put(action, expectedFreeEnergy);
        }
        
        // Return the action with the lowest expected free energy
        return expectedFreeEnergies.entrySet().stream()
            .min(Map.Entry.comparingByValue())
            .map(Map.Entry::getKey)
            .orElse("explore"); // Default to explore if no action is found
    }

    private double calculateExpectedFreeEnergy(String action) {
        // Simplified calculation of expected free energy for a given action
        Map<String, Double> expectedObservations = predictObservations(action);
        double expectedAccuracy = calculateExpectedAccuracy(expectedObservations);
        double expectedComplexity = calculateExpectedComplexity(expectedObservations);
        return expectedComplexity - expectedAccuracy;
    }

    private Map<String, Double> predictObservations(String action) {
        // Predict observations based on current beliefs and the proposed action
        Map<String, Double> predictedObservations = new HashMap<>(beliefs);
        
        // Modify predictions based on the action
        switch (action) {
            case "forage":
                predictedObservations.put("food", predictedObservations.get("food") * 1.2);
                break;
            case "return":
                predictedObservations.put("pheromone", predictedObservations.get("pheromone") * 1.5);
                break;
            case "communicate":
                predictedObservations.put("pheromone", predictedObservations.get("pheromone") * 1.3);
                break;
            case "explore":
                predictedObservations.put("food", predictedObservations.get("food") * 1.1);
                predictedObservations.put("danger", predictedObservations.get("danger") * 1.2);
                break;
        }
        
        return predictedObservations;
    }

    private double calculateExpectedAccuracy(Map<String, Double> expectedObservations) {
        // Calculate expected accuracy for predicted observations
        return -expectedObservations.entrySet().stream()
            .mapToDouble(entry -> {
                String key = entry.getKey();
                double predictedValue = entry.getValue();
                double belief = beliefs.get(key);
                return Math.log(calculateLikelihood(predictedValue, belief));
            })
            .sum();
    }

    private double calculateExpectedComplexity(Map<String, Double> expectedObservations) {
        // Calculate expected complexity for predicted observations
        return expectedObservations.entrySet().stream()
            .mapToDouble(entry -> {
                String key = entry.getKey();
                double predictedValue = entry.getValue();
                double prior = priors.get(key);
                return predictedValue * Math.log(predictedValue / prior);
            })
            .sum();
    }
}

public class AntColony {
    private List<Ant> ants;
    private Map<String, Double> environment;

    public AntColony(int antCount) {
        this.ants = new ArrayList<>();
        for (int i = 0; i < antCount; i++) {
            ants.add(new Ant());
        }
        this.environment = initializeEnvironment();
    }

    private Map<String, Double> initializeEnvironment() {
        Map<String, Double> env = new HashMap<>();
        env.put("food", 0.5);
        env.put("pheromone", 0.2);
        env.put("danger", 0.1);
        return env;
    }

    public void runSimulation(int steps) {
        for (int i = 0; i < steps; i++) {
            System.out.println("Step " + (i + 1));
            for (Ant ant : ants) {
                // Active Inference loop
                Map<String, Double> observations = getObservations();
                ant.updateBeliefs(observations);
                ant.minimizeFreeEnergy();
                String action = ant.selectAction();
                executeAction(action);
            }
            updateEnvironment();
        }
    }

    private Map<String, Double> getObservations() {
        // Generate observations based on the current environment state
        Map<String, Double> observations = new HashMap<>(environment);
        // Add some noise to the observations
        observations.replaceAll((k, v) -> v + (Math.random() - 0.5) * 0.1);
        return observations;
    }

    private void executeAction(String action) {
        // Simulate action execution and its effect on the environment
        System.out.println("Executing action: " + action);
        switch (action) {
            case "forage":
                environment.put("food", Math.max(0, environment.get("food") - 0.1));
                break;
            case "return":
                environment.put("pheromone", Math.min(1, environment.get("pheromone") + 0.1));
                break;
            case "communicate":
                environment.put("pheromone", Math.min(1, environment.get("pheromone") + 0.05));
                break;
            case "explore":
                environment.put("food", Math.min(1, environment.get("food") + 0.05));
                environment.put("danger", Math.max(0, environment.get("danger") - 0.02));
                break;
        }
    }

    private void updateEnvironment() {
        // Simulate environmental changes
        environment.replaceAll((k, v) -> Math.max(0, Math.min(1, v + (Math.random() - 0.5) * 0.1)));
    }

    public static void main(String[] args) {
        AntColony colony = new AntColony(10);
        colony.runSimulation(100);
    }
}