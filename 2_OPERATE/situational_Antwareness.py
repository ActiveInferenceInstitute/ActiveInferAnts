import logging
from typing import Any, Callable, Dict, List

class AgentVisualizer:
    """
    Enhances situational awareness by visualizing the internal state of ActiveInferenceAgent or its subclasses.
    It integrates simulation, execution, and rendering contexts for a comprehensive overview, adhering to Active Inference best practices.
    """
    def __init__(self, agent: Any) -> None:
        self.agent = agent
        self.required_attrs: List[str] = ['position', 'influence_factor', 'agent_params', 'A_matrix', 'B_matrix', 'C_matrix', 'D_matrix']
        self.matrices: List[str] = ['A_matrix', 'B_matrix', 'C_matrix', 'D_matrix']
        self.agent_specific_info: Dict[str, tuple] = {
            'ActiveNestmate': ("Nestmate Config", lambda agent: agent.nestmate_config),
            'ActiveColony': ("Colony Config", lambda agent: agent.colony_config)
        }

    def check_agent_attributes(self) -> bool:
        missing_attrs = [attr for attr in self.required_attrs if not hasattr(self.agent, attr)]
        if missing_attrs:
            logging.error(f"Agent is missing required attributes: {', '.join(missing_attrs)}")
            return False
        return True

    def log_basic_info(self) -> None:
        logging.info(f"Position: {self.agent.position} - The current position of the agent in the environment")
        logging.info(f"Influence Factor: {self.agent.influence_factor} - A measure of the agent's influence on its surroundings")
        logging.info(f"Agent Parameters: {self.agent.agent_params} - A dictionary of agent-specific parameters")

    def log_matrices_info(self) -> None:
        for matrix in self.matrices:
            mat = getattr(self.agent, matrix)
            logging.info(f"{matrix}: Shape {mat.shape}, Size {mat.size}")

    def log_agent_specific_info(self) -> None:
        agent_type_name = type(self.agent).__name__
        if agent_type_name in self.agent_specific_info:
            info_title, info_extractor = self.agent_specific_info[agent_type_name]
            logging.info(f"{agent_type_name} Specific Information: {info_title}: {info_extractor(self.agent)}")

    def integrate_situational_awareness(self) -> None:
        try:
            from plan_Simulation import SimulationSetup
            from execute_Simulation import SimulationExecutor
            from render_Simulation import SimulationRenderer

            simulation_context = SimulationSetup()
            execution_context = SimulationExecutor()
            rendering_context = SimulationRenderer(simulation_context.simulation_environment, [], [])

            logging.info(f"Simulation Environment: {simulation_context.simulation_environment}")
            logging.info(f"Execution Parameters: Visualization Frequency - {execution_context.visualization_frequency}, Sleep Duration - {execution_context.sleep_duration}")
            logging.info(f"Rendering Context: {rendering_context.fig.canvas.get_default_filename()}")
        except ImportError as e:
            logging.warning("Could not integrate broader situational awareness due to missing modules: " + str(e))

    def visualize(self) -> None:
        logging.info("Enhanced Situational Awareness: Visualizing Agent Internals and Context")
        if not self.check_agent_attributes():
            return
        self.log_basic_info()
        self.log_matrices_info()
        total_variables = len(self.required_attrs) + sum(getattr(self.agent, matrix).size for matrix in self.matrices)
        logging.info(f"Total Number of Variables: {total_variables}")
        logging.info(f"Total Size of Variables: {sum(getattr(self.agent, matrix).size for matrix in self.matrices)}")
        self.log_agent_specific_info()
        self.integrate_situational_awareness()
