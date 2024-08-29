import logging
from pymdp.agent import Agent as PymdpAgent

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CustomAgent(PymdpAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_solution = None
        self.current_fitness = None
        logger.info("CustomAgent initialized with args: %s, kwargs: %s", args, kwargs)
        
        
# Helper function to process subnetwork results
def process_subnetwork_results(subnetwork_dict_1, subnetwork_dict_2, error_rate, p, C_improvement_pref, learn_A_after_every_X_timesteps_i, trial, network_type):
    logger.info("Processing subnetwork results with error_rate: %s, p: %s, C_improvement_pref: %s, learn_A_after_every_X_timesteps_i: %s, trial: %s, network_type: %s", 
                error_rate, p, C_improvement_pref, learn_A_after_every_X_timesteps_i, trial, network_type)
    
    for i in range(len(subnetwork_dict_1)):
        subnetwork_dict_1[i]['stage'] = ['First'] * len(subnetwork_dict_1[i]['avg_efe'])
        subnetwork_dict_2[i]['stage'] = ['Second'] * len(subnetwork_dict_2[i]['avg_efe'])

    subnetwork_dict = {key: {inner_key: subnetwork_dict_1[key][inner_key] + subnetwork_dict_2[key][inner_key] for inner_key in subnetwork_dict_1[key]} for key in subnetwork_dict_1}
    
    for i in range(len(subnetwork_dict)):
        subnetwork_dict[i]['error_rate'] = [error_rate] * len(subnetwork_dict[i]['avg_efe'])
        subnetwork_dict[i]['p'] = [p] * len(subnetwork_dict[i]['avg_efe'])
        subnetwork_dict[i]['C_improvement_prefs'] = [C_improvement_pref] * len(subnetwork_dict[i]['avg_efe'])
        subnetwork_dict[i]['learn_A_after_every_X_timesteps'] = [learn_A_after_every_X_timesteps_i] * len(subnetwork_dict[i]['avg_efe'])
        subnetwork_dict[i]['trial'] = [trial] * len(subnetwork_dict[i]['avg_efe'])
        subnetwork_dict[i]['network_type'] = [network_type] * len(subnetwork_dict[i]['avg_efe'])

    logger.info("Subnetwork results processed successfully")
    return subnetwork_dict

