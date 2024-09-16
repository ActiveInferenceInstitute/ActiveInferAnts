import java.util.*;
import java.util.stream.Collectors;

/**
 * Represents an individual ant with beliefs about the environment.
 */
class Ant {
    private double freeEnergy;
    private Map<String, Double> beliefs;
    private Map<String, Double> observations;
    private Map<String, Double> priors;
    private final double precision;

    /**
     * Initializes a new Ant with default priors and precision.
     */
    public Ant() {
        this.freeEnergy = 0.0;
        this.beliefs = new HashMap<>();
        this.observations = new HashMap<>();
        this.priors = initializePriors();
        this.precision = 1.0;
    }

    /**
     * Initializes prior probabilities for different environmental factors.
     *
     * @return A map of priors.
     */
    private Map<String, Double> initializePriors() {
        Map<String, Double> priors = new HashMap<>();
        priors.put("food", 0.5);
        priors.put("pheromone", 0.5);
        priors.put("danger", 0.1);
        return Collections.unmodifiableMap(priors);
    }

    /**
     * Updates the ant's beliefs based on new observations using Bayesian inference.
     *
     * @param newObservations The latest environmental observations.
     */
    public void updateBeliefs(Map<String, Double> newObservations) {
        for (Map.Entry<String, Double> entry : newObservations.entrySet()) {
            String key = entry.getKey();
            double observedValue = entry.getValue();
            double priorBelief = priors.getOrDefault(key, 0.0);
            double likelihood = calculateLikelihood(observedValue, priorBelief);
            double posterior = (likelihood * priorBelief) / 
                               (likelihood * priorBelief + (1 - likelihood) * (1 - priorBelief));
            beliefs.put(key, posterior);
        }
        this.observations = new HashMap<>(newObservations);
    }

    /**
     * Calculates the likelihood of an observation given a belief.
     *
     * @param observation The observed value.
     * @param belief      The current belief.
     * @return The calculated likelihood.
     */
    private double calculateLikelihood(double observation, double belief) {
        double variance = Math.pow(precision, 2);
        return (1 / (Math.sqrt(2 * Math.PI) * precision)) *
               Math.exp(-Math.pow(observation - belief, 2) / (2 * variance));
    }

    /**
     * Minimizes the free energy based on accuracy and complexity.
     */
    public void minimizeFreeEnergy() {
        double accuracy = calculateAccuracy();
        double complexity = calculateComplexity();
        this.freeEnergy = complexity - accuracy;
    }

    /**
     * Calculates the accuracy term as the negative log-likelihood.
     *
     * @return The accuracy value.
     */
    private double calculateAccuracy() {
        return observations.values().stream()
                .mapToDouble(obs -> Math.log(calculateLikelihood(obs, beliefs.getOrDefault("food", priors.get("food")))))
                .sum() * -1;
    }

    /**
     * Calculates the complexity term as the Kullback-Leibler divergence between posterior and prior.
     *
     * @return The complexity value.
     */
    private double calculateComplexity() {
        return beliefs.entrySet().stream()
                .mapToDouble(entry -> entry.getValue() * Math.log(entry.getValue() / priors.get(entry.getKey())))
                .sum();
    }

    /**
     * Selects an action that minimizes the expected free energy.
     *
     * @return The chosen action.
     */
    public String selectAction() {
        Map<String, Double> expectedFreeEnergies = new HashMap<>();
        String[] actions = {"forage", "return", "communicate", "explore"};

        for (String action : actions) {
            double efe = calculateExpectedFreeEnergy(action);
            expectedFreeEnergies.put(action, efe);
        }

        return expectedFreeEnergies.entrySet().stream()
                .min(Map.Entry.comparingByValue())
                .map(Map.Entry::getKey)
                .orElse("explore");
    }

    /**
     * Calculates the expected free energy for a given action.
     *
     * @param action The action to evaluate.
     * @return The expected free energy.
     */
    private double calculateExpectedFreeEnergy(String action) {
        Map<String, Double> predictedObservations = predictObservations(action);
        double expectedAccuracy = calculateExpectedAccuracy(predictedObservations);
        double expectedComplexity = calculateExpectedComplexity(predictedObservations);
        return expectedComplexity - expectedAccuracy;
    }

    /**
     * Predicts observations based on the current beliefs and the proposed action.
     *
     * @param action The action to predict.
     * @return A map of predicted observations.
     */
    private Map<String, Double> predictObservations(String action) {
        Map<String, Double> predicted = new HashMap<>(beliefs);

        switch (action) {
            case "forage":
                predicted.put("food", predicted.getOrDefault("food", 0.0) * 1.2);
                break;
            case "return":
                predicted.put("pheromone", predicted.getOrDefault("pheromone", 0.0) * 1.5);
                break;
            case "communicate":
                predicted.put("pheromone", predicted.getOrDefault("pheromone", 0.0) * 1.3);
                break;
            case "explore":
                predicted.put("food", predicted.getOrDefault("food", 0.0) * 1.1);
                predicted.put("danger", predicted.getOrDefault("danger", 0.0) * 1.2);
                break;
            default:
                break;
        }

        return predicted;
    }

    /**
     * Calculates the expected accuracy for predicted observations.
     *
     * @param predictedObservations The predicted observations.
     * @return The expected accuracy.
     */
    private double calculateExpectedAccuracy(Map<String, Double> predictedObservations) {
        return predictedObservations.values().stream()
                .mapToDouble(pred -> Math.log(calculateLikelihood(pred, beliefs.getOrDefault("food", priors.get("food")))))
                .sum() * -1;
    }

    /**
     * Calculates the expected complexity for predicted observations.
     *
     * @param predictedObservations The predicted observations.
     * @return The expected complexity.
     */
    private double calculateExpectedComplexity(Map<String, Double> predictedObservations) {
        return predictedObservations.entrySet().stream()
                .mapToDouble(entry -> entry.getValue() * Math.log(entry.getValue() / priors.get(entry.getKey())))
                .sum();
    }
}

/**
 * Represents a colony of ants and manages the simulation environment.
 */
public class AntColony {
    private final List<Ant> ants;
    private final Map<String, Double> environment;
    private final Random random;

    /**
     * Initializes an AntColony with a specified number of ants.
     *
     * @param antCount The number of ants in the colony.
     */
    public AntColony(int antCount) {
        this.ants = new ArrayList<>();
        for (int i = 0; i < antCount; i++) {
            ants.add(new Ant());
        }
        this.environment = initializeEnvironment();
        this.random = new Random();
    }

    /**
     * Initializes the environment with default values.
     *
     * @return A map representing the environment.
     */
    private Map<String, Double> initializeEnvironment() {
        Map<String, Double> env = new HashMap<>();
        env.put("food", 0.5);
        env.put("pheromone", 0.2);
        env.put("danger", 0.1);
        return env;
    }

    /**
     * Runs the simulation for a specified number of steps.
     *
     * @param steps The number of simulation steps.
     */
    public void runSimulation(int steps) {
        for (int step = 1; step <= steps; step++) {
            System.out.println("Step " + step);
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

    /**
     * Generates observations based on the current environment state with added noise.
     *
     * @return A map of observations.
     */
    private Map<String, Double> getObservations() {
        Map<String, Double> observations = new HashMap<>();
        environment.forEach((key, value) -> {
            double noise = (random.nextDouble() - 0.5) * 0.1;
            observations.put(key, Math.max(0.0, Math.min(1.0, value + noise)));
        });
        return observations;
    }

    /**
     * Executes the specified action and updates the environment accordingly.
     *
     * @param action The action to execute.
     */
    private void executeAction(String action) {
        System.out.println("Executing action: " + action);
        switch (action) {
            case "forage":
                environment.put("food", Math.max(0.0, environment.get("food") - 0.1));
                break;
            case "return":
                environment.put("pheromone", Math.min(1.0, environment.get("pheromone") + 0.1));
                break;
            case "communicate":
                environment.put("pheromone", Math.min(1.0, environment.get("pheromone") + 0.05));
                break;
            case "explore":
                environment.put("food", Math.min(1.0, environment.get("food") + 0.05));
                environment.put("danger", Math.max(0.0, environment.get("danger") - 0.02));
                break;
            default:
                System.out.println("Unknown action: " + action);
                break;
        }
    }

    /**
     * Updates the environment by simulating random changes.
     */
    private void updateEnvironment() {
        environment.replaceAll((key, value) -> {
            double change = (random.nextDouble() - 0.5) * 0.1;
            return Math.max(0.0, Math.min(1.0, value + change));
        });
    }

    /**
     * The main method to start the AntColony simulation.
     *
     * @param args Command-line arguments.
     */
    public static void main(String[] args) {
        AntColony colony = new AntColony(10);
        colony.runSimulation(100);
    }
}