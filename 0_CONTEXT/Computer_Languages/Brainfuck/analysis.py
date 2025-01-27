"""
Advanced analysis tools for Brainfuck Active Inference simulation.
"""
import numpy as np
from scipy import stats
from typing import Dict, List, Tuple
import networkx as nx
from dataclasses import dataclass

@dataclass
class SimulationMetrics:
    """Container for simulation metrics."""
    prediction_accuracy: float
    free_energy_reduction: float
    uncertainty_dynamics: float
    temporal_complexity: float
    causal_structure: nx.DiGraph

class ActiveInferenceAnalyzer:
    """Analyzer for active inference simulation results."""
    
    def __init__(self, history: Dict[str, List[float]]):
        self.history = history
        self.metrics = self._calculate_metrics()
        
    def _calculate_metrics(self) -> SimulationMetrics:
        """Calculate comprehensive metrics for the simulation."""
        return SimulationMetrics(
            prediction_accuracy=self._calculate_prediction_accuracy(),
            free_energy_reduction=self._calculate_free_energy_reduction(),
            uncertainty_dynamics=self._calculate_uncertainty_dynamics(),
            temporal_complexity=self._calculate_temporal_complexity(),
            causal_structure=self._build_causal_structure()
        )
        
    def _calculate_prediction_accuracy(self) -> float:
        """Calculate prediction accuracy using dynamic time warping."""
        from scipy.spatial.distance import euclidean
        from fastdtw import fastdtw
        
        distance, _ = fastdtw(
            self.history['sensory_input'],
            self.history['prediction'],
            dist=euclidean
        )
        return 1 / (1 + distance)
        
    def _build_causal_structure(self) -> nx.DiGraph:
        """Build a causal graph of variable interactions."""
        G = nx.DiGraph()
        variables = ['prediction', 'free_energy', 'action', 'uncertainty']
        
        for v1 in variables:
            for v2 in variables:
                if v1 != v2:
                    granger_p_value = self._granger_causality(
                        self.history[v1],
                        self.history[v2]
                    )
                    if granger_p_value < 0.05:
                        G.add_edge(v1, v2, weight=1-granger_p_value)
        
        return G
        
    def _granger_causality(self, x: List[float], y: List[float]) -> float:
        """Calculate Granger causality p-value between two time series."""
        from statsmodels.tsa.stattools import grangercausalitytests
        data = np.column_stack([x, y])
        result = grangercausalitytests(data, maxlag=2, verbose=False)
        return min(result[1][0]['ssr_chi2test'][1],
                  result[2][0]['ssr_chi2test'][1]) 