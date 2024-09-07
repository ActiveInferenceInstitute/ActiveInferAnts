# PyMDP Methods

## pymdp.agent.Agent

**Arguments:** (A, B, C=None, D=None, E=None, H=None, pA=None, pB=None, pD=None, num_controls=None, policy_len=1, inference_horizon=1, control_fac_idx=None, policies=None, gamma=16.0, alpha=16.0, use_utility=True, use_states_info_gain=True, use_param_info_gain=False, action_selection='deterministic', sampling_mode='marginal', inference_algo='VANILLA', inference_params=None, modalities_to_learn='all', lr_pA=1.0, factors_to_learn='all', lr_pB=1.0, lr_pD=1.0, use_BMA=True, policy_sep_prior=False, save_belief_hist=False, A_factor_list=None, B_factor_list=None, sophisticated=False, si_horizon=3, si_policy_prune_threshold=0.0625, si_state_prune_threshold=0.0625, si_prune_penalty=512, ii_depth=10, ii_threshold=0.0625)

**Description:**
The Agent class, the highest-level API that wraps together processes for action, perception, and learning under active inference.

The basic usage is as follows:

>>> my_agent = Agent(A = A, B = C, <more_params>)
>>> observation = env.step(initial_action)
>>> qs = my_agent.infer_states(observation)
>>> q_pi, G = my_agent.infer_policies()
>>> next_action = my_agent.sample_action()
>>> next_observation = env.step(next_action)

This represents one timestep of an active inference process. Wrapping this step in a loop with an ``Env()`` class that returns
observations and takes actions as inputs, would entail a dynamic agent-environment interaction.

---

## pymdp.algos.run_mmp

**Arguments:** (lh_seq, B, policy, prev_actions=None, prior=None, num_iter=10, grad_descent=True, tau=0.25, last_timestep=False)

**Description:**
Marginal message passing scheme for updating marginal posterior beliefs about hidden states over time, 
conditioned on a particular policy.

Parameters
----------
lh_seq: ``numpy.ndarray`` of dtype object
    Log likelihoods of hidden states under a sequence of observations over time. This is assumed to already be log-transformed. Each ``lh_seq[t]`` contains
    the log likelihood of hidden states for a particular observation at time ``t``
B: ``numpy.ndarray`` of dtype object
    Dynamics likelihood mapping or 'transition model', mapping from hidden states at ``t`` to hidden states at ``t+1``, given some control state ``u``.
    Each element ``B[f]`` of this object array stores a 3-D tensor for hidden state factor ``f``, whose entries ``B[f][s, v, u]`` store the probability
    of hidden state level ``s`` at the current time, given hidden state level ``v`` and action ``u`` at the previous time.
policy: 2D ``numpy.ndarray``
    Matrix of shape ``(policy_len, num_control_factors)`` that indicates the indices of each action (control state index) upon timestep ``t`` and control_factor ``f` in the element ``policy[t,f]`` for a given policy.
prev_actions: ``numpy.ndarray``, default None
    If provided, should be a matrix of previous actions of shape ``(infer_len, num_control_factors)`` that indicates the indices of each action (control state index) taken in the past (up until the current timestep).
prior: ``numpy.ndarray`` of dtype object, default None
    If provided, the prior beliefs about initial states (at t = 0, relative to ``infer_len``). If ``None``, this defaults
    to a flat (uninformative) prior over hidden states.
numiter: int, default 10
    Number of variational iterations.
grad_descent: Bool, default True
    Flag for whether to use gradient descent (free energy gradient updates) instead of fixed point solution to the posterior beliefs
tau: float, default 0.25
    Decay constant for use in ``grad_descent`` version. Tunes the size of the gradient descent updates to the posterior.
last_timestep: Bool, default False
    Flag for whether we are at the last timestep of belief updating
    
Returns
---------
qs_seq: ``numpy.ndarray`` of dtype object
    Posterior beliefs over hidden states under the policy. Nesting structure is timepoints, factors,
    where e.g. ``qs_seq[t][f]`` stores the marginal belief about factor ``f`` at timepoint ``t`` under the policy in question.
F: float
    Variational free energy of the policy.

---

## pymdp.algos.run_mmp_factorized

**Arguments:** (lh_seq, mb_dict, B, B_factor_list, policy, prev_actions=None, prior=None, num_iter=10, grad_descent=True, tau=0.25, last_timestep=False)

**Description:**
Marginal message passing scheme for updating marginal posterior beliefs about hidden states over time, 
conditioned on a particular policy.

Parameters
----------
lh_seq: ``numpy.ndarray`` of dtype object
    Log likelihoods of hidden states under a sequence of observations over time. This is assumed to already be log-transformed. Each ``lh_seq[t]`` contains
    the log likelihood of hidden states for a particular observation at time ``t``
mb_dict: ``Dict``
    Dictionary with two keys (``A_factor_list`` and ``A_modality_list``), that stores the factor indices that influence each modality (``A_factor_list``)
    and the modality indices influenced by each factor (``A_modality_list``).
B: ``numpy.ndarray`` of dtype object
    Dynamics likelihood mapping or 'transition model', mapping from hidden states at ``t`` to hidden states at ``t+1``, given some control state ``u``.
    Each element ``B[f]`` of this object array stores a 3-D tensor for hidden state factor ``f``, whose entries ``B[f][s, v, u]`` store the probability
    of hidden state level ``s`` at the current time, given hidden state level ``v`` and action ``u`` at the previous time.
B_factor_list: ``list`` of ``list`` of ``int``
    List of lists of hidden state factors each hidden state factor depends on. Each element ``B_factor_list[i]`` is a list of the factor indices that factor i's dynamics depend on.
policy: 2D ``numpy.ndarray``
    Matrix of shape ``(policy_len, num_control_factors)`` that indicates the indices of each action (control state index) upon timestep ``t`` and control_factor ``f` in the element ``policy[t,f]`` for a given policy.
prev_actions: ``numpy.ndarray``, default None
    If provided, should be a matrix of previous actions of shape ``(infer_len, num_control_factors)`` that indicates the indices of each action (control state index) taken in the past (up until the current timestep).
prior: ``numpy.ndarray`` of dtype object, default None
    If provided, the prior beliefs about initial states (at t = 0, relative to ``infer_len``). If ``None``, this defaults
    to a flat (uninformative) prior over hidden states.
numiter: int, default 10
    Number of variational iterations.
grad_descent: Bool, default True
    Flag for whether to use gradient descent (free energy gradient updates) instead of fixed point solution to the posterior beliefs
tau: float, default 0.25
    Decay constant for use in ``grad_descent`` version. Tunes the size of the gradient descent updates to the posterior.
last_timestep: Bool, default False
    Flag for whether we are at the last timestep of belief updating
    
Returns
---------
qs_seq: ``numpy.ndarray`` of dtype object
    Posterior beliefs over hidden states under the policy. Nesting structure is timepoints, factors,
    where e.g. ``qs_seq[t][f]`` stores the marginal belief about factor ``f`` at timepoint ``t`` under the policy in question.
F: float
    Variational free energy of the policy.

---

## pymdp.algos.run_vanilla_fpi

**Arguments:** (A, obs, num_obs, num_states, prior=None, num_iter=10, dF=1.0, dF_tol=0.001, compute_vfe=True)

**Description:**
Update marginal posterior beliefs over hidden states using mean-field variational inference, via
fixed point iteration. 

Parameters
----------
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``np.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``
obs: numpy 1D array or numpy ndarray of dtype object
    The observation (generated by the environment). If single modality, this should be a 1D ``np.ndarray``
    (one-hot vector representation). If multi-modality, this should be ``np.ndarray`` of dtype object whose entries are 1D one-hot vectors.
num_obs: list of ints
    List of dimensionalities of each observation modality
num_states: list of ints
    List of dimensionalities of each hidden state factor
prior: numpy ndarray of dtype object, default None
    Prior over hidden states. If absent, prior is set to be the log uniform distribution over hidden states (identical to the 
    initialisation of the posterior)
num_iter: int, default 10
    Number of variational fixed-point iterations to run until convergence.
dF: float, default 1.0
    Initial free energy gradient (dF/dt) before updating in the course of gradient descent.
dF_tol: float, default 0.001
    Threshold value of the time derivative of the variational free energy (dF/dt), to be checked at 
    each iteration. If dF <= dF_tol, the iterations are halted pre-emptively and the final 
    marginal posterior belief(s) is(are) returned
compute_vfe: bool, default True
    Whether to compute the variational free energy at each iteration. If False, the function runs through 
    all variational iterations.

Returns
----------
qs: numpy 1D array, numpy ndarray of dtype object, optional
    Marginal posterior beliefs over hidden states at current timepoint

---

## pymdp.algos.run_vanilla_fpi_factorized

**Arguments:** (A, obs, num_obs, num_states, mb_dict, prior=None, num_iter=10, dF=1.0, dF_tol=0.001, compute_vfe=True)

**Description:**
Update marginal posterior beliefs over hidden states using mean-field variational inference, via
fixed point iteration. 

Parameters
----------
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``np.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``
obs: numpy 1D array or numpy ndarray of dtype object
    The observation (generated by the environment). If single modality, this should be a 1D ``np.ndarray``
    (one-hot vector representation). If multi-modality, this should be ``np.ndarray`` of dtype object whose entries are 1D one-hot vectors.
num_obs: ``list`` of ints
    List of dimensionalities of each observation modality
num_states: ``list`` of ints
    List of dimensionalities of each hidden state factor
mb_dict: ``Dict``
    Dictionary with two keys (``A_factor_list`` and ``A_modality_list``), that stores the factor indices that influence each modality (``A_factor_list``)
    and the modality indices influenced by each factor (``A_modality_list``).
prior: numpy ndarray of dtype object, default None
    Prior over hidden states. If absent, prior is set to be the log uniform distribution over hidden states (identical to the 
    initialisation of the posterior)
num_iter: int, default 10
    Number of variational fixed-point iterations to run until convergence.
dF: float, default 1.0
    Initial free energy gradient (dF/dt) before updating in the course of gradient descent.
dF_tol: float, default 0.001
    Threshold value of the time derivative of the variational free energy (dF/dt), to be checked at 
    each iteration. If dF <= dF_tol, the iterations are halted pre-emptively and the final 
    marginal posterior belief(s) is(are) returned
compute_vfe: bool, default True
    Whether to compute the variational free energy at each iteration. If False, the function runs through 
    all variational iterations.

Returns
----------
qs: numpy 1D array, numpy ndarray of dtype object, optional
    Marginal posterior beliefs over hidden states at current timepoint

---

## pymdp.control.average_states_over_policies

**Arguments:** (qs_pi, q_pi)

**Description:**
This function computes a expected posterior over hidden states with respect to the posterior over policies, 
also known as the 'Bayesian model average of states with respect to policies'.

Parameters
----------
qs_pi: ``numpy.ndarray`` of dtype object
    Posterior beliefs over hidden states for each policy. Nesting structure is policies, factors,
    where e.g. ``qs_pi[p][f]`` stores the marginal belief about factor ``f`` under policy ``p``.
q_pi: ``numpy.ndarray`` of dtype object
    Posterior beliefs about policies where ``len(q_pi) = num_policies``

Returns
---------
qs_bma: ``numpy.ndarray`` of dtype object
    Marginal posterior over hidden states for the current timepoint, 
    averaged across policies according to their posterior probability given by ``q_pi``

---

## pymdp.control.backwards_induction

**Arguments:** (H, B, B_factor_list, threshold, depth)

**Description:**
Runs backwards induction of reaching a goal state H given a transition model B.

Parameters
----------    
H: ``numpy.ndarray`` of dtype object
   Prior over states
B: ``numpy.ndarray`` of dtype object
    Dynamics likelihood mapping or 'transition model', mapping from hidden states at ``t`` to hidden states at ``t+1``, given some control state ``u``.
    Each element ``B[f]`` of this object array stores a 3-D tensor for hidden state factor ``f``, whose entries ``B[f][s, v, u]`` store the probability
    of hidden state level ``s`` at the current time, given hidden state level ``v`` and action ``u`` at the previous time.
B_factor_list: ``list`` of ``list`` of ``int``
    List of lists of hidden state factors each hidden state factor depends on. Each element ``B_factor_list[i]`` is a list of the factor indices that factor i's dynamics depend on.
threshold: ``float``
    The threshold for pruning transitions that are below a certain probability
depth: ``int``
    The temporal depth of the backward induction

Returns
----------
I: ``numpy.ndarray`` of dtype object
    For each state factor, contains a 2D ``numpy.ndarray`` whose element i,j yields the probability 
    of reaching the goal state backwards from state j after i steps.

---

## pymdp.control.calc_ambiguity_factorized

**Arguments:** (qs_pi, A, A_factor_list)

**Description:**
Computes the Ambiguity term.

Parameters
----------
qs_pi: ``list`` of ``numpy.ndarray`` of dtype object
    Predictive posterior beliefs over hidden states expected under the policy, where ``qs_pi[t]`` stores the beliefs about
    hidden states expected under the policy at time ``t``
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``numpy.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``
A_factor_list: ``list`` of ``list`` of ``int``
    List of lists, where ``A_factor_list[m]`` is a list of the hidden state factor indices that observation modality with the index ``m`` depends on

Returns
-------
ambiguity: float

---

## pymdp.control.calc_expected_utility

**Arguments:** (qo_pi, C)

**Description:**
Computes the expected utility of a policy, using the observation distribution expected under that policy and a prior preference vector.

Parameters
----------
qo_pi: ``list`` of ``numpy.ndarray`` of dtype object
    Predictive posterior beliefs over observations expected under the policy, where ``qo_pi[t]`` stores the beliefs about
    observations expected under the policy at time ``t``
C: ``numpy.ndarray`` of dtype object
   Prior over observations or 'prior preferences', storing the "value" of each outcome in terms of relative log probabilities. 
   This is softmaxed to form a proper probability distribution before being used to compute the expected utility.

Returns
-------
expected_util: float
    Utility (reward) expected under the policy in question

---

## pymdp.control.calc_inductive_cost

**Arguments:** (qs, qs_pi, I, epsilon=0.001)

**Description:**
Computes the inductive cost of a state.

Parameters
----------
qs: ``numpy.ndarray`` of dtype object
    Marginal posterior beliefs over hidden states at a given timepoint.
qs_pi: ``list`` of ``numpy.ndarray`` of dtype object
    Predictive posterior beliefs over hidden states expected under the policy, where ``qs_pi[t]`` stores the beliefs about
    states expected under the policy at time ``t``
I: ``numpy.ndarray`` of dtype object
    For each state factor, contains a 2D ``numpy.ndarray`` whose element i,j yields the probability 
    of reaching the goal state backwards from state j after i steps.

Returns
-------
inductive_cost: float
    Cost of visited this state using backwards induction under the policy in question

---

## pymdp.control.calc_pA_info_gain

**Arguments:** (pA, qo_pi, qs_pi)

**Description:**
Compute expected Dirichlet information gain about parameters ``pA`` under a policy

Parameters
----------
pA: ``numpy.ndarray`` of dtype object
    Dirichlet parameters over observation model (same shape as ``A``)
qo_pi: ``list`` of ``numpy.ndarray`` of dtype object
    Predictive posterior beliefs over observations expected under the policy, where ``qo_pi[t]`` stores the beliefs about
    observations expected under the policy at time ``t``
qs_pi: ``list`` of ``numpy.ndarray`` of dtype object
    Predictive posterior beliefs over hidden states expected under the policy, where ``qs_pi[t]`` stores the beliefs about
    hidden states expected under the policy at time ``t``

Returns
-------
infogain_pA: float
    Surprise (about Dirichlet parameters) expected under the policy in question

---

## pymdp.control.calc_pA_info_gain_factorized

**Arguments:** (pA, qo_pi, qs_pi, A_factor_list)

**Description:**
Compute expected Dirichlet information gain about parameters ``pA`` under a policy.
In this version of the function, we assume that the observation model is factorized, i.e. that each observation modality depends on a subset of the hidden state factors.

Parameters
----------
pA: ``numpy.ndarray`` of dtype object
    Dirichlet parameters over observation model (same shape as ``A``)
qo_pi: ``list`` of ``numpy.ndarray`` of dtype object
    Predictive posterior beliefs over observations expected under the policy, where ``qo_pi[t]`` stores the beliefs about
    observations expected under the policy at time ``t``
qs_pi: ``list`` of ``numpy.ndarray`` of dtype object
    Predictive posterior beliefs over hidden states expected under the policy, where ``qs_pi[t]`` stores the beliefs about
    hidden states expected under the policy at time ``t``
A_factor_list: ``list`` of ``list`` of ``int``
    List of lists, where ``A_factor_list[m]`` is a list of the hidden state factor indices that observation modality with the index ``m`` depends on

Returns
-------
infogain_pA: float
    Surprise (about Dirichlet parameters) expected under the policy in question

---

## pymdp.control.calc_pB_info_gain

**Arguments:** (pB, qs_pi, qs_prev, policy)

**Description:**
Compute expected Dirichlet information gain about parameters ``pB`` under a given policy

Parameters
----------
pB: ``numpy.ndarray`` of dtype object
    Dirichlet parameters over transition model (same shape as ``B``)
qs_pi: ``list`` of ``numpy.ndarray`` of dtype object
    Predictive posterior beliefs over hidden states expected under the policy, where ``qs_pi[t]`` stores the beliefs about
    hidden states expected under the policy at time ``t``
qs_prev: ``numpy.ndarray`` of dtype object
    Posterior over hidden states at beginning of trajectory (before receiving observations)
policy: 2D ``numpy.ndarray``
    Array that stores actions entailed by a policy over time. Shape is ``(num_timesteps, num_factors)`` where ``num_timesteps`` is the temporal
    depth of the policy and ``num_factors`` is the number of control factors.

Returns
-------
infogain_pB: float
    Surprise (about dirichlet parameters) expected under the policy in question

---

## pymdp.control.calc_pB_info_gain_interactions

**Arguments:** (pB, qs_pi, qs_prev, B_factor_list, policy)

**Description:**
Compute expected Dirichlet information gain about parameters ``pB`` under a given policy

Parameters
----------
pB: ``numpy.ndarray`` of dtype object
    Dirichlet parameters over transition model (same shape as ``B``)
qs_pi: ``list`` of ``numpy.ndarray`` of dtype object
    Predictive posterior beliefs over hidden states expected under the policy, where ``qs_pi[t]`` stores the beliefs about
    hidden states expected under the policy at time ``t``
qs_prev: ``numpy.ndarray`` of dtype object
    Posterior over hidden states at beginning of trajectory (before receiving observations)
B_factor_list: ``list`` of ``list`` of ``int``
    List of lists, where ``B_factor_list[f]`` is a list of the hidden state factor indices that hidden state factor with the index ``f`` depends on
policy: 2D ``numpy.ndarray``
    Array that stores actions entailed by a policy over time. Shape is ``(num_timesteps, num_factors)`` where ``num_timesteps`` is the temporal
    depth of the policy and ``num_factors`` is the number of control factors.

Returns
-------
infogain_pB: float
    Surprise (about dirichlet parameters) expected under the policy in question

---

## pymdp.control.calc_states_info_gain

**Arguments:** (A, qs_pi)

**Description:**
Computes the Bayesian surprise or information gain about states of a policy, 
using the observation model and the hidden state distribution expected under that policy.

Parameters
----------
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``numpy.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``
qs_pi: ``list`` of ``numpy.ndarray`` of dtype object
    Predictive posterior beliefs over hidden states expected under the policy, where ``qs_pi[t]`` stores the beliefs about
    hidden states expected under the policy at time ``t``

Returns
-------
states_surprise: float
    Bayesian surprise (about states) or salience expected under the policy in question

---

## pymdp.control.calc_states_info_gain_factorized

**Arguments:** (A, qs_pi, A_factor_list)

**Description:**
Computes the Bayesian surprise or information gain about states of a policy, 
using the observation model and the hidden state distribution expected under that policy.

Parameters
----------
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``numpy.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``
qs_pi: ``list`` of ``numpy.ndarray`` of dtype object
    Predictive posterior beliefs over hidden states expected under the policy, where ``qs_pi[t]`` stores the beliefs about
    hidden states expected under the policy at time ``t``
A_factor_list: ``list`` of ``list`` of ``int``
    List of lists, where ``A_factor_list[m]`` is a list of the hidden state factor indices that observation modality with the index ``m`` depends on

Returns
-------
states_surprise: float
    Bayesian surprise (about states) or salience expected under the policy in question

---

## pymdp.control.construct_policies

**Arguments:** (num_states, num_controls=None, policy_len=1, control_fac_idx=None)

**Description:**
Generate a ``list`` of policies. The returned array ``policies`` is a ``list`` that stores one policy per entry.
A particular policy (``policies[i]``) has shape ``(num_timesteps, num_factors)`` 
where ``num_timesteps`` is the temporal depth of the policy and ``num_factors`` is the number of control factors.

Parameters
----------
num_states: ``list`` of ``int``
    ``list`` of the dimensionalities of each hidden state factor
num_controls: ``list`` of ``int``, default ``None``
    ``list`` of the dimensionalities of each control state factor. If ``None``, then is automatically computed as the dimensionality of each hidden state factor that is controllable
policy_len: ``int``, default 1
    temporal depth ("planning horizon") of policies
control_fac_idx: ``list`` of ``int``
    ``list`` of indices of the hidden state factors that are controllable (i.e. those state factors ``i`` where ``num_controls[i] > 1``)

Returns
----------
policies: ``list`` of 2D ``numpy.ndarray``
    ``list`` that stores each policy as a 2D array in ``policies[p_idx]``. Shape of ``policies[p_idx]`` 
    is ``(num_timesteps, num_factors)`` where ``num_timesteps`` is the temporal
    depth of the policy and ``num_factors`` is the number of control factors.

---

## pymdp.control.entropy

**Arguments:** (A)

**Description:**
Compute the entropy term H of the likelihood matrix,
i.e. one entropy value per column

---

## pymdp.control.get_expected_obs

**Arguments:** (qs_pi, A)

**Description:**
Compute the expected observations under a policy, also known as the posterior predictive density over observations

Parameters
----------
qs_pi: ``list`` of ``numpy.ndarray`` of dtype object
    Predictive posterior beliefs over hidden states expected under the policy, where ``qs_pi[t]`` stores the beliefs about
    hidden states expected under the policy at time ``t``
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``numpy.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``

Returns
-------
qo_pi: ``list`` of ``numpy.ndarray`` of dtype object
    Predictive posterior beliefs over observations expected under the policy, where ``qo_pi[t]`` stores the beliefs about
    observations expected under the policy at time ``t``

---

## pymdp.control.get_expected_obs_factorized

**Arguments:** (qs_pi, A, A_factor_list)

**Description:**
Compute the expected observations under a policy, also known as the posterior predictive density over observations

Parameters
----------
qs_pi: ``list`` of ``numpy.ndarray`` of dtype object
    Predictive posterior beliefs over hidden states expected under the policy, where ``qs_pi[t]`` stores the beliefs about
    hidden states expected under the policy at time ``t``
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``numpy.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``
A_factor_list: ``list`` of ``list`` of ``int``
    List of lists of hidden state factor indices that each observation modality depends on. Each element ``A_factor_list[i]`` is a list of the factor indices that modality i's observation model depends on.
Returns
-------
qo_pi: ``list`` of ``numpy.ndarray`` of dtype object
    Predictive posterior beliefs over observations expected under the policy, where ``qo_pi[t]`` stores the beliefs about
    observations expected under the policy at time ``t``

---

## pymdp.control.get_expected_states

**Arguments:** (qs, B, policy)

**Description:**
Compute the expected states under a policy, also known as the posterior predictive density over states

Parameters
----------
qs: ``numpy.ndarray`` of dtype object
    Marginal posterior beliefs over hidden states at a given timepoint.
B: ``numpy.ndarray`` of dtype object
    Dynamics likelihood mapping or 'transition model', mapping from hidden states at ``t`` to hidden states at ``t+1``, given some control state ``u``.
    Each element ``B[f]`` of this object array stores a 3-D tensor for hidden state factor ``f``, whose entries ``B[f][s, v, u]`` store the probability
    of hidden state level ``s`` at the current time, given hidden state level ``v`` and action ``u`` at the previous time.
policy: 2D ``numpy.ndarray``
    Array that stores actions entailed by a policy over time. Shape is ``(num_timesteps, num_factors)`` where ``num_timesteps`` is the temporal
    depth of the policy and ``num_factors`` is the number of control factors.

Returns
-------
qs_pi: ``list`` of ``numpy.ndarray`` of dtype object
    Predictive posterior beliefs over hidden states expected under the policy, where ``qs_pi[t]`` stores the beliefs about
    hidden states expected under the policy at time ``t``

---

## pymdp.control.get_expected_states_interactions

**Arguments:** (qs, B, B_factor_list, policy)

**Description:**
Compute the expected states under a policy, also known as the posterior predictive density over states

Parameters
----------
qs: ``numpy.ndarray`` of dtype object
    Marginal posterior beliefs over hidden states at a given timepoint.
B: ``numpy.ndarray`` of dtype object
    Dynamics likelihood mapping or 'transition model', mapping from hidden states at ``t`` to hidden states at ``t+1``, given some control state ``u``.
    Each element ``B[f]`` of this object array stores a 3-D tensor for hidden state factor ``f``, whose entries ``B[f][s, v, u]`` store the probability
    of hidden state level ``s`` at the current time, given hidden state level ``v`` and action ``u`` at the previous time.
B_factor_list: ``list`` of ``list`` of ``int``
    List of lists of hidden state factors each hidden state factor depends on. Each element ``B_factor_list[i]`` is a list of the factor indices that factor i's dynamics depend on.
policy: 2D ``numpy.ndarray``
    Array that stores actions entailed by a policy over time. Shape is ``(num_timesteps, num_factors)`` where ``num_timesteps`` is the temporal
    depth of the policy and ``num_factors`` is the number of control factors.

Returns
-------
qs_pi: ``list`` of ``numpy.ndarray`` of dtype object
    Predictive posterior beliefs over hidden states expected under the policy, where ``qs_pi[t]`` stores the beliefs about
    hidden states expected under the policy at time ``t``

---

## pymdp.control.get_num_controls_from_policies

**Arguments:** (policies)

**Description:**
Calculates the ``list`` of dimensionalities of control factors (``num_controls``)
from the ``list`` or array of policies. This assumes a policy space such that for each control factor, there is at least
one policy that entails taking the action with the maximum index along that control factor.

Parameters
----------
policies: ``list`` of 2D ``numpy.ndarray``
    ``list`` that stores each policy as a 2D array in ``policies[p_idx]``. Shape of ``policies[p_idx]`` 
    is ``(num_timesteps, num_factors)`` where ``num_timesteps`` is the temporal
    depth of the policy and ``num_factors`` is the number of control factors.

Returns
----------
num_controls: ``list`` of ``int``
    ``list`` of the dimensionalities of each control state factor, computed here automatically from a ``list`` of policies.

---

## pymdp.control.kl_div

**Arguments:** (P, Q)

**Description:**
Parameters
----------
P : Categorical probability distribution
Q : Categorical probability distribution

Returns
-------
The KL-divergence of P and Q

---

## pymdp.control.sample_action

**Arguments:** (q_pi, policies, num_controls, action_selection='deterministic', alpha=16.0)

**Description:**
Computes the marginal posterior over actions and then samples an action from it, one action per control factor.

Parameters
----------
q_pi: 1D ``numpy.ndarray``
    Posterior beliefs over policies, i.e. a vector containing one posterior probability per policy.
policies: ``list`` of 2D ``numpy.ndarray``
    ``list`` that stores each policy as a 2D array in ``policies[p_idx]``. Shape of ``policies[p_idx]`` 
    is ``(num_timesteps, num_factors)`` where ``num_timesteps`` is the temporal
    depth of the policy and ``num_factors`` is the number of control factors.
num_controls: ``list`` of ``int``
    ``list`` of the dimensionalities of each control state factor.
action_selection: ``str``, default "deterministic"
    String indicating whether whether the selected action is chosen as the maximum of the posterior over actions,
    or whether it's sampled from the posterior marginal over actions
alpha: ``float``, default 16.0
    Action selection precision -- the inverse temperature of the softmax that is used to scale the 
    action marginals before sampling. This is only used if ``action_selection`` argument is "stochastic"

Returns
----------
selected_policy: 1D ``numpy.ndarray``
    Vector containing the indices of the actions for each control factor

---

## pymdp.control.sample_policy

**Arguments:** (q_pi, policies, num_controls, action_selection='deterministic', alpha=16.0)

**Description:**
Samples a policy from the posterior over policies, taking the action (per control factor) entailed by the first timestep of the selected policy.

Parameters
----------
q_pi: 1D ``numpy.ndarray``
    Posterior beliefs over policies, i.e. a vector containing one posterior probability per policy.
policies: ``list`` of 2D ``numpy.ndarray``
    ``list`` that stores each policy as a 2D array in ``policies[p_idx]``. Shape of ``policies[p_idx]`` 
    is ``(num_timesteps, num_factors)`` where ``num_timesteps`` is the temporal
    depth of the policy and ``num_factors`` is the number of control factors.
num_controls: ``list`` of ``int``
    ``list`` of the dimensionalities of each control state factor.
action_selection: string, default "deterministic"
    String indicating whether whether the selected policy is chosen as the maximum of the posterior over policies,
    or whether it's sampled from the posterior over policies.
alpha: float, default 16.0
    Action selection precision -- the inverse temperature of the softmax that is used to scale the 
    policy posterior before sampling. This is only used if ``action_selection`` argument is "stochastic"

Returns
----------
selected_policy: 1D ``numpy.ndarray``
    Vector containing the indices of the actions for each control factor

---

## pymdp.control.select_highest

**Arguments:** (options_array)

**Description:**
Selects the highest value among the provided ones. If the higher value is more than once and they're closer than 1e-5, a random choice is made.
Parameters
----------
options_array: ``numpy.ndarray``
    The array to examine

Returns
-------
The highest value in the given list

---

## pymdp.control.softmax

**Arguments:** (dist)

**Description:**
Computes the softmax function on a set of values

---

## pymdp.control.softmax_obj_arr

**Arguments:** (arr)

---

## pymdp.control.sophisticated_inference_search

**Arguments:** (qs, policies, A, B, C, A_factor_list, B_factor_list, I=None, horizon=1, policy_prune_threshold=0.0625, state_prune_threshold=0.0625, prune_penalty=512, gamma=16, inference_params={'num_iter': 10, 'dF': 1.0, 'dF_tol': 0.001, 'compute_vfe': False}, n=0)

**Description:**
Performs sophisticated inference to find the optimal policy for a given generative model and prior preferences.

Parameters
----------
qs: ``numpy.ndarray`` of dtype object
    Marginal posterior beliefs over hidden states at a given timepoint.
policies: ``list`` of 1D ``numpy.ndarray``                    inference_params = {"num_iter": 10, "dF": 1.0, "dF_tol": 0.001, "compute_vfe": False}

    ``list`` that stores each policy as a 1D array in ``policies[p_idx]``. Shape of ``policies[p_idx]`` 
    is ``(num_factors)`` where ``num_factors`` is the number of control factors.        
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``numpy.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``
B: ``numpy.ndarray`` of dtype object
    Dynamics likelihood mapping or 'transition model', mapping from hidden states at ``t`` to hidden states at ``t+1``, given some control state ``u``.
    Each element ``B[f]`` of this object array stores a 3-D tensor for hidden state factor ``f``, whose entries ``B[f][s, v, u]`` store the probability
    of hidden state level ``s`` at the current time, given hidden state level ``v`` and action ``u`` at the previous time.
C: ``numpy.ndarray`` of dtype object
   Prior over observations or 'prior preferences', storing the "value" of each outcome in terms of relative log probabilities. 
   This is softmaxed to form a proper probability distribution before being used to compute the expected utility term of the expected free energy.
A_factor_list: ``list`` of ``list`` of ``int``
    List of lists, where ``A_factor_list[m]`` is a list of the hidden state factor indices that observation modality with the index ``m`` depends on
B_factor_list: ``list`` of ``list`` of ``int``
    List of lists of hidden state factors each hidden state factor depends on. Each element ``B_factor_list[i]`` is a list of the factor indices that factor i's dynamics depend on.
I: ``numpy.ndarray`` of dtype object
    For each state factor, contains a 2D ``numpy.ndarray`` whose element i,j yields the probability 
    of reaching the goal state backwards from state j after i steps.
horizon: ``int``
    The temporal depth of the policy
policy_prune_threshold: ``float``
    The threshold for pruning policies that are below a certain probability
state_prune_threshold: ``float``
    The threshold for pruning states in the expectation that are below a certain probability
prune_penalty: ``float``
    Penalty to add to the EFE when a policy is pruned
gamma: ``float``, default 16.0
    Prior precision over policies, scales the contribution of the expected free energy to the posterior over policies
n: ``int``
    timestep in the future we are calculating
    
Returns
----------
q_pi: 1D ``numpy.ndarray``
    Posterior beliefs over policies, i.e. a vector containing one posterior probability per policy.
 
G: 1D ``numpy.ndarray``
    Negative expected free energies of each policy, i.e. a vector containing one negative expected free energy per policy.

---

## pymdp.control.spm_MDP_G

**Arguments:** (A, x)

**Description:**
Calculates the Bayesian surprise in the same way as spm_MDP_G.m does in 
the original matlab code.

Parameters
----------
A (numpy ndarray or array-object):
    array assigning likelihoods of observations/outcomes under the various 
    hidden state configurations

x (numpy ndarray or array-object):
    Categorical distribution presenting probabilities of hidden states 
    (this can also be interpreted as the predictive density over hidden 
    states/causes if you're calculating the expected Bayesian surprise)
    
Returns
-------
G (float):
    the (expected or not) Bayesian surprise under the density specified by x --
    namely, this scores how much an expected observation would update beliefs 
    about hidden states x, were it to be observed. 

---

## pymdp.control.spm_dot

**Arguments:** (X, x, dims_to_omit=None)

**Description:**
Dot product of a multidimensional array with `x`. The dimensions in `dims_to_omit` 
will not be summed across during the dot product

Parameters
----------
- `x` [1D numpy.ndarray] - either vector or array of arrays
    The alternative array to perform the dot product with
- `dims_to_omit` [list :: int] (optional)
    Which dimensions to omit

Returns 
-------
- `Y` [1D numpy.ndarray] - the result of the dot product

---

## pymdp.control.spm_log_single

**Arguments:** (arr)

**Description:**
Adds small epsilon value to an array before natural logging it

---

## pymdp.control.spm_wnorm

**Arguments:** (A)

**Description:**
Returns Expectation of logarithm of Dirichlet parameters over a set of 
Categorical distributions, stored in the columns of A.

---

## pymdp.control.update_posterior_policies

**Arguments:** (qs, A, B, C, policies, use_utility=True, use_states_info_gain=True, use_param_info_gain=False, pA=None, pB=None, E=None, I=None, gamma=16.0)

**Description:**
Update posterior beliefs about policies by computing expected free energy of each policy and integrating that
with the prior over policies ``E``. This is intended to be used in conjunction
with the ``update_posterior_states`` method of the ``inference`` module, since only the posterior about the hidden states at the current timestep
``qs`` is assumed to be provided, unconditional on policies. The predictive posterior over hidden states under all policies Q(s, pi) is computed 
using the starting posterior about states at the current timestep ``qs`` and the generative model (e.g. ``A``, ``B``, ``C``)

Parameters
----------
qs: ``numpy.ndarray`` of dtype object
    Marginal posterior beliefs over hidden states at current timepoint (unconditioned on policies)
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``numpy.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``
B: ``numpy.ndarray`` of dtype object
    Dynamics likelihood mapping or 'transition model', mapping from hidden states at ``t`` to hidden states at ``t+1``, given some control state ``u``.
    Each element ``B[f]`` of this object array stores a 3-D tensor for hidden state factor ``f``, whose entries ``B[f][s, v, u]`` store the probability
    of hidden state level ``s`` at the current time, given hidden state level ``v`` and action ``u`` at the previous time.
C: ``numpy.ndarray`` of dtype object
   Prior over observations or 'prior preferences', storing the "value" of each outcome in terms of relative log probabilities. 
   This is softmaxed to form a proper probability distribution before being used to compute the expected utility term of the expected free energy.
policies: ``list`` of 2D ``numpy.ndarray``
    ``list`` that stores each policy in ``policies[p_idx]``. Shape of ``policies[p_idx]`` is ``(num_timesteps, num_factors)`` where `num_timesteps` is the temporal
    depth of the policy and ``num_factors`` is the number of control factors.
use_utility: ``Bool``, default ``True``
    Boolean flag that determines whether expected utility should be incorporated into computation of EFE.
use_states_info_gain: ``Bool``, default ``True``
    Boolean flag that determines whether state epistemic value (info gain about hidden states) should be incorporated into computation of EFE.
use_param_info_gain: ``Bool``, default ``False`` 
    Boolean flag that determines whether parameter epistemic value (info gain about generative model parameters) should be incorporated into computation of EFE.
pA: ``numpy.ndarray`` of dtype object, optional
    Dirichlet parameters over observation model (same shape as ``A``)
pB: ``numpy.ndarray`` of dtype object, optional
    Dirichlet parameters over transition model (same shape as ``B``)
E: 1D ``numpy.ndarray``, optional
    Vector of prior probabilities of each policy (what's referred to in the active inference literature as "habits")
I: ``numpy.ndarray`` of dtype object
    For each state factor, contains a 2D ``numpy.ndarray`` whose element i,j yields the probability 
    of reaching the goal state backwards from state j after i steps.
gamma: float, default 16.0
    Prior precision over policies, scales the contribution of the expected free energy to the posterior over policies

Returns
----------
q_pi: 1D ``numpy.ndarray``
    Posterior beliefs over policies, i.e. a vector containing one posterior probability per policy.
G: 1D ``numpy.ndarray``
    Negative expected free energies of each policy, i.e. a vector containing one negative expected free energy per policy.

---

## pymdp.control.update_posterior_policies_factorized

**Arguments:** (qs, A, B, C, A_factor_list, B_factor_list, policies, use_utility=True, use_states_info_gain=True, use_param_info_gain=False, pA=None, pB=None, E=None, I=None, gamma=16.0)

**Description:**
Update posterior beliefs about policies by computing expected free energy of each policy and integrating that
with the prior over policies ``E``. This is intended to be used in conjunction
with the ``update_posterior_states`` method of the ``inference`` module, since only the posterior about the hidden states at the current timestep
``qs`` is assumed to be provided, unconditional on policies. The predictive posterior over hidden states under all policies Q(s, pi) is computed 
using the starting posterior about states at the current timestep ``qs`` and the generative model (e.g. ``A``, ``B``, ``C``)

Parameters
----------
qs: ``numpy.ndarray`` of dtype object
    Marginal posterior beliefs over hidden states at current timepoint (unconditioned on policies)
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``numpy.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``
B: ``numpy.ndarray`` of dtype object
    Dynamics likelihood mapping or 'transition model', mapping from hidden states at ``t`` to hidden states at ``t+1``, given some control state ``u``.
    Each element ``B[f]`` of this object array stores a 3-D tensor for hidden state factor ``f``, whose entries ``B[f][s, v, u]`` store the probability
    of hidden state level ``s`` at the current time, given hidden state level ``v`` and action ``u`` at the previous time.
C: ``numpy.ndarray`` of dtype object
   Prior over observations or 'prior preferences', storing the "value" of each outcome in terms of relative log probabilities. 
   This is softmaxed to form a proper probability distribution before being used to compute the expected utility term of the expected free energy.
A_factor_list: ``list`` of ``list``s of ``int``
    ``list`` that stores the indices of the hidden state factor indices that each observation modality depends on. For example, if ``A_factor_list[m] = [0, 1]``, then
    observation modality ``m`` depends on hidden state factors 0 and 1.
B_factor_list: ``list`` of ``list``s of ``int``
    ``list`` that stores the indices of the hidden state factor indices that each hidden state factor depends on. For example, if ``B_factor_list[f] = [0, 1]``, then
    the transitions in hidden state factor ``f`` depend on hidden state factors 0 and 1.
policies: ``list`` of 2D ``numpy.ndarray``
    ``list`` that stores each policy in ``policies[p_idx]``. Shape of ``policies[p_idx]`` is ``(num_timesteps, num_factors)`` where `num_timesteps` is the temporal
    depth of the policy and ``num_factors`` is the number of control factors.
use_utility: ``Bool``, default ``True``
    Boolean flag that determines whether expected utility should be incorporated into computation of EFE.
use_states_info_gain: ``Bool``, default ``True``
    Boolean flag that determines whether state epistemic value (info gain about hidden states) should be incorporated into computation of EFE.
use_param_info_gain: ``Bool``, default ``False`` 
    Boolean flag that determines whether parameter epistemic value (info gain about generative model parameters) should be incorporated into computation of EFE.
pA: ``numpy.ndarray`` of dtype object, optional
    Dirichlet parameters over observation model (same shape as ``A``)
pB: ``numpy.ndarray`` of dtype object, optional
    Dirichlet parameters over transition model (same shape as ``B``)
E: 1D ``numpy.ndarray``, optional
    Vector of prior probabilities of each policy (what's referred to in the active inference literature as "habits")
I: ``numpy.ndarray`` of dtype object
    For each state factor, contains a 2D ``numpy.ndarray`` whose element i,j yields the probability 
    of reaching the goal state backwards from state j after i steps.
gamma: float, default 16.0
    Prior precision over policies, scales the contribution of the expected free energy to the posterior over policies

Returns
----------
q_pi: 1D ``numpy.ndarray``
    Posterior beliefs over policies, i.e. a vector containing one posterior probability per policy.
G: 1D ``numpy.ndarray``
    Negative expected free energies of each policy, i.e. a vector containing one negative expected free energy per policy.

---

## pymdp.control.update_posterior_policies_full

**Arguments:** (qs_seq_pi, A, B, C, policies, use_utility=True, use_states_info_gain=True, use_param_info_gain=False, prior=None, pA=None, pB=None, F=None, E=None, I=None, gamma=16.0)

**Description:**
Update posterior beliefs about policies by computing expected free energy of each policy and integrating that
with the variational free energy of policies ``F`` and prior over policies ``E``. This is intended to be used in conjunction
with the ``update_posterior_states_full`` method of ``inference.py``, since the full posterior over future timesteps, under all policies, is
assumed to be provided in the input array ``qs_seq_pi``.

Parameters
----------
qs_seq_pi: ``numpy.ndarray`` of dtype object
    Posterior beliefs over hidden states for each policy. Nesting structure is policies, timepoints, factors,
    where e.g. ``qs_seq_pi[p][t][f]`` stores the marginal belief about factor ``f`` at timepoint ``t`` under policy ``p``.
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``numpy.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``
B: ``numpy.ndarray`` of dtype object
    Dynamics likelihood mapping or 'transition model', mapping from hidden states at ``t`` to hidden states at ``t+1``, given some control state ``u``.
    Each element ``B[f]`` of this object array stores a 3-D tensor for hidden state factor ``f``, whose entries ``B[f][s, v, u]`` store the probability
    of hidden state level ``s`` at the current time, given hidden state level ``v`` and action ``u`` at the previous time.
C: ``numpy.ndarray`` of dtype object
   Prior over observations or 'prior preferences', storing the "value" of each outcome in terms of relative log probabilities. 
   This is softmaxed to form a proper probability distribution before being used to compute the expected utility term of the expected free energy.
policies: ``list`` of 2D ``numpy.ndarray``
    ``list`` that stores each policy in ``policies[p_idx]``. Shape of ``policies[p_idx]`` is ``(num_timesteps, num_factors)`` where `num_timesteps` is the temporal
    depth of the policy and ``num_factors`` is the number of control factors.
use_utility: ``Bool``, default ``True``
    Boolean flag that determines whether expected utility should be incorporated into computation of EFE.
use_states_info_gain: ``Bool``, default ``True``
    Boolean flag that determines whether state epistemic value (info gain about hidden states) should be incorporated into computation of EFE.
use_param_info_gain: ``Bool``, default ``False`` 
    Boolean flag that determines whether parameter epistemic value (info gain about generative model parameters) should be incorporated into computation of EFE. 
prior: ``numpy.ndarray`` of dtype object, default ``None``
    If provided, this is a ``numpy`` object array with one sub-array per hidden state factor, that stores the prior beliefs about initial states. 
    If ``None``, this defaults to a flat (uninformative) prior over hidden states.
pA: ``numpy.ndarray`` of dtype object, default ``None``
    Dirichlet parameters over observation model (same shape as ``A``)
pB: ``numpy.ndarray`` of dtype object, default ``None``
    Dirichlet parameters over transition model (same shape as ``B``)
F: 1D ``numpy.ndarray``, default ``None``
    Vector of variational free energies for each policy
E: 1D ``numpy.ndarray``, default ``None``
    Vector of prior probabilities of each policy (what's referred to in the active inference literature as "habits"). If ``None``, this defaults to a flat (uninformative) prior over policies.
I: ``numpy.ndarray`` of dtype object
    For each state factor, contains a 2D ``numpy.ndarray`` whose element i,j yields the probability 
    of reaching the goal state backwards from state j after i steps.
gamma: ``float``, default 16.0
    Prior precision over policies, scales the contribution of the expected free energy to the posterior over policies

Returns
----------
q_pi: 1D ``numpy.ndarray``
    Posterior beliefs over policies, i.e. a vector containing one posterior probability per policy.
G: 1D ``numpy.ndarray``
    Negative expected free energies of each policy, i.e. a vector containing one negative expected free energy per policy.

---

## pymdp.control.update_posterior_policies_full_factorized

**Arguments:** (qs_seq_pi, A, B, C, A_factor_list, B_factor_list, policies, use_utility=True, use_states_info_gain=True, use_param_info_gain=False, prior=None, pA=None, pB=None, F=None, E=None, I=None, gamma=16.0)

**Description:**
Update posterior beliefs about policies by computing expected free energy of each policy and integrating that
with the variational free energy of policies ``F`` and prior over policies ``E``. This is intended to be used in conjunction
with the ``update_posterior_states_full`` method of ``inference.py``, since the full posterior over future timesteps, under all policies, is
assumed to be provided in the input array ``qs_seq_pi``.

Parameters
----------
qs_seq_pi: ``numpy.ndarray`` of dtype object
    Posterior beliefs over hidden states for each policy. Nesting structure is policies, timepoints, factors,
    where e.g. ``qs_seq_pi[p][t][f]`` stores the marginal belief about factor ``f`` at timepoint ``t`` under policy ``p``.
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``numpy.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``
B: ``numpy.ndarray`` of dtype object
    Dynamics likelihood mapping or 'transition model', mapping from hidden states at ``t`` to hidden states at ``t+1``, given some control state ``u``.
    Each element ``B[f]`` of this object array stores a 3-D tensor for hidden state factor ``f``, whose entries ``B[f][s, v, u]`` store the probability
    of hidden state level ``s`` at the current time, given hidden state level ``v`` and action ``u`` at the previous time.
C: ``numpy.ndarray`` of dtype object
   Prior over observations or 'prior preferences', storing the "value" of each outcome in terms of relative log probabilities. 
   This is softmaxed to form a proper probability distribution before being used to compute the expected utility term of the expected free energy.
A_factor_list: ``list`` of ``list``s of ``int``
    ``list`` that stores the indices of the hidden state factor indices that each observation modality depends on. For example, if ``A_factor_list[m] = [0, 1]``, then
    observation modality ``m`` depends on hidden state factors 0 and 1.
B_factor_list: ``list`` of ``list``s of ``int``
    ``list`` that stores the indices of the hidden state factor indices that each hidden state factor depends on. For example, if ``B_factor_list[f] = [0, 1]``, then
    the transitions in hidden state factor ``f`` depend on hidden state factors 0 and 1.
policies: ``list`` of 2D ``numpy.ndarray``
    ``list`` that stores each policy in ``policies[p_idx]``. Shape of ``policies[p_idx]`` is ``(num_timesteps, num_factors)`` where `num_timesteps` is the temporal
    depth of the policy and ``num_factors`` is the number of control factors.
use_utility: ``Bool``, default ``True``
    Boolean flag that determines whether expected utility should be incorporated into computation of EFE.
use_states_info_gain: ``Bool``, default ``True``
    Boolean flag that determines whether state epistemic value (info gain about hidden states) should be incorporated into computation of EFE.
use_param_info_gain: ``Bool``, default ``False`` 
    Boolean flag that determines whether parameter epistemic value (info gain about generative model parameters) should be incorporated into computation of EFE. 
prior: ``numpy.ndarray`` of dtype object, default ``None``
    If provided, this is a ``numpy`` object array with one sub-array per hidden state factor, that stores the prior beliefs about initial states. 
    If ``None``, this defaults to a flat (uninformative) prior over hidden states.
pA: ``numpy.ndarray`` of dtype object, default ``None``
    Dirichlet parameters over observation model (same shape as ``A``)
pB: ``numpy.ndarray`` of dtype object, default ``None``
    Dirichlet parameters over transition model (same shape as ``B``)
F: 1D ``numpy.ndarray``, default ``None``
    Vector of variational free energies for each policy
E: 1D ``numpy.ndarray``, default ``None``
    Vector of prior probabilities of each policy (what's referred to in the active inference literature as "habits"). If ``None``, this defaults to a flat (uninformative) prior over policies.
I: ``numpy.ndarray`` of dtype object
    For each state factor, contains a 2D ``numpy.ndarray`` whose element i,j yields the probability 
    of reaching the goal state backwards from state j after i steps.
gamma: ``float``, default 16.0
    Prior precision over policies, scales the contribution of the expected free energy to the posterior over policies

Returns
----------
q_pi: 1D ``numpy.ndarray``
    Posterior beliefs over policies, i.e. a vector containing one posterior probability per policy.
G: 1D ``numpy.ndarray``
    Negative expected free energies of each policy, i.e. a vector containing one negative expected free energy per policy.

---

## pymdp.control.update_posterior_states_factorized

**Arguments:** (A, obs, num_obs, num_states, mb_dict, prior=None, **kwargs)

**Description:**
Update marginal posterior over hidden states using mean-field fixed point iteration 
FPI or Fixed point iteration. This version identifies the Markov blanket of each factor using `A_factor_list`

See the following links for details:
http://www.cs.cmu.edu/~guestrin/Class/10708/recitations/r9/VI-view.pdf, slides 13- 18, and http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.137.221&rep=rep1&type=pdf, slides 24 - 38.

Parameters
----------
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``np.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``
obs: 1D ``numpy.ndarray``, ``numpy.ndarray`` of dtype object, int or tuple
    The observation (generated by the environment). If single modality, this can be a 1D ``np.ndarray``
    (one-hot vector representation) or an ``int`` (observation index)
    If multi-modality, this can be ``np.ndarray`` of dtype object whose entries are 1D one-hot vectors,
    or a tuple (of ``int``)
num_obs: ``list`` of ``int``
    List of dimensionalities of each observation modality
num_states: ``list`` of ``int``
    List of dimensionalities of each hidden state factor
mb_dict: ``Dict``
    Dictionary with two keys (``A_factor_list`` and ``A_modality_list``), that stores the factor indices that influence each modality (``A_factor_list``)
    and the modality indices influenced by each factor (``A_modality_list``).
prior: 1D ``numpy.ndarray`` or ``numpy.ndarray`` of dtype object, default None
    Prior beliefs about hidden states, to be integrated with the marginal likelihood to obtain
    a posterior distribution. If not provided, prior is set to be equal to a flat categorical distribution (at the level of
    the individual inference functions).
**kwargs: keyword arguments 
    List of keyword/parameter arguments corresponding to parameter values for the fixed-point iteration
    algorithm ``algos.fpi.run_vanilla_fpi.py``

Returns
----------
qs: 1D ``numpy.ndarray`` or ``numpy.ndarray`` of dtype object
    Marginal posterior beliefs over hidden states at current timepoint

---

## pymdp.inference.average_states_over_policies

**Arguments:** (qs_pi, q_pi)

**Description:**
This function computes a expected posterior over hidden states with respect to the posterior over policies, 
also known as the 'Bayesian model average of states with respect to policies'.

Parameters
----------
qs_pi: ``numpy.ndarray`` of dtype object
    Posterior beliefs over hidden states for each policy. Nesting structure is policies, factors,
    where e.g. ``qs_pi[p][f]`` stores the marginal belief about factor ``f`` under policy ``p``.
q_pi: ``numpy.ndarray`` of dtype object
    Posterior beliefs about policies where ``len(q_pi) = num_policies``

Returns
---------
qs_bma: ``numpy.ndarray`` of dtype object
    Marginal posterior over hidden states for the current timepoint, 
    averaged across policies according to their posterior probability given by ``q_pi``

---

## pymdp.inference.get_joint_likelihood_seq

**Arguments:** (A, obs, num_states)

---

## pymdp.inference.get_joint_likelihood_seq_by_modality

**Arguments:** (A, obs, num_states)

**Description:**
Returns joint likelihoods for each modality separately

---

## pymdp.inference.run_mmp

**Arguments:** (lh_seq, B, policy, prev_actions=None, prior=None, num_iter=10, grad_descent=True, tau=0.25, last_timestep=False)

**Description:**
Marginal message passing scheme for updating marginal posterior beliefs about hidden states over time, 
conditioned on a particular policy.

Parameters
----------
lh_seq: ``numpy.ndarray`` of dtype object
    Log likelihoods of hidden states under a sequence of observations over time. This is assumed to already be log-transformed. Each ``lh_seq[t]`` contains
    the log likelihood of hidden states for a particular observation at time ``t``
B: ``numpy.ndarray`` of dtype object
    Dynamics likelihood mapping or 'transition model', mapping from hidden states at ``t`` to hidden states at ``t+1``, given some control state ``u``.
    Each element ``B[f]`` of this object array stores a 3-D tensor for hidden state factor ``f``, whose entries ``B[f][s, v, u]`` store the probability
    of hidden state level ``s`` at the current time, given hidden state level ``v`` and action ``u`` at the previous time.
policy: 2D ``numpy.ndarray``
    Matrix of shape ``(policy_len, num_control_factors)`` that indicates the indices of each action (control state index) upon timestep ``t`` and control_factor ``f` in the element ``policy[t,f]`` for a given policy.
prev_actions: ``numpy.ndarray``, default None
    If provided, should be a matrix of previous actions of shape ``(infer_len, num_control_factors)`` that indicates the indices of each action (control state index) taken in the past (up until the current timestep).
prior: ``numpy.ndarray`` of dtype object, default None
    If provided, the prior beliefs about initial states (at t = 0, relative to ``infer_len``). If ``None``, this defaults
    to a flat (uninformative) prior over hidden states.
numiter: int, default 10
    Number of variational iterations.
grad_descent: Bool, default True
    Flag for whether to use gradient descent (free energy gradient updates) instead of fixed point solution to the posterior beliefs
tau: float, default 0.25
    Decay constant for use in ``grad_descent`` version. Tunes the size of the gradient descent updates to the posterior.
last_timestep: Bool, default False
    Flag for whether we are at the last timestep of belief updating
    
Returns
---------
qs_seq: ``numpy.ndarray`` of dtype object
    Posterior beliefs over hidden states under the policy. Nesting structure is timepoints, factors,
    where e.g. ``qs_seq[t][f]`` stores the marginal belief about factor ``f`` at timepoint ``t`` under the policy in question.
F: float
    Variational free energy of the policy.

---

## pymdp.inference.run_mmp_factorized

**Arguments:** (lh_seq, mb_dict, B, B_factor_list, policy, prev_actions=None, prior=None, num_iter=10, grad_descent=True, tau=0.25, last_timestep=False)

**Description:**
Marginal message passing scheme for updating marginal posterior beliefs about hidden states over time, 
conditioned on a particular policy.

Parameters
----------
lh_seq: ``numpy.ndarray`` of dtype object
    Log likelihoods of hidden states under a sequence of observations over time. This is assumed to already be log-transformed. Each ``lh_seq[t]`` contains
    the log likelihood of hidden states for a particular observation at time ``t``
mb_dict: ``Dict``
    Dictionary with two keys (``A_factor_list`` and ``A_modality_list``), that stores the factor indices that influence each modality (``A_factor_list``)
    and the modality indices influenced by each factor (``A_modality_list``).
B: ``numpy.ndarray`` of dtype object
    Dynamics likelihood mapping or 'transition model', mapping from hidden states at ``t`` to hidden states at ``t+1``, given some control state ``u``.
    Each element ``B[f]`` of this object array stores a 3-D tensor for hidden state factor ``f``, whose entries ``B[f][s, v, u]`` store the probability
    of hidden state level ``s`` at the current time, given hidden state level ``v`` and action ``u`` at the previous time.
B_factor_list: ``list`` of ``list`` of ``int``
    List of lists of hidden state factors each hidden state factor depends on. Each element ``B_factor_list[i]`` is a list of the factor indices that factor i's dynamics depend on.
policy: 2D ``numpy.ndarray``
    Matrix of shape ``(policy_len, num_control_factors)`` that indicates the indices of each action (control state index) upon timestep ``t`` and control_factor ``f` in the element ``policy[t,f]`` for a given policy.
prev_actions: ``numpy.ndarray``, default None
    If provided, should be a matrix of previous actions of shape ``(infer_len, num_control_factors)`` that indicates the indices of each action (control state index) taken in the past (up until the current timestep).
prior: ``numpy.ndarray`` of dtype object, default None
    If provided, the prior beliefs about initial states (at t = 0, relative to ``infer_len``). If ``None``, this defaults
    to a flat (uninformative) prior over hidden states.
numiter: int, default 10
    Number of variational iterations.
grad_descent: Bool, default True
    Flag for whether to use gradient descent (free energy gradient updates) instead of fixed point solution to the posterior beliefs
tau: float, default 0.25
    Decay constant for use in ``grad_descent`` version. Tunes the size of the gradient descent updates to the posterior.
last_timestep: Bool, default False
    Flag for whether we are at the last timestep of belief updating
    
Returns
---------
qs_seq: ``numpy.ndarray`` of dtype object
    Posterior beliefs over hidden states under the policy. Nesting structure is timepoints, factors,
    where e.g. ``qs_seq[t][f]`` stores the marginal belief about factor ``f`` at timepoint ``t`` under the policy in question.
F: float
    Variational free energy of the policy.

---

## pymdp.inference.run_vanilla_fpi

**Arguments:** (A, obs, num_obs, num_states, prior=None, num_iter=10, dF=1.0, dF_tol=0.001, compute_vfe=True)

**Description:**
Update marginal posterior beliefs over hidden states using mean-field variational inference, via
fixed point iteration. 

Parameters
----------
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``np.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``
obs: numpy 1D array or numpy ndarray of dtype object
    The observation (generated by the environment). If single modality, this should be a 1D ``np.ndarray``
    (one-hot vector representation). If multi-modality, this should be ``np.ndarray`` of dtype object whose entries are 1D one-hot vectors.
num_obs: list of ints
    List of dimensionalities of each observation modality
num_states: list of ints
    List of dimensionalities of each hidden state factor
prior: numpy ndarray of dtype object, default None
    Prior over hidden states. If absent, prior is set to be the log uniform distribution over hidden states (identical to the 
    initialisation of the posterior)
num_iter: int, default 10
    Number of variational fixed-point iterations to run until convergence.
dF: float, default 1.0
    Initial free energy gradient (dF/dt) before updating in the course of gradient descent.
dF_tol: float, default 0.001
    Threshold value of the time derivative of the variational free energy (dF/dt), to be checked at 
    each iteration. If dF <= dF_tol, the iterations are halted pre-emptively and the final 
    marginal posterior belief(s) is(are) returned
compute_vfe: bool, default True
    Whether to compute the variational free energy at each iteration. If False, the function runs through 
    all variational iterations.

Returns
----------
qs: numpy 1D array, numpy ndarray of dtype object, optional
    Marginal posterior beliefs over hidden states at current timepoint

---

## pymdp.inference.run_vanilla_fpi_factorized

**Arguments:** (A, obs, num_obs, num_states, mb_dict, prior=None, num_iter=10, dF=1.0, dF_tol=0.001, compute_vfe=True)

**Description:**
Update marginal posterior beliefs over hidden states using mean-field variational inference, via
fixed point iteration. 

Parameters
----------
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``np.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``
obs: numpy 1D array or numpy ndarray of dtype object
    The observation (generated by the environment). If single modality, this should be a 1D ``np.ndarray``
    (one-hot vector representation). If multi-modality, this should be ``np.ndarray`` of dtype object whose entries are 1D one-hot vectors.
num_obs: ``list`` of ints
    List of dimensionalities of each observation modality
num_states: ``list`` of ints
    List of dimensionalities of each hidden state factor
mb_dict: ``Dict``
    Dictionary with two keys (``A_factor_list`` and ``A_modality_list``), that stores the factor indices that influence each modality (``A_factor_list``)
    and the modality indices influenced by each factor (``A_modality_list``).
prior: numpy ndarray of dtype object, default None
    Prior over hidden states. If absent, prior is set to be the log uniform distribution over hidden states (identical to the 
    initialisation of the posterior)
num_iter: int, default 10
    Number of variational fixed-point iterations to run until convergence.
dF: float, default 1.0
    Initial free energy gradient (dF/dt) before updating in the course of gradient descent.
dF_tol: float, default 0.001
    Threshold value of the time derivative of the variational free energy (dF/dt), to be checked at 
    each iteration. If dF <= dF_tol, the iterations are halted pre-emptively and the final 
    marginal posterior belief(s) is(are) returned
compute_vfe: bool, default True
    Whether to compute the variational free energy at each iteration. If False, the function runs through 
    all variational iterations.

Returns
----------
qs: numpy 1D array, numpy ndarray of dtype object, optional
    Marginal posterior beliefs over hidden states at current timepoint

---

## pymdp.inference.update_posterior_states

**Arguments:** (A, obs, prior=None, **kwargs)

**Description:**
Update marginal posterior over hidden states using mean-field fixed point iteration 
FPI or Fixed point iteration. 

See the following links for details:
http://www.cs.cmu.edu/~guestrin/Class/10708/recitations/r9/VI-view.pdf, slides 13- 18, and http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.137.221&rep=rep1&type=pdf, slides 24 - 38.

Parameters
----------
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``np.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``
obs: 1D ``numpy.ndarray``, ``numpy.ndarray`` of dtype object, int or tuple
    The observation (generated by the environment). If single modality, this can be a 1D ``np.ndarray``
    (one-hot vector representation) or an ``int`` (observation index)
    If multi-modality, this can be ``np.ndarray`` of dtype object whose entries are 1D one-hot vectors,
    or a tuple (of ``int``)
prior: 1D ``numpy.ndarray`` or ``numpy.ndarray`` of dtype object, default None
    Prior beliefs about hidden states, to be integrated with the marginal likelihood to obtain
    a posterior distribution. If not provided, prior is set to be equal to a flat categorical distribution (at the level of
    the individual inference functions).
**kwargs: keyword arguments 
    List of keyword/parameter arguments corresponding to parameter values for the fixed-point iteration
    algorithm ``algos.fpi.run_vanilla_fpi.py``

Returns
----------
qs: 1D ``numpy.ndarray`` or ``numpy.ndarray`` of dtype object
    Marginal posterior beliefs over hidden states at current timepoint

---

## pymdp.inference.update_posterior_states_factorized

**Arguments:** (A, obs, num_obs, num_states, mb_dict, prior=None, **kwargs)

**Description:**
Update marginal posterior over hidden states using mean-field fixed point iteration 
FPI or Fixed point iteration. This version identifies the Markov blanket of each factor using `A_factor_list`

See the following links for details:
http://www.cs.cmu.edu/~guestrin/Class/10708/recitations/r9/VI-view.pdf, slides 13- 18, and http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.137.221&rep=rep1&type=pdf, slides 24 - 38.

Parameters
----------
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``np.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``
obs: 1D ``numpy.ndarray``, ``numpy.ndarray`` of dtype object, int or tuple
    The observation (generated by the environment). If single modality, this can be a 1D ``np.ndarray``
    (one-hot vector representation) or an ``int`` (observation index)
    If multi-modality, this can be ``np.ndarray`` of dtype object whose entries are 1D one-hot vectors,
    or a tuple (of ``int``)
num_obs: ``list`` of ``int``
    List of dimensionalities of each observation modality
num_states: ``list`` of ``int``
    List of dimensionalities of each hidden state factor
mb_dict: ``Dict``
    Dictionary with two keys (``A_factor_list`` and ``A_modality_list``), that stores the factor indices that influence each modality (``A_factor_list``)
    and the modality indices influenced by each factor (``A_modality_list``).
prior: 1D ``numpy.ndarray`` or ``numpy.ndarray`` of dtype object, default None
    Prior beliefs about hidden states, to be integrated with the marginal likelihood to obtain
    a posterior distribution. If not provided, prior is set to be equal to a flat categorical distribution (at the level of
    the individual inference functions).
**kwargs: keyword arguments 
    List of keyword/parameter arguments corresponding to parameter values for the fixed-point iteration
    algorithm ``algos.fpi.run_vanilla_fpi.py``

Returns
----------
qs: 1D ``numpy.ndarray`` or ``numpy.ndarray`` of dtype object
    Marginal posterior beliefs over hidden states at current timepoint

---

## pymdp.inference.update_posterior_states_full

**Arguments:** (A, B, prev_obs, policies, prev_actions=None, prior=None, policy_sep_prior=True, **kwargs)

**Description:**
Update posterior over hidden states using marginal message passing

Parameters
----------
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``numpy.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``
B: ``numpy.ndarray`` of dtype object
    Dynamics likelihood mapping or 'transition model', mapping from hidden states at ``t`` to hidden states at ``t+1``, given some control state ``u``.
    Each element ``B[f]`` of this object array stores a 3-D tensor for hidden state factor ``f``, whose entries ``B[f][s, v, u]`` store the probability
    of hidden state level ``s`` at the current time, given hidden state level ``v`` and action ``u`` at the previous time.
prev_obs: ``list``
    List of observations over time. Each observation in the list can be an ``int``, a ``list`` of ints, a ``tuple`` of ints, a one-hot vector or an object array of one-hot vectors.
policies: ``list`` of 2D ``numpy.ndarray``
    List that stores each policy in ``policies[p_idx]``. Shape of ``policies[p_idx]`` is ``(num_timesteps, num_factors)`` where `num_timesteps` is the temporal
    depth of the policy and ``num_factors`` is the number of control factors.
prior: ``numpy.ndarray`` of dtype object, default ``None``
    If provided, this a ``numpy.ndarray`` of dtype object, with one sub-array per hidden state factor, that stores the prior beliefs about initial states. 
    If ``None``, this defaults to a flat (uninformative) prior over hidden states.
policy_sep_prior: ``Bool``, default ``True``
    Flag determining whether the prior beliefs from the past are unconditioned on policy, or separated by /conditioned on the policy variable.
**kwargs: keyword arguments
    Optional keyword arguments for the function ``algos.mmp.run_mmp``

Returns
---------
qs_seq_pi: ``numpy.ndarray`` of dtype object
    Posterior beliefs over hidden states for each policy. Nesting structure is policies, timepoints, factors,
    where e.g. ``qs_seq_pi[p][t][f]`` stores the marginal belief about factor ``f`` at timepoint ``t`` under policy ``p``.
F: 1D ``numpy.ndarray``
    Vector of variational free energies for each policy

---

## pymdp.inference.update_posterior_states_full_factorized

**Arguments:** (A, mb_dict, B, B_factor_list, prev_obs, policies, prev_actions=None, prior=None, policy_sep_prior=True, **kwargs)

**Description:**
Update posterior over hidden states using marginal message passing

Parameters
----------
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``numpy.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``
mb_dict: ``Dict``
    Dictionary with two keys (``A_factor_list`` and ``A_modality_list``), that stores the factor indices that influence each modality (``A_factor_list``)
    and the modality indices influenced by each factor (``A_modality_list``).
B: ``numpy.ndarray`` of dtype object
    Dynamics likelihood mapping or 'transition model', mapping from hidden states at ``t`` to hidden states at ``t+1``, given some control state ``u``.
    Each element ``B[f]`` of this object array stores a 3-D tensor for hidden state factor ``f``, whose entries ``B[f][s, v, u]`` store the probability
    of hidden state level ``s`` at the current time, given hidden state level ``v`` and action ``u`` at the previous time.
B_factor_list: ``list`` of ``list`` of ``int``
    List of lists of hidden state factors each hidden state factor depends on. Each element ``B_factor_list[i]`` is a list of the factor indices that factor i's dynamics depend on.
prev_obs: ``list``
    List of observations over time. Each observation in the list can be an ``int``, a ``list`` of ints, a ``tuple`` of ints, a one-hot vector or an object array of one-hot vectors.
policies: ``list`` of 2D ``numpy.ndarray``
    List that stores each policy in ``policies[p_idx]``. Shape of ``policies[p_idx]`` is ``(num_timesteps, num_factors)`` where `num_timesteps` is the temporal
    depth of the policy and ``num_factors`` is the number of control factors.
prior: ``numpy.ndarray`` of dtype object, default ``None``
    If provided, this a ``numpy.ndarray`` of dtype object, with one sub-array per hidden state factor, that stores the prior beliefs about initial states. 
    If ``None``, this defaults to a flat (uninformative) prior over hidden states.
policy_sep_prior: ``Bool``, default ``True``
    Flag determining whether the prior beliefs from the past are unconditioned on policy, or separated by /conditioned on the policy variable.
**kwargs: keyword arguments
    Optional keyword arguments for the function ``algos.mmp.run_mmp``

Returns
---------
qs_seq_pi: ``numpy.ndarray`` of dtype object
    Posterior beliefs over hidden states for each policy. Nesting structure is policies, timepoints, factors,
    where e.g. ``qs_seq_pi[p][t][f]`` stores the marginal belief about factor ``f`` at timepoint ``t`` under policy ``p``.
F: 1D ``numpy.ndarray``
    Vector of variational free energies for each policy

---

## pymdp.learning.update_obs_likelihood_dirichlet

**Arguments:** (pA, A, obs, qs, lr=1.0, modalities='all')

**Description:**
Update Dirichlet parameters of the observation likelihood distribution.

Parameters
-----------
pA: ``numpy.ndarray`` of dtype object
    Prior Dirichlet parameters over observation model (same shape as ``A``)
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``numpy.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``
obs: 1D ``numpy.ndarray``, ``numpy.ndarray`` of dtype object, ``int`` or ``tuple``
    The observation (generated by the environment). If single modality, this can be a 1D ``numpy.ndarray``
    (one-hot vector representation) or an ``int`` (observation index)
    If multi-modality, this can be ``numpy.ndarray`` of dtype object whose entries are 1D one-hot vectors,
    or a ``tuple`` (of ``int``)
qs: 1D ``numpy.ndarray`` or ``numpy.ndarray`` of dtype object, default None
    Marginal posterior beliefs over hidden states at current timepoint.
lr: float, default 1.0
    Learning rate, scale of the Dirichlet pseudo-count update.
modalities: ``list``, default "all"
    Indices (ranging from 0 to ``n_modalities - 1``) of the observation modalities to include 
    in learning. Defaults to "all", meaning that modality-specific sub-arrays of ``pA``
    are all updated using the corresponding observations.

Returns
-----------
qA: ``numpy.ndarray`` of dtype object
    Posterior Dirichlet parameters over observation model (same shape as ``A``), after having updated it with observations.

---

## pymdp.learning.update_obs_likelihood_dirichlet_factorized

**Arguments:** (pA, A, obs, qs, A_factor_list, lr=1.0, modalities='all')

**Description:**
Update Dirichlet parameters of the observation likelihood distribution, in a case where the observation model is reduced (factorized) and only represents
the conditional dependencies between the observation modalities and particular hidden state factors (whose indices are specified in each modality-specific entry of ``A_factor_list``)

Parameters
-----------
pA: ``numpy.ndarray`` of dtype object
    Prior Dirichlet parameters over observation model (same shape as ``A``)
A: ``numpy.ndarray`` of dtype object
    Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
    stores an ``numpy.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
    the probability of observation level ``i`` given hidden state levels ``j, k, ...``
obs: 1D ``numpy.ndarray``, ``numpy.ndarray`` of dtype object, ``int`` or ``tuple``
    The observation (generated by the environment). If single modality, this can be a 1D ``numpy.ndarray``
    (one-hot vector representation) or an ``int`` (observation index)
    If multi-modality, this can be ``numpy.ndarray`` of dtype object whose entries are 1D one-hot vectors,
    or a ``tuple`` (of ``int``)
qs: 1D ``numpy.ndarray`` or ``numpy.ndarray`` of dtype object, default None
    Marginal posterior beliefs over hidden states at current timepoint.
A_factor_list: ``list`` of ``list`` of ``int``
    List of lists, where each list with index `m` contains the indices of the hidden states that observation modality `m` depends on.
lr: float, default 1.0
    Learning rate, scale of the Dirichlet pseudo-count update.
modalities: ``list``, default "all"
    Indices (ranging from 0 to ``n_modalities - 1``) of the observation modalities to include 
    in learning. Defaults to "all", meaning that modality-specific sub-arrays of ``pA``
    are all updated using the corresponding observations.

Returns
-----------
qA: ``numpy.ndarray`` of dtype object
    Posterior Dirichlet parameters over observation model (same shape as ``A``), after having updated it with observations.

---

## pymdp.learning.update_state_likelihood_dirichlet

**Arguments:** (pB, B, actions, qs, qs_prev, lr=1.0, factors='all')

**Description:**
Update Dirichlet parameters of the transition distribution. 

Parameters
-----------
pB: ``numpy.ndarray`` of dtype object
    Prior Dirichlet parameters over transition model (same shape as ``B``)
B: ``numpy.ndarray`` of dtype object
    Dynamics likelihood mapping or 'transition model', mapping from hidden states at ``t`` to hidden states at ``t+1``, given some control state ``u``.
    Each element ``B[f]`` of this object array stores a 3-D tensor for hidden state factor ``f``, whose entries ``B[f][s, v, u]`` store the probability
    of hidden state level ``s`` at the current time, given hidden state level ``v`` and action ``u`` at the previous time.
actions: 1D ``numpy.ndarray``
    A vector with length equal to the number of control factors, where each element contains the index of the action (for that control factor) performed at 
    a given timestep.
qs: 1D ``numpy.ndarray`` or ``numpy.ndarray`` of dtype object
    Marginal posterior beliefs over hidden states at current timepoint.
qs_prev: 1D ``numpy.ndarray`` or ``numpy.ndarray`` of dtype object
    Marginal posterior beliefs over hidden states at previous timepoint.
lr: float, default ``1.0``
    Learning rate, scale of the Dirichlet pseudo-count update.
factors: ``list``, default "all"
    Indices (ranging from 0 to ``n_factors - 1``) of the hidden state factors to include 
    in learning. Defaults to "all", meaning that factor-specific sub-arrays of ``pB``
    are all updated using the corresponding hidden state distributions and actions.

Returns
-----------
qB: ``numpy.ndarray`` of dtype object
    Posterior Dirichlet parameters over transition model (same shape as ``B``), after having updated it with state beliefs and actions.

---

## pymdp.learning.update_state_likelihood_dirichlet_interactions

**Arguments:** (pB, B, actions, qs, qs_prev, B_factor_list, lr=1.0, factors='all')

**Description:**
Update Dirichlet parameters of the transition distribution, in the case when 'interacting' hidden state factors are present, i.e.
the dynamics of a given hidden state factor `f` are no longer independent of the dynamics of other hidden state factors.

Parameters
-----------
pB: ``numpy.ndarray`` of dtype object
    Prior Dirichlet parameters over transition model (same shape as ``B``)
B: ``numpy.ndarray`` of dtype object
    Dynamics likelihood mapping or 'transition model', mapping from hidden states at ``t`` to hidden states at ``t+1``, given some control state ``u``.
    Each element ``B[f]`` of this object array stores a 3-D tensor for hidden state factor ``f``, whose entries ``B[f][s, v, u]`` store the probability
    of hidden state level ``s`` at the current time, given hidden state level ``v`` and action ``u`` at the previous time.
actions: 1D ``numpy.ndarray``
    A vector with length equal to the number of control factors, where each element contains the index of the action (for that control factor) performed at 
    a given timestep.
qs: 1D ``numpy.ndarray`` or ``numpy.ndarray`` of dtype object
    Marginal posterior beliefs over hidden states at current timepoint.
qs_prev: 1D ``numpy.ndarray`` or ``numpy.ndarray`` of dtype object
    Marginal posterior beliefs over hidden states at previous timepoint.
B_factor_list: ``list`` of ``list`` of ``int``
    A list of lists, where each element ``B_factor_list[f]`` is a list of indices of hidden state factors that that are needed to predict the dynamics of hidden state factor ``f``.
lr: float, default ``1.0``
    Learning rate, scale of the Dirichlet pseudo-count update.
factors: ``list``, default "all"
    Indices (ranging from 0 to ``n_factors - 1``) of the hidden state factors to include 
    in learning. Defaults to "all", meaning that factor-specific sub-arrays of ``pB``
    are all updated using the corresponding hidden state distributions and actions.

Returns
-----------
qB: ``numpy.ndarray`` of dtype object
    Posterior Dirichlet parameters over transition model (same shape as ``B``), after having updated it with state beliefs and actions.

---

## pymdp.learning.update_state_prior_dirichlet

**Arguments:** (pD, qs, lr=1.0, factors='all')

**Description:**
Update Dirichlet parameters of the initial hidden state distribution 
(prior beliefs about hidden states at the beginning of the inference window).

Parameters
-----------
pD: ``numpy.ndarray`` of dtype object
    Prior Dirichlet parameters over initial hidden state prior (same shape as ``qs``)
qs: 1D ``numpy.ndarray`` or ``numpy.ndarray`` of dtype object
    Marginal posterior beliefs over hidden states at current timepoint
lr: float, default ``1.0``
    Learning rate, scale of the Dirichlet pseudo-count update.
factors: ``list``, default "all"
    Indices (ranging from 0 to ``n_factors - 1``) of the hidden state factors to include 
    in learning. Defaults to "all", meaning that factor-specific sub-vectors of ``pD``
    are all updated using the corresponding hidden state distributions.

Returns
-----------
qD: ``numpy.ndarray`` of dtype object
    Posterior Dirichlet parameters over initial hidden state prior (same shape as ``qs``), after having updated it with state beliefs.

---

## pymdp.maths.calc_free_energy

**Arguments:** (qs, prior, n_factors, likelihood=None)

**Description:**
Calculate variational free energy
@TODO Primarily used in FPI algorithm, needs to be made general

---

## pymdp.maths.compute_accuracy

**Arguments:** (log_likelihood, qs)

**Description:**
Function that computes the accuracy term of the variational free energy. This is essentially a stripped down version of `spm_dot` above,
with fewer conditions / dimension handling in the beginning.

---

## pymdp.maths.contract

**Arguments:** (*operands, **kwargs)

**Description:**
contract(subscripts, *operands, out=None, dtype=None, order='K', casting='safe', use_blas=True, optimize=True, memory_limit=None, backend='numpy')

Evaluates the Einstein summation convention on the operands. A drop in
replacement for NumPy's einsum function that optimizes the order of contraction
to reduce overall scaling at the cost of several intermediate arrays.

Parameters
----------
subscripts : str
    Specifies the subscripts for summation.
*operands : list of array_like
    These are the arrays for the operation.
out : array_like
    A output array in which set the resulting output.
dtype : str
    The dtype of the given contraction, see np.einsum.
order : str
    The order of the resulting contraction, see np.einsum.
casting : str
    The casting procedure for operations of different dtype, see np.einsum.
use_blas : bool
    Do you use BLAS for valid operations, may use extra memory for more intermediates.
optimize : str, list or bool, optional (default: ``auto``)
    Choose the type of path.

    - if a list is given uses this as the path.
    - ``'optimal'`` An algorithm that explores all possible ways of
      contracting the listed tensors. Scales factorially with the number of
      terms in the contraction.
    - ``'dp'`` A faster (but essentially optimal) algorithm that uses
      dynamic programming to exhaustively search all contraction paths
      without outer-products.
    - ``'greedy'`` An cheap algorithm that heuristically chooses the best
      pairwise contraction at each step. Scales linearly in the number of
      terms in the contraction.
    - ``'random-greedy'`` Run a randomized version of the greedy algorithm
      32 times and pick the best path.
    - ``'random-greedy-128'`` Run a randomized version of the greedy
      algorithm 128 times and pick the best path.
    - ``'branch-all'`` An algorithm like optimal but that restricts itself
      to searching 'likely' paths. Still scales factorially.
    - ``'branch-2'`` An even more restricted version of 'branch-all' that
      only searches the best two options at each step. Scales exponentially
      with the number of terms in the contraction.
    - ``'auto'`` Choose the best of the above algorithms whilst aiming to
      keep the path finding time below 1ms.
    - ``'auto-hq'`` Aim for a high quality contraction, choosing the best
      of the above algorithms whilst aiming to keep the path finding time
      below 1sec.

memory_limit : {None, int, 'max_input'} (default: None)
    Give the upper bound of the largest intermediate tensor contract will build.

    - None or -1 means there is no limit
    - 'max_input' means the limit is set as largest input tensor
    - a positive integer is taken as an explicit limit on the number of elements

    The default is None. Note that imposing a limit can make contractions
    exponentially slower to perform.
backend : str, optional (default: ``auto``)
    Which library to use to perform the required ``tensordot``, ``transpose``
    and ``einsum`` calls. Should match the types of arrays supplied, See
    :func:`contract_expression` for generating expressions which convert
    numpy arrays to and from the backend library automatically.

Returns
-------
out : array_like
    The result of the einsum expression.

Notes
-----
This function should produce a result identical to that of NumPy's einsum
function. The primary difference is ``contract`` will attempt to form
intermediates which reduce the overall scaling of the given einsum contraction.
By default the worst intermediate formed will be equal to that of the largest
input array. For large einsum expressions with many input arrays this can
provide arbitrarily large (1000 fold+) speed improvements.

For contractions with just two tensors this function will attempt to use
NumPy's built-in BLAS functionality to ensure that the given operation is
preformed optimally. When NumPy is linked to a threaded BLAS, potential
speedups are on the order of 20-100 for a six core machine.

Examples
--------

See :func:`opt_einsum.contract_path` or :func:`numpy.einsum`

---

## pymdp.maths.dirichlet_log_evidence

**Arguments:** (q_dir, p_dir, r_dir)

**Description:**
Bayesian model reduction and log evidence calculations for Dirichlet hyperparameters
This is a NumPY translation of the MATLAB function `spm_MDP_log_evidence.m` from the
DEM package of spm. 

Description (adapted from MATLAB docstring)
This function computes the negative log evidence of a reduced model of a
Categorical distribution parameterised in terms of Dirichlet hyperparameters 
(i.e., concentration parameters encoding probabilities). It uses Bayesian model reduction 
to evaluate the evidence for models with and without a particular parameter.
Arguments:
===========
`q_dir` [1D np.ndarray]: sufficient statistics of posterior of full model
`p_dir` [1D np.ndarray]: sufficient statistics of prior of full model
`r_dir` [1D np.ndarray]: sufficient statistics of prior of reduced model
Returns:
==========
`F` [float]: free energy or (negative) log evidence of reduced model
`s_dir` [1D np.ndarray]: sufficient statistics of reduced posterior

---

## pymdp.maths.dot_likelihood

**Arguments:** (A, obs)

---

## pymdp.maths.entropy

**Arguments:** (A)

**Description:**
Compute the entropy term H of the likelihood matrix,
i.e. one entropy value per column

---

## pymdp.maths.factor_dot_flex

**Arguments:** (M, xs, dims, keep_dims=None)

**Description:**
Dot product of a multidimensional array with `x`.

Parameters
----------
- `M` [numpy.ndarray] - tensor
- 'xs' [list of numpyr.ndarray] - list of tensors
- 'dims' [list of tuples] - list of dimensions of xs tensors in tensor M
- 'keep_dims' [tuple] - tuple of integers denoting dimesions to keep
Returns 
-------
- `Y` [1D numpy.ndarray] - the result of the dot product

---

## pymdp.maths.get_joint_likelihood

**Arguments:** (A, obs, num_states)

---

## pymdp.maths.get_joint_likelihood_seq

**Arguments:** (A, obs, num_states)

---

## pymdp.maths.get_joint_likelihood_seq_by_modality

**Arguments:** (A, obs, num_states)

**Description:**
Returns joint likelihoods for each modality separately

---

## pymdp.maths.kl_div

**Arguments:** (P, Q)

**Description:**
Parameters
----------
P : Categorical probability distribution
Q : Categorical probability distribution

Returns
-------
The KL-divergence of P and Q

---

## pymdp.maths.softmax

**Arguments:** (dist)

**Description:**
Computes the softmax function on a set of values

---

## pymdp.maths.softmax_obj_arr

**Arguments:** (arr)

---

## pymdp.maths.spm_MDP_G

**Arguments:** (A, x)

**Description:**
Calculates the Bayesian surprise in the same way as spm_MDP_G.m does in 
the original matlab code.

Parameters
----------
A (numpy ndarray or array-object):
    array assigning likelihoods of observations/outcomes under the various 
    hidden state configurations

x (numpy ndarray or array-object):
    Categorical distribution presenting probabilities of hidden states 
    (this can also be interpreted as the predictive density over hidden 
    states/causes if you're calculating the expected Bayesian surprise)
    
Returns
-------
G (float):
    the (expected or not) Bayesian surprise under the density specified by x --
    namely, this scores how much an expected observation would update beliefs 
    about hidden states x, were it to be observed. 

---

## pymdp.maths.spm_betaln

**Arguments:** (z)

**Description:**
Log of the multivariate beta function of a vector.
@NOTE this function computes across columns if `z` is a matrix

---

## pymdp.maths.spm_calc_neg_ambig

**Arguments:** (A, x)

**Description:**
Function that just calculates the negativity ambiguity part of the state information gain, using the same method used in 
spm_MDP_G.m in the original matlab code.

Parameters
----------
A (numpy ndarray or array-object):
    array assigning likelihoods of observations/outcomes under the various 
    hidden state configurations

x (numpy ndarray or array-object):
    Categorical distribution presenting probabilities of hidden states 
    (this can also be interpreted as the predictive density over hidden 
    states/causes if you're calculating the expected Bayesian surprise)
    
Returns
-------
G (float):
    the negative ambiguity (negative entropy of the likelihood of observations given hidden states, expected under current posterior over hidden states)

---

## pymdp.maths.spm_calc_qo_entropy

**Arguments:** (A, x)

**Description:**
Function that just calculates the entropy part of the state information gain, using the same method used in 
spm_MDP_G.m in the original matlab code.

Parameters
----------
A (numpy ndarray or array-object):
    array assigning likelihoods of observations/outcomes under the various 
    hidden state configurations

x (numpy ndarray or array-object):
    Categorical distribution presenting probabilities of hidden states 
    (this can also be interpreted as the predictive density over hidden 
    states/causes if you're calculating the expected Bayesian surprise)
    
Returns
-------
H (float):
    the entropy of the marginal distribution over observations/outcomes

---

## pymdp.maths.spm_cross

**Arguments:** (x, y=None, *args)

**Description:**
Multi-dimensional outer product

Parameters
----------
- `x` [np.ndarray] || [Categorical] (optional)
    The values to perfrom the outer-product with. If empty, then the outer-product 
    is taken between x and itself. If y is not empty, then outer product is taken 
    between x and the various dimensions of y.
- `args` [np.ndarray] || [Categorical] (optional)
    Remaining arrays to perform outer-product with. These extra arrays are recursively 
    multiplied with the 'initial' outer product (that between X and x).

Returns
-------
- `z` [np.ndarray] || [Categorical]
      The result of the outer-product

---

## pymdp.maths.spm_dot

**Arguments:** (X, x, dims_to_omit=None)

**Description:**
Dot product of a multidimensional array with `x`. The dimensions in `dims_to_omit` 
will not be summed across during the dot product

Parameters
----------
- `x` [1D numpy.ndarray] - either vector or array of arrays
    The alternative array to perform the dot product with
- `dims_to_omit` [list :: int] (optional)
    Which dimensions to omit

Returns 
-------
- `Y` [1D numpy.ndarray] - the result of the dot product

---

## pymdp.maths.spm_dot_classic

**Arguments:** (X, x, dims_to_omit=None)

**Description:**
Dot product of a multidimensional array with `x`. The dimensions in `dims_to_omit` 
will not be summed across during the dot product

Parameters
----------
- `x` [1D numpy.ndarray] - either vector or array of arrays
    The alternative array to perform the dot product with
- `dims_to_omit` [list :: int] (optional)
    Which dimensions to omit

Returns 
-------
- `Y` [1D numpy.ndarray] - the result of the dot product

---

## pymdp.maths.spm_dot_old

**Arguments:** (X, x, dims_to_omit=None, obs_mode=False)

**Description:**
Dot product of a multidimensional array with `x`. The dimensions in `dims_to_omit` 
will not be summed across during the dot product

#TODO: we should look for an alternative to obs_mode

Parameters
----------
- `x` [1D numpy.ndarray] - either vector or array of arrays
    The alternative array to perform the dot product with
- `dims_to_omit` [list :: int] (optional)
    Which dimensions to omit

Returns 
-------
- `Y` [1D numpy.ndarray] - the result of the dot product

---

## pymdp.maths.spm_log_obj_array

**Arguments:** (obj_arr)

**Description:**
Applies `spm_log_single` to multiple elements of a numpy object array

---

## pymdp.maths.spm_log_single

**Arguments:** (arr)

**Description:**
Adds small epsilon value to an array before natural logging it

---

## pymdp.maths.spm_norm

**Arguments:** (A)

**Description:**
Returns normalization of Categorical distribution, 
stored in the columns of A.

---

## pymdp.maths.spm_wnorm

**Arguments:** (A)

**Description:**
Returns Expectation of logarithm of Dirichlet parameters over a set of 
Categorical distributions, stored in the columns of A.

---

## pymdp.utils.Dimensions

**Arguments:** (num_observations=None, num_observation_modalities=0, num_states=None, num_state_factors=0, num_controls=None, num_control_factors=0)

**Description:**
The Dimensions class stores all data related to the size and shape of a model.

---

## pymdp.utils.build_xn_vn_array

**Arguments:** (xn)

**Description:**
This function constructs array-ified (not nested) versions
of the posterior xn (beliefs) or vn (prediction error) arrays, that are separated 
by iteration, hidden state factor, timepoint, and policy

---

## pymdp.utils.construct_controllable_B

**Arguments:** (num_states, num_controls)

**Description:**
Generates a fully controllable transition likelihood array, where each 
action (control state) corresponds to a move to the n-th state from any 
other state, for each control factor

---

## pymdp.utils.construct_full_a

**Arguments:** (A_reduced, original_factor_idx, num_states)

**Description:**
Utility function for reconstruction a full A matrix from a reduced A matrix, using known factor indices
to tile out the reduced A matrix along the 'non-informative' dimensions
Parameters:
==========
- `A_reduced` [np.ndarray]:
    The reduced A matrix or likelihood array that encodes probabilistic relationship
    of the generative model between hidden state factors (lagging dimensions, columns, slices, etc...)
    and observations (leading dimension, rows). 
- `original_factor_idx` [list]:
    List of hidden state indices in terms of the full hidden state factor list, that comprise
    the lagging dimensions of `A_reduced`
- `num_states` [list]:
    The list of all the dimensionalities of hidden state factors in the full generative model.
    `A_reduced.shape[1:]` should be equal to `num_states[original_factor_idx]`
Returns:
=========
- `A` [np.ndarray]:
    The full A matrix, containing all the lagging dimensions that correspond to hidden state factors, including
    those that are statistically independent of observations

@ NOTE: This is the "inverse" of the reduce_a_matrix function, 
i.e. `reduce_a_matrix(construct_full_a(A_reduced, original_factor_idx, num_states)) == A_reduced, original_factor_idx`

---

## pymdp.utils.convert_observation_array

**Arguments:** (obs, num_obs)

**Description:**
Converts from SPM-style observation array to infer-actively one-hot object arrays.

Parameters
----------
- 'obs' [numpy 2-D nd.array]:
    SPM-style observation arrays are of shape (num_modalities, T), where each row 
    contains observation indices for a different modality, and columns indicate 
    different timepoints. Entries store the indices of the discrete observations 
    within each modality. 

- 'num_obs' [list]:
    List of the dimensionalities of the observation modalities. `num_modalities` 
    is calculated as `len(num_obs)` in the function to determine whether we're 
    dealing with a single- or multi-modality 
    case.

Returns
----------
- `obs_t`[list]: 
    A list with length equal to T, where each entry of the list is either a) an object 
    array (in the case of multiple modalities) where each sub-array is a one-hot vector 
    with the observation for the correspond modality, or b) a 1D numpy array (in the case
    of one modality) that is a single one-hot vector encoding the observation for the 
    single modality.

---

## pymdp.utils.dirichlet_like

**Arguments:** (template_categorical, scale=1.0)

**Description:**
Helper function to construct a Dirichlet distribution based on an existing Categorical distribution

---

## pymdp.utils.get_model_dimensions

**Arguments:** (A=None, B=None, factorized=False)

---

## pymdp.utils.get_model_dimensions_from_labels

**Arguments:** (model_labels)

---

## pymdp.utils.initialize_empty_A

**Arguments:** (num_obs, num_states)

**Description:**
Initializes an empty observation likelihood array or `A` array using a list of observation-modality dimensions (`num_obs`)
and hidden state factor dimensions (`num_states`)

---

## pymdp.utils.initialize_empty_B

**Arguments:** (num_states, num_controls)

**Description:**
Initializes an empty (controllable) transition likelihood array or `B` array using a list of hidden state factor dimensions (`num_states`)
and control factor dimensions (`num_controls)

---

## pymdp.utils.insert_multiple

**Arguments:** (s, indices, items)

---

## pymdp.utils.is_normalized

**Arguments:** (dist)

**Description:**
Utility function for checking whether a single distribution or set of conditional categorical distributions is normalized.
Returns True if all distributions integrate to 1.0

---

## pymdp.utils.is_obj_array

**Arguments:** (arr)

---

## pymdp.utils.norm_dist

**Arguments:** (dist)

**Description:**
Normalizes a Categorical probability distribution (or set of them) assuming sufficient statistics are stored in leading dimension

---

## pymdp.utils.norm_dist_obj_arr

**Arguments:** (obj_arr)

**Description:**
Normalizes a multi-factor or -modality collection of Categorical probability distributions, assuming sufficient statistics of each conditional distribution
are stored in the leading dimension

---

## pymdp.utils.obj_array

**Arguments:** (num_arr)

**Description:**
Creates a generic object array with the desired number of sub-arrays, given by `num_arr`

---

## pymdp.utils.obj_array_from_list

**Arguments:** (list_input)

**Description:**
Takes a list of `numpy.ndarray` and converts them to a `numpy.ndarray` of `dtype = object`

---

## pymdp.utils.obj_array_ones

**Arguments:** (shape_list, scale=1.0)

---

## pymdp.utils.obj_array_uniform

**Arguments:** (shape_list)

**Description:**
Creates a numpy object array whose sub-arrays are uniform Categorical
distributions with shapes given by shape_list[i]. The shapes (elements of shape_list)
can either be tuples or lists.

---

## pymdp.utils.obj_array_zeros

**Arguments:** (shape_list)

**Description:**
Creates a numpy object array whose sub-arrays are 1-D vectors
filled with zeros, with shapes given by shape_list[i]

---

## pymdp.utils.onehot

**Arguments:** (value, num_values)

---

## pymdp.utils.plot_beliefs

**Arguments:** (belief_dist, title='')

**Description:**
Utility function that plots a bar chart of a categorical probability distribution,
with each bar height corresponding to the probability of one of the elements of the categorical
probability vector.

---

## pymdp.utils.plot_likelihood

**Arguments:** (A, title='')

**Description:**
Utility function that shows a heatmap of a 2-D likelihood (hidden causes in the columns, observations in the rows),
with hotter colors indicating higher probability.

---

## pymdp.utils.process_observation

**Arguments:** (obs, num_modalities, num_observations)

**Description:**
Helper function for formatting observations    
USAGE NOTES:
- If `obs` is a 1D numpy array, it must be a one-hot vector, where one entry (the entry of the observation) is 1.0 
and all other entries are 0. This therefore assumes it's a single modality observation. If these conditions are met, then
this function will return `obs` unchanged. Otherwise, it'll throw an error.
- If `obs` is an int, it assumes this is a single modality observation, whose observation index is given by the value of `obs`. This function will convert
it to be a one hot vector.
- If `obs` is a list, it assumes this is a multiple modality observation, whose len is equal to the number of observation modalities,
and where each entry `obs[m]` is the index of the observation, for that modality. This function will convert it into an object array
of one-hot vectors.
- If `obs` is a tuple, same logic as applies for list (see above).
- if `obs` is a numpy object array (array of arrays), this function will return `obs` unchanged.

---

## pymdp.utils.process_observation_seq

**Arguments:** (obs_seq, n_modalities, n_observations)

**Description:**
Helper function for formatting observations    

    Observations can either be `int` (converted to one-hot)
    or `tuple` (obs for each modality), or `list` (obs for each modality)
    If list, the entries could be object arrays of one-hots, in which
    case this function returns `obs_seq` as is.

---

## pymdp.utils.random_A_matrix

**Arguments:** (num_obs, num_states, A_factor_list=None)

---

## pymdp.utils.random_B_matrix

**Arguments:** (num_states, num_controls, B_factor_list=None)

---

## pymdp.utils.random_single_categorical

**Arguments:** (shape_list)

**Description:**
Creates a random 1-D categorical distribution (or set of 1-D categoricals, e.g. multiple marginals of different factors) and returns them in an object array 

---

## pymdp.utils.reduce_a_matrix

**Arguments:** (A)

**Description:**
Utility function for throwing away dimensions (lagging dimensions, hidden state factors)
of a particular A matrix that are independent of the observation. 
Parameters:
==========
- `A` [np.ndarray]:
    The A matrix or likelihood array that encodes probabilistic relationship
    of the generative model between hidden state factors (lagging dimensions, columns, slices, etc...)
    and observations (leading dimension, rows). 
Returns:
=========
- `A_reduced` [np.ndarray]:
    The reduced A matrix, missing the lagging dimensions that correspond to hidden state factors
    that are statistically independent of observations
- `original_factor_idx` [list]:
    List of the indices (in terms of the original dimensionality) of the hidden state factors
    that are maintained in the A matrix (and thus have an informative / non-degenerate relationship to observations

---

## pymdp.utils.sample

**Arguments:** (probabilities)

---

## pymdp.utils.sample_obj_array

**Arguments:** (arr)

**Description:**
Sample from set of Categorical distributions, stored in the sub-arrays of an object array 

---

## pymdp.utils.to_obj_array

**Arguments:** (arr)

---

