import unittest
import numpy as np
from scripts.utils import process_data, calculate_metrics

class TestUtils(unittest.TestCase):
    def test_process_data(self):
        input_data = np.array([1, 2, 3])
        processed = process_data(input_data)
        self.assertTrue(np.array_equal(input_data, processed))

    def test_calculate_metrics(self):
        results = {
            'agent1': [0, 1, 0],
            'agent2': [1, 1, 1]
        }
        metrics = calculate_metrics(results)
        self.assertAlmostEqual(metrics['mean_actions'], 0.6666666666666666)
        self.assertAlmostEqual(metrics['std_actions'], 0.4714045207910317)

if __name__ == '__main__':
    unittest.main()