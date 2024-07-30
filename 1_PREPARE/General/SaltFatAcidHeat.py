import numpy as np
from pymdp import inference, control
from typing import List, Dict, Tuple
from scipy.special import softmax

class CulinaryMDP:
    def __init__(self, n_ingredients: int, n_techniques: int, n_flavors: int = 4):
        self.ingredients = np.arange(n_ingredients)
        self.techniques = np.arange(n_techniques)
        self.flavors = np.array(['Salt', 'Fat', 'Acid', 'Heat'])
        self.n_states = n_ingredients * n_techniques * len(self.flavors)
        self.n_observations = self.n_states
        self.n_actions = n_techniques

        self.A = self._build_A_matrix()
        self.B = self._build_B_matrix()
        self.C = self._build_C_matrix()
        self.D = self._build_D_matrix()

    def _build_A_matrix(self) -> np.ndarray:
        A = np.zeros((len(self.flavors), self.n_observations, self.n_states))
        for flavor_idx in range(len(self.flavors)):
            A[flavor_idx] = np.eye(self.n_observations, self.n_states)
        return A

    def _build_B_matrix(self) -> np.ndarray:
        B = np.zeros((self.n_states, self.n_states, self.n_actions))
        for ingredient in self.ingredients:
            for technique in self.techniques:
                for flavor_idx in range(len(self.flavors)):
                    s1 = (ingredient * len(self.techniques) + technique) * len(self.flavors) + flavor_idx
                    for next_technique in self.techniques:
                        s2 = (ingredient * len(self.techniques) + next_technique) * len(self.flavors) + flavor_idx
                        B[s1, s2, next_technique] = 1.0
        return B

    def _build_C_matrix(self) -> np.ndarray:
        C = np.zeros((len(self.flavors), self.n_observations))
        preferences = {'Salt': 0.9, 'Fat': 0.3, 'Acid': 0.3, 'Heat': 0.9}
        for flavor_idx, flavor in enumerate(self.flavors):
            C[flavor_idx] = np.ones(self.n_observations) * (1.0 - preferences[flavor]) / (self.n_observations - 1)
            C[flavor_idx][-1] = preferences[flavor]
        return C

    def _build_D_matrix(self) -> np.ndarray:
        return np.ones(self.n_states) / self.n_states

    def infer_states(self, observation: np.ndarray) -> np.ndarray:
        return inference.update_posterior_states(observation, self.A, self.B, self.C, self.D)

    def infer_policies(self) -> np.ndarray:
        q_pi, _, _ = control.update_posterior_policies(self.A, self.B, self.C, self.D)
        return q_pi

    def sample_action(self, q_pi: np.ndarray) -> int:
        return control.sample_action(q_pi, self.B)

    def _simulate_noisy_observations(self, noise_level: float = 0.1) -> None:
        self.A += np.random.normal(0, noise_level, self.A.shape)
        self.A = softmax(self.A, axis=1)  # Ensure probabilities sum to 1

    def update_preferences(self, new_preferences: Dict[str, float]) -> None:
        for flavor_idx, flavor in enumerate(self.flavors):
            if flavor in new_preferences:
                self.C[flavor_idx][-1] = new_preferences[flavor]
        self.C = softmax(self.C, axis=1)  # Ensure probabilities sum to 1

    def _enhance_B_matrix(self, technique_effects: Dict[int, float]) -> None:
        for technique, effect in technique_effects.items():
            self.B[:, :, technique] *= effect
        self.B = self.B / np.sum(self.B, axis=1, keepdims=True)  # Normalize

    def learn_from_outcome(self, success: bool, learning_rate: float = 0.1) -> None:
        if success:
            self.C *= (1 + learning_rate)
        else:
            self.C *= (1 - learning_rate)
        self.C = softmax(self.C, axis=1)  # Ensure probabilities sum to 1

    def step(self, action: int) -> Tuple[np.ndarray, float]:
        new_state = np.argmax(self.B[:, :, action], axis=1)
        observation = np.random.choice(self.n_observations, p=self.A[:, new_state].flatten())
        reward = self.C.flatten()[observation]
        return observation, reward

# Example usage
if __name__ == "__main__":
    mdp = CulinaryMDP(n_ingredients=10, n_techniques=4)

    obs = np.random.randint(0, mdp.n_observations, size=len(mdp.flavors))
    qs = mdp.infer_states(obs)

    q_pi = mdp.infer_policies()
    action = mdp.sample_action(q_pi)

    new_obs, reward = mdp.step(action)
    print(f"Action: {action}, New Observation: {new_obs}, Reward: {reward}")

    mdp.update_preferences({'Salt': 0.8, 'Heat': 0.7})
    mdp._enhance_B_matrix({0: 1.2, 1: 0.9})
    mdp.learn_from_outcome(success=True)
