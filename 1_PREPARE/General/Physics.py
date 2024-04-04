import numpy as np
from ActiveInferAnts.General.Coordinates import VectorAdapter
from ActiveInferAnts.General.CogSec import CognitiveSecurity, ThreatLevel
from ActiveInferAnts.General.Metaphysics import MetaphysicsSpecGenerator

class Constants:
    G = 6.67430e-11  # Gravitational constant
    k = 1.380649e-23  # Boltzmann constant
    c = 299792458  # Speed of light in vacuum
    h = 6.62607015e-34  # Planck constant
    ε0 = 8.854187817e-12  # Vacuum permittivity

class PhysicsSimulation:
    def __init__(self):
        self.cog_sec = CognitiveSecurity()
        self.metaphysics = MetaphysicsSpecGenerator()
    
    @staticmethod
    def entropy(energy, temperature):
        assert temperature > 0, "Temperature must be greater than 0."
        return energy / temperature
    
    @staticmethod
    def informational_entropy(probabilities):
        assert all(p >= 0 for p in probabilities) and sum(probabilities) <= 1, \
            "Probabilities must be non-negative and sum to 1 or less."
        return -np.sum([p * np.log2(p) for p in probabilities if p > 0])
    
    @staticmethod
    def gravity_force(mass1, mass2, distance):
        assert distance > 0, "Distance must be greater than 0."
        return Constants.G * (mass1 * mass2) / (distance ** 2)
    
    @staticmethod
    def electromagnetic_force(charge1, charge2, distance):
        assert distance > 0, "Distance must be greater than 0."
        return (1 / (4 * np.pi * Constants.ε0)) * (charge1 * charge2) / (distance ** 2)
    
    @staticmethod
    def matter_phase(temperature, pressure):
        assert temperature >= 0, "Temperature must be greater than 0."
        if temperature < 273.15 and pressure > 101.325:
            return 'Solid'
        elif 273.15 <= temperature < 373.15:
            return 'Liquid'
        else:
            return 'Gas'
    
    def friction(self, normal_force, coefficient_of_friction):
        assert normal_force >= 0 and coefficient_of_friction >= 0, \
            "Normal force and coefficient of friction must be non-negative."
        metaphysical_influence = self.metaphysics_influence(normal_force, coefficient_of_friction)
        return normal_force * coefficient_of_friction * metaphysical_influence
    
    def metaphysics_influence(self, normal_force, coefficient):
        # Integration with MetaphysicsSpecGenerator
        return 1.05  # Assuming a 5% influence for demonstration purposes
    
    def displacement(self, time, velocity):
        assert time >= 0, "Time must be non-negative."
        displacement_vector = VectorAdapter([velocity * time, 0, 0], 'xyz')
        return displacement_vector.length()
    
    def simulate(self, parameters):
        threat_level = self.cog_sec.assess_threats(parameters)
        cognitive_security_influence = self.cognitive_security_influence(threat_level)
        
        results = {
            'entropy': self.entropy(parameters['energy'], parameters['temperature']),
            'informational_entropy': self.informational_entropy(parameters['probabilities']),
            'gravity': self.gravity_force(parameters['mass1'], parameters['mass2'], parameters['distance']),
            'electromagnetic': self.electromagnetic_force(parameters['charge1'], parameters['charge2'], parameters['distance']),
            'phase': self.matter_phase(parameters['temperature'], parameters['pressure']),
            'friction': self.friction(parameters['normal_force'], parameters['coefficient_of_friction']),
            'displacement': self.displacement(parameters['time'], parameters['velocity']),
            'cognitive_security_influence': cognitive_security_influence,
        }
        return results
    
    def cognitive_security_influence(self, threat_level):
        if threat_level == ThreatLevel.HIGH:
            return "High Threat - Adjusting parameters for maximum security."
        elif threat_level == ThreatLevel.MEDIUM:
            return "Medium Threat - Moderate adjustments applied."
        else:
            return "Low Threat - Standard operation parameters."
