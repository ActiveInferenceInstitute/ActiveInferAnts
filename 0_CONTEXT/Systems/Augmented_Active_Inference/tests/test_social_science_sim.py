import unittest
from scripts.social_science_sim import SocialAgent, run_simulation

class TestSocialScienceSim(unittest.TestCase):
    def test_social_agent_initialization(self):
        agent = SocialAgent(5, 3, 2)
        self.assertEqual(len(agent.beliefs), 5)

    def test_run_simulation(self):
        try:
            run_simulation(num_agents=2, num_steps=5)
        except Exception as e:
            self.fail(f"run_simulation raised {type(e).__name__} unexpectedly!")

if __name__ == '__main__':
    unittest.main()