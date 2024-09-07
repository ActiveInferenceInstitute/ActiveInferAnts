# All utility functions and classes from pymdp

class TestSPM(unittest.TestCase):
    
    def test_active_inference_SPM_1a(self):
        """
        Test against output of SPM_MDP_VB_X.m
        1A - one hidden state factor, one observation modality, backwards horizon = 3, policy_len = 1, policy-conditional prior
        """
        array_path = os.path.join(os.getcwd(), DATA_PATH + "vbx_test_1a.mat")
        mat_contents = loadmat(file_name=array_path)

        A = mat_contents["A"][0]
        B = mat_contents["B"][0]
        C = to_obj_array(mat_contents["C"][0][0][:,0])
        obs_matlab = mat_contents["obs"].astype("int64")
        policy = mat_contents["policies"].astype("int64") - 1
        t_horizon = mat_contents["t_horizon"][0, 0].astype("int64")
        actions_matlab = mat_contents["actions"].astype("int64") - 1
        qs_matlab = mat_contents["qs"][0]
        xn_matlab = mat_contents["xn"][0]
        vn_matlab = mat_contents["vn"][0]

        likelihoods_matlab = mat_contents["likelihoods"][0]

        num_obs, num_states, _, num_factors = get_model_dimensions(A, B)
        obs = convert_observation_array(obs_matlab, num_obs)
        T = len(obs)

        agent = Agent(A=A, B=B, C=C, inference_algo="MMP", policy_len=1, 
                        inference_horizon=t_horizon, use_BMA = False, 
                        policy_sep_prior = True)
        
        actions_python = np.zeros(T)

        for t in range(T):
            o_t = (np.where(obs[t])[0][0],)
            qx, xn_t, vn_t = agent._infer_states_test(o_t)
            q_pi, G= agent.infer_policies()
            action = agent.sample_action()

            actions_python[t] = action.item()

            xn_python = build_xn_vn_array(xn_t)
            vn_python = build_xn_vn_array(vn_t)

            if t == T-1:
                xn_python = xn_python[:,:,:-1,:]
                vn_python = vn_python[:,:,:-1,:]

            start_tstep = max(0, agent.curr_timestep - agent.inference_horizon)
            end_tstep = min(agent.curr_timestep + agent.policy_len, T)

            xn_validation = xn_matlab[0][:,:,start_tstep:end_tstep,t,:]
            vn_validation = vn_matlab[0][:,:,start_tstep:end_tstep,t,:]

            self.assertTrue(np.isclose(xn_python, xn_validation).all())
            self.assertTrue(np.isclose(vn_python, vn_validation).all())
        
        self.assertTrue(np.isclose(actions_matlab[0,:],actions_python[:-1]).all())

    def test_BMR_SPM_a(self):
        """
        Validate output of pymdp's `dirichlet_log_evidence` function 
        against output of `spm_MDP_log_evidence` from DEM in SPM (MATLAB)
        Test `a` tests the log evidence calculations across for a single
        reduced model, stored in a vector `r_dir`
        """
        array_path = os.path.join(os.getcwd(), DATA_PATH + "bmr_test_a.mat")
        mat_contents = loadmat(file_name=array_path)
        F_valid = mat_contents["F"]

        # create BMR example from MATLAB
        x = np.linspace(1, 32, 128)

        p_dir    = np.ones(2)
        r_dir    = p_dir.copy()
        r_dir[1] = 8.

        F_out = np.zeros( (len(x), len(x)) )
        for i in range(len(x)):
            for j in range(len(x)):
                q_dir = np.array([x[i], x[j]])
                F_out[i,j] = dirichlet_log_evidence(q_dir, p_dir, r_dir)[0]

        self.assertTrue(np.allclose(F_valid, F_out))

    def test_BMR_SPM_b(self):
        """
        Validate output of pymdp's `dirichlet_log_evidence` function 
        against output of `spm_MDP_log_evidence` from DEM in SPM (MATLAB). 
        Test `b` vectorizes the log evidence calculations across a _matrix_ of 
        reduced models, with one reduced model prior per column of the argument `r_dir`
        """
        array_path = os.path.join(os.getcwd(), DATA_PATH + "bmr_test_b.mat")
        mat_contents = loadmat(file_name=array_path)
        F_valid = mat_contents["F"]
        s_dir_valid = mat_contents['s_dir']
        q_dir = mat_contents["q_dir"]
        p_dir = mat_contents["p_dir"]
        r_dir = mat_contents["r_dir"]
        
        F_out, s_dir_out = dirichlet_log_evidence(q_dir, p_dir, r_dir)

        self.assertTrue(np.allclose(F_valid, F_out))

        self.assertTrue(np.allclose(s_dir_valid, s_dir_out))

def test_active_inference_SPM_1a(self):
        """
        Test against output of SPM_MDP_VB_X.m
        1A - one hidden state factor, one observation modality, backwards horizon = 3, policy_len = 1, policy-conditional prior
        """
        array_path = os.path.join(os.getcwd(), DATA_PATH + "vbx_test_1a.mat")
        mat_contents = loadmat(file_name=array_path)

        A = mat_contents["A"][0]
        B = mat_contents["B"][0]
        C = to_obj_array(mat_contents["C"][0][0][:,0])
        obs_matlab = mat_contents["obs"].astype("int64")
        policy = mat_contents["policies"].astype("int64") - 1
        t_horizon = mat_contents["t_horizon"][0, 0].astype("int64")
        actions_matlab = mat_contents["actions"].astype("int64") - 1
        qs_matlab = mat_contents["qs"][0]
        xn_matlab = mat_contents["xn"][0]
        vn_matlab = mat_contents["vn"][0]

        likelihoods_matlab = mat_contents["likelihoods"][0]

        num_obs, num_states, _, num_factors = get_model_dimensions(A, B)
        obs = convert_observation_array(obs_matlab, num_obs)
        T = len(obs)

        agent = Agent(A=A, B=B, C=C, inference_algo="MMP", policy_len=1, 
                        inference_horizon=t_horizon, use_BMA = False, 
                        policy_sep_prior = True)
        
        actions_python = np.zeros(T)

        for t in range(T):
            o_t = (np.where(obs[t])[0][0],)
            qx, xn_t, vn_t = agent._infer_states_test(o_t)
            q_pi, G= agent.infer_policies()
            action = agent.sample_action()

            actions_python[t] = action.item()

            xn_python = build_xn_vn_array(xn_t)
            vn_python = build_xn_vn_array(vn_t)

            if t == T-1:
                xn_python = xn_python[:,:,:-1,:]
                vn_python = vn_python[:,:,:-1,:]

            start_tstep = max(0, agent.curr_timestep - agent.inference_horizon)
            end_tstep = min(agent.curr_timestep + agent.policy_len, T)

            xn_validation = xn_matlab[0][:,:,start_tstep:end_tstep,t,:]
            vn_validation = vn_matlab[0][:,:,start_tstep:end_tstep,t,:]

            self.assertTrue(np.isclose(xn_python, xn_validation).all())
            self.assertTrue(np.isclose(vn_python, vn_validation).all())
        
        self.assertTrue(np.isclose(actions_matlab[0,:],actions_python[:-1]).all())

def test_BMR_SPM_a(self):
        """
        Validate output of pymdp's `dirichlet_log_evidence` function 
        against output of `spm_MDP_log_evidence` from DEM in SPM (MATLAB)
        Test `a` tests the log evidence calculations across for a single
        reduced model, stored in a vector `r_dir`
        """
        array_path = os.path.join(os.getcwd(), DATA_PATH + "bmr_test_a.mat")
        mat_contents = loadmat(file_name=array_path)
        F_valid = mat_contents["F"]

        # create BMR example from MATLAB
        x = np.linspace(1, 32, 128)

        p_dir    = np.ones(2)
        r_dir    = p_dir.copy()
        r_dir[1] = 8.

        F_out = np.zeros( (len(x), len(x)) )
        for i in range(len(x)):
            for j in range(len(x)):
                q_dir = np.array([x[i], x[j]])
                F_out[i,j] = dirichlet_log_evidence(q_dir, p_dir, r_dir)[0]

        self.assertTrue(np.allclose(F_valid, F_out))

def test_BMR_SPM_b(self):
        """
        Validate output of pymdp's `dirichlet_log_evidence` function 
        against output of `spm_MDP_log_evidence` from DEM in SPM (MATLAB). 
        Test `b` vectorizes the log evidence calculations across a _matrix_ of 
        reduced models, with one reduced model prior per column of the argument `r_dir`
        """
        array_path = os.path.join(os.getcwd(), DATA_PATH + "bmr_test_b.mat")
        mat_contents = loadmat(file_name=array_path)
        F_valid = mat_contents["F"]
        s_dir_valid = mat_contents['s_dir']
        q_dir = mat_contents["q_dir"]
        p_dir = mat_contents["p_dir"]
        r_dir = mat_contents["r_dir"]
        
        F_out, s_dir_out = dirichlet_log_evidence(q_dir, p_dir, r_dir)

        self.assertTrue(np.allclose(F_valid, F_out))

        self.assertTrue(np.allclose(s_dir_valid, s_dir_out))

class TestAgent(unittest.TestCase):
    
    def test_agent_init_without_control_fac_idx(self):
        """
        Initialize instance of the agent class and pass in a custom `control_fac_idx`
        """

        num_obs = [2, 4]
        num_states = [2, 2]
        num_controls = [2, 2]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B)

        self.assertEqual(agent.num_controls[0], 2)
        self.assertEqual(agent.num_controls[1], 2)

        self.assertEqual([0, 1], agent.control_fac_idx)

    def test_reset_agent_VANILLA(self):
        """
        Ensure the `reset` method of Agent() using the new refactor is working as intended, 
        using the `VANILLA` argument to `inference_algo` 
        """

        num_obs = [2, 4]
        num_states = [2, 3]
        num_controls = [2, 3]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, inference_algo = "VANILLA")

        init_qs = utils.obj_array_uniform(agent.num_states)
        self.assertTrue(all( [ (agent.qs[f] == init_qs[f]).all() for f in range(agent.num_factors)]) )
        self.assertTrue(agent.curr_timestep == 0)

    def test_reset_agent_MMP_wBMA(self):
        """
        Ensure the `reset` method of Agent() using the new refactor is working as intended, 
        using the `MMP` argument to `inference_algo`, and `use_BMA` equal to True
        """

        num_obs = [2, 4]
        num_states = [2, 3]
        num_controls = [2, 3]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, inference_algo = "MMP", use_BMA=True)

        self.assertEqual(len(agent.latest_belief), agent.num_factors)
        self.assertTrue(all( [ (agent.latest_belief[f] == agent.D[f]).all() for f in range(agent.num_factors)]) )
        self.assertTrue(agent.curr_timestep == 0)
    
    def test_reset_agent_MMP_wPSP(self):
        """
        Ensure the `reset` method of Agent() using the new refactor is working as intended, 
        using the `MMP` argument to `inference_algo`, and `policy-separated prior` equal to True
        """

        num_obs = [2, 4]
        num_states = [2, 3]
        num_controls = [2, 3]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, inference_algo = "MMP", use_BMA = False, policy_sep_prior = True)

        self.assertEqual(len(agent.qs[0]) - agent.inference_horizon - 1, agent.policy_len)
    
    def test_agent_infer_states(self):
        """
        Test `infer_states` method of the Agent() class
        """

        ''' VANILLA method (fixed point iteration) with one hidden state factor and one observation modality '''
        num_obs = [5]
        num_states = [3]
        num_controls = [1]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, inference_algo = "VANILLA")

        o = tuple([np.random.randint(obs_dim) for obs_dim in num_obs])
        qs_out = agent.infer_states(o)

        qs_validation = inference.update_posterior_states(A, o, prior=agent.D)

        for f in range(len(num_states)):
            self.assertTrue(np.isclose(qs_validation[f], qs_out[f]).all())

        ''' VANILLA method (fixed point iteration) with multiple hidden state factors and multiple observation modalities '''
        num_obs = [2, 4]
        num_states = [2, 3]
        num_controls = [2, 3]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, inference_algo = "VANILLA")

        o = tuple([np.random.randint(obs_dim) for obs_dim in num_obs])
        qs_out = agent.infer_states(o)

        qs_validation = inference.update_posterior_states(A, o, prior=agent.D)

        for f in range(len(num_states)):
            self.assertTrue(np.isclose(qs_validation[f], qs_out[f]).all())

        ''' Marginal message passing inference with one hidden state factor and one observation modality '''
        num_obs = [5]
        num_states = [3]
        num_controls = [1]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, inference_algo = "MMP")

        o = tuple([np.random.randint(obs_dim) for obs_dim in num_obs])
        qs_pi_out = agent.infer_states(o)

        policies = control.construct_policies(num_states, num_controls, policy_len = 1)

        qs_pi_validation, _ = inference.update_posterior_states_full(A, B, [o], policies, prior = agent.D, policy_sep_prior = False)

        for p_idx in range(len(policies)):
            for f in range(len(num_states)):
                self.assertTrue(np.isclose(qs_pi_validation[p_idx][0][f], qs_pi_out[p_idx][0][f]).all())

        ''' Marginal message passing inference with multiple hidden state factors and multiple observation modalities '''
        num_obs = [2, 4]
        num_states = [2, 2]
        num_controls = [2, 2]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls) 

        planning_horizon = 3
        backwards_horizon = 1
        agent = Agent(A=A, B=B, inference_algo="MMP", policy_len=planning_horizon, inference_horizon=backwards_horizon)
        o = [0, 2]
        qs_pi_out = agent.infer_states(o)

        policies = control.construct_policies(num_states, num_controls, policy_len = planning_horizon)

        qs_pi_validation, _ = inference.update_posterior_states_full_factorized(A, agent.mb_dict, B, agent.B_factor_list, [o], policies, prior = agent.D, policy_sep_prior = False)

        for p_idx in range(len(policies)):
            for t in range(planning_horizon+backwards_horizon):
                for f in range(len(num_states)):
                    self.assertTrue(np.isclose(qs_pi_validation[p_idx][t][f], qs_pi_out[p_idx][t][f]).all())

    def test_mmp_active_inference(self):
        """
        Tests to make sure whole active inference loop works (with various past and future
        inference/policy horizons).
        """

        num_obs = [3, 2]
        num_states = [4, 3]
        num_controls = [1, 3]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        C = utils.obj_array_zeros(num_obs)
        C[1][0] = 1.0  
        C[1][1] = -2.0  

        agent = Agent(A=A, B=B, C=C, control_fac_idx=[1], inference_algo="MMP", policy_len=2, inference_horizon=3)

        T = 10

        for t in range(T):

            o = [np.random.randint(num_ob) for num_ob in num_obs] # just randomly generate observations at each timestep, no generative process
            qx = agent.infer_states(o)
            agent.infer_policies()
            action = agent.sample_action()
        
        self.assertEqual(len(agent.prev_obs), T)
        self.assertEqual(len(agent.prev_actions), T)

    def test_agent_with_A_learning_vanilla(self):
        """ Unit test for updating prior Dirichlet parameters over likelihood model (pA) with the ``Agent`` class,
        in the case that you're using "vanilla" inference mode.
        """

        # 3 x 3, 2-dimensional grid world
        num_obs = [9]
        num_states = [9]
        num_controls = [4]

        A = utils.obj_array_zeros([ [num_obs[0], num_states[0]] ])
        A[0] = np.eye(num_obs[0])

        pA = utils.dirichlet_like(A, scale=1.)

        action_labels = ["LEFT", "DOWN", "RIGHT", "UP"]

        # get some true transition dynamics
        true_transition_matrix = generate_grid_world_transitions(action_labels, num_rows = 3, num_cols = 3)
        B = utils.to_obj_array(true_transition_matrix)
        
        # instantiate the agent
        learning_rate_pA = np.random.rand()
        agent = Agent(A=A, B=B, pA=pA, inference_algo="VANILLA", action_selection="stochastic", lr_pA=learning_rate_pA)

        # time horizon
        T = 10
        next_state = 0

        for t in range(T):
            
            prev_state = next_state
            o = [prev_state] 
            qx = agent.infer_states(o)
            agent.infer_policies()
            agent.sample_action()

            # sample the next state given the true transition dynamics and the sampled action
            next_state = utils.sample(true_transition_matrix[:,prev_state,int(agent.action[0])])
            
            # compute the predicted update to the action-conditioned slice of qB
            predicted_update = agent.pA[0] + learning_rate_pA*maths.spm_cross(utils.onehot(o[0], num_obs[0]), qx[0])
            qA = agent.update_A(o) # update qA using the agent function

            # check if the predicted update and the actual update are the same
            self.assertTrue(np.allclose(predicted_update, qA[0]))
    
    def test_agent_with_A_learning_vanilla_factorized(self):
        """ Unit test for updating prior Dirichlet parameters over likelihood model (pA) with the ``Agent`` class,
        in the case that you're using "vanilla" inference mode. In this case, we encode sparse conditional dependencies by specifying
        a non-all-to-all `A_factor_list`, that specifies the subset of hidden state factors that different modalities depend on.
        """

        num_obs = [5, 4, 3]
        num_states = [9, 8, 2, 4]
        num_controls = [2, 2, 1, 1]

        A_factor_list = [[0, 1], [0, 2], [3]]

        A = utils.random_A_matrix(num_obs, num_states, A_factor_list=A_factor_list)
        pA = utils.dirichlet_like(A, scale=1.)

        B = utils.random_B_matrix(num_states, num_controls)
        
        # instantiate the agent
        learning_rate_pA = np.random.rand()
        agent = Agent(A=A, B=B, pA=pA, A_factor_list=A_factor_list, inference_algo="VANILLA", action_selection="stochastic", lr_pA=learning_rate_pA)

        # time horizon
        T = 10

        obs_seq = []
        for t in range(T):
            obs_seq.append([np.random.randint(obs_dim) for obs_dim in num_obs])
        
        for t in range(T):
            print(t)
            
            qx = agent.infer_states(obs_seq[t])
            agent.infer_policies()
            agent.sample_action()
            
            # compute the predicted update to the action-conditioned slice of qB
            qA_valid = utils.obj_array_zeros([A_m.shape for A_m in A])
            for m, pA_m in enumerate(agent.pA):
                qA_valid[m] = pA_m + learning_rate_pA*maths.spm_cross(utils.onehot(obs_seq[t][m], num_obs[m]), qx[A_factor_list[m]])
            qA_test = agent.update_A(obs_seq[t]) # update qA using the agent function

            # check if the predicted update and the actual update are the same
            for m, qA_valid_m in enumerate(qA_valid):
                self.assertTrue(np.allclose(qA_valid_m, qA_test[m]))

    def test_agent_with_B_learning_vanilla(self):
        """ Unit test for updating prior Dirichlet parameters over transition model (pB) with the ``Agent`` class,
        in the case that you're using "vanilla" inference mode.
        """

        # 3 x 3, 2-dimensional grid world
        num_obs = [9]
        num_states = [9]
        num_controls = [4]

        A = utils.obj_array_zeros([ [num_obs[0], num_states[0]] ])
        A[0] = np.eye(num_obs[0])

        action_labels = ["LEFT", "DOWN", "RIGHT", "UP"]

        # flat transition prior
        pB = utils.obj_array_ones([[num_states[0], num_states[0], num_controls[0]]])
        B = utils.norm_dist_obj_arr(pB)
        
        # instantiate the agent
        learning_rate_pB = 2.0
        agent = Agent(A = A, B = B, pB = pB, inference_algo="VANILLA", save_belief_hist = True, action_selection="stochastic", lr_pB= learning_rate_pB)

        # get some true transition dynamics
        true_transition_matrix = generate_grid_world_transitions(action_labels, num_rows = 3, num_cols = 3)

        # time horizon
        T = 10
        next_state = 0

        for t in range(T):
            
            prev_state = next_state
            o = [prev_state] 
            qx = agent.infer_states(o)
            agent.infer_policies()
            agent.sample_action()

            # sample the next state given the true transition dynamics and the sampled action
            next_state = utils.sample(true_transition_matrix[:,prev_state,int(agent.action[0])])

            if t > 0:
                
                # compute the predicted update to the action-conditioned slice of qB
                predicted_update = agent.pB[0][:,:,int(agent.action[0])] + learning_rate_pB * maths.spm_cross(agent.qs_hist[-1][0], agent.qs_hist[-2][0])
                qB = agent.update_B(qs_prev = agent.qs_hist[-2]) # update qB using the agent function

                # check if the predicted update and the actual update are the same
                self.assertTrue(np.allclose(predicted_update, qB[0][:,:,int(agent.action[0])]))
    
    def test_agent_with_D_learning_vanilla(self):
        """
        Test updating prior Dirichlet parameters over initial hidden states (pD) with the ``Agent`` class,
        in the case that you're using "vanilla" inference mode.
        """

        num_obs = [2, 4]
        num_states = [2, 3]
        num_controls = [1, 1] # HMM mode
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        pD = utils.dirichlet_like(utils.random_single_categorical(num_states))

        # 1. Test that the updating works when `save_belief_hist` is True, and you don't need to pass in the beliefs about first hidden states
        agent = Agent(A=A, B=B, pD = pD, inference_algo = "VANILLA", save_belief_hist=True)

        T = 10

        qs_history = []

        for t in range(T):

            # get some random hidden state distribution
            p_states = utils.random_single_categorical(num_states)
            observation = [utils.sample(maths.spm_dot(A_g, p_states)) for A_g in A]

            qs_t = agent.infer_states(observation)

            qs_history.append(qs_t)

        pD_validation = learning.update_state_prior_dirichlet(agent.pD, qs_history[0], agent.lr_pD, factors = agent.factors_to_learn)

        pD_test = agent.update_D()

        for factor in range(len(num_states)):

            self.assertTrue(np.allclose(pD_test[factor], pD_validation[factor]))
        
        # 2. Test that the updating works when `save_belief_hist` is False, and you do have to pass in the beliefs about first hidden states
        agent = Agent(A=A, B=B, pD = pD, inference_algo = "VANILLA", save_belief_hist=False)

        T = 10

        qs_history = []

        for t in range(T):

            # get some random hidden state distribution
            p_states = utils.random_single_categorical(num_states)
            observation = [utils.sample(maths.spm_dot(A_g, p_states)) for A_g in A]

            qs_t = agent.infer_states(observation)

            qs_history.append(qs_t)

        pD_validation = learning.update_state_prior_dirichlet(agent.pD, qs_history[0], agent.lr_pD, factors = agent.factors_to_learn)

        pD_test = agent.update_D(qs_t0=qs_history[0])

        for factor in range(len(num_states)):

            self.assertTrue(np.allclose(pD_test[factor], pD_validation[factor]))
        
        # 3. Same as test #1, except with learning on only certain hidden state factors. Also passed in a different learning rate
        agent = Agent(A=A, B=B, pD = pD, lr_pD = 2.0, inference_algo = "VANILLA", save_belief_hist=True, factors_to_learn= [0])

        T = 10

        qs_history = []

        for t in range(T):

            # get some random hidden state distribution
            p_states = utils.random_single_categorical(num_states)
            observation = [utils.sample(maths.spm_dot(A_g, p_states)) for A_g in A]

            qs_t = agent.infer_states(observation)

            qs_history.append(qs_t)

        pD_validation = learning.update_state_prior_dirichlet(agent.pD, qs_history[0], agent.lr_pD, factors = agent.factors_to_learn)

        pD_test = agent.update_D()

        for factor in range(len(num_states)):

            self.assertTrue(np.allclose(pD_test[factor], pD_validation[factor]))
    
    def test_agent_with_D_learning_MMP(self):
        """
        Test updating prior Dirichlet parameters over initial hidden states (pD) with the agent class,
        in the case that you're using MMP inference and various combinations of Bayesian model averaging at the edge of the inference horizon vs. other possibilities
        """

        num_obs = [2]
        num_states = [2, 3, 3]
        num_controls = [2, 3, 1]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        pD = utils.dirichlet_like(utils.random_single_categorical(num_states))

        # 1. Using Bayesian model average over hidden states at the edge of the inference horizon
        agent = Agent(A=A, B=B, pD = pD, inference_algo = "MMP", use_BMA = True, policy_sep_prior = False, inference_horizon = 10, save_belief_hist = True)

        T = 10

        for t in range(T):

            # get some random hidden state distribution
            p_states = utils.random_single_categorical(num_states)
            observation = [utils.sample(maths.spm_dot(A_g, p_states)) for A_g in A]

            agent.infer_states(observation)
            agent.infer_policies()
            agent.sample_action()

        qs_t0 = agent.latest_belief

        pD_validation = learning.update_state_prior_dirichlet(pD, qs_t0, agent.lr_pD, factors = agent.factors_to_learn)

        pD_test = agent.update_D()

        for factor in range(len(num_states)):

            self.assertTrue(np.allclose(pD_test[factor], pD_validation[factor]))

        # 2. Using policy-conditioned prior over hidden states at the edge of the inference horizon
        agent = Agent(A=A, B=B, pD = pD, inference_algo = "MMP", use_BMA = False, policy_sep_prior = True, inference_horizon = 10, save_belief_hist = True)

        T = 10

        q_pi_hist = []
        for t in range(T):

            # get some random hidden state distribution
            p_states = utils.random_single_categorical(num_states)
            observation = [utils.sample(maths.spm_dot(A_g, p_states)) for A_g in A]

            qs_final = agent.infer_states(observation)
            q_pi, _ = agent.infer_policies()
            q_pi_hist.append(q_pi)
            agent.sample_action()

        # get beliefs about policies at the time at the beginning of the inference horizon
        
        qs_pi_t0 = utils.obj_array(len(agent.policies))
        for p_i in range(len(qs_pi_t0)):
            qs_pi_t0[p_i] = qs_final[p_i][0]

        qs_t0 = inference.average_states_over_policies(qs_pi_t0,q_pi_hist[0]) # beliefs about hidden states at the first timestep of the inference horizon
     
        pD_validation = learning.update_state_prior_dirichlet(pD, qs_t0, agent.lr_pD, factors = agent.factors_to_learn)

        pD_test = agent.update_D()

        for factor in range(len(num_states)):

            self.assertTrue(np.allclose(pD_test[factor], pD_validation[factor]))
    
    def test_agent_with_input_alpha(self):
        """
        Test for passing in `alpha` (action sampling precision parameter) as argument to `agent.Agent()` constructor.
        Test two cases to make sure alpha scaling is working properly, by comparing entropies of action marginals 
        after computing posterior over actions in cases where alpha is passed in as two different values to the Agent constructor.
        """

        num_obs = [2]
        num_states = [2]
        num_controls = [2]
        A = utils.to_obj_array(np.eye(num_obs[0], num_states[0]))
        B = utils.construct_controllable_B(num_states, num_controls)
        C = utils.to_obj_array(np.array([1.01, 1.0]))

        agent = Agent(A=A, B=B, C=C, alpha = 16.0, action_selection = "stochastic")
        agent.infer_states(([0]))
        agent.infer_policies()
        chosen_action, p_actions1 = agent._sample_action_test()

        agent = Agent(A=A, B=B, C=C, alpha = 0.0, action_selection = "stochastic")
        agent.infer_states(([0]))
        agent.infer_policies()
        chosen_action, p_actions2 = agent._sample_action_test()

        entropy_p_actions1 = -maths.spm_log_single(p_actions1[0]).dot(p_actions1[0])
        entropy_p_actions2 = -maths.spm_log_single(p_actions2[0]).dot(p_actions2[0])

        self.assertGreater(entropy_p_actions2, entropy_p_actions1)
    
    def test_agent_with_sampling_mode(self):
        """
        Test for passing in `sampling_mode` argument to `agent.Agent()` constructor, which determines whether you sample
        from posterior marginal over actions ("marginal", default) or posterior over policies ("full")
        """

        num_obs = [2]
        num_states = [2]
        num_controls = [2]
        A = utils.to_obj_array(np.eye(num_obs[0], num_states[0]))
        B = utils.construct_controllable_B(num_states, num_controls)
        C = utils.to_obj_array(np.array([1.01, 1.0]))

        agent = Agent(A=A, B=B, C=C, alpha = 16.0, sampling_mode = "full", action_selection = "stochastic")
        agent.infer_states(([0]))
        agent.infer_policies()
        chosen_action, p_policies = agent._sample_action_test()
        self.assertEqual(len(p_policies), len(agent.q_pi))

        agent = Agent(A=A, B=B, C=C, alpha = 16.0, sampling_mode = "full", action_selection = "deterministic")
        agent.infer_states(([0]))
        agent.infer_policies()
        chosen_action, p_policies = agent._sample_action_test()
        self.assertEqual(len(p_policies), len(agent.q_pi))

        agent = Agent(A=A, B=B, C=C, alpha = 16.0, sampling_mode = "marginal", action_selection = "stochastic")
        agent.infer_states(([0]))
        agent.infer_policies()
        chosen_action, p_actions = agent._sample_action_test()
        self.assertEqual(len(p_actions[0]), num_controls[0])

    def test_agent_with_stochastic_action_unidimensional_control(self):
        """
        Test stochastic action sampling in case that one of the control states is one-dimensional, within the agent
        method `sample_action()`.
        Due to a call to probabilities.squeeze() in an earlier version of utils.sample(), this was throwing an
        error due to the inability to use np.random.multinomial on an array with undefined length (an 'unsized' array)
        """
        
        num_obs = [2]
        num_states = [2, 2]
        num_controls = [2, 1]

        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, action_selection = "stochastic")
        agent.infer_policies()
        chosen_action = agent.sample_action()
        self.assertEqual(chosen_action[1], 0)

        agent = Agent(A=A, B=B, action_selection = "deterministic")
        agent.infer_policies()
        chosen_action = agent.sample_action()
        self.assertEqual(chosen_action[1], 0)
    
    def test_agent_distributional_obs(self):

        ''' VANILLA method (fixed point iteration) with one hidden state factor and one observation modality '''
        num_obs = [5]
        num_states = [3]
        num_controls = [1]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, inference_algo = "VANILLA")

        p_o = utils.obj_array_zeros(num_obs) # use a distributional observation
        # @NOTE: `utils.obj_array_from_list` will make a nested list of object arrays if you only put in a list with one vector!!! Makes me think we should remove utils.obj_array_from_list potentially
        p_o[0] = A[0][:,0]
        qs_out = agent.infer_states(p_o, distr_obs=True)

        qs_validation = inference.update_posterior_states(A, p_o, prior=agent.D)

        for f in range(len(num_states)):
            self.assertTrue(np.isclose(qs_validation[f], qs_out[f]).all())

        ''' VANILLA method (fixed point iteration) with multiple hidden state factors and multiple observation modalities '''
        num_obs = [2, 4]
        num_states = [2, 3]
        num_controls = [2, 3]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, inference_algo = "VANILLA")

        p_o = utils.obj_array_from_list([A[0][:,0,0], A[1][:,1,1]]) # use a distributional observation
        qs_out = agent.infer_states(p_o, distr_obs=True)

        qs_validation = inference.update_posterior_states(A, p_o, prior=agent.D)

        for f in range(len(num_states)):
            self.assertTrue(np.isclose(qs_validation[f], qs_out[f]).all())

        ''' Marginal message passing inference with one hidden state factor and one observation modality '''
        num_obs = [5]
        num_states = [3]
        num_controls = [1]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, inference_algo = "MMP")

        p_o = utils.obj_array_zeros(num_obs) # use a distributional observation
        # @NOTE: `utils.obj_array_from_list` will make a nested list of object arrays if you only put in a list with one vector!!! Makes me think we should remove utils.obj_array_from_list potentially
        p_o[0] = A[0][:,0]
        qs_pi_out = agent.infer_states(p_o, distr_obs=True)

        policies = control.construct_policies(num_states, num_controls, policy_len = 1)

        qs_pi_validation, _ = inference.update_posterior_states_full(A, B, [p_o], policies, prior = agent.D, policy_sep_prior = False)

        for p_idx in range(len(policies)):
            for f in range(len(num_states)):
                self.assertTrue(np.isclose(qs_pi_validation[p_idx][0][f], qs_pi_out[p_idx][0][f]).all())
        
        ''' Marginal message passing inference with multiple hidden state factors and multiple observation modalities '''
        num_obs = [2, 4]
        num_states = [2, 2]
        num_controls = [2, 2]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls) 

        planning_horizon = 3
        backwards_horizon = 1
        agent = Agent(A=A, B=B, inference_algo="MMP", policy_len=planning_horizon, inference_horizon=backwards_horizon)
        p_o = utils.obj_array_from_list([A[0][:,0,0], A[1][:,1,1]]) # use a distributional observation
        qs_pi_out = agent.infer_states(p_o, distr_obs=True)

        policies = control.construct_policies(num_states, num_controls, policy_len = planning_horizon)

        qs_pi_validation, _ = inference.update_posterior_states_full_factorized(A, agent.mb_dict, B, agent.B_factor_list, [p_o], policies, prior = agent.D, policy_sep_prior = False)

        for p_idx in range(len(policies)):
            for t in range(planning_horizon+backwards_horizon):
                for f in range(len(num_states)):
                    self.assertTrue(np.isclose(qs_pi_validation[p_idx][t][f], qs_pi_out[p_idx][t][f]).all())

    def test_agent_with_factorized_inference(self):
        """
        Test that an instance of the `Agent` class can be initialized with a provided `A_factor_list` and run the factorized inference algorithm. Validate
        against an equivalent `Agent` whose `A` matrix represents the full set of (redundant) conditional dependence relationships.
        """

        num_obs = [5, 4]
        num_states = [2, 3]
        num_controls = [2, 3]

        A_factor_list = [ [0], [1] ]
        A_reduced = utils.random_A_matrix(num_obs, num_states, A_factor_list)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A_reduced, B=B, A_factor_list=A_factor_list, inference_algo = "VANILLA")

        obs = [np.random.randint(obs_dim) for obs_dim in num_obs]

        qs_out = agent.infer_states(obs)

        A_full = utils.initialize_empty_A(num_obs, num_states)
        for m, A_m in enumerate(A_full):
            other_factors = list(set(range(len(num_states))) - set(A_factor_list[m])) # list of the factors that modality `m` does not depend on

            # broadcast or tile the reduced A matrix (`A_reduced`) along the dimensions of corresponding to `other_factors`
            expanded_dims = [num_obs[m]] + [1 if f in other_factors else ns for (f, ns) in enumerate(num_states)]
            tile_dims = [1] + [ns if f in other_factors else 1 for (f, ns) in enumerate(num_states)]
            A_full[m] = np.tile(A_reduced[m].reshape(expanded_dims), tile_dims)
        
        agent = Agent(A=A_full, B=B, inference_algo = "VANILLA")
        qs_validation = agent._infer_states_test(obs)

        for qs_out_f, qs_val_f in zip(qs_out, qs_validation):
            self.assertTrue(np.isclose(qs_out_f, qs_val_f).all())
    
    def test_agent_with_interactions_in_B(self):
        """
        Test that an instance of the `Agent` class can be initialized with a provided `B_factor_list` and run a time loop of active inferece
        """

        num_obs = [5, 4]
        num_states = [2, 3]
        num_controls = [2, 3]

        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent_test = Agent(A=A, B=B, B_factor_list=[[0], [1]])
        agent_val = Agent(A=A, B=B)

        obs_seq = []
        for t in range(5):
            obs_seq.append([np.random.randint(obs_dim) for obs_dim in num_obs])
        
        for t in range(5):
            qs_out = agent_test.infer_states(obs_seq[t])
            qs_val = agent_val._infer_states_test(obs_seq[t])
            for qs_out_f, qs_val_f in zip(qs_out, qs_val):
                self.assertTrue(np.isclose(qs_out_f, qs_val_f).all())
            
            agent_test.infer_policies()
            agent_val.infer_policies()

            agent_test.sample_action()
            agent_val.sample_action()
    
    def test_actinfloop_factorized(self):
        """
        Test that an instance of the `Agent` class can be initialized and run
        with the fully-factorized generative model functions (including policy inference)
        """

        num_obs = [5, 4, 4]
        num_states = [2, 3, 5]
        num_controls = [2, 3, 2]

        A_factor_list = [[0], [0, 1], [0, 1, 2]]
        B_factor_list = [[0], [0, 1], [1, 2]]
        A = utils.random_A_matrix(num_obs, num_states, A_factor_list=A_factor_list)
        B = utils.random_B_matrix(num_states, num_controls, B_factor_list=B_factor_list)

        agent = Agent(A=A, B=B, A_factor_list=A_factor_list, B_factor_list=B_factor_list, inference_algo="VANILLA")

        obs_seq = []
        for t in range(5):
            obs_seq.append([np.random.randint(obs_dim) for obs_dim in num_obs])
        
        for t in range(5):
            qs_out = agent.infer_states(obs_seq[t])
            agent.infer_policies()
            agent.sample_action()

        """ Test to make sure it works even when generative model sparsity is not taken advantage of """
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, inference_algo="VANILLA")

        obs_seq = []
        for t in range(5):
            obs_seq.append([np.random.randint(obs_dim) for obs_dim in num_obs])
        
        for t in range(5):
            qs_out = agent.infer_states(obs_seq[t])
            agent.infer_policies()
            agent.sample_action()
        
        """ Test with pA and pB learning & information gain """

        num_obs = [5, 4, 4]
        num_states = [2, 3, 5]
        num_controls = [2, 3, 2]

        A_factor_list = [[0], [0, 1], [0, 1, 2]]
        B_factor_list = [[0], [0, 1], [1, 2]]
        A = utils.random_A_matrix(num_obs, num_states, A_factor_list=A_factor_list)
        B = utils.random_B_matrix(num_states, num_controls, B_factor_list=B_factor_list)
        pA = utils.dirichlet_like(A)
        pB = utils.dirichlet_like(B)

        agent = Agent(A=A, pA=pA, B=B, pB=pB, save_belief_hist=True, use_param_info_gain=True, A_factor_list=A_factor_list, B_factor_list=B_factor_list, inference_algo="VANILLA")

        obs_seq = []
        for t in range(5):
            obs_seq.append([np.random.randint(obs_dim) for obs_dim in num_obs])
        
        for t in range(5):
            qs_out = agent.infer_states(obs_seq[t])
            agent.infer_policies()
            agent.sample_action()
            agent.update_A(obs_seq[t])
            if t > 0:
                agent.update_B(qs_prev = agent.qs_hist[-2])

def test_agent_init_without_control_fac_idx(self):
        """
        Initialize instance of the agent class and pass in a custom `control_fac_idx`
        """

        num_obs = [2, 4]
        num_states = [2, 2]
        num_controls = [2, 2]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B)

        self.assertEqual(agent.num_controls[0], 2)
        self.assertEqual(agent.num_controls[1], 2)

        self.assertEqual([0, 1], agent.control_fac_idx)

def test_reset_agent_VANILLA(self):
        """
        Ensure the `reset` method of Agent() using the new refactor is working as intended, 
        using the `VANILLA` argument to `inference_algo` 
        """

        num_obs = [2, 4]
        num_states = [2, 3]
        num_controls = [2, 3]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, inference_algo = "VANILLA")

        init_qs = utils.obj_array_uniform(agent.num_states)
        self.assertTrue(all( [ (agent.qs[f] == init_qs[f]).all() for f in range(agent.num_factors)]) )
        self.assertTrue(agent.curr_timestep == 0)

def test_reset_agent_MMP_wBMA(self):
        """
        Ensure the `reset` method of Agent() using the new refactor is working as intended, 
        using the `MMP` argument to `inference_algo`, and `use_BMA` equal to True
        """

        num_obs = [2, 4]
        num_states = [2, 3]
        num_controls = [2, 3]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, inference_algo = "MMP", use_BMA=True)

        self.assertEqual(len(agent.latest_belief), agent.num_factors)
        self.assertTrue(all( [ (agent.latest_belief[f] == agent.D[f]).all() for f in range(agent.num_factors)]) )
        self.assertTrue(agent.curr_timestep == 0)

def test_reset_agent_MMP_wPSP(self):
        """
        Ensure the `reset` method of Agent() using the new refactor is working as intended, 
        using the `MMP` argument to `inference_algo`, and `policy-separated prior` equal to True
        """

        num_obs = [2, 4]
        num_states = [2, 3]
        num_controls = [2, 3]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, inference_algo = "MMP", use_BMA = False, policy_sep_prior = True)

        self.assertEqual(len(agent.qs[0]) - agent.inference_horizon - 1, agent.policy_len)

def test_agent_infer_states(self):
        """
        Test `infer_states` method of the Agent() class
        """

        ''' VANILLA method (fixed point iteration) with one hidden state factor and one observation modality '''
        num_obs = [5]
        num_states = [3]
        num_controls = [1]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, inference_algo = "VANILLA")

        o = tuple([np.random.randint(obs_dim) for obs_dim in num_obs])
        qs_out = agent.infer_states(o)

        qs_validation = inference.update_posterior_states(A, o, prior=agent.D)

        for f in range(len(num_states)):
            self.assertTrue(np.isclose(qs_validation[f], qs_out[f]).all())

        ''' VANILLA method (fixed point iteration) with multiple hidden state factors and multiple observation modalities '''
        num_obs = [2, 4]
        num_states = [2, 3]
        num_controls = [2, 3]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, inference_algo = "VANILLA")

        o = tuple([np.random.randint(obs_dim) for obs_dim in num_obs])
        qs_out = agent.infer_states(o)

        qs_validation = inference.update_posterior_states(A, o, prior=agent.D)

        for f in range(len(num_states)):
            self.assertTrue(np.isclose(qs_validation[f], qs_out[f]).all())

        ''' Marginal message passing inference with one hidden state factor and one observation modality '''
        num_obs = [5]
        num_states = [3]
        num_controls = [1]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, inference_algo = "MMP")

        o = tuple([np.random.randint(obs_dim) for obs_dim in num_obs])
        qs_pi_out = agent.infer_states(o)

        policies = control.construct_policies(num_states, num_controls, policy_len = 1)

        qs_pi_validation, _ = inference.update_posterior_states_full(A, B, [o], policies, prior = agent.D, policy_sep_prior = False)

        for p_idx in range(len(policies)):
            for f in range(len(num_states)):
                self.assertTrue(np.isclose(qs_pi_validation[p_idx][0][f], qs_pi_out[p_idx][0][f]).all())

        ''' Marginal message passing inference with multiple hidden state factors and multiple observation modalities '''
        num_obs = [2, 4]
        num_states = [2, 2]
        num_controls = [2, 2]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls) 

        planning_horizon = 3
        backwards_horizon = 1
        agent = Agent(A=A, B=B, inference_algo="MMP", policy_len=planning_horizon, inference_horizon=backwards_horizon)
        o = [0, 2]
        qs_pi_out = agent.infer_states(o)

        policies = control.construct_policies(num_states, num_controls, policy_len = planning_horizon)

        qs_pi_validation, _ = inference.update_posterior_states_full_factorized(A, agent.mb_dict, B, agent.B_factor_list, [o], policies, prior = agent.D, policy_sep_prior = False)

        for p_idx in range(len(policies)):
            for t in range(planning_horizon+backwards_horizon):
                for f in range(len(num_states)):
                    self.assertTrue(np.isclose(qs_pi_validation[p_idx][t][f], qs_pi_out[p_idx][t][f]).all())

def test_mmp_active_inference(self):
        """
        Tests to make sure whole active inference loop works (with various past and future
        inference/policy horizons).
        """

        num_obs = [3, 2]
        num_states = [4, 3]
        num_controls = [1, 3]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        C = utils.obj_array_zeros(num_obs)
        C[1][0] = 1.0  
        C[1][1] = -2.0  

        agent = Agent(A=A, B=B, C=C, control_fac_idx=[1], inference_algo="MMP", policy_len=2, inference_horizon=3)

        T = 10

        for t in range(T):

            o = [np.random.randint(num_ob) for num_ob in num_obs] # just randomly generate observations at each timestep, no generative process
            qx = agent.infer_states(o)
            agent.infer_policies()
            action = agent.sample_action()
        
        self.assertEqual(len(agent.prev_obs), T)
        self.assertEqual(len(agent.prev_actions), T)

def test_agent_with_A_learning_vanilla(self):
        """ Unit test for updating prior Dirichlet parameters over likelihood model (pA) with the ``Agent`` class,
        in the case that you're using "vanilla" inference mode.
        """

        # 3 x 3, 2-dimensional grid world
        num_obs = [9]
        num_states = [9]
        num_controls = [4]

        A = utils.obj_array_zeros([ [num_obs[0], num_states[0]] ])
        A[0] = np.eye(num_obs[0])

        pA = utils.dirichlet_like(A, scale=1.)

        action_labels = ["LEFT", "DOWN", "RIGHT", "UP"]

        # get some true transition dynamics
        true_transition_matrix = generate_grid_world_transitions(action_labels, num_rows = 3, num_cols = 3)
        B = utils.to_obj_array(true_transition_matrix)
        
        # instantiate the agent
        learning_rate_pA = np.random.rand()
        agent = Agent(A=A, B=B, pA=pA, inference_algo="VANILLA", action_selection="stochastic", lr_pA=learning_rate_pA)

        # time horizon
        T = 10
        next_state = 0

        for t in range(T):
            
            prev_state = next_state
            o = [prev_state] 
            qx = agent.infer_states(o)
            agent.infer_policies()
            agent.sample_action()

            # sample the next state given the true transition dynamics and the sampled action
            next_state = utils.sample(true_transition_matrix[:,prev_state,int(agent.action[0])])
            
            # compute the predicted update to the action-conditioned slice of qB
            predicted_update = agent.pA[0] + learning_rate_pA*maths.spm_cross(utils.onehot(o[0], num_obs[0]), qx[0])
            qA = agent.update_A(o) # update qA using the agent function

            # check if the predicted update and the actual update are the same
            self.assertTrue(np.allclose(predicted_update, qA[0]))

def test_agent_with_A_learning_vanilla_factorized(self):
        """ Unit test for updating prior Dirichlet parameters over likelihood model (pA) with the ``Agent`` class,
        in the case that you're using "vanilla" inference mode. In this case, we encode sparse conditional dependencies by specifying
        a non-all-to-all `A_factor_list`, that specifies the subset of hidden state factors that different modalities depend on.
        """

        num_obs = [5, 4, 3]
        num_states = [9, 8, 2, 4]
        num_controls = [2, 2, 1, 1]

        A_factor_list = [[0, 1], [0, 2], [3]]

        A = utils.random_A_matrix(num_obs, num_states, A_factor_list=A_factor_list)
        pA = utils.dirichlet_like(A, scale=1.)

        B = utils.random_B_matrix(num_states, num_controls)
        
        # instantiate the agent
        learning_rate_pA = np.random.rand()
        agent = Agent(A=A, B=B, pA=pA, A_factor_list=A_factor_list, inference_algo="VANILLA", action_selection="stochastic", lr_pA=learning_rate_pA)

        # time horizon
        T = 10

        obs_seq = []
        for t in range(T):
            obs_seq.append([np.random.randint(obs_dim) for obs_dim in num_obs])
        
        for t in range(T):
            print(t)
            
            qx = agent.infer_states(obs_seq[t])
            agent.infer_policies()
            agent.sample_action()
            
            # compute the predicted update to the action-conditioned slice of qB
            qA_valid = utils.obj_array_zeros([A_m.shape for A_m in A])
            for m, pA_m in enumerate(agent.pA):
                qA_valid[m] = pA_m + learning_rate_pA*maths.spm_cross(utils.onehot(obs_seq[t][m], num_obs[m]), qx[A_factor_list[m]])
            qA_test = agent.update_A(obs_seq[t]) # update qA using the agent function

            # check if the predicted update and the actual update are the same
            for m, qA_valid_m in enumerate(qA_valid):
                self.assertTrue(np.allclose(qA_valid_m, qA_test[m]))

def test_agent_with_B_learning_vanilla(self):
        """ Unit test for updating prior Dirichlet parameters over transition model (pB) with the ``Agent`` class,
        in the case that you're using "vanilla" inference mode.
        """

        # 3 x 3, 2-dimensional grid world
        num_obs = [9]
        num_states = [9]
        num_controls = [4]

        A = utils.obj_array_zeros([ [num_obs[0], num_states[0]] ])
        A[0] = np.eye(num_obs[0])

        action_labels = ["LEFT", "DOWN", "RIGHT", "UP"]

        # flat transition prior
        pB = utils.obj_array_ones([[num_states[0], num_states[0], num_controls[0]]])
        B = utils.norm_dist_obj_arr(pB)
        
        # instantiate the agent
        learning_rate_pB = 2.0
        agent = Agent(A = A, B = B, pB = pB, inference_algo="VANILLA", save_belief_hist = True, action_selection="stochastic", lr_pB= learning_rate_pB)

        # get some true transition dynamics
        true_transition_matrix = generate_grid_world_transitions(action_labels, num_rows = 3, num_cols = 3)

        # time horizon
        T = 10
        next_state = 0

        for t in range(T):
            
            prev_state = next_state
            o = [prev_state] 
            qx = agent.infer_states(o)
            agent.infer_policies()
            agent.sample_action()

            # sample the next state given the true transition dynamics and the sampled action
            next_state = utils.sample(true_transition_matrix[:,prev_state,int(agent.action[0])])

            if t > 0:
                
                # compute the predicted update to the action-conditioned slice of qB
                predicted_update = agent.pB[0][:,:,int(agent.action[0])] + learning_rate_pB * maths.spm_cross(agent.qs_hist[-1][0], agent.qs_hist[-2][0])
                qB = agent.update_B(qs_prev = agent.qs_hist[-2]) # update qB using the agent function

                # check if the predicted update and the actual update are the same
                self.assertTrue(np.allclose(predicted_update, qB[0][:,:,int(agent.action[0])]))

def test_agent_with_D_learning_vanilla(self):
        """
        Test updating prior Dirichlet parameters over initial hidden states (pD) with the ``Agent`` class,
        in the case that you're using "vanilla" inference mode.
        """

        num_obs = [2, 4]
        num_states = [2, 3]
        num_controls = [1, 1] # HMM mode
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        pD = utils.dirichlet_like(utils.random_single_categorical(num_states))

        # 1. Test that the updating works when `save_belief_hist` is True, and you don't need to pass in the beliefs about first hidden states
        agent = Agent(A=A, B=B, pD = pD, inference_algo = "VANILLA", save_belief_hist=True)

        T = 10

        qs_history = []

        for t in range(T):

            # get some random hidden state distribution
            p_states = utils.random_single_categorical(num_states)
            observation = [utils.sample(maths.spm_dot(A_g, p_states)) for A_g in A]

            qs_t = agent.infer_states(observation)

            qs_history.append(qs_t)

        pD_validation = learning.update_state_prior_dirichlet(agent.pD, qs_history[0], agent.lr_pD, factors = agent.factors_to_learn)

        pD_test = agent.update_D()

        for factor in range(len(num_states)):

            self.assertTrue(np.allclose(pD_test[factor], pD_validation[factor]))
        
        # 2. Test that the updating works when `save_belief_hist` is False, and you do have to pass in the beliefs about first hidden states
        agent = Agent(A=A, B=B, pD = pD, inference_algo = "VANILLA", save_belief_hist=False)

        T = 10

        qs_history = []

        for t in range(T):

            # get some random hidden state distribution
            p_states = utils.random_single_categorical(num_states)
            observation = [utils.sample(maths.spm_dot(A_g, p_states)) for A_g in A]

            qs_t = agent.infer_states(observation)

            qs_history.append(qs_t)

        pD_validation = learning.update_state_prior_dirichlet(agent.pD, qs_history[0], agent.lr_pD, factors = agent.factors_to_learn)

        pD_test = agent.update_D(qs_t0=qs_history[0])

        for factor in range(len(num_states)):

            self.assertTrue(np.allclose(pD_test[factor], pD_validation[factor]))
        
        # 3. Same as test #1, except with learning on only certain hidden state factors. Also passed in a different learning rate
        agent = Agent(A=A, B=B, pD = pD, lr_pD = 2.0, inference_algo = "VANILLA", save_belief_hist=True, factors_to_learn= [0])

        T = 10

        qs_history = []

        for t in range(T):

            # get some random hidden state distribution
            p_states = utils.random_single_categorical(num_states)
            observation = [utils.sample(maths.spm_dot(A_g, p_states)) for A_g in A]

            qs_t = agent.infer_states(observation)

            qs_history.append(qs_t)

        pD_validation = learning.update_state_prior_dirichlet(agent.pD, qs_history[0], agent.lr_pD, factors = agent.factors_to_learn)

        pD_test = agent.update_D()

        for factor in range(len(num_states)):

            self.assertTrue(np.allclose(pD_test[factor], pD_validation[factor]))

def test_agent_with_D_learning_MMP(self):
        """
        Test updating prior Dirichlet parameters over initial hidden states (pD) with the agent class,
        in the case that you're using MMP inference and various combinations of Bayesian model averaging at the edge of the inference horizon vs. other possibilities
        """

        num_obs = [2]
        num_states = [2, 3, 3]
        num_controls = [2, 3, 1]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        pD = utils.dirichlet_like(utils.random_single_categorical(num_states))

        # 1. Using Bayesian model average over hidden states at the edge of the inference horizon
        agent = Agent(A=A, B=B, pD = pD, inference_algo = "MMP", use_BMA = True, policy_sep_prior = False, inference_horizon = 10, save_belief_hist = True)

        T = 10

        for t in range(T):

            # get some random hidden state distribution
            p_states = utils.random_single_categorical(num_states)
            observation = [utils.sample(maths.spm_dot(A_g, p_states)) for A_g in A]

            agent.infer_states(observation)
            agent.infer_policies()
            agent.sample_action()

        qs_t0 = agent.latest_belief

        pD_validation = learning.update_state_prior_dirichlet(pD, qs_t0, agent.lr_pD, factors = agent.factors_to_learn)

        pD_test = agent.update_D()

        for factor in range(len(num_states)):

            self.assertTrue(np.allclose(pD_test[factor], pD_validation[factor]))

        # 2. Using policy-conditioned prior over hidden states at the edge of the inference horizon
        agent = Agent(A=A, B=B, pD = pD, inference_algo = "MMP", use_BMA = False, policy_sep_prior = True, inference_horizon = 10, save_belief_hist = True)

        T = 10

        q_pi_hist = []
        for t in range(T):

            # get some random hidden state distribution
            p_states = utils.random_single_categorical(num_states)
            observation = [utils.sample(maths.spm_dot(A_g, p_states)) for A_g in A]

            qs_final = agent.infer_states(observation)
            q_pi, _ = agent.infer_policies()
            q_pi_hist.append(q_pi)
            agent.sample_action()

        # get beliefs about policies at the time at the beginning of the inference horizon
        
        qs_pi_t0 = utils.obj_array(len(agent.policies))
        for p_i in range(len(qs_pi_t0)):
            qs_pi_t0[p_i] = qs_final[p_i][0]

        qs_t0 = inference.average_states_over_policies(qs_pi_t0,q_pi_hist[0]) # beliefs about hidden states at the first timestep of the inference horizon
     
        pD_validation = learning.update_state_prior_dirichlet(pD, qs_t0, agent.lr_pD, factors = agent.factors_to_learn)

        pD_test = agent.update_D()

        for factor in range(len(num_states)):

            self.assertTrue(np.allclose(pD_test[factor], pD_validation[factor]))

def test_agent_with_input_alpha(self):
        """
        Test for passing in `alpha` (action sampling precision parameter) as argument to `agent.Agent()` constructor.
        Test two cases to make sure alpha scaling is working properly, by comparing entropies of action marginals 
        after computing posterior over actions in cases where alpha is passed in as two different values to the Agent constructor.
        """

        num_obs = [2]
        num_states = [2]
        num_controls = [2]
        A = utils.to_obj_array(np.eye(num_obs[0], num_states[0]))
        B = utils.construct_controllable_B(num_states, num_controls)
        C = utils.to_obj_array(np.array([1.01, 1.0]))

        agent = Agent(A=A, B=B, C=C, alpha = 16.0, action_selection = "stochastic")
        agent.infer_states(([0]))
        agent.infer_policies()
        chosen_action, p_actions1 = agent._sample_action_test()

        agent = Agent(A=A, B=B, C=C, alpha = 0.0, action_selection = "stochastic")
        agent.infer_states(([0]))
        agent.infer_policies()
        chosen_action, p_actions2 = agent._sample_action_test()

        entropy_p_actions1 = -maths.spm_log_single(p_actions1[0]).dot(p_actions1[0])
        entropy_p_actions2 = -maths.spm_log_single(p_actions2[0]).dot(p_actions2[0])

        self.assertGreater(entropy_p_actions2, entropy_p_actions1)

def test_agent_with_sampling_mode(self):
        """
        Test for passing in `sampling_mode` argument to `agent.Agent()` constructor, which determines whether you sample
        from posterior marginal over actions ("marginal", default) or posterior over policies ("full")
        """

        num_obs = [2]
        num_states = [2]
        num_controls = [2]
        A = utils.to_obj_array(np.eye(num_obs[0], num_states[0]))
        B = utils.construct_controllable_B(num_states, num_controls)
        C = utils.to_obj_array(np.array([1.01, 1.0]))

        agent = Agent(A=A, B=B, C=C, alpha = 16.0, sampling_mode = "full", action_selection = "stochastic")
        agent.infer_states(([0]))
        agent.infer_policies()
        chosen_action, p_policies = agent._sample_action_test()
        self.assertEqual(len(p_policies), len(agent.q_pi))

        agent = Agent(A=A, B=B, C=C, alpha = 16.0, sampling_mode = "full", action_selection = "deterministic")
        agent.infer_states(([0]))
        agent.infer_policies()
        chosen_action, p_policies = agent._sample_action_test()
        self.assertEqual(len(p_policies), len(agent.q_pi))

        agent = Agent(A=A, B=B, C=C, alpha = 16.0, sampling_mode = "marginal", action_selection = "stochastic")
        agent.infer_states(([0]))
        agent.infer_policies()
        chosen_action, p_actions = agent._sample_action_test()
        self.assertEqual(len(p_actions[0]), num_controls[0])

def test_agent_with_stochastic_action_unidimensional_control(self):
        """
        Test stochastic action sampling in case that one of the control states is one-dimensional, within the agent
        method `sample_action()`.
        Due to a call to probabilities.squeeze() in an earlier version of utils.sample(), this was throwing an
        error due to the inability to use np.random.multinomial on an array with undefined length (an 'unsized' array)
        """
        
        num_obs = [2]
        num_states = [2, 2]
        num_controls = [2, 1]

        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, action_selection = "stochastic")
        agent.infer_policies()
        chosen_action = agent.sample_action()
        self.assertEqual(chosen_action[1], 0)

        agent = Agent(A=A, B=B, action_selection = "deterministic")
        agent.infer_policies()
        chosen_action = agent.sample_action()
        self.assertEqual(chosen_action[1], 0)

def test_agent_distributional_obs(self):

        ''' VANILLA method (fixed point iteration) with one hidden state factor and one observation modality '''
        num_obs = [5]
        num_states = [3]
        num_controls = [1]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, inference_algo = "VANILLA")

        p_o = utils.obj_array_zeros(num_obs) # use a distributional observation
        # @NOTE: `utils.obj_array_from_list` will make a nested list of object arrays if you only put in a list with one vector!!! Makes me think we should remove utils.obj_array_from_list potentially
        p_o[0] = A[0][:,0]
        qs_out = agent.infer_states(p_o, distr_obs=True)

        qs_validation = inference.update_posterior_states(A, p_o, prior=agent.D)

        for f in range(len(num_states)):
            self.assertTrue(np.isclose(qs_validation[f], qs_out[f]).all())

        ''' VANILLA method (fixed point iteration) with multiple hidden state factors and multiple observation modalities '''
        num_obs = [2, 4]
        num_states = [2, 3]
        num_controls = [2, 3]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, inference_algo = "VANILLA")

        p_o = utils.obj_array_from_list([A[0][:,0,0], A[1][:,1,1]]) # use a distributional observation
        qs_out = agent.infer_states(p_o, distr_obs=True)

        qs_validation = inference.update_posterior_states(A, p_o, prior=agent.D)

        for f in range(len(num_states)):
            self.assertTrue(np.isclose(qs_validation[f], qs_out[f]).all())

        ''' Marginal message passing inference with one hidden state factor and one observation modality '''
        num_obs = [5]
        num_states = [3]
        num_controls = [1]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, inference_algo = "MMP")

        p_o = utils.obj_array_zeros(num_obs) # use a distributional observation
        # @NOTE: `utils.obj_array_from_list` will make a nested list of object arrays if you only put in a list with one vector!!! Makes me think we should remove utils.obj_array_from_list potentially
        p_o[0] = A[0][:,0]
        qs_pi_out = agent.infer_states(p_o, distr_obs=True)

        policies = control.construct_policies(num_states, num_controls, policy_len = 1)

        qs_pi_validation, _ = inference.update_posterior_states_full(A, B, [p_o], policies, prior = agent.D, policy_sep_prior = False)

        for p_idx in range(len(policies)):
            for f in range(len(num_states)):
                self.assertTrue(np.isclose(qs_pi_validation[p_idx][0][f], qs_pi_out[p_idx][0][f]).all())
        
        ''' Marginal message passing inference with multiple hidden state factors and multiple observation modalities '''
        num_obs = [2, 4]
        num_states = [2, 2]
        num_controls = [2, 2]
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls) 

        planning_horizon = 3
        backwards_horizon = 1
        agent = Agent(A=A, B=B, inference_algo="MMP", policy_len=planning_horizon, inference_horizon=backwards_horizon)
        p_o = utils.obj_array_from_list([A[0][:,0,0], A[1][:,1,1]]) # use a distributional observation
        qs_pi_out = agent.infer_states(p_o, distr_obs=True)

        policies = control.construct_policies(num_states, num_controls, policy_len = planning_horizon)

        qs_pi_validation, _ = inference.update_posterior_states_full_factorized(A, agent.mb_dict, B, agent.B_factor_list, [p_o], policies, prior = agent.D, policy_sep_prior = False)

        for p_idx in range(len(policies)):
            for t in range(planning_horizon+backwards_horizon):
                for f in range(len(num_states)):
                    self.assertTrue(np.isclose(qs_pi_validation[p_idx][t][f], qs_pi_out[p_idx][t][f]).all())

def test_agent_with_factorized_inference(self):
        """
        Test that an instance of the `Agent` class can be initialized with a provided `A_factor_list` and run the factorized inference algorithm. Validate
        against an equivalent `Agent` whose `A` matrix represents the full set of (redundant) conditional dependence relationships.
        """

        num_obs = [5, 4]
        num_states = [2, 3]
        num_controls = [2, 3]

        A_factor_list = [ [0], [1] ]
        A_reduced = utils.random_A_matrix(num_obs, num_states, A_factor_list)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A_reduced, B=B, A_factor_list=A_factor_list, inference_algo = "VANILLA")

        obs = [np.random.randint(obs_dim) for obs_dim in num_obs]

        qs_out = agent.infer_states(obs)

        A_full = utils.initialize_empty_A(num_obs, num_states)
        for m, A_m in enumerate(A_full):
            other_factors = list(set(range(len(num_states))) - set(A_factor_list[m])) # list of the factors that modality `m` does not depend on

            # broadcast or tile the reduced A matrix (`A_reduced`) along the dimensions of corresponding to `other_factors`
            expanded_dims = [num_obs[m]] + [1 if f in other_factors else ns for (f, ns) in enumerate(num_states)]
            tile_dims = [1] + [ns if f in other_factors else 1 for (f, ns) in enumerate(num_states)]
            A_full[m] = np.tile(A_reduced[m].reshape(expanded_dims), tile_dims)
        
        agent = Agent(A=A_full, B=B, inference_algo = "VANILLA")
        qs_validation = agent._infer_states_test(obs)

        for qs_out_f, qs_val_f in zip(qs_out, qs_validation):
            self.assertTrue(np.isclose(qs_out_f, qs_val_f).all())

def test_agent_with_interactions_in_B(self):
        """
        Test that an instance of the `Agent` class can be initialized with a provided `B_factor_list` and run a time loop of active inferece
        """

        num_obs = [5, 4]
        num_states = [2, 3]
        num_controls = [2, 3]

        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent_test = Agent(A=A, B=B, B_factor_list=[[0], [1]])
        agent_val = Agent(A=A, B=B)

        obs_seq = []
        for t in range(5):
            obs_seq.append([np.random.randint(obs_dim) for obs_dim in num_obs])
        
        for t in range(5):
            qs_out = agent_test.infer_states(obs_seq[t])
            qs_val = agent_val._infer_states_test(obs_seq[t])
            for qs_out_f, qs_val_f in zip(qs_out, qs_val):
                self.assertTrue(np.isclose(qs_out_f, qs_val_f).all())
            
            agent_test.infer_policies()
            agent_val.infer_policies()

            agent_test.sample_action()
            agent_val.sample_action()

def test_actinfloop_factorized(self):
        """
        Test that an instance of the `Agent` class can be initialized and run
        with the fully-factorized generative model functions (including policy inference)
        """

        num_obs = [5, 4, 4]
        num_states = [2, 3, 5]
        num_controls = [2, 3, 2]

        A_factor_list = [[0], [0, 1], [0, 1, 2]]
        B_factor_list = [[0], [0, 1], [1, 2]]
        A = utils.random_A_matrix(num_obs, num_states, A_factor_list=A_factor_list)
        B = utils.random_B_matrix(num_states, num_controls, B_factor_list=B_factor_list)

        agent = Agent(A=A, B=B, A_factor_list=A_factor_list, B_factor_list=B_factor_list, inference_algo="VANILLA")

        obs_seq = []
        for t in range(5):
            obs_seq.append([np.random.randint(obs_dim) for obs_dim in num_obs])
        
        for t in range(5):
            qs_out = agent.infer_states(obs_seq[t])
            agent.infer_policies()
            agent.sample_action()

        """ Test to make sure it works even when generative model sparsity is not taken advantage of """
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        agent = Agent(A=A, B=B, inference_algo="VANILLA")

        obs_seq = []
        for t in range(5):
            obs_seq.append([np.random.randint(obs_dim) for obs_dim in num_obs])
        
        for t in range(5):
            qs_out = agent.infer_states(obs_seq[t])
            agent.infer_policies()
            agent.sample_action()
        
        """ Test with pA and pB learning & information gain """

        num_obs = [5, 4, 4]
        num_states = [2, 3, 5]
        num_controls = [2, 3, 2]

        A_factor_list = [[0], [0, 1], [0, 1, 2]]
        B_factor_list = [[0], [0, 1], [1, 2]]
        A = utils.random_A_matrix(num_obs, num_states, A_factor_list=A_factor_list)
        B = utils.random_B_matrix(num_states, num_controls, B_factor_list=B_factor_list)
        pA = utils.dirichlet_like(A)
        pB = utils.dirichlet_like(B)

        agent = Agent(A=A, pA=pA, B=B, pB=pB, save_belief_hist=True, use_param_info_gain=True, A_factor_list=A_factor_list, B_factor_list=B_factor_list, inference_algo="VANILLA")

        obs_seq = []
        for t in range(5):
            obs_seq.append([np.random.randint(obs_dim) for obs_dim in num_obs])
        
        for t in range(5):
            qs_out = agent.infer_states(obs_seq[t])
            agent.infer_policies()
            agent.sample_action()
            agent.update_A(obs_seq[t])
            if t > 0:
                agent.update_B(qs_prev = agent.qs_hist[-2])

def make_model_configs(source_seed=0, num_models=4) -> Dict:
    rng_keys = jr.split(jr.PRNGKey(source_seed), num_models)
    num_factors_list = [ jr.randint(key, (1,), 1, 7)[0].item() for key in rng_keys ] # list of total numbers of hidden state factors per model
    num_states_list = [ jr.randint(key, (nf,), 2, 5).tolist() for nf, key in zip(num_factors_list, rng_keys) ]
    num_controls_list = [ jr.randint(key, (nf,), 1, 3).tolist() for nf, key in zip(num_factors_list, rng_keys) ]

    rng_keys = jr.split(rng_keys[-1], num_models)
    num_modalities_list = [ jr.randint(key, (1,), 1, 10)[0].item() for key in rng_keys ]
    num_obs_list = [ jr.randint(key, (nm,), 1, 5).tolist() for nm, key in zip(num_modalities_list, rng_keys) ]

    rng_keys = jr.split(rng_keys[-1], num_models)
    A_deps_list, B_deps_list = [], []
    for nf, nm, model_key in zip(num_factors_list, num_modalities_list, rng_keys):
        modality_keys_model_i = jr.split(model_key, nm)
        num_f_per_modality = [jr.randint(key, shape=(), minval=1, maxval=nf+1).item() for key in modality_keys_model_i] # this is the number of factors that each modality depends on
        A_deps_model_i = [sorted(jr.choice(key, a=nf, shape=(num_f_m,), replace=False).tolist()) for key, num_f_m in zip(modality_keys_model_i, num_f_per_modality)]
        A_deps_list.append(A_deps_model_i)

        factor_keys_model_i = jr.split(modality_keys_model_i[-1], nf)
        num_f_per_factor = [jr.randint(key, shape=(), minval=1, maxval=nf+1).item() for key in factor_keys_model_i] # this is the number of factors that each factor depends on
        B_deps_model_i = [sorted(jr.choice(key, a=nf, shape=(num_f_f,), replace=False).tolist()) for key, num_f_f in zip(factor_keys_model_i, num_f_per_factor)]
        B_deps_list.append(B_deps_model_i)

    return {'nf_list': num_factors_list, 
            'ns_list': num_states_list, 
            'nc_list': num_controls_list,
            'nm_list': num_modalities_list, 
            'no_list': num_obs_list, 
            'A_deps_list': A_deps_list,
            'B_deps_list': B_deps_list
        }

def make_A_full(A_reduced: List[np.ndarray], A_dependencies: List[List[int]], num_obs: List[int], num_states: List[int]) -> np.ndarray:
    """ 
    Given a reduced A matrix, `A_reduced`, and a list of dependencies between hidden state factors and observation modalities, `A_dependencies`,
    return a full A matrix, `A_full`, where `A_full[m]` is the full A matrix for modality `m`. This means all redundant conditional independencies
    between observation modalities `m` and all hidden state factors (i.e. `range(len(num_states))`) are represented as lagging dimensions in `A_full`.
    """
    A_full = utils.initialize_empty_A(num_obs, num_states) # initialize the full likelihood tensor (ALL modalities might depend on ALL factors)
    all_factors = range(len(num_states)) # indices of all hidden state factors
    for m, A_m in enumerate(A_full):

        # Step 1. Extract the list of the factors that modality `m` does NOT depend on
        non_dependent_factors = list(set(all_factors) - set(A_dependencies[m])) 

        # Step 2. broadcast or tile the reduced A matrix (`A_reduced`) along the dimensions of corresponding to `non_dependent_factors`, to give it the full shape of `(num_obs[m], *num_states)`
        expanded_dims = [num_obs[m]] + [1 if f in non_dependent_factors else ns for (f, ns) in enumerate(num_states)]
        tile_dims = [1] + [ns if f in non_dependent_factors else 1 for (f, ns) in enumerate(num_states)]
        A_full[m] = np.tile(A_reduced[m].reshape(expanded_dims), tile_dims)
    
    return A_full

class TestMessagePassing(unittest.TestCase):

    def test_fixed_point_iteration(self):
        cfg = {'source_seed': 0,
                'num_models': 4
            }
        gm_params = make_model_configs(**cfg)
        num_states_list, num_obs_list = gm_params['ns_list'], gm_params['no_list']

        for (num_states, num_obs) in zip(num_states_list, num_obs_list):

            # numpy version
            prior = utils.random_single_categorical(num_states)
            A = utils.random_A_matrix(num_obs, num_states)

            obs = utils.obj_array(len(num_obs))
            for m, obs_dim in enumerate(num_obs):
                obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

            qs_numpy = fpi_numpy(A, obs, num_obs, num_states, prior=prior, num_iter=16, dF=1.0, dF_tol=-1.0) # set dF_tol to negative number so numpy version of FPI never stops early due to convergence

            # jax version
            prior = [jnp.array(prior_f) for prior_f in prior]
            A = [jnp.array(a_m) for a_m in A]
            obs = [jnp.array(o_m) for o_m in obs]

            qs_jax = fpi_jax(A, obs, prior, num_iter=16)

            for f, _ in enumerate(qs_jax):
                self.assertTrue(np.allclose(qs_numpy[f], qs_jax[f], atol=1e-6))


    def test_fixed_point_iteration_factorized_fullyconnected(self):
        """
        Test the factorized version of `run_vanilla_fpi`, named `run_factorized_fpi`
        with multiple hidden state factors and multiple observation modalities.
        """
        cfg = {'source_seed': 1,
                'num_models': 4
            }
        gm_params = make_model_configs(**cfg)
        num_states_list, num_obs_list = gm_params['ns_list'], gm_params['no_list']

        for (num_states, num_obs) in zip(num_states_list, num_obs_list):

            # initialize arrays in numpy version
            prior = utils.random_single_categorical(num_states)
            A = utils.random_A_matrix(num_obs, num_states)

            obs = utils.obj_array(len(num_obs))
            for m, obs_dim in enumerate(num_obs):
                obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

            # jax version
            prior = [jnp.array(prior_f) for prior_f in prior]
            A = [jnp.array(a_m) for a_m in A]
            obs = [jnp.array(o_m) for o_m in obs]

            factor_lists = len(num_obs) * [list(range(len(num_states)))]

            qs_jax = fpi_jax(A, obs, prior, num_iter=16)
            qs_jax_factorized = fpi_jax_factorized(A, obs, prior, factor_lists, num_iter=16)

            for f, _ in enumerate(qs_jax):
                self.assertTrue(np.allclose(qs_jax[f], qs_jax_factorized[f], atol=1e-6))

    def test_fixed_point_iteration_factorized_sparsegraph(self):
        """
        Test the factorized version of `run_vanilla_fpi`, named `run_factorized_fpi`
        with multiple hidden state factors and multiple observation modalities, and with sparse conditional dependence relationships between hidden states
        and observation modalities
        """
        cfg = {'source_seed': 3,
                'num_models': 4
            }
        gm_params = make_model_configs(**cfg)

        num_states_list, num_obs_list, A_dependencies_list = gm_params['ns_list'], gm_params['no_list'], gm_params['A_deps_list']

        for (num_states, num_obs, a_deps_i) in zip(num_states_list, num_obs_list, A_dependencies_list):
            
            prior = utils.random_single_categorical(num_states)

            obs = utils.obj_array(len(num_obs))
            for m, obs_dim in enumerate(num_obs):
                obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

            A_reduced = utils.random_A_matrix(num_obs, num_states, A_factor_list=a_deps_i)

            # jax version
            prior_jax = [jnp.array(prior_f) for prior_f in prior]
            A_reduced_jax = [jnp.array(a_m) for a_m in A_reduced]
            obs_jax = [jnp.array(o_m) for o_m in obs]

            qs_out = fpi_jax_factorized(A_reduced_jax, obs_jax, prior_jax, a_deps_i, num_iter=16)

            # create the full A matrix, where all hidden state factors are represented in the lagging dimensions of each sub-A array
            A_full = make_A_full(A_reduced, a_deps_i, num_obs, num_states)
           
            # jax version
            A_full_jax = [jnp.array(a_m) for a_m in A_full]

            qs_validation = fpi_jax(A_full_jax, obs_jax, prior_jax, num_iter=16)

            for qs_f_val, qs_f_out in zip(qs_validation, qs_out):
                self.assertTrue(np.allclose(qs_f_val, qs_f_out))

    def test_marginal_message_passing(self):

        cfg = {'source_seed': 5,
                'num_models': 4
            }
        gm_params = make_model_configs(**cfg)

        num_states_list, num_obs_list, num_controls_list, A_dependencies_list, B_dependencies_list = gm_params['ns_list'], gm_params['no_list'], gm_params['nc_list'], \
                                                                                                     gm_params['A_deps_list'], gm_params['B_deps_list']

        batch_size = 10
        n_timesteps = 4

        for num_states, num_obs, num_controls, A_deps, B_deps in zip(num_states_list, num_obs_list, num_controls_list, A_dependencies_list, B_dependencies_list):

            # create a version of a_deps_i where each sub-list is sorted
            prior = [jr.dirichlet(key, alpha=jnp.ones((ns,)), shape=(batch_size,)) for ns, key in zip(num_states, jr.split(jr.PRNGKey(0), len(num_states)))] 

            obs = [jr.categorical(key, logits=jnp.zeros(no), shape=(n_timesteps,batch_size)) for no, key in zip(num_obs, jr.split(jr.PRNGKey(1), len(num_obs)))]
            obs = jtu.tree_map(lambda x, no: nn.one_hot(x, num_classes=no), obs, num_obs)

            A_sub_shapes = [ [ns for f, ns in enumerate(num_states) if f in a_deps_i] for a_deps_i in A_deps ]
            A_sampling_keys = jr.split(jr.PRNGKey(2), len(num_obs))
            A = [jr.dirichlet(key, alpha=jnp.ones(no) / no, shape=factor_shapes) for no, factor_shapes, key in zip(num_obs, A_sub_shapes, A_sampling_keys)]
            A = jtu.tree_map(lambda a: jnp.moveaxis(a, -1, 0), A) # move observations into leading dimensions
            A = jtu.tree_map(lambda a: jnp.broadcast_to(a, (batch_size,) + a.shape), A)

            B_sub_shapes = [ [ns for f, ns in enumerate(num_states) if f in b_deps_i] + [nc] for nc, b_deps_i in zip(num_controls, B_deps) ]
            B_sampling_keys = jr.split(jr.PRNGKey(3), len(num_states))
            B = [jr.dirichlet(key, alpha=jnp.ones(ns) / ns, shape=factor_shapes) for ns, factor_shapes, key in zip(num_states, B_sub_shapes, B_sampling_keys)]
            B = jtu.tree_map(lambda b: jnp.moveaxis(b, -2, -1), B) # move u_t to the rightmost axis of the array
            B = jtu.tree_map(lambda b: jnp.moveaxis(b, -2, 0), B) # s_t+1 to the leading dimension of the array
            B = jtu.tree_map(lambda b: jnp.broadcast_to(b, (batch_size,) + b.shape), B)

            # # create a policy-dependent sequence of B matrices, but now we store the sequence dimension (action indices) in the first dimension (0th dimension is still batch dimension)
            policy = []
            key = jr.PRNGKey(11)
            for nc in num_controls:
                key, k = jr.split(key)
                policy.append( jr.choice(k, jnp.arange(nc), shape=(n_timesteps - 1, 1)) )
            
            policy = jnp.concatenate(policy, -1)
            nf = len(B)
            actions_tree = [policy[:, i] for i in range(nf)]
            B_seq = jtu.tree_map(lambda b, a_idx: jnp.moveaxis(b[..., a_idx], -1, 0), B, actions_tree)

            mmp = vmap(
                partial(mmp_jax, num_iter=16, tau=1.0),
                in_axes=(0, 1, 1, 0, None, None)
            )
            qs_out = mmp(A, B_seq, obs, prior, A_deps, B_deps)

            self.assertTrue(qs_out[0].shape[0] == obs[0].shape[1])

def test_fixed_point_iteration(self):
        cfg = {'source_seed': 0,
                'num_models': 4
            }
        gm_params = make_model_configs(**cfg)
        num_states_list, num_obs_list = gm_params['ns_list'], gm_params['no_list']

        for (num_states, num_obs) in zip(num_states_list, num_obs_list):

            # numpy version
            prior = utils.random_single_categorical(num_states)
            A = utils.random_A_matrix(num_obs, num_states)

            obs = utils.obj_array(len(num_obs))
            for m, obs_dim in enumerate(num_obs):
                obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

            qs_numpy = fpi_numpy(A, obs, num_obs, num_states, prior=prior, num_iter=16, dF=1.0, dF_tol=-1.0) # set dF_tol to negative number so numpy version of FPI never stops early due to convergence

            # jax version
            prior = [jnp.array(prior_f) for prior_f in prior]
            A = [jnp.array(a_m) for a_m in A]
            obs = [jnp.array(o_m) for o_m in obs]

            qs_jax = fpi_jax(A, obs, prior, num_iter=16)

            for f, _ in enumerate(qs_jax):
                self.assertTrue(np.allclose(qs_numpy[f], qs_jax[f], atol=1e-6))

def test_fixed_point_iteration_factorized_fullyconnected(self):
        """
        Test the factorized version of `run_vanilla_fpi`, named `run_factorized_fpi`
        with multiple hidden state factors and multiple observation modalities.
        """
        cfg = {'source_seed': 1,
                'num_models': 4
            }
        gm_params = make_model_configs(**cfg)
        num_states_list, num_obs_list = gm_params['ns_list'], gm_params['no_list']

        for (num_states, num_obs) in zip(num_states_list, num_obs_list):

            # initialize arrays in numpy version
            prior = utils.random_single_categorical(num_states)
            A = utils.random_A_matrix(num_obs, num_states)

            obs = utils.obj_array(len(num_obs))
            for m, obs_dim in enumerate(num_obs):
                obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

            # jax version
            prior = [jnp.array(prior_f) for prior_f in prior]
            A = [jnp.array(a_m) for a_m in A]
            obs = [jnp.array(o_m) for o_m in obs]

            factor_lists = len(num_obs) * [list(range(len(num_states)))]

            qs_jax = fpi_jax(A, obs, prior, num_iter=16)
            qs_jax_factorized = fpi_jax_factorized(A, obs, prior, factor_lists, num_iter=16)

            for f, _ in enumerate(qs_jax):
                self.assertTrue(np.allclose(qs_jax[f], qs_jax_factorized[f], atol=1e-6))

def test_fixed_point_iteration_factorized_sparsegraph(self):
        """
        Test the factorized version of `run_vanilla_fpi`, named `run_factorized_fpi`
        with multiple hidden state factors and multiple observation modalities, and with sparse conditional dependence relationships between hidden states
        and observation modalities
        """
        cfg = {'source_seed': 3,
                'num_models': 4
            }
        gm_params = make_model_configs(**cfg)

        num_states_list, num_obs_list, A_dependencies_list = gm_params['ns_list'], gm_params['no_list'], gm_params['A_deps_list']

        for (num_states, num_obs, a_deps_i) in zip(num_states_list, num_obs_list, A_dependencies_list):
            
            prior = utils.random_single_categorical(num_states)

            obs = utils.obj_array(len(num_obs))
            for m, obs_dim in enumerate(num_obs):
                obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

            A_reduced = utils.random_A_matrix(num_obs, num_states, A_factor_list=a_deps_i)

            # jax version
            prior_jax = [jnp.array(prior_f) for prior_f in prior]
            A_reduced_jax = [jnp.array(a_m) for a_m in A_reduced]
            obs_jax = [jnp.array(o_m) for o_m in obs]

            qs_out = fpi_jax_factorized(A_reduced_jax, obs_jax, prior_jax, a_deps_i, num_iter=16)

            # create the full A matrix, where all hidden state factors are represented in the lagging dimensions of each sub-A array
            A_full = make_A_full(A_reduced, a_deps_i, num_obs, num_states)
           
            # jax version
            A_full_jax = [jnp.array(a_m) for a_m in A_full]

            qs_validation = fpi_jax(A_full_jax, obs_jax, prior_jax, num_iter=16)

            for qs_f_val, qs_f_out in zip(qs_validation, qs_out):
                self.assertTrue(np.allclose(qs_f_val, qs_f_out))

def test_marginal_message_passing(self):

        cfg = {'source_seed': 5,
                'num_models': 4
            }
        gm_params = make_model_configs(**cfg)

        num_states_list, num_obs_list, num_controls_list, A_dependencies_list, B_dependencies_list = gm_params['ns_list'], gm_params['no_list'], gm_params['nc_list'], \
                                                                                                     gm_params['A_deps_list'], gm_params['B_deps_list']

        batch_size = 10
        n_timesteps = 4

        for num_states, num_obs, num_controls, A_deps, B_deps in zip(num_states_list, num_obs_list, num_controls_list, A_dependencies_list, B_dependencies_list):

            # create a version of a_deps_i where each sub-list is sorted
            prior = [jr.dirichlet(key, alpha=jnp.ones((ns,)), shape=(batch_size,)) for ns, key in zip(num_states, jr.split(jr.PRNGKey(0), len(num_states)))] 

            obs = [jr.categorical(key, logits=jnp.zeros(no), shape=(n_timesteps,batch_size)) for no, key in zip(num_obs, jr.split(jr.PRNGKey(1), len(num_obs)))]
            obs = jtu.tree_map(lambda x, no: nn.one_hot(x, num_classes=no), obs, num_obs)

            A_sub_shapes = [ [ns for f, ns in enumerate(num_states) if f in a_deps_i] for a_deps_i in A_deps ]
            A_sampling_keys = jr.split(jr.PRNGKey(2), len(num_obs))
            A = [jr.dirichlet(key, alpha=jnp.ones(no) / no, shape=factor_shapes) for no, factor_shapes, key in zip(num_obs, A_sub_shapes, A_sampling_keys)]
            A = jtu.tree_map(lambda a: jnp.moveaxis(a, -1, 0), A) # move observations into leading dimensions
            A = jtu.tree_map(lambda a: jnp.broadcast_to(a, (batch_size,) + a.shape), A)

            B_sub_shapes = [ [ns for f, ns in enumerate(num_states) if f in b_deps_i] + [nc] for nc, b_deps_i in zip(num_controls, B_deps) ]
            B_sampling_keys = jr.split(jr.PRNGKey(3), len(num_states))
            B = [jr.dirichlet(key, alpha=jnp.ones(ns) / ns, shape=factor_shapes) for ns, factor_shapes, key in zip(num_states, B_sub_shapes, B_sampling_keys)]
            B = jtu.tree_map(lambda b: jnp.moveaxis(b, -2, -1), B) # move u_t to the rightmost axis of the array
            B = jtu.tree_map(lambda b: jnp.moveaxis(b, -2, 0), B) # s_t+1 to the leading dimension of the array
            B = jtu.tree_map(lambda b: jnp.broadcast_to(b, (batch_size,) + b.shape), B)

            # # create a policy-dependent sequence of B matrices, but now we store the sequence dimension (action indices) in the first dimension (0th dimension is still batch dimension)
            policy = []
            key = jr.PRNGKey(11)
            for nc in num_controls:
                key, k = jr.split(key)
                policy.append( jr.choice(k, jnp.arange(nc), shape=(n_timesteps - 1, 1)) )
            
            policy = jnp.concatenate(policy, -1)
            nf = len(B)
            actions_tree = [policy[:, i] for i in range(nf)]
            B_seq = jtu.tree_map(lambda b, a_idx: jnp.moveaxis(b[..., a_idx], -1, 0), B, actions_tree)

            mmp = vmap(
                partial(mmp_jax, num_iter=16, tau=1.0),
                in_axes=(0, 1, 1, 0, None, None)
            )
            qs_out = mmp(A, B_seq, obs, prior, A_deps, B_deps)

            self.assertTrue(qs_out[0].shape[0] == obs[0].shape[1])

class TestAgentJax(unittest.TestCase):

    def test_vmappable_agent_methods(self):

        dim, N = 5, 10
        sampling_key = random.PRNGKey(1)

        class BasicAgent(Module):
            A: jnp.ndarray
            B: jnp.ndarray 
            qs: jnp.ndarray

            def __init__(self, A, B, qs=None):
                self.A = A
                self.B = B
                self.qs = jnp.ones((N, dim))/dim if qs is None else qs
            
            @vmap
            def infer_states(self, obs):
                qs = nn.softmax(compute_log_likelihood_single_modality(obs, self.A))
                return qs, BasicAgent(self.A, self.B, qs=qs)

        A_key, B_key, obs_key, test_key = random.split(sampling_key, 4)

        all_A = vmap(norm_dist)(random.uniform(A_key, shape = (N, dim, dim)))
        all_B = vmap(norm_dist)(random.uniform(B_key, shape = (N, dim, dim)))
        all_obs = vmap(nn.one_hot, (0, None))(random.choice(obs_key, dim, shape = (N,)), dim)

        my_agent = BasicAgent(all_A, all_B)

        all_qs, my_agent = my_agent.infer_states(all_obs)

        assert all_qs.shape == my_agent.qs.shape
        self.assertTrue(jnp.allclose(all_qs, my_agent.qs))

        # validate that the method broadcasted properly
        for id_to_check in range(N):
            validation_qs = nn.softmax(compute_log_likelihood_single_modality(all_obs[id_to_check], all_A[id_to_check]))
            self.assertTrue(jnp.allclose(validation_qs, all_qs[id_to_check]))

def test_vmappable_agent_methods(self):

        dim, N = 5, 10
        sampling_key = random.PRNGKey(1)

        class BasicAgent(Module):
            A: jnp.ndarray
            B: jnp.ndarray 
            qs: jnp.ndarray

            def __init__(self, A, B, qs=None):
                self.A = A
                self.B = B
                self.qs = jnp.ones((N, dim))/dim if qs is None else qs
            
            @vmap
            def infer_states(self, obs):
                qs = nn.softmax(compute_log_likelihood_single_modality(obs, self.A))
                return qs, BasicAgent(self.A, self.B, qs=qs)

        A_key, B_key, obs_key, test_key = random.split(sampling_key, 4)

        all_A = vmap(norm_dist)(random.uniform(A_key, shape = (N, dim, dim)))
        all_B = vmap(norm_dist)(random.uniform(B_key, shape = (N, dim, dim)))
        all_obs = vmap(nn.one_hot, (0, None))(random.choice(obs_key, dim, shape = (N,)), dim)

        my_agent = BasicAgent(all_A, all_B)

        all_qs, my_agent = my_agent.infer_states(all_obs)

        assert all_qs.shape == my_agent.qs.shape
        self.assertTrue(jnp.allclose(all_qs, my_agent.qs))

        # validate that the method broadcasted properly
        for id_to_check in range(N):
            validation_qs = nn.softmax(compute_log_likelihood_single_modality(all_obs[id_to_check], all_A[id_to_check]))
            self.assertTrue(jnp.allclose(validation_qs, all_qs[id_to_check]))

class BasicAgent(Module):
            A: jnp.ndarray
            B: jnp.ndarray 
            qs: jnp.ndarray

            def __init__(self, A, B, qs=None):
                self.A = A
                self.B = B
                self.qs = jnp.ones((N, dim))/dim if qs is None else qs
            
            @vmap
            def infer_states(self, obs):
                qs = nn.softmax(compute_log_likelihood_single_modality(obs, self.A))
                return qs, BasicAgent(self.A, self.B, qs=qs)

def __init__(self, A, B, qs=None):
                self.A = A
                self.B = B
                self.qs = jnp.ones((N, dim))/dim if qs is None else qs

def infer_states(self, obs):
                qs = nn.softmax(compute_log_likelihood_single_modality(obs, self.A))
                return qs, BasicAgent(self.A, self.B, qs=qs)

class TestControl(unittest.TestCase):

    def test_get_expected_states(self):
        """
        Tests the refactored (Categorical-less) version of `get_expected_states`
        """

        '''Test with single hidden state factor and single timestep'''

        num_states = [3]
        num_controls = [3]

        qs = utils.obj_array_uniform(num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        qs_pi = [control.get_expected_states(qs, B, policy) for policy in policies]

        factor_idx = 0
        t_idx = 0

        for p_idx in range(len(policies)):
            self.assertTrue((qs_pi[p_idx][t_idx][factor_idx] == B[factor_idx][:,:,policies[p_idx][t_idx,factor_idx]].dot(qs[factor_idx])).all())

        '''Test with single hidden state factor and multiple-timesteps'''

        num_states = [3]
        num_controls = [3]

        qs = utils.obj_array_uniform(num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        policies = control.construct_policies(num_states, num_controls, policy_len=2)

        qs_pi = [control.get_expected_states(qs, B, policy) for policy in policies]

        for p_idx in range(len(policies)):
            for t_idx in range(2):
                if t_idx == 0:
                    self.assertTrue((qs_pi[p_idx][t_idx][factor_idx] == B[factor_idx][:,:,policies[p_idx][t_idx,factor_idx]].dot(qs[factor_idx])).all())
                else:
                    self.assertTrue((qs_pi[p_idx][t_idx][factor_idx] == B[factor_idx][:,:,policies[p_idx][t_idx,factor_idx]].dot(qs_pi[p_idx][t_idx-1][factor_idx])).all())
       
        '''Test with multiple hidden state factors and single timestep'''

        num_states = [3, 3]
        num_controls = [3, 1]

        num_factors = len(num_states)

        qs = utils.obj_array_uniform(num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        qs_pi = [control.get_expected_states(qs, B, policy) for policy in policies]

        t_idx = 0

        for p_idx in range(len(policies)):
            for factor_idx in range(num_factors):
                self.assertTrue((qs_pi[p_idx][t_idx][factor_idx] == B[factor_idx][:,:,policies[p_idx][t_idx,factor_idx]].dot(qs[factor_idx])).all())

        '''Test with multiple hidden state factors and multiple timesteps'''

        num_states = [3, 3]
        num_controls = [3, 3]

        num_factors = len(num_states)

        qs = utils.obj_array_uniform(num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        policies = control.construct_policies(num_states, num_controls, policy_len=3)

        qs_pi = [control.get_expected_states(qs, B, policy) for policy in policies]

        for p_idx in range(len(policies)):
            for t_idx in range(3):
                for factor_idx in range(num_factors):
                    if t_idx == 0:
                        self.assertTrue((qs_pi[p_idx][t_idx][factor_idx] == B[factor_idx][:,:,policies[p_idx][t_idx,factor_idx]].dot(qs[factor_idx])).all())
                    else:
                        self.assertTrue((qs_pi[p_idx][t_idx][factor_idx] == B[factor_idx][:,:,policies[p_idx][t_idx,factor_idx]].dot(qs_pi[p_idx][t_idx-1][factor_idx])).all())

    def test_get_expected_states_interactions_single_factor(self):
        """
        Test the new version of `get_expected_states` that includes `B` array inter-factor dependencies, in case a of trivial single factor
        """
        
        num_states = [3]
        num_controls = [3]

        B_factor_list = [[0]]

        qs = utils.random_single_categorical(num_states)
        B = utils.random_B_matrix(num_states, num_controls, B_factor_list=B_factor_list)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        qs_pi_0 = control.get_expected_states_interactions(qs, B, B_factor_list, policies[0])

        self.assertTrue(np.allclose(qs_pi_0[0][0], B[0][:,:,policies[0][0,0]].dot(qs[0])))

    def test_get_expected_states_interactions_multi_factor(self):
        """
        Test the new version of `get_expected_states` that includes `B` array inter-factor dependencies, 
        in the case where there are two hidden state factors: one that depends on itself and another that depends on both itself and the other factor.
        """
        
        num_states = [3, 4]
        num_controls = [3, 2]

        B_factor_list = [[0], [0, 1]]

        qs = utils.random_single_categorical(num_states)
        B = utils.random_B_matrix(num_states, num_controls, B_factor_list=B_factor_list)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        qs_pi_0 = control.get_expected_states_interactions(qs, B, B_factor_list, policies[0])

        self.assertTrue(np.allclose(qs_pi_0[0][0], B[0][:,:,policies[0][0,0]].dot(qs[0])))

        qs_next_validation = (B[1][..., policies[0][0,1]] * maths.spm_cross(qs)[None,...]).sum(axis=(1,2)) # how to compute equivalent of `spm_dot(B[...,past_action], qs)`
        self.assertTrue(np.allclose(qs_pi_0[0][1], qs_next_validation))
    
    def test_get_expected_states_interactions_multi_factor_independent(self):
        """
        Test the new version of `get_expected_states` that includes `B` array inter-factor dependencies, 
        in the case where there are multiple hidden state factors, but they all only depend on themselves
        """
        
        num_states = [3, 4, 5, 6]
        num_controls = [1, 2, 5, 3]

        B_factor_list = [[f] for f in range(len(num_states))] # each factor only depends on itself

        qs = utils.random_single_categorical(num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        qs_pi_0 = control.get_expected_states_interactions(qs, B, B_factor_list, policies[0])

        qs_pi_0_validation = control.get_expected_states(qs, B, policies[0])

        for qs_f, qs_val_f in zip(qs_pi_0[0], qs_pi_0_validation[0]):
            self.assertTrue(np.allclose(qs_f, qs_val_f))

    def test_get_expected_obs_factorized(self):
        """
        Test the new version of `get_expected_obs` that includes sparse dependencies of `A` array on hidden state factors (not all observation modalities depend on all hidden state factors)
        """

        """ Case 1, where all modalities depend on all hidden state factors """

        num_states = [3, 4]
        num_obs = [3, 4]

        A_factor_list = [[0, 1], [0, 1]]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states, A_factor_list=A_factor_list)

        qo_test = control.get_expected_obs_factorized([qs], A, A_factor_list) # need to wrap `qs` in list because `get_expected_obs_factorized` expects a list of `qs` (representing multiple timesteps)
        qo_val = control.get_expected_obs([qs], A) # need to wrap `qs` in list because `get_expected_obs` expects a list of `qs` (representing multiple timesteps)

        for qo_m, qo_val_m in zip(qo_test[0], qo_val[0]): # need to extract first index of `qo_test` and `qo_val` because `get_expected_obs_factorized` returns a list of `qo` (representing multiple timesteps)
            self.assertTrue(np.allclose(qo_m, qo_val_m))
        
        """ Case 2, where some modalities depend on some hidden state factors """

        num_states = [3, 4]
        num_obs = [3, 4]

        A_factor_list = [[0], [0, 1]]

        qs = utils.random_single_categorical(num_states)
        A_reduced = utils.random_A_matrix(num_obs, num_states, A_factor_list=A_factor_list)

        qo_test = control.get_expected_obs_factorized([qs], A_reduced, A_factor_list) # need to wrap `qs` in list because `get_expected_obs_factorized` expects a list of `qs` (representing multiple timesteps)

        A_full = utils.initialize_empty_A(num_obs, num_states)
        for m, A_m in enumerate(A_full):
            other_factors = list(set(range(len(num_states))) - set(A_factor_list[m])) # list of the factors that modality `m` does not depend on

            # broadcast or tile the reduced A matrix (`A_reduced`) along the dimensions of corresponding to `other_factors`
            expanded_dims = [num_obs[m]] + [1 if f in other_factors else ns for (f, ns) in enumerate(num_states)]
            tile_dims = [1] + [ns if f in other_factors else 1 for (f, ns) in enumerate(num_states)]
            A_full[m] = np.tile(A_reduced[m].reshape(expanded_dims), tile_dims)
        
        qo_val = control.get_expected_obs([qs], A_full) # need to wrap `qs` in list because `get_expected_obs` expects a list of `qs` (representing multiple timesteps)
        
        for qo_m, qo_val_m in zip(qo_test[0], qo_val[0]): # need to extract first index of `qo_test` and `qo_val` because `get_expected_obs_factorized` returns a list of `qo` (representing multiple timesteps)
            self.assertTrue(np.allclose(qo_m, qo_val_m))

    def test_get_expected_states_and_obs(self):
        """
        Tests the refactored (Categorical-less) versions of `get_expected_states` and `get_expected_obs` together
        """

        '''Test with single observation modality, single hidden state factor and single timestep'''

        num_obs = [3]
        num_states = [3]
        num_controls = [3]

        qs = utils.obj_array_uniform(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)
        
        factor_idx = 0
        modality_idx = 0
        t_idx = 0

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)

            # validation qs_pi
            qs_pi_valid = B[factor_idx][:,:,policies[idx][t_idx,factor_idx]].dot(qs[factor_idx])

            self.assertTrue((qs_pi[t_idx][factor_idx] == qs_pi_valid).all())

            qo_pi = control.get_expected_obs(qs_pi, A)

            # validation qo_pi
            qo_pi_valid = maths.spm_dot(A[modality_idx],utils.to_obj_array(qs_pi_valid))

            self.assertTrue((qo_pi[t_idx][modality_idx] == qo_pi_valid).all())

        '''Test with multiple observation modalities, multiple hidden state factors and single timestep'''

        num_obs = [3, 3]
        num_states = [3, 3]
        num_controls = [3, 2]

        num_factors = len(num_states)
        num_modalities = len(num_obs)

        qs = utils.obj_array_uniform(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)
        
        t_idx = 0

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)

            for factor_idx in range(num_factors):
                # validation qs_pi
                qs_pi_valid = B[factor_idx][:,:,policies[idx][t_idx,factor_idx]].dot(qs[factor_idx])
                self.assertTrue((qs_pi[t_idx][factor_idx] == qs_pi_valid).all())

            qo_pi = control.get_expected_obs(qs_pi, A)

            for modality_idx in range(num_modalities):
                # validation qo_pi
                qo_pi_valid = maths.spm_dot(A[modality_idx],qs_pi[t_idx])
                self.assertTrue((qo_pi[t_idx][modality_idx] == qo_pi_valid).all())
        
        '''Test with multiple observation modalities, multiple hidden state factors and multiple timesteps'''

        num_obs = [3, 3]
        num_states = [3, 3]
        num_controls = [3, 2]

        num_factors = len(num_states)
        num_modalities = len(num_obs)

        qs = utils.obj_array_uniform(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        policies = control.construct_policies(num_states, num_controls, policy_len=3)
        
        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)

            for t_idx in range(3):
                for factor_idx in range(num_factors):
                    # validation qs_pi
                    if t_idx == 0:
                        qs_pi_valid = B[factor_idx][:,:,policies[idx][t_idx,factor_idx]].dot(qs[factor_idx])
                    else:
                        qs_pi_valid = B[factor_idx][:,:,policies[idx][t_idx,factor_idx]].dot(qs_pi[t_idx-1][factor_idx])

                    self.assertTrue((qs_pi[t_idx][factor_idx] == qs_pi_valid).all())

            qo_pi = control.get_expected_obs(qs_pi, A)

            for t_idx in range(3):
                for modality_idx in range(num_modalities):
                    # validation qo_pi
                    qo_pi_valid = maths.spm_dot(A[modality_idx],qs_pi[t_idx])
                    self.assertTrue((qo_pi[t_idx][modality_idx] == qo_pi_valid).all())

    def test_expected_utility(self):
        """
        Test for the expected utility function, for a simple single factor generative model 
        where there are imbalances in the preferences for different outcomes. Test for both single
        timestep policy horizons and multiple timestep policy horizons (planning)
        """

        '''1-step policies'''
        num_states = [2]
        num_controls = [2]

        qs = utils.random_single_categorical(num_states)
        B = utils.construct_controllable_B(num_states, num_controls)

        # Single timestep
        n_step = 1
        policies = control.construct_policies(num_states, num_controls, policy_len=n_step)

        # Single observation modality
        num_obs = [2]

        # Create noiseless identity A matrix
        A = utils.to_obj_array(np.eye(num_obs[0]))

        # Create imbalance in preferences for observations
        C = utils.to_obj_array(utils.onehot(1, num_obs[0]))
        
        # Compute expected utility of policies
        expected_utilities = np.zeros(len(policies))
        for idx, policy in enumerate(policies):
            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)
            expected_utilities[idx] += control.calc_expected_utility(qo_pi, C)

        self.assertGreater(expected_utilities[1], expected_utilities[0])

        '''3-step policies'''
        # One policy entails going to state 0 two times in a row, and then state 2 at the end
        # Another policy entails going to state 1 three times in a row

        num_states = [3]
        num_controls = [3]

        qs = utils.random_single_categorical(num_states)
        B = utils.construct_controllable_B(num_states, num_controls)

        policies = [np.array([0, 0, 2]).reshape(-1, 1), np.array([1, 1, 1]).reshape(-1, 1)]

        # single observation modality
        num_obs = [3]

        # create noiseless identity A matrix
        A = utils.to_obj_array(np.eye(num_obs[0]))

        # create imbalance in preferences for observations
        # This test is designed to illustrate the emergence of planning by
        # using the time-integral of the expected free energy.
        # Even though the first observation (index 0) is the most preferred, the policy
        # that frequents this observation the most is actually not optimal, because that policy
        # terminates in a less preferred state by timestep 3.
        C = utils.to_obj_array(np.array([1.2, 1.0, 0.55]))

        expected_utilities = np.zeros(len(policies))
        for idx, policy in enumerate(policies):
            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)
            expected_utilities[idx] += control.calc_expected_utility(qo_pi, C)

        self.assertGreater(expected_utilities[1], expected_utilities[0])
    
    def test_state_info_gain(self):
        """
        Test the states_info_gain function. 
        Function is tested by manipulating uncertainty in the likelihood matrices (A or B)
        in a ways that alternatively change the resolvability of uncertainty
        This is done with A) an imprecise expected state and a precise sensory mapping, 
        and B) high ambiguity and imprecise sensory mapping.
        """

        num_states = [2]
        num_controls = [2]

        # start with a precise initial state
        qs = utils.to_obj_array(utils.onehot(0, num_states[0]))

        '''Case study 1: Uncertain states, unambiguous observations'''
        # add some uncertainty into the consequences of the second policy, which
        # leads to increased epistemic value of observations, in case of pursuing
        # that policy -- this of course depends on a precise observation likelihood model
        B = utils.construct_controllable_B(num_states, num_controls)
        B[0][:, :, 1] = maths.softmax(B[0][:, :, 1]) # "noise-ify" the consequences of the 1-th action

        # single timestep
        n_step = 1
        policies = control.construct_policies(num_states, num_controls, policy_len=n_step)

        # single observation modality
        num_obs = [2]

        # create noiseless identity A matrix
        A = utils.to_obj_array(np.eye(num_obs[0]))

        state_info_gains = np.zeros(len(policies)) # store the Bayesian surprise / epistemic values of states here (AKA state info gain)
        for idx, policy in enumerate(policies):
            qs_pi = control.get_expected_states(qs, B, policy)
            state_info_gains[idx] += control.calc_states_info_gain(A, qs_pi)
        self.assertGreater(state_info_gains[1], state_info_gains[0])

        '''Case study 2: Uncertain states, ambiguous observations (for all states)'''
        # now we 'undo' the epistemic bonus of the second policy by making the A matrix
        # totally ambiguous; thus observations cannot resolve uncertainty about hidden states.
        # In this case, uncertainty in the posterior beliefs induced by Policy 1 doesn't tip the balance
        # of epistemic value, because uncertainty is irresolveable either way.
        A = utils.obj_array_uniform([ [num_obs[0], num_states[0]] ])

        state_info_gains = np.zeros(len(policies))
        for idx, policy in enumerate(policies):
            qs_pi = control.get_expected_states(qs, B, policy)
            state_info_gains[idx] += control.calc_states_info_gain(A, qs_pi)
        self.assertEqual(state_info_gains[0], state_info_gains[1])

        '''Case study 2: Uncertain states, ambiguous observations (for particular states)'''

        # create noiseless identity A matrix
        A = utils.to_obj_array(np.eye(num_obs[0]))

        # add some uncertainty into the consequences of the both policies
        B = utils.construct_controllable_B(num_states, num_controls)

        B[0][:, :, 0] = maths.softmax(B[0][:, :, 0]*2.0) # "noise-ify" the consequences of the 0-th action, but to a lesser extent than the 1-th action
        B[0][:, :, 1] = maths.softmax(B[0][:, :, 1]) # "noise-ify" the consequences of the 1-th action

        # Although in the presence of a precise likelihood mapping, 
        # Policy 1 would be preferred (due to higher resolve-able uncertainty, introduced by a noisier action-dependent B matrix),
        # if the expected observation likelihood of being in state 1 (the most likely consequence of Policy 1) is not precise, then 
        # Policy 0 (which has more probability loaded over state 0) will have more resolveable uncertainty, due to the
        # higher precision of the A matrix over that column (column 0, which is identity). Even though the expected density over states
        # is less noisy for policy 0.
        A[0][:,1] = maths.softmax(A[0][:,1]) 

        state_info_gains = np.zeros(len(policies))
        for idx, policy in enumerate(policies):
            qs_pi = control.get_expected_states(qs, B, policy)
            state_info_gains[idx] += control.calc_states_info_gain(A, qs_pi)
        self.assertGreater(state_info_gains[1], state_info_gains[0])

    def test_state_info_gain_factorized(self):
        """ 
        Unit test the `calc_states_info_gain_factorized` function by qualitatively checking that in the T-Maze (contextual bandit)
        example, the state info gain is higher for the policy that leads to visiting the cue, which is higher than state info gain
        for visiting the bandit arm, which in turn is higher than the state info gain for the policy that leads to staying in the start state.
        """

        num_states = [2, 3]  
        num_obs = [3, 3, 3]
        num_controls = [1, 3]

        A_factor_list = [[0, 1], [0, 1], [1]] 
        
        A = utils.obj_array(len(num_obs))
        for m, obs in enumerate(num_obs):
            lagging_dimensions = [ns for i, ns in enumerate(num_states) if i in A_factor_list[m]]
            modality_shape = [obs] + lagging_dimensions
            A[m] = np.zeros(modality_shape)
            if m == 0:
                A[m][:, :, 0] = np.ones( (num_obs[m], num_states[0]) ) / num_obs[m]
                A[m][:, :, 1] = np.ones( (num_obs[m], num_states[0]) ) / num_obs[m]
                A[m][:, :, 2] = np.array([[0.9, 0.1], [0.0, 0.0], [0.1, 0.9]]) # cue statistics
            if m == 1:
                A[m][2, :, 0] = np.ones(num_states[0])
                A[m][0:2, :, 1] = np.array([[0.6, 0.4], [0.6, 0.4]]) # bandit statistics (mapping between reward-state (first hidden state factor) and rewards (Good vs Bad))
                A[m][2, :, 2] = np.ones(num_states[0])
            if m == 2:
                A[m] = np.eye(obs)

        qs_start = utils.obj_array_uniform(num_states)
        qs_start[1] = np.array([1., 0., 0.]) # agent believes it's in the start state

        state_info_gain_visit_start = 0.
        for m, A_m in enumerate(A):
            if len(A_factor_list[m]) == 1:
                qs_that_matter = utils.to_obj_array(qs_start[A_factor_list[m]])
            else:
                qs_that_matter = qs_start[A_factor_list[m]]
            state_info_gain_visit_start += control.calc_states_info_gain(A_m, [qs_that_matter])

        qs_arm = utils.obj_array_uniform(num_states)
        qs_arm[1] = np.array([0., 1., 0.]) # agent believes it's in the arm-visiting state

        state_info_gain_visit_arm = 0.
        for m, A_m in enumerate(A):
            if len(A_factor_list[m]) == 1:
                qs_that_matter = utils.to_obj_array(qs_arm[A_factor_list[m]])
            else:
                qs_that_matter = qs_arm[A_factor_list[m]]
            state_info_gain_visit_arm += control.calc_states_info_gain(A_m, [qs_that_matter])

        qs_cue = utils.obj_array_uniform(num_states)
        qs_cue[1] = np.array([0., 0., 1.]) # agent believes it's in the cue-visiting state

        state_info_gain_visit_cue = 0.
        for m, A_m in enumerate(A):
            if len(A_factor_list[m]) == 1:
                qs_that_matter = utils.to_obj_array(qs_cue[A_factor_list[m]])
            else:
                qs_that_matter = qs_cue[A_factor_list[m]]
            state_info_gain_visit_cue += control.calc_states_info_gain(A_m, [qs_that_matter])
        
        self.assertGreater(state_info_gain_visit_arm, state_info_gain_visit_start)
        self.assertGreater(state_info_gain_visit_cue, state_info_gain_visit_arm)

    # def test_neg_ambiguity_modality_sum(self):
    #     """
    #     Test that the negativity ambiguity function is the same when computed using the full (unfactorized) joint distribution over observations and hidden state factors vs. when computed for each modality separately and summed together.
    #     """

    #     num_states = [10, 20, 10, 10]
    #     num_obs = [2, 25, 10, 8]

    #     qs = utils.random_single_categorical(num_states)
    #     A = utils.random_A_matrix(num_obs, num_states)

    #     neg_ambig_full = maths.spm_calc_neg_ambig(A, qs) # need to wrap `qs` in a list because the function expects a list of policy-conditioned posterior beliefs (corresponding to each timestep)
    #     neg_ambig_by_modality = 0.
    #     for m, A_m in enumerate(A):
    #         neg_ambig_by_modality += maths.spm_calc_neg_ambig(A_m, qs)
        
    #     self.assertEqual(neg_ambig_full, neg_ambig_by_modality)
    
    # def test_entropy_modality_sum(self):
    #     """
    #     Test that the negativity ambiguity function is the same when computed using the full (unfactorized) joint distribution over observations and hidden state factors vs. when computed for each modality separately and summed together.
    #     """

    #     num_states = [10, 20, 10, 10]
    #     num_obs = [2, 25, 10, 8]

    #     qs = utils.random_single_categorical(num_states)
    #     A = utils.random_A_matrix(num_obs, num_states)

    #     H_full = maths.spm_calc_qo_entropy(A, qs) # need to wrap `qs` in a list because the function expects a list of policy-conditioned posterior beliefs (corresponding to each timestep)
    #     H_by_modality = 0.
    #     for m, A_m in enumerate(A):
    #         H_by_modality += maths.spm_calc_qo_entropy(A_m, qs)
        
    #     self.assertEqual(H_full, H_by_modality)

    def test_pA_info_gain(self):
        """
        Test the pA_info_gain function. Demonstrates operation
        by manipulating shape of the Dirichlet priors over likelihood parameters
        (pA), which affects information gain for different expected observations
        """

        num_states = [2]
        num_controls = [2]

        # start with a precise initial state
        qs = utils.to_obj_array(utils.onehot(0, num_states[0]))

        B = utils.construct_controllable_B(num_states, num_controls)

        # single timestep
        n_step = 1
        policies = control.construct_policies(num_states, num_controls, policy_len=n_step)

        # single observation modality
        num_obs = [2]

        # create noiseless identity A matrix
        A = utils.to_obj_array(np.eye(num_obs[0]))

        # create prior over dirichlets such that there is a skew
        # in the parameters about the likelihood mapping from the
        # second hidden state (index 1) to observations, such that
        # Observation 0 is believed to be more likely than the other, conditioned on State 1.
        # Therefore sampling observations conditioned on State 1 would afford high info gain
        # about parameters, for that part of the likelhood distribution.

        pA = utils.obj_array_ones([ [num_obs[0], num_states[0]]] )
        pA[0][0, 1] += 1.0

        pA_info_gains = np.zeros(len(policies))
        for idx, policy in enumerate(policies):
            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)
            pA_info_gains[idx] += control.calc_pA_info_gain(pA, qo_pi, qs_pi).item()

        self.assertGreater(pA_info_gains[1], pA_info_gains[0])

        """ Test the factorized version of the pA_info_gain function. """
        pA_info_gains_fac = np.zeros(len(policies))
        for idx, policy in enumerate(policies):
            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs_factorized(qs_pi, A, A_factor_list=[[0]])
            pA_info_gains_fac[idx] += control.calc_pA_info_gain_factorized(pA, qo_pi, qs_pi, A_factor_list=[[0]]).item()

        self.assertTrue(np.allclose(pA_info_gains_fac,  pA_info_gains))  
    
    def test_pB_info_gain(self):
        """
        Test the pB_info_gain function. Demonstrates operation
        by manipulating shape of the Dirichlet priors over likelihood parameters
        (pB), which affects information gain for different states
        """
        num_states = [2]
        num_controls = [2]

        # start with a precise initial state
        qs = utils.to_obj_array(utils.onehot(0, num_states[0]))

        B = utils.construct_controllable_B(num_states, num_controls)

        pB = utils.obj_array_ones([ [num_states[0], num_states[0], num_controls[0]] ])

        # create prior over dirichlets such that there is a skew
        # in the parameters about the likelihood mapping from the
        # hidden states to hidden states under the second action,
        # such that hidden state 0 is considered to be more likely than the other,
        # given the action in question
        # Therefore taking that action would yield an expected state that afford
        # high information gain about that part of the likelihood distribution.
        #
        pB[0][0, :, 1] += 1.0

        # single timestep
        n_step = 1
        policies = control.construct_policies(num_states, num_controls, policy_len=n_step)

        pB_info_gains = np.zeros(len(policies))
        for idx, policy in enumerate(policies):
            qs_pi = control.get_expected_states(qs, B, policy)
            pB_info_gains[idx] += control.calc_pB_info_gain(pB, qs_pi, qs, policy)
        self.assertGreater(pB_info_gains[1], pB_info_gains[0])

        B_factor_list = [[0]]
        pB_info_gains_interactions = np.zeros(len(policies))
        for idx, policy in enumerate(policies):
            qs_pi = control.get_expected_states_interactions(qs, B, B_factor_list, policy)
            pB_info_gains_interactions[idx] += control.calc_pB_info_gain_interactions(pB, qs_pi, qs, B_factor_list, policy)
        self.assertTrue(np.allclose(pB_info_gains_interactions, pB_info_gains))

    def test_update_posterior_policies_utility(self):
        """
        Tests the refactored (Categorical-less) version of `update_posterior_policies`, using only the expected utility component of the expected free energy
        """

        '''Test with single observation modality, single hidden state factor and single timestep'''

        num_obs = [3]
        num_states = [3]
        num_controls = [3]

        qs = utils.obj_array_uniform(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros(num_obs)
        C[0][0] = 1.0  
        C[0][1] = -2.0  

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = False,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            gamma=16.0
        )

        factor_idx = 0
        modality_idx = 0
        t_idx = 0

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            
            qo_pi = control.get_expected_obs(qs_pi, A)

            lnC = maths.spm_log_single(maths.softmax(C[modality_idx][:, np.newaxis]))
            efe_valid[idx] += qo_pi[t_idx][modality_idx].dot(lnC).item()
        
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

        '''Test with multiple observation modalities, multiple hidden state factors and single timestep'''

        num_obs = [3, 3]
        num_states = [3, 2]
        num_controls = [3, 1]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros(num_obs)
        C[0][0] = 1.0  
        C[0][1] = -2.0
        C[1][2] = 4.0  

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = False,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            gamma=16.0
        )

        t_idx = 0

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)

            for modality_idx in range(len(A)):
                lnC = maths.spm_log_single(maths.softmax(C[modality_idx][:, np.newaxis]))
                efe_valid[idx] += qo_pi[t_idx][modality_idx].dot(lnC).item()
        
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

        '''Test with multiple observation modalities, multiple hidden state factors and multiple timesteps'''

        num_obs = [3, 3]
        num_states = [3, 2]
        num_controls = [3, 1]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros(num_obs)
        C[0][0] = 1.0  
        C[0][1] = -2.0
        C[1][2] = 4.0  

        policies = control.construct_policies(num_states, num_controls, policy_len=3)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = False,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            gamma=16.0
        )

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)

            for t_idx in range(3):
                for modality_idx in range(len(A)):
                    lnC = maths.spm_log_single(maths.softmax(C[modality_idx][:, np.newaxis]))
                    efe_valid[idx] += qo_pi[t_idx][modality_idx].dot(lnC).item()
        
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))
    
    def test_temporal_C_matrix(self):
        """ Unit-tests for preferences that change over time """

        '''Test with single observation modality, single hidden state factor and single timestep, and non-temporal C vector'''

        num_obs = [3]
        num_states = [3]
        num_controls = [3]

        qs = utils.obj_array_uniform(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros(num_obs)
        C[0][0] = 1.0  
        C[0][1] = -2.0  

        policies = control.construct_policies(num_states, num_controls, policy_len=3)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = False,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            gamma=16.0
        )

        factor_idx = 0
        modality_idx = 0
        t_idx = 0

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)

            for t_idx in range(3):
                for modality_idx in range(len(A)):
                    lnC = maths.spm_log_single(maths.softmax(C[modality_idx][:, np.newaxis]))
                    efe_valid[idx] += qo_pi[t_idx][modality_idx].dot(lnC).item()

        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

        '''Test with single observation modality, single hidden state factor and single timestep, and temporal C vector'''

        num_obs = [3]
        num_states = [3]
        num_controls = [3]

        qs = utils.obj_array_uniform(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros([(3,3)])
        C[0][0,:] = np.array([1.0, 2.0, 0.0])
        C[0][1,:] = np.array([-2.0, -1.0, 0.0])  

        policies = control.construct_policies(num_states, num_controls, policy_len=3)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = False,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            gamma=16.0
        )

        factor_idx = 0
        modality_idx = 0
        t_idx = 0

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)

            for t_idx in range(3):
                for modality_idx in range(len(A)):
                    lnC = maths.spm_log_single(maths.softmax(C[modality_idx][:, t_idx]))
                    efe_valid[idx] += qo_pi[t_idx][modality_idx].dot(lnC).item()

        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

        '''Test with multiple observation modalities, multiple hidden state factors and multiple timesteps'''

        num_obs = [3, 3]
        num_states = [3, 2]
        num_controls = [3, 1]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array(len(num_obs))

        # C vectors for modalities 0 is time-dependent
        C[0] = np.random.rand(3, 3) 

        # C vectors for modalities 1 is time-independent
        C[1] = np.random.rand(3)

        policies = control.construct_policies(num_states, num_controls, policy_len=3)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = False,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            gamma=16.0
        )

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)

            for t_idx in range(3):
                for modality_idx in range(len(A)):
                    if modality_idx == 0:
                        lnC = maths.spm_log_single(maths.softmax(C[modality_idx][:, t_idx]))
                    elif modality_idx == 1:
                        lnC = maths.spm_log_single(maths.softmax(C[modality_idx][:, np.newaxis]))
                    efe_valid[idx] += qo_pi[t_idx][modality_idx].dot(lnC).item()
        
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))


    def test_update_posterior_policies_states_infogain(self):
        """
        Tests the refactored (Categorical-less) version of `update_posterior_policies`, using only the information gain (about states) component of the expected free energy
        """

        '''Test with single observation modality, single hidden state factor and single timestep'''

        num_obs = [3]
        num_states = [3]
        num_controls = [3]

        qs = utils.obj_array_uniform(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros(num_obs)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = False,
            use_states_info_gain = True,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            gamma=16.0
        )

        factor_idx = 0
        modality_idx = 0
        t_idx = 0

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            
            efe_valid[idx] += maths.spm_MDP_G(A, qs_pi[0])
        
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

        '''Test with multiple observation modalities, multiple hidden state factors and single timestep'''

        num_obs = [3, 3]
        num_states = [3, 2]
        num_controls = [3, 1]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros(num_obs)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = False,
            use_states_info_gain = True,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            gamma=16.0
        )

        t_idx = 0

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)

            efe_valid[idx] += maths.spm_MDP_G(A, qs_pi[0])
        
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

        '''Test with multiple observation modalities, multiple hidden state factors and multiple timesteps'''

        num_obs = [3, 3]
        num_states = [3, 2]
        num_controls = [3, 1]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros(num_obs) 

        policies = control.construct_policies(num_states, num_controls, policy_len=3)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = False,
            use_states_info_gain = True,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            gamma=16.0
        )

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)

            for t_idx in range(3):
                efe_valid[idx] += maths.spm_MDP_G(A, qs_pi[t_idx])
    
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

    def test_update_posterior_policies_pA_infogain(self):
        """
        Tests the refactored (Categorical-less) version of `update_posterior_policies`, using only the information gain (about likelihood parameters) component of the expected free energy
        """

        '''Test with single observation modality, single hidden state factor and single timestep'''

        num_obs = [3]
        num_states = [3]
        num_controls = [3]

        qs = utils.obj_array_uniform(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])

        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros(num_obs)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = False,
            use_states_info_gain = False,
            use_param_info_gain = True,
            pA=pA,
            pB=None,
            gamma=16.0
        )

        factor_idx = 0
        modality_idx = 0
        t_idx = 0

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)
            
            efe_valid[idx] += control.calc_pA_info_gain(pA, qo_pi, qs_pi).item()
        
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

        '''Test with multiple observation modalities, multiple hidden state factors and single timestep'''

        num_obs = [3, 3]
        num_states = [3, 2]
        num_controls = [3, 1]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])

        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros(num_obs)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = False,
            use_states_info_gain = False,
            use_param_info_gain = True,
            pA=pA,
            pB=None,
            gamma=16.0
        )

        t_idx = 0

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)
            
            efe_valid[idx] += control.calc_pA_info_gain(pA, qo_pi, qs_pi).item()
        
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

        '''Test with multiple observation modalities, multiple hidden state factors and multiple timesteps'''

        num_obs = [3, 3]
        num_states = [3, 2]
        num_controls = [3, 1]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])

        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros(num_obs) 

        policies = control.construct_policies(num_states, num_controls, policy_len=3)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = False,
            use_states_info_gain = False,
            use_param_info_gain = True,
            pA=pA,
            pB=None,
            gamma=16.0
        )

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)

            efe_valid[idx] += control.calc_pA_info_gain(pA, qo_pi, qs_pi).item()
    
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))
    
    def test_update_posterior_policies_pB_infogain(self):
        """
        Tests the refactored (Categorical-less) version of `update_posterior_policies`, using only the information gain (about transition likelihood parameters) component of the expected free energy
        """

        '''Test with single observation modality, single hidden state factor and single timestep'''

        num_obs = [3]
        num_states = [3]
        num_controls = [3]

        qs = utils.obj_array_uniform(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        C = utils.obj_array_zeros(num_obs)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = False,
            use_states_info_gain = False,
            use_param_info_gain = True,
            pA=None,
            pB=pB,
            gamma=16.0
        )

        factor_idx = 0
        modality_idx = 0
        t_idx = 0

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            
            efe_valid[idx] += control.calc_pB_info_gain(pB, qs_pi, qs, policy)
        
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

        '''Test with multiple observation modalities, multiple hidden state factors and single timestep'''

        num_obs = [3, 3]
        num_states = [3, 2]
        num_controls = [3, 1]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])
        
        C = utils.obj_array_zeros(num_obs)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = False,
            use_states_info_gain = False,
            use_param_info_gain = True,
            pA=None,
            pB=pB,
            gamma=16.0
        )

        t_idx = 0

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            
            efe_valid[idx] += control.calc_pB_info_gain(pB, qs_pi, qs, policy)
        
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

        '''Test with multiple observation modalities, multiple hidden state factors and multiple timesteps'''

        num_obs = [3, 3]
        num_states = [3, 2]
        num_controls = [3, 1]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        C = utils.obj_array_zeros(num_obs) 

        policies = control.construct_policies(num_states, num_controls, policy_len=3)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = False,
            use_states_info_gain = False,
            use_param_info_gain = True,
            pA=None,
            pB=pB,
            gamma=16.0
        )

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)

            efe_valid[idx] += control.calc_pB_info_gain(pB, qs_pi, qs, policy)
    
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))
    
    def test_update_posterior_policies_factorized(self):
        """ 
        Test new update_posterior_policies_factorized function, just to make sure it runs through and outputs correct shapes
        """

        num_obs = [3, 3]
        num_states = [3, 2]
        num_controls = [3, 2]

        A_factor_list = [[0, 1], [1]]
        B_factor_list = [[0], [0, 1]]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states, A_factor_list=A_factor_list)
        B = utils.random_B_matrix(num_states, num_controls, B_factor_list=B_factor_list)
        C = utils.obj_array_zeros(num_obs)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies_factorized(
            qs,
            A,
            B,
            C,
            A_factor_list,
            B_factor_list,
            policies,
            use_utility = True,
            use_states_info_gain = True,
            gamma=16.0
        )

        self.assertEqual(len(q_pi), len(policies))
        self.assertEqual(len(efe), len(policies))

        chosen_action = control.sample_action(q_pi, policies, num_controls, action_selection="deterministic")

    def test_sample_action(self):
        """
        Tests the refactored (Categorical-less) version of `sample_action`
        """

        '''Test with single observation modality, single hidden state factor and single timestep'''

        num_obs = [3]
        num_states = [3]
        num_controls = [3]

        qs = utils.obj_array_uniform(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        C = utils.obj_array_zeros(num_obs)
        C[0][0] = 1.0  
        C[0][1] = -2.0

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = True,
            use_param_info_gain = True,
            pA=pA,
            pB=pB,
            gamma=16.0
        )

        factor_idx = 0
        modality_idx = 0
        t_idx = 0

        chosen_action = control.sample_action(q_pi, policies, num_controls, action_selection="deterministic")
        sampled_action = control.sample_action(q_pi, policies, num_controls, action_selection="stochastic", alpha=1.0)

        self.assertEqual(chosen_action.shape, sampled_action.shape)

        '''Test with multiple observation modalities, multiple hidden state factors and single timestep'''

        num_obs = [3, 4]
        num_states = [3, 4]
        num_controls = [3, 3]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        C = utils.obj_array_zeros(num_obs)
        C[0][0] = 1.0  
        C[0][1] = -2.0
        C[1][3] = 3.0

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = True,
            use_param_info_gain = True,
            pA=pA,
            pB=pB,
            gamma=16.0
        )

        chosen_action = control.sample_action(q_pi, policies, num_controls, action_selection="deterministic")
        sampled_action = control.sample_action(q_pi, policies, num_controls, action_selection="stochastic", alpha=1.0)

        self.assertEqual(chosen_action.shape, sampled_action.shape)

        '''Test with multiple observation modalities, multiple hidden state factors and multiple timesteps'''

        num_obs = [3, 4]
        num_states = [3, 4]
        num_controls = [3, 3]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        C = utils.obj_array_zeros(num_obs)
        C[0][0] = 1.0  
        C[0][1] = -2.0
        C[1][3] = 3.0

        policies = control.construct_policies(num_states, num_controls, policy_len=3)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = True,
            use_param_info_gain = True,
            pA=pA,
            pB=pB,
            gamma=16.0
        )

        chosen_action = control.sample_action(q_pi, policies, num_controls, action_selection="deterministic")
        sampled_action = control.sample_action(q_pi, policies, num_controls, action_selection="stochastic", alpha=1.0)

        self.assertEqual(chosen_action.shape, sampled_action.shape)


        '''Single observation modality, single (controllable) hidden state factor, 3-step policies. Using utility only'''
        # One policy entails going to state 0 two times in a row, and then state 2 at the end
        # Another policy entails going to state 1 three times in a row

        num_obs = [3]
        num_states = [3]
        num_controls = [3]

        qs = utils.random_single_categorical(num_states)
        B = utils.construct_controllable_B(num_states, num_controls)

        policies = [np.array([0, 0, 2]).reshape(-1, 1), np.array([1, 1, 1]).reshape(-1, 1)]

        # create noiseless identity A matrix
        A = utils.to_obj_array(np.eye(num_obs[0]))

        # create imbalance in preferences for observations
        # This test is designed to illustrate the emergence of planning by
        # using the time-integral of the expected free energy.
        # Even though the first observation (index 0) is the most preferred, the policy
        # that frequents this observation the most is actually not optimal, because that policy
        # terminates in a less preferred state by timestep 3.
        C = utils.to_obj_array(np.array([1.2, 1.0, 0.55]))

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = False,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            gamma=16.0
        )

        chosen_action = control.sample_action(q_pi, policies, num_controls, action_selection="deterministic")
        self.assertEqual(int(chosen_action[0]), 1)

    def test_sample_policy(self):
        """
        Tests the action selection function where policies are sampled directly from posterior over policies `q_pi`
        """

        num_states = [3, 2]
        num_controls = [3, 2]

        policies = control.construct_policies(num_states, num_controls, policy_len=3)

        q_pi = utils.norm_dist(np.random.rand(len(policies)))
        best_policy = policies[np.argmax(q_pi)]

        selected_policy = control.sample_policy(q_pi, policies, num_controls)

        for factor_ii in range(len(num_controls)):
            self.assertEqual(selected_policy[factor_ii], best_policy[0,factor_ii])
        
        selected_policy_stochastic = control.sample_policy(q_pi, policies, num_controls, action_selection="stochastic",
                                                           alpha=1.0)
        self.assertEqual(selected_policy_stochastic.shape, selected_policy.shape)
        
    def test_update_posterior_policies_withE_vector(self):
        """
        Test update posterior policies in the case that there is a prior over policies
        """

        """ Construct an explicit example where policy 0 is preferred based on utility,
        but action 2 also gets a bump in probability because of prior over policies
        """
        num_obs = [3]
        num_states = [3]
        num_controls = [3]

        qs = utils.to_obj_array(utils.onehot(0, num_states[0]))
        A = utils.to_obj_array(np.eye(num_obs[0]))
        B = utils.construct_controllable_B(num_states, num_controls)
        
        C = utils.to_obj_array(np.array([1.5, 1.0, 1.0]))

        D = utils.to_obj_array(utils.onehot(0, num_states[0]))
        E = np.array([0.05, 0.05, 0.9])

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = False,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            E = E,
            gamma=16.0
        )

        self.assertGreater(q_pi[0], q_pi[1])
        self.assertGreater(q_pi[2], q_pi[1])
    
    def test_stochastic_action_unidimensional_control(self):
        """
        Test stochastic action sampling in case that one of the control states is one-dimensional.
        Due to a call to probabilities.squeeze() in an earlier version of utils.sample(), this was throwing an
        error due to the inability to use np.random.multinomial on an array with undefined length (an 'unsized' array)
        """
        
        num_states = [2, 2]
        num_controls = [2, 1]
        policies = control.construct_policies(num_states, num_controls = num_controls, policy_len=1)
        q_pi = utils.norm_dist(np.random.rand(len(policies)))
        sampled_action = control.sample_action(q_pi, policies, num_controls, action_selection="stochastic")
        self.assertEqual(sampled_action[1], 0)

        sampled_action = control.sample_action(q_pi, policies, num_controls, action_selection="deterministic")
        self.assertEqual(sampled_action[1], 0)
    
    def test_deterministic_action_sampling_equal_value(self):
        """
        Test `deterministic` action sampling in the case that multiple actions have the same probability. 
        Desired behavior is that actions are randomly sampled from the subset of total actions that have the highest (but equal) probability.
        """

        num_states = [3]
        num_controls = [3]
        policies = control.construct_policies(num_states, num_controls = num_controls, policy_len=1)
        q_pi = np.array([0.4, 0.4, 0.2])

        seeds = [1923, 48323]

        sampled_action = control._sample_action_test(q_pi, policies, num_controls, action_selection="deterministic", seed=seeds[0])
        self.assertEqual(sampled_action[0], 0)

        sampled_action = control._sample_action_test(q_pi, policies, num_controls, action_selection="deterministic", seed=seeds[1])
        self.assertEqual(sampled_action[0], 1)
    
    def test_deterministic_policy_selection_equal_value(self):
        """
        Test `deterministic` action sampling in the case that multiple actions have the same probability. 
        Desired behavior is that actions are randomly sampled from the subset of total actions that have the highest (but equal) probability.
        """

        num_states = [3]
        num_controls = [3]
        policies = control.construct_policies(num_states, num_controls = num_controls, policy_len=1)
        q_pi = np.array([0.1, 0.45, 0.45])

        seeds = [1923, 48323]

        sampled_action = control._sample_policy_test(q_pi, policies, num_controls, action_selection="deterministic", seed=seeds[0])
        self.assertEqual(sampled_action[0], 1)

        sampled_action = control._sample_policy_test(q_pi, policies, num_controls, action_selection="deterministic", seed=seeds[1])
        self.assertEqual(sampled_action[0], 2)

def test_get_expected_states(self):
        """
        Tests the refactored (Categorical-less) version of `get_expected_states`
        """

        '''Test with single hidden state factor and single timestep'''

        num_states = [3]
        num_controls = [3]

        qs = utils.obj_array_uniform(num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        qs_pi = [control.get_expected_states(qs, B, policy) for policy in policies]

        factor_idx = 0
        t_idx = 0

        for p_idx in range(len(policies)):
            self.assertTrue((qs_pi[p_idx][t_idx][factor_idx] == B[factor_idx][:,:,policies[p_idx][t_idx,factor_idx]].dot(qs[factor_idx])).all())

        '''Test with single hidden state factor and multiple-timesteps'''

        num_states = [3]
        num_controls = [3]

        qs = utils.obj_array_uniform(num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        policies = control.construct_policies(num_states, num_controls, policy_len=2)

        qs_pi = [control.get_expected_states(qs, B, policy) for policy in policies]

        for p_idx in range(len(policies)):
            for t_idx in range(2):
                if t_idx == 0:
                    self.assertTrue((qs_pi[p_idx][t_idx][factor_idx] == B[factor_idx][:,:,policies[p_idx][t_idx,factor_idx]].dot(qs[factor_idx])).all())
                else:
                    self.assertTrue((qs_pi[p_idx][t_idx][factor_idx] == B[factor_idx][:,:,policies[p_idx][t_idx,factor_idx]].dot(qs_pi[p_idx][t_idx-1][factor_idx])).all())
       
        '''Test with multiple hidden state factors and single timestep'''

        num_states = [3, 3]
        num_controls = [3, 1]

        num_factors = len(num_states)

        qs = utils.obj_array_uniform(num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        qs_pi = [control.get_expected_states(qs, B, policy) for policy in policies]

        t_idx = 0

        for p_idx in range(len(policies)):
            for factor_idx in range(num_factors):
                self.assertTrue((qs_pi[p_idx][t_idx][factor_idx] == B[factor_idx][:,:,policies[p_idx][t_idx,factor_idx]].dot(qs[factor_idx])).all())

        '''Test with multiple hidden state factors and multiple timesteps'''

        num_states = [3, 3]
        num_controls = [3, 3]

        num_factors = len(num_states)

        qs = utils.obj_array_uniform(num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        policies = control.construct_policies(num_states, num_controls, policy_len=3)

        qs_pi = [control.get_expected_states(qs, B, policy) for policy in policies]

        for p_idx in range(len(policies)):
            for t_idx in range(3):
                for factor_idx in range(num_factors):
                    if t_idx == 0:
                        self.assertTrue((qs_pi[p_idx][t_idx][factor_idx] == B[factor_idx][:,:,policies[p_idx][t_idx,factor_idx]].dot(qs[factor_idx])).all())
                    else:
                        self.assertTrue((qs_pi[p_idx][t_idx][factor_idx] == B[factor_idx][:,:,policies[p_idx][t_idx,factor_idx]].dot(qs_pi[p_idx][t_idx-1][factor_idx])).all())

def test_get_expected_states_interactions_single_factor(self):
        """
        Test the new version of `get_expected_states` that includes `B` array inter-factor dependencies, in case a of trivial single factor
        """
        
        num_states = [3]
        num_controls = [3]

        B_factor_list = [[0]]

        qs = utils.random_single_categorical(num_states)
        B = utils.random_B_matrix(num_states, num_controls, B_factor_list=B_factor_list)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        qs_pi_0 = control.get_expected_states_interactions(qs, B, B_factor_list, policies[0])

        self.assertTrue(np.allclose(qs_pi_0[0][0], B[0][:,:,policies[0][0,0]].dot(qs[0])))

def test_get_expected_states_interactions_multi_factor(self):
        """
        Test the new version of `get_expected_states` that includes `B` array inter-factor dependencies, 
        in the case where there are two hidden state factors: one that depends on itself and another that depends on both itself and the other factor.
        """
        
        num_states = [3, 4]
        num_controls = [3, 2]

        B_factor_list = [[0], [0, 1]]

        qs = utils.random_single_categorical(num_states)
        B = utils.random_B_matrix(num_states, num_controls, B_factor_list=B_factor_list)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        qs_pi_0 = control.get_expected_states_interactions(qs, B, B_factor_list, policies[0])

        self.assertTrue(np.allclose(qs_pi_0[0][0], B[0][:,:,policies[0][0,0]].dot(qs[0])))

        qs_next_validation = (B[1][..., policies[0][0,1]] * maths.spm_cross(qs)[None,...]).sum(axis=(1,2)) # how to compute equivalent of `spm_dot(B[...,past_action], qs)`
        self.assertTrue(np.allclose(qs_pi_0[0][1], qs_next_validation))

def test_get_expected_states_interactions_multi_factor_independent(self):
        """
        Test the new version of `get_expected_states` that includes `B` array inter-factor dependencies, 
        in the case where there are multiple hidden state factors, but they all only depend on themselves
        """
        
        num_states = [3, 4, 5, 6]
        num_controls = [1, 2, 5, 3]

        B_factor_list = [[f] for f in range(len(num_states))] # each factor only depends on itself

        qs = utils.random_single_categorical(num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        qs_pi_0 = control.get_expected_states_interactions(qs, B, B_factor_list, policies[0])

        qs_pi_0_validation = control.get_expected_states(qs, B, policies[0])

        for qs_f, qs_val_f in zip(qs_pi_0[0], qs_pi_0_validation[0]):
            self.assertTrue(np.allclose(qs_f, qs_val_f))

def test_get_expected_obs_factorized(self):
        """
        Test the new version of `get_expected_obs` that includes sparse dependencies of `A` array on hidden state factors (not all observation modalities depend on all hidden state factors)
        """

        """ Case 1, where all modalities depend on all hidden state factors """

        num_states = [3, 4]
        num_obs = [3, 4]

        A_factor_list = [[0, 1], [0, 1]]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states, A_factor_list=A_factor_list)

        qo_test = control.get_expected_obs_factorized([qs], A, A_factor_list) # need to wrap `qs` in list because `get_expected_obs_factorized` expects a list of `qs` (representing multiple timesteps)
        qo_val = control.get_expected_obs([qs], A) # need to wrap `qs` in list because `get_expected_obs` expects a list of `qs` (representing multiple timesteps)

        for qo_m, qo_val_m in zip(qo_test[0], qo_val[0]): # need to extract first index of `qo_test` and `qo_val` because `get_expected_obs_factorized` returns a list of `qo` (representing multiple timesteps)
            self.assertTrue(np.allclose(qo_m, qo_val_m))
        
        """ Case 2, where some modalities depend on some hidden state factors """

        num_states = [3, 4]
        num_obs = [3, 4]

        A_factor_list = [[0], [0, 1]]

        qs = utils.random_single_categorical(num_states)
        A_reduced = utils.random_A_matrix(num_obs, num_states, A_factor_list=A_factor_list)

        qo_test = control.get_expected_obs_factorized([qs], A_reduced, A_factor_list) # need to wrap `qs` in list because `get_expected_obs_factorized` expects a list of `qs` (representing multiple timesteps)

        A_full = utils.initialize_empty_A(num_obs, num_states)
        for m, A_m in enumerate(A_full):
            other_factors = list(set(range(len(num_states))) - set(A_factor_list[m])) # list of the factors that modality `m` does not depend on

            # broadcast or tile the reduced A matrix (`A_reduced`) along the dimensions of corresponding to `other_factors`
            expanded_dims = [num_obs[m]] + [1 if f in other_factors else ns for (f, ns) in enumerate(num_states)]
            tile_dims = [1] + [ns if f in other_factors else 1 for (f, ns) in enumerate(num_states)]
            A_full[m] = np.tile(A_reduced[m].reshape(expanded_dims), tile_dims)
        
        qo_val = control.get_expected_obs([qs], A_full) # need to wrap `qs` in list because `get_expected_obs` expects a list of `qs` (representing multiple timesteps)
        
        for qo_m, qo_val_m in zip(qo_test[0], qo_val[0]): # need to extract first index of `qo_test` and `qo_val` because `get_expected_obs_factorized` returns a list of `qo` (representing multiple timesteps)
            self.assertTrue(np.allclose(qo_m, qo_val_m))

def test_get_expected_states_and_obs(self):
        """
        Tests the refactored (Categorical-less) versions of `get_expected_states` and `get_expected_obs` together
        """

        '''Test with single observation modality, single hidden state factor and single timestep'''

        num_obs = [3]
        num_states = [3]
        num_controls = [3]

        qs = utils.obj_array_uniform(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)
        
        factor_idx = 0
        modality_idx = 0
        t_idx = 0

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)

            # validation qs_pi
            qs_pi_valid = B[factor_idx][:,:,policies[idx][t_idx,factor_idx]].dot(qs[factor_idx])

            self.assertTrue((qs_pi[t_idx][factor_idx] == qs_pi_valid).all())

            qo_pi = control.get_expected_obs(qs_pi, A)

            # validation qo_pi
            qo_pi_valid = maths.spm_dot(A[modality_idx],utils.to_obj_array(qs_pi_valid))

            self.assertTrue((qo_pi[t_idx][modality_idx] == qo_pi_valid).all())

        '''Test with multiple observation modalities, multiple hidden state factors and single timestep'''

        num_obs = [3, 3]
        num_states = [3, 3]
        num_controls = [3, 2]

        num_factors = len(num_states)
        num_modalities = len(num_obs)

        qs = utils.obj_array_uniform(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)
        
        t_idx = 0

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)

            for factor_idx in range(num_factors):
                # validation qs_pi
                qs_pi_valid = B[factor_idx][:,:,policies[idx][t_idx,factor_idx]].dot(qs[factor_idx])
                self.assertTrue((qs_pi[t_idx][factor_idx] == qs_pi_valid).all())

            qo_pi = control.get_expected_obs(qs_pi, A)

            for modality_idx in range(num_modalities):
                # validation qo_pi
                qo_pi_valid = maths.spm_dot(A[modality_idx],qs_pi[t_idx])
                self.assertTrue((qo_pi[t_idx][modality_idx] == qo_pi_valid).all())
        
        '''Test with multiple observation modalities, multiple hidden state factors and multiple timesteps'''

        num_obs = [3, 3]
        num_states = [3, 3]
        num_controls = [3, 2]

        num_factors = len(num_states)
        num_modalities = len(num_obs)

        qs = utils.obj_array_uniform(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)

        policies = control.construct_policies(num_states, num_controls, policy_len=3)
        
        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)

            for t_idx in range(3):
                for factor_idx in range(num_factors):
                    # validation qs_pi
                    if t_idx == 0:
                        qs_pi_valid = B[factor_idx][:,:,policies[idx][t_idx,factor_idx]].dot(qs[factor_idx])
                    else:
                        qs_pi_valid = B[factor_idx][:,:,policies[idx][t_idx,factor_idx]].dot(qs_pi[t_idx-1][factor_idx])

                    self.assertTrue((qs_pi[t_idx][factor_idx] == qs_pi_valid).all())

            qo_pi = control.get_expected_obs(qs_pi, A)

            for t_idx in range(3):
                for modality_idx in range(num_modalities):
                    # validation qo_pi
                    qo_pi_valid = maths.spm_dot(A[modality_idx],qs_pi[t_idx])
                    self.assertTrue((qo_pi[t_idx][modality_idx] == qo_pi_valid).all())

def test_expected_utility(self):
        """
        Test for the expected utility function, for a simple single factor generative model 
        where there are imbalances in the preferences for different outcomes. Test for both single
        timestep policy horizons and multiple timestep policy horizons (planning)
        """

        '''1-step policies'''
        num_states = [2]
        num_controls = [2]

        qs = utils.random_single_categorical(num_states)
        B = utils.construct_controllable_B(num_states, num_controls)

        # Single timestep
        n_step = 1
        policies = control.construct_policies(num_states, num_controls, policy_len=n_step)

        # Single observation modality
        num_obs = [2]

        # Create noiseless identity A matrix
        A = utils.to_obj_array(np.eye(num_obs[0]))

        # Create imbalance in preferences for observations
        C = utils.to_obj_array(utils.onehot(1, num_obs[0]))
        
        # Compute expected utility of policies
        expected_utilities = np.zeros(len(policies))
        for idx, policy in enumerate(policies):
            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)
            expected_utilities[idx] += control.calc_expected_utility(qo_pi, C)

        self.assertGreater(expected_utilities[1], expected_utilities[0])

        '''3-step policies'''
        # One policy entails going to state 0 two times in a row, and then state 2 at the end
        # Another policy entails going to state 1 three times in a row

        num_states = [3]
        num_controls = [3]

        qs = utils.random_single_categorical(num_states)
        B = utils.construct_controllable_B(num_states, num_controls)

        policies = [np.array([0, 0, 2]).reshape(-1, 1), np.array([1, 1, 1]).reshape(-1, 1)]

        # single observation modality
        num_obs = [3]

        # create noiseless identity A matrix
        A = utils.to_obj_array(np.eye(num_obs[0]))

        # create imbalance in preferences for observations
        # This test is designed to illustrate the emergence of planning by
        # using the time-integral of the expected free energy.
        # Even though the first observation (index 0) is the most preferred, the policy
        # that frequents this observation the most is actually not optimal, because that policy
        # terminates in a less preferred state by timestep 3.
        C = utils.to_obj_array(np.array([1.2, 1.0, 0.55]))

        expected_utilities = np.zeros(len(policies))
        for idx, policy in enumerate(policies):
            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)
            expected_utilities[idx] += control.calc_expected_utility(qo_pi, C)

        self.assertGreater(expected_utilities[1], expected_utilities[0])

def test_state_info_gain(self):
        """
        Test the states_info_gain function. 
        Function is tested by manipulating uncertainty in the likelihood matrices (A or B)
        in a ways that alternatively change the resolvability of uncertainty
        This is done with A) an imprecise expected state and a precise sensory mapping, 
        and B) high ambiguity and imprecise sensory mapping.
        """

        num_states = [2]
        num_controls = [2]

        # start with a precise initial state
        qs = utils.to_obj_array(utils.onehot(0, num_states[0]))

        '''Case study 1: Uncertain states, unambiguous observations'''
        # add some uncertainty into the consequences of the second policy, which
        # leads to increased epistemic value of observations, in case of pursuing
        # that policy -- this of course depends on a precise observation likelihood model
        B = utils.construct_controllable_B(num_states, num_controls)
        B[0][:, :, 1] = maths.softmax(B[0][:, :, 1]) # "noise-ify" the consequences of the 1-th action

        # single timestep
        n_step = 1
        policies = control.construct_policies(num_states, num_controls, policy_len=n_step)

        # single observation modality
        num_obs = [2]

        # create noiseless identity A matrix
        A = utils.to_obj_array(np.eye(num_obs[0]))

        state_info_gains = np.zeros(len(policies)) # store the Bayesian surprise / epistemic values of states here (AKA state info gain)
        for idx, policy in enumerate(policies):
            qs_pi = control.get_expected_states(qs, B, policy)
            state_info_gains[idx] += control.calc_states_info_gain(A, qs_pi)
        self.assertGreater(state_info_gains[1], state_info_gains[0])

        '''Case study 2: Uncertain states, ambiguous observations (for all states)'''
        # now we 'undo' the epistemic bonus of the second policy by making the A matrix
        # totally ambiguous; thus observations cannot resolve uncertainty about hidden states.
        # In this case, uncertainty in the posterior beliefs induced by Policy 1 doesn't tip the balance
        # of epistemic value, because uncertainty is irresolveable either way.
        A = utils.obj_array_uniform([ [num_obs[0], num_states[0]] ])

        state_info_gains = np.zeros(len(policies))
        for idx, policy in enumerate(policies):
            qs_pi = control.get_expected_states(qs, B, policy)
            state_info_gains[idx] += control.calc_states_info_gain(A, qs_pi)
        self.assertEqual(state_info_gains[0], state_info_gains[1])

        '''Case study 2: Uncertain states, ambiguous observations (for particular states)'''

        # create noiseless identity A matrix
        A = utils.to_obj_array(np.eye(num_obs[0]))

        # add some uncertainty into the consequences of the both policies
        B = utils.construct_controllable_B(num_states, num_controls)

        B[0][:, :, 0] = maths.softmax(B[0][:, :, 0]*2.0) # "noise-ify" the consequences of the 0-th action, but to a lesser extent than the 1-th action
        B[0][:, :, 1] = maths.softmax(B[0][:, :, 1]) # "noise-ify" the consequences of the 1-th action

        # Although in the presence of a precise likelihood mapping, 
        # Policy 1 would be preferred (due to higher resolve-able uncertainty, introduced by a noisier action-dependent B matrix),
        # if the expected observation likelihood of being in state 1 (the most likely consequence of Policy 1) is not precise, then 
        # Policy 0 (which has more probability loaded over state 0) will have more resolveable uncertainty, due to the
        # higher precision of the A matrix over that column (column 0, which is identity). Even though the expected density over states
        # is less noisy for policy 0.
        A[0][:,1] = maths.softmax(A[0][:,1]) 

        state_info_gains = np.zeros(len(policies))
        for idx, policy in enumerate(policies):
            qs_pi = control.get_expected_states(qs, B, policy)
            state_info_gains[idx] += control.calc_states_info_gain(A, qs_pi)
        self.assertGreater(state_info_gains[1], state_info_gains[0])

def test_state_info_gain_factorized(self):
        """ 
        Unit test the `calc_states_info_gain_factorized` function by qualitatively checking that in the T-Maze (contextual bandit)
        example, the state info gain is higher for the policy that leads to visiting the cue, which is higher than state info gain
        for visiting the bandit arm, which in turn is higher than the state info gain for the policy that leads to staying in the start state.
        """

        num_states = [2, 3]  
        num_obs = [3, 3, 3]
        num_controls = [1, 3]

        A_factor_list = [[0, 1], [0, 1], [1]] 
        
        A = utils.obj_array(len(num_obs))
        for m, obs in enumerate(num_obs):
            lagging_dimensions = [ns for i, ns in enumerate(num_states) if i in A_factor_list[m]]
            modality_shape = [obs] + lagging_dimensions
            A[m] = np.zeros(modality_shape)
            if m == 0:
                A[m][:, :, 0] = np.ones( (num_obs[m], num_states[0]) ) / num_obs[m]
                A[m][:, :, 1] = np.ones( (num_obs[m], num_states[0]) ) / num_obs[m]
                A[m][:, :, 2] = np.array([[0.9, 0.1], [0.0, 0.0], [0.1, 0.9]]) # cue statistics
            if m == 1:
                A[m][2, :, 0] = np.ones(num_states[0])
                A[m][0:2, :, 1] = np.array([[0.6, 0.4], [0.6, 0.4]]) # bandit statistics (mapping between reward-state (first hidden state factor) and rewards (Good vs Bad))
                A[m][2, :, 2] = np.ones(num_states[0])
            if m == 2:
                A[m] = np.eye(obs)

        qs_start = utils.obj_array_uniform(num_states)
        qs_start[1] = np.array([1., 0., 0.]) # agent believes it's in the start state

        state_info_gain_visit_start = 0.
        for m, A_m in enumerate(A):
            if len(A_factor_list[m]) == 1:
                qs_that_matter = utils.to_obj_array(qs_start[A_factor_list[m]])
            else:
                qs_that_matter = qs_start[A_factor_list[m]]
            state_info_gain_visit_start += control.calc_states_info_gain(A_m, [qs_that_matter])

        qs_arm = utils.obj_array_uniform(num_states)
        qs_arm[1] = np.array([0., 1., 0.]) # agent believes it's in the arm-visiting state

        state_info_gain_visit_arm = 0.
        for m, A_m in enumerate(A):
            if len(A_factor_list[m]) == 1:
                qs_that_matter = utils.to_obj_array(qs_arm[A_factor_list[m]])
            else:
                qs_that_matter = qs_arm[A_factor_list[m]]
            state_info_gain_visit_arm += control.calc_states_info_gain(A_m, [qs_that_matter])

        qs_cue = utils.obj_array_uniform(num_states)
        qs_cue[1] = np.array([0., 0., 1.]) # agent believes it's in the cue-visiting state

        state_info_gain_visit_cue = 0.
        for m, A_m in enumerate(A):
            if len(A_factor_list[m]) == 1:
                qs_that_matter = utils.to_obj_array(qs_cue[A_factor_list[m]])
            else:
                qs_that_matter = qs_cue[A_factor_list[m]]
            state_info_gain_visit_cue += control.calc_states_info_gain(A_m, [qs_that_matter])
        
        self.assertGreater(state_info_gain_visit_arm, state_info_gain_visit_start)
        self.assertGreater(state_info_gain_visit_cue, state_info_gain_visit_arm)

def test_pA_info_gain(self):
        """
        Test the pA_info_gain function. Demonstrates operation
        by manipulating shape of the Dirichlet priors over likelihood parameters
        (pA), which affects information gain for different expected observations
        """

        num_states = [2]
        num_controls = [2]

        # start with a precise initial state
        qs = utils.to_obj_array(utils.onehot(0, num_states[0]))

        B = utils.construct_controllable_B(num_states, num_controls)

        # single timestep
        n_step = 1
        policies = control.construct_policies(num_states, num_controls, policy_len=n_step)

        # single observation modality
        num_obs = [2]

        # create noiseless identity A matrix
        A = utils.to_obj_array(np.eye(num_obs[0]))

        # create prior over dirichlets such that there is a skew
        # in the parameters about the likelihood mapping from the
        # second hidden state (index 1) to observations, such that
        # Observation 0 is believed to be more likely than the other, conditioned on State 1.
        # Therefore sampling observations conditioned on State 1 would afford high info gain
        # about parameters, for that part of the likelhood distribution.

        pA = utils.obj_array_ones([ [num_obs[0], num_states[0]]] )
        pA[0][0, 1] += 1.0

        pA_info_gains = np.zeros(len(policies))
        for idx, policy in enumerate(policies):
            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)
            pA_info_gains[idx] += control.calc_pA_info_gain(pA, qo_pi, qs_pi).item()

        self.assertGreater(pA_info_gains[1], pA_info_gains[0])

        """ Test the factorized version of the pA_info_gain function. """
        pA_info_gains_fac = np.zeros(len(policies))
        for idx, policy in enumerate(policies):
            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs_factorized(qs_pi, A, A_factor_list=[[0]])
            pA_info_gains_fac[idx] += control.calc_pA_info_gain_factorized(pA, qo_pi, qs_pi, A_factor_list=[[0]]).item()

        self.assertTrue(np.allclose(pA_info_gains_fac,  pA_info_gains))

def test_pB_info_gain(self):
        """
        Test the pB_info_gain function. Demonstrates operation
        by manipulating shape of the Dirichlet priors over likelihood parameters
        (pB), which affects information gain for different states
        """
        num_states = [2]
        num_controls = [2]

        # start with a precise initial state
        qs = utils.to_obj_array(utils.onehot(0, num_states[0]))

        B = utils.construct_controllable_B(num_states, num_controls)

        pB = utils.obj_array_ones([ [num_states[0], num_states[0], num_controls[0]] ])

        # create prior over dirichlets such that there is a skew
        # in the parameters about the likelihood mapping from the
        # hidden states to hidden states under the second action,
        # such that hidden state 0 is considered to be more likely than the other,
        # given the action in question
        # Therefore taking that action would yield an expected state that afford
        # high information gain about that part of the likelihood distribution.
        #
        pB[0][0, :, 1] += 1.0

        # single timestep
        n_step = 1
        policies = control.construct_policies(num_states, num_controls, policy_len=n_step)

        pB_info_gains = np.zeros(len(policies))
        for idx, policy in enumerate(policies):
            qs_pi = control.get_expected_states(qs, B, policy)
            pB_info_gains[idx] += control.calc_pB_info_gain(pB, qs_pi, qs, policy)
        self.assertGreater(pB_info_gains[1], pB_info_gains[0])

        B_factor_list = [[0]]
        pB_info_gains_interactions = np.zeros(len(policies))
        for idx, policy in enumerate(policies):
            qs_pi = control.get_expected_states_interactions(qs, B, B_factor_list, policy)
            pB_info_gains_interactions[idx] += control.calc_pB_info_gain_interactions(pB, qs_pi, qs, B_factor_list, policy)
        self.assertTrue(np.allclose(pB_info_gains_interactions, pB_info_gains))

def test_update_posterior_policies_utility(self):
        """
        Tests the refactored (Categorical-less) version of `update_posterior_policies`, using only the expected utility component of the expected free energy
        """

        '''Test with single observation modality, single hidden state factor and single timestep'''

        num_obs = [3]
        num_states = [3]
        num_controls = [3]

        qs = utils.obj_array_uniform(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros(num_obs)
        C[0][0] = 1.0  
        C[0][1] = -2.0  

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = False,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            gamma=16.0
        )

        factor_idx = 0
        modality_idx = 0
        t_idx = 0

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            
            qo_pi = control.get_expected_obs(qs_pi, A)

            lnC = maths.spm_log_single(maths.softmax(C[modality_idx][:, np.newaxis]))
            efe_valid[idx] += qo_pi[t_idx][modality_idx].dot(lnC).item()
        
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

        '''Test with multiple observation modalities, multiple hidden state factors and single timestep'''

        num_obs = [3, 3]
        num_states = [3, 2]
        num_controls = [3, 1]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros(num_obs)
        C[0][0] = 1.0  
        C[0][1] = -2.0
        C[1][2] = 4.0  

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = False,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            gamma=16.0
        )

        t_idx = 0

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)

            for modality_idx in range(len(A)):
                lnC = maths.spm_log_single(maths.softmax(C[modality_idx][:, np.newaxis]))
                efe_valid[idx] += qo_pi[t_idx][modality_idx].dot(lnC).item()
        
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

        '''Test with multiple observation modalities, multiple hidden state factors and multiple timesteps'''

        num_obs = [3, 3]
        num_states = [3, 2]
        num_controls = [3, 1]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros(num_obs)
        C[0][0] = 1.0  
        C[0][1] = -2.0
        C[1][2] = 4.0  

        policies = control.construct_policies(num_states, num_controls, policy_len=3)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = False,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            gamma=16.0
        )

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)

            for t_idx in range(3):
                for modality_idx in range(len(A)):
                    lnC = maths.spm_log_single(maths.softmax(C[modality_idx][:, np.newaxis]))
                    efe_valid[idx] += qo_pi[t_idx][modality_idx].dot(lnC).item()
        
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

def test_temporal_C_matrix(self):
        """ Unit-tests for preferences that change over time """

        '''Test with single observation modality, single hidden state factor and single timestep, and non-temporal C vector'''

        num_obs = [3]
        num_states = [3]
        num_controls = [3]

        qs = utils.obj_array_uniform(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros(num_obs)
        C[0][0] = 1.0  
        C[0][1] = -2.0  

        policies = control.construct_policies(num_states, num_controls, policy_len=3)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = False,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            gamma=16.0
        )

        factor_idx = 0
        modality_idx = 0
        t_idx = 0

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)

            for t_idx in range(3):
                for modality_idx in range(len(A)):
                    lnC = maths.spm_log_single(maths.softmax(C[modality_idx][:, np.newaxis]))
                    efe_valid[idx] += qo_pi[t_idx][modality_idx].dot(lnC).item()

        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

        '''Test with single observation modality, single hidden state factor and single timestep, and temporal C vector'''

        num_obs = [3]
        num_states = [3]
        num_controls = [3]

        qs = utils.obj_array_uniform(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros([(3,3)])
        C[0][0,:] = np.array([1.0, 2.0, 0.0])
        C[0][1,:] = np.array([-2.0, -1.0, 0.0])  

        policies = control.construct_policies(num_states, num_controls, policy_len=3)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = False,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            gamma=16.0
        )

        factor_idx = 0
        modality_idx = 0
        t_idx = 0

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)

            for t_idx in range(3):
                for modality_idx in range(len(A)):
                    lnC = maths.spm_log_single(maths.softmax(C[modality_idx][:, t_idx]))
                    efe_valid[idx] += qo_pi[t_idx][modality_idx].dot(lnC).item()

        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

        '''Test with multiple observation modalities, multiple hidden state factors and multiple timesteps'''

        num_obs = [3, 3]
        num_states = [3, 2]
        num_controls = [3, 1]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array(len(num_obs))

        # C vectors for modalities 0 is time-dependent
        C[0] = np.random.rand(3, 3) 

        # C vectors for modalities 1 is time-independent
        C[1] = np.random.rand(3)

        policies = control.construct_policies(num_states, num_controls, policy_len=3)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = False,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            gamma=16.0
        )

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)

            for t_idx in range(3):
                for modality_idx in range(len(A)):
                    if modality_idx == 0:
                        lnC = maths.spm_log_single(maths.softmax(C[modality_idx][:, t_idx]))
                    elif modality_idx == 1:
                        lnC = maths.spm_log_single(maths.softmax(C[modality_idx][:, np.newaxis]))
                    efe_valid[idx] += qo_pi[t_idx][modality_idx].dot(lnC).item()
        
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

def test_update_posterior_policies_states_infogain(self):
        """
        Tests the refactored (Categorical-less) version of `update_posterior_policies`, using only the information gain (about states) component of the expected free energy
        """

        '''Test with single observation modality, single hidden state factor and single timestep'''

        num_obs = [3]
        num_states = [3]
        num_controls = [3]

        qs = utils.obj_array_uniform(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros(num_obs)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = False,
            use_states_info_gain = True,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            gamma=16.0
        )

        factor_idx = 0
        modality_idx = 0
        t_idx = 0

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            
            efe_valid[idx] += maths.spm_MDP_G(A, qs_pi[0])
        
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

        '''Test with multiple observation modalities, multiple hidden state factors and single timestep'''

        num_obs = [3, 3]
        num_states = [3, 2]
        num_controls = [3, 1]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros(num_obs)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = False,
            use_states_info_gain = True,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            gamma=16.0
        )

        t_idx = 0

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)

            efe_valid[idx] += maths.spm_MDP_G(A, qs_pi[0])
        
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

        '''Test with multiple observation modalities, multiple hidden state factors and multiple timesteps'''

        num_obs = [3, 3]
        num_states = [3, 2]
        num_controls = [3, 1]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros(num_obs) 

        policies = control.construct_policies(num_states, num_controls, policy_len=3)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = False,
            use_states_info_gain = True,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            gamma=16.0
        )

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)

            for t_idx in range(3):
                efe_valid[idx] += maths.spm_MDP_G(A, qs_pi[t_idx])
    
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

def test_update_posterior_policies_pA_infogain(self):
        """
        Tests the refactored (Categorical-less) version of `update_posterior_policies`, using only the information gain (about likelihood parameters) component of the expected free energy
        """

        '''Test with single observation modality, single hidden state factor and single timestep'''

        num_obs = [3]
        num_states = [3]
        num_controls = [3]

        qs = utils.obj_array_uniform(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])

        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros(num_obs)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = False,
            use_states_info_gain = False,
            use_param_info_gain = True,
            pA=pA,
            pB=None,
            gamma=16.0
        )

        factor_idx = 0
        modality_idx = 0
        t_idx = 0

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)
            
            efe_valid[idx] += control.calc_pA_info_gain(pA, qo_pi, qs_pi).item()
        
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

        '''Test with multiple observation modalities, multiple hidden state factors and single timestep'''

        num_obs = [3, 3]
        num_states = [3, 2]
        num_controls = [3, 1]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])

        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros(num_obs)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = False,
            use_states_info_gain = False,
            use_param_info_gain = True,
            pA=pA,
            pB=None,
            gamma=16.0
        )

        t_idx = 0

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)
            
            efe_valid[idx] += control.calc_pA_info_gain(pA, qo_pi, qs_pi).item()
        
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

        '''Test with multiple observation modalities, multiple hidden state factors and multiple timesteps'''

        num_obs = [3, 3]
        num_states = [3, 2]
        num_controls = [3, 1]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])

        B = utils.random_B_matrix(num_states, num_controls)
        C = utils.obj_array_zeros(num_obs) 

        policies = control.construct_policies(num_states, num_controls, policy_len=3)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = False,
            use_states_info_gain = False,
            use_param_info_gain = True,
            pA=pA,
            pB=None,
            gamma=16.0
        )

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            qo_pi = control.get_expected_obs(qs_pi, A)

            efe_valid[idx] += control.calc_pA_info_gain(pA, qo_pi, qs_pi).item()
    
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

def test_update_posterior_policies_pB_infogain(self):
        """
        Tests the refactored (Categorical-less) version of `update_posterior_policies`, using only the information gain (about transition likelihood parameters) component of the expected free energy
        """

        '''Test with single observation modality, single hidden state factor and single timestep'''

        num_obs = [3]
        num_states = [3]
        num_controls = [3]

        qs = utils.obj_array_uniform(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        C = utils.obj_array_zeros(num_obs)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = False,
            use_states_info_gain = False,
            use_param_info_gain = True,
            pA=None,
            pB=pB,
            gamma=16.0
        )

        factor_idx = 0
        modality_idx = 0
        t_idx = 0

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            
            efe_valid[idx] += control.calc_pB_info_gain(pB, qs_pi, qs, policy)
        
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

        '''Test with multiple observation modalities, multiple hidden state factors and single timestep'''

        num_obs = [3, 3]
        num_states = [3, 2]
        num_controls = [3, 1]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])
        
        C = utils.obj_array_zeros(num_obs)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = False,
            use_states_info_gain = False,
            use_param_info_gain = True,
            pA=None,
            pB=pB,
            gamma=16.0
        )

        t_idx = 0

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)
            
            efe_valid[idx] += control.calc_pB_info_gain(pB, qs_pi, qs, policy)
        
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

        '''Test with multiple observation modalities, multiple hidden state factors and multiple timesteps'''

        num_obs = [3, 3]
        num_states = [3, 2]
        num_controls = [3, 1]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        C = utils.obj_array_zeros(num_obs) 

        policies = control.construct_policies(num_states, num_controls, policy_len=3)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = False,
            use_states_info_gain = False,
            use_param_info_gain = True,
            pA=None,
            pB=pB,
            gamma=16.0
        )

        efe_valid = np.zeros(len(policies))

        for idx, policy in enumerate(policies):

            qs_pi = control.get_expected_states(qs, B, policy)

            efe_valid[idx] += control.calc_pB_info_gain(pB, qs_pi, qs, policy)
    
        q_pi_valid = maths.softmax(efe_valid * 16.0)

        self.assertTrue(np.allclose(efe, efe_valid))
        self.assertTrue(np.allclose(q_pi, q_pi_valid))

def test_update_posterior_policies_factorized(self):
        """ 
        Test new update_posterior_policies_factorized function, just to make sure it runs through and outputs correct shapes
        """

        num_obs = [3, 3]
        num_states = [3, 2]
        num_controls = [3, 2]

        A_factor_list = [[0, 1], [1]]
        B_factor_list = [[0], [0, 1]]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states, A_factor_list=A_factor_list)
        B = utils.random_B_matrix(num_states, num_controls, B_factor_list=B_factor_list)
        C = utils.obj_array_zeros(num_obs)

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies_factorized(
            qs,
            A,
            B,
            C,
            A_factor_list,
            B_factor_list,
            policies,
            use_utility = True,
            use_states_info_gain = True,
            gamma=16.0
        )

        self.assertEqual(len(q_pi), len(policies))
        self.assertEqual(len(efe), len(policies))

        chosen_action = control.sample_action(q_pi, policies, num_controls, action_selection="deterministic")

def test_sample_action(self):
        """
        Tests the refactored (Categorical-less) version of `sample_action`
        """

        '''Test with single observation modality, single hidden state factor and single timestep'''

        num_obs = [3]
        num_states = [3]
        num_controls = [3]

        qs = utils.obj_array_uniform(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        C = utils.obj_array_zeros(num_obs)
        C[0][0] = 1.0  
        C[0][1] = -2.0

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = True,
            use_param_info_gain = True,
            pA=pA,
            pB=pB,
            gamma=16.0
        )

        factor_idx = 0
        modality_idx = 0
        t_idx = 0

        chosen_action = control.sample_action(q_pi, policies, num_controls, action_selection="deterministic")
        sampled_action = control.sample_action(q_pi, policies, num_controls, action_selection="stochastic", alpha=1.0)

        self.assertEqual(chosen_action.shape, sampled_action.shape)

        '''Test with multiple observation modalities, multiple hidden state factors and single timestep'''

        num_obs = [3, 4]
        num_states = [3, 4]
        num_controls = [3, 3]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        C = utils.obj_array_zeros(num_obs)
        C[0][0] = 1.0  
        C[0][1] = -2.0
        C[1][3] = 3.0

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = True,
            use_param_info_gain = True,
            pA=pA,
            pB=pB,
            gamma=16.0
        )

        chosen_action = control.sample_action(q_pi, policies, num_controls, action_selection="deterministic")
        sampled_action = control.sample_action(q_pi, policies, num_controls, action_selection="stochastic", alpha=1.0)

        self.assertEqual(chosen_action.shape, sampled_action.shape)

        '''Test with multiple observation modalities, multiple hidden state factors and multiple timesteps'''

        num_obs = [3, 4]
        num_states = [3, 4]
        num_controls = [3, 3]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        C = utils.obj_array_zeros(num_obs)
        C[0][0] = 1.0  
        C[0][1] = -2.0
        C[1][3] = 3.0

        policies = control.construct_policies(num_states, num_controls, policy_len=3)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = True,
            use_param_info_gain = True,
            pA=pA,
            pB=pB,
            gamma=16.0
        )

        chosen_action = control.sample_action(q_pi, policies, num_controls, action_selection="deterministic")
        sampled_action = control.sample_action(q_pi, policies, num_controls, action_selection="stochastic", alpha=1.0)

        self.assertEqual(chosen_action.shape, sampled_action.shape)


        '''Single observation modality, single (controllable) hidden state factor, 3-step policies. Using utility only'''
        # One policy entails going to state 0 two times in a row, and then state 2 at the end
        # Another policy entails going to state 1 three times in a row

        num_obs = [3]
        num_states = [3]
        num_controls = [3]

        qs = utils.random_single_categorical(num_states)
        B = utils.construct_controllable_B(num_states, num_controls)

        policies = [np.array([0, 0, 2]).reshape(-1, 1), np.array([1, 1, 1]).reshape(-1, 1)]

        # create noiseless identity A matrix
        A = utils.to_obj_array(np.eye(num_obs[0]))

        # create imbalance in preferences for observations
        # This test is designed to illustrate the emergence of planning by
        # using the time-integral of the expected free energy.
        # Even though the first observation (index 0) is the most preferred, the policy
        # that frequents this observation the most is actually not optimal, because that policy
        # terminates in a less preferred state by timestep 3.
        C = utils.to_obj_array(np.array([1.2, 1.0, 0.55]))

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = False,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            gamma=16.0
        )

        chosen_action = control.sample_action(q_pi, policies, num_controls, action_selection="deterministic")
        self.assertEqual(int(chosen_action[0]), 1)

def test_sample_policy(self):
        """
        Tests the action selection function where policies are sampled directly from posterior over policies `q_pi`
        """

        num_states = [3, 2]
        num_controls = [3, 2]

        policies = control.construct_policies(num_states, num_controls, policy_len=3)

        q_pi = utils.norm_dist(np.random.rand(len(policies)))
        best_policy = policies[np.argmax(q_pi)]

        selected_policy = control.sample_policy(q_pi, policies, num_controls)

        for factor_ii in range(len(num_controls)):
            self.assertEqual(selected_policy[factor_ii], best_policy[0,factor_ii])
        
        selected_policy_stochastic = control.sample_policy(q_pi, policies, num_controls, action_selection="stochastic",
                                                           alpha=1.0)
        self.assertEqual(selected_policy_stochastic.shape, selected_policy.shape)

def test_update_posterior_policies_withE_vector(self):
        """
        Test update posterior policies in the case that there is a prior over policies
        """

        """ Construct an explicit example where policy 0 is preferred based on utility,
        but action 2 also gets a bump in probability because of prior over policies
        """
        num_obs = [3]
        num_states = [3]
        num_controls = [3]

        qs = utils.to_obj_array(utils.onehot(0, num_states[0]))
        A = utils.to_obj_array(np.eye(num_obs[0]))
        B = utils.construct_controllable_B(num_states, num_controls)
        
        C = utils.to_obj_array(np.array([1.5, 1.0, 1.0]))

        D = utils.to_obj_array(utils.onehot(0, num_states[0]))
        E = np.array([0.05, 0.05, 0.9])

        policies = control.construct_policies(num_states, num_controls, policy_len=1)

        q_pi, efe = control.update_posterior_policies(
            qs,
            A,
            B,
            C,
            policies,
            use_utility = True,
            use_states_info_gain = False,
            use_param_info_gain = False,
            pA=None,
            pB=None,
            E = E,
            gamma=16.0
        )

        self.assertGreater(q_pi[0], q_pi[1])
        self.assertGreater(q_pi[2], q_pi[1])

def test_stochastic_action_unidimensional_control(self):
        """
        Test stochastic action sampling in case that one of the control states is one-dimensional.
        Due to a call to probabilities.squeeze() in an earlier version of utils.sample(), this was throwing an
        error due to the inability to use np.random.multinomial on an array with undefined length (an 'unsized' array)
        """
        
        num_states = [2, 2]
        num_controls = [2, 1]
        policies = control.construct_policies(num_states, num_controls = num_controls, policy_len=1)
        q_pi = utils.norm_dist(np.random.rand(len(policies)))
        sampled_action = control.sample_action(q_pi, policies, num_controls, action_selection="stochastic")
        self.assertEqual(sampled_action[1], 0)

        sampled_action = control.sample_action(q_pi, policies, num_controls, action_selection="deterministic")
        self.assertEqual(sampled_action[1], 0)

def test_deterministic_action_sampling_equal_value(self):
        """
        Test `deterministic` action sampling in the case that multiple actions have the same probability. 
        Desired behavior is that actions are randomly sampled from the subset of total actions that have the highest (but equal) probability.
        """

        num_states = [3]
        num_controls = [3]
        policies = control.construct_policies(num_states, num_controls = num_controls, policy_len=1)
        q_pi = np.array([0.4, 0.4, 0.2])

        seeds = [1923, 48323]

        sampled_action = control._sample_action_test(q_pi, policies, num_controls, action_selection="deterministic", seed=seeds[0])
        self.assertEqual(sampled_action[0], 0)

        sampled_action = control._sample_action_test(q_pi, policies, num_controls, action_selection="deterministic", seed=seeds[1])
        self.assertEqual(sampled_action[0], 1)

def test_deterministic_policy_selection_equal_value(self):
        """
        Test `deterministic` action sampling in the case that multiple actions have the same probability. 
        Desired behavior is that actions are randomly sampled from the subset of total actions that have the highest (but equal) probability.
        """

        num_states = [3]
        num_controls = [3]
        policies = control.construct_policies(num_states, num_controls = num_controls, policy_len=1)
        q_pi = np.array([0.1, 0.45, 0.45])

        seeds = [1923, 48323]

        sampled_action = control._sample_policy_test(q_pi, policies, num_controls, action_selection="deterministic", seed=seeds[0])
        self.assertEqual(sampled_action[0], 1)

        sampled_action = control._sample_policy_test(q_pi, policies, num_controls, action_selection="deterministic", seed=seeds[1])
        self.assertEqual(sampled_action[0], 2)

class TestWrappers(unittest.TestCase):

    def test_get_model_dimensions_from_labels(self):
        """
        Tests model dimension extraction from labels including observations, states and actions.
        """
        model_labels = {
            "observations": {
                "species_observation": [
                    "absent",
                    "present",
                ],
                "budget_observation": [
                    "high",
                    "medium",
                    "low",
                ],
            },
            "states": {
                "species_state": [
                    "extant",
                    "extinct",
                ],
            },
            "actions": {
                "conservation_action": [
                    "manage",
                    "survey",
                    "stop",
                ],
            },
        }

        want = Dimensions(
            num_observations=[2, 3],
            num_observation_modalities=2,
            num_states=[2],
            num_state_factors=1,
            num_controls=[3],
            num_control_factors=1,
        )

        got = get_model_dimensions_from_labels(model_labels)

        self.assertEqual(want.num_observations, got.num_observations)
        self.assertEqual(want.num_observation_modalities, got.num_observation_modalities)
        self.assertEqual(want.num_states, got.num_states)
        self.assertEqual(want.num_state_factors, got.num_state_factors)
        self.assertEqual(want.num_controls, got.num_controls)
        self.assertEqual(want.num_control_factors, got.num_control_factors)

def test_get_model_dimensions_from_labels(self):
        """
        Tests model dimension extraction from labels including observations, states and actions.
        """
        model_labels = {
            "observations": {
                "species_observation": [
                    "absent",
                    "present",
                ],
                "budget_observation": [
                    "high",
                    "medium",
                    "low",
                ],
            },
            "states": {
                "species_state": [
                    "extant",
                    "extinct",
                ],
            },
            "actions": {
                "conservation_action": [
                    "manage",
                    "survey",
                    "stop",
                ],
            },
        }

        want = Dimensions(
            num_observations=[2, 3],
            num_observation_modalities=2,
            num_states=[2],
            num_state_factors=1,
            num_controls=[3],
            num_control_factors=1,
        )

        got = get_model_dimensions_from_labels(model_labels)

        self.assertEqual(want.num_observations, got.num_observations)
        self.assertEqual(want.num_observation_modalities, got.num_observation_modalities)
        self.assertEqual(want.num_states, got.num_states)
        self.assertEqual(want.num_state_factors, got.num_state_factors)
        self.assertEqual(want.num_controls, got.num_controls)
        self.assertEqual(want.num_control_factors, got.num_control_factors)

class TestLearning(unittest.TestCase):

    def test_update_pA_single_factor_all(self):
        """
        Test for updating prior Dirichlet parameters over sensory likelihood (pA)
        in the case that all observation modalities are updated and the generative model 
        has a single hidden state factor
        """
        num_states = [3]
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        '''single observation modality'''
        num_obs = [4]
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])
        
        observation = utils.sample(maths.spm_dot(A[0], qs))

        pA_updated = learning.update_obs_likelihood_dirichlet(
            pA, A, observation, qs, lr=l_rate, modalities="all")
        validation_pA = pA[0] + l_rate * maths.spm_cross(utils.onehot(observation, num_obs[0]), qs)
        self.assertTrue(np.all(pA_updated[0] == validation_pA))

        '''multiple observation modalities'''
        num_obs = [3, 4]
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])
        
        observation = [utils.sample(maths.spm_dot(A_m, qs)) for A_m in A]

        pA_updated = learning.update_obs_likelihood_dirichlet(
            pA, A, observation, qs, lr=l_rate, modalities="all")

        for modality, obs_dim in enumerate(num_obs):
            update = maths.spm_cross(utils.onehot(observation[modality], obs_dim), qs)
            validation_pA = pA[modality] + l_rate * update
            self.assertTrue(np.all(pA_updated[modality] == validation_pA))

    def test_update_pA_single_factor_one_modality(self):
        """
        Test for updating prior Dirichlet parameters over sensory likelihood (pA)
        in the case that ONE observation modalities is updated and the generative model 
        has a single hidden state factor
        """

        num_states = [3]
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        '''multiple observation modalities'''
        num_obs = [3, 4]

        modality_to_update = [np.random.randint(len(num_obs))]
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])
        
        observation = [utils.sample(maths.spm_dot(A_m, qs)) for A_m in A]

        pA_updated = learning.update_obs_likelihood_dirichlet(
            pA, A, observation, qs, lr=l_rate, modalities=modality_to_update)

        for modality, obs_dim in enumerate(num_obs):
            if modality in modality_to_update:
                update = maths.spm_cross(utils.onehot(observation[modality], obs_dim), qs)
                validation_pA = pA[modality] + l_rate * update
            else:
                validation_pA = pA[modality]
            self.assertTrue(np.all(pA_updated[modality] == validation_pA))
    
    def test_update_pA_single_factor_some_modalities(self):
        """
        Test for updating prior Dirichlet parameters over sensory likelihood (pA)
        in the case that some observation modalities are updated and the generative model 
        has a single hidden state factor
        """
        num_states = [3]
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0
        
        '''multiple observation modalities'''
        num_obs = [3, 4, 5]
        modalities_to_update = [0, 2]
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])

        observation = [utils.sample(maths.spm_dot(A_m, qs)) for A_m in A]

        pA_updated = learning.update_obs_likelihood_dirichlet(
            pA, A, observation, qs, lr=l_rate, modalities=modalities_to_update)

        for modality, obs_dim in enumerate(num_obs):
            if modality in modalities_to_update:
                update = maths.spm_cross(utils.onehot(observation[modality], obs_dim), qs)
                validation_pA = pA[modality] + l_rate * update
            else:
                validation_pA = pA[modality]
            self.assertTrue(np.all(pA_updated[modality] == validation_pA))
    
    def test_update_pA_multi_factor_all(self):
        """
        Test for updating prior Dirichlet parameters over sensory likelihood (pA)
        in the case that all observation modalities are updated and the generative model 
        has multiple hidden state factors
        """
        num_states = [2, 6]
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        # single observation modality
        num_obs = [4]
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])
        observation = [utils.sample(maths.spm_dot(A_m, qs)) for A_m in A]
        pA_updated = learning.update_obs_likelihood_dirichlet(
            pA, A, observation, qs, lr=l_rate, modalities="all")
        update = maths.spm_cross(utils.onehot(observation[0], num_obs[0]), qs)
        validation_pA = pA[0] + l_rate * update
        self.assertTrue(np.all(pA_updated[0] == validation_pA))

        # multiple observation modalities
        num_obs = [3, 4]
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])
        observation = [utils.sample(maths.spm_dot(A_m, qs)) for A_m in A]
        pA_updated = learning.update_obs_likelihood_dirichlet(
            pA, A, observation, qs, lr=l_rate, modalities="all")
        for modality, obs_dim in enumerate(num_obs):
            update = maths.spm_cross(utils.onehot(observation[modality], obs_dim), qs)
            validation_pA = pA[modality] + l_rate * update
            self.assertTrue(np.all(pA_updated[modality] == validation_pA))
    
    def test_update_pA_multi_factor_one_modality(self):
        """
        Test for updating prior Dirichlet parameters over sensory likelihood (pA)
        in the case that ONE observation modalities is updated and the generative model 
        has multiple hidden state factors
        """
        num_states = [2, 6]
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        # multiple observation modalities
        num_obs = [3, 4]
        modality_to_update = [np.random.randint(len(num_obs))]
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])
        observation = [utils.sample(maths.spm_dot(A_m, qs)) for A_m in A]
        pA_updated = learning.update_obs_likelihood_dirichlet(
            pA, A, observation, qs, lr=l_rate, modalities=modality_to_update)

        for modality, obs_dim in enumerate(num_obs):
            if modality in modality_to_update:
                update = maths.spm_cross(utils.onehot(observation[modality], obs_dim), qs)
                validation_pA = pA[modality] + l_rate * update
            else:
                validation_pA = pA[modality]
            self.assertTrue(np.all(pA_updated[modality] == validation_pA))
    
    def test_update_pA_multi_factor_some_modalities(self):
        """
        Test for updating prior Dirichlet parameters over sensory likelihood (pA)
        in the case that SOME observation modalities are updated and the generative model 
        has multiple hidden state factors
        """
        num_states = [2, 6]
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        # multiple observation modalities
        num_obs = [3, 4, 5]
        modalities_to_update = [0, 2]
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])
        observation = [utils.sample(maths.spm_dot(A_m, qs)) for A_m in A]
        pA_updated = learning.update_obs_likelihood_dirichlet(
            pA, A, observation, qs, lr=l_rate, modalities=modalities_to_update)

        for modality, obs_dim in enumerate(num_obs):
            if modality in modalities_to_update:
                update = maths.spm_cross(utils.onehot(observation[modality], obs_dim), qs)
                validation_pA = pA[modality] + l_rate * update
            else:
                validation_pA = pA[modality]
            self.assertTrue(np.all(pA_updated[modality] == validation_pA))
    
    def test_update_pA_diff_observation_formats(self):
        """
        Test for updating prior Dirichlet parameters over sensory likelihood (pA)
        in the case that observation is stored in various formats
        """

        num_states = [2, 6]
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        # multiple observation modalities
        num_obs = [3, 4, 5]
        modalities_to_update = "all"
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])

        observation_list = [0, 3, 2]

        pA_updated_1 = learning.update_obs_likelihood_dirichlet(
            pA, A, observation_list, qs, lr=l_rate, modalities=modalities_to_update)

        observation_tuple = (0, 3, 2)

        pA_updated_2 = learning.update_obs_likelihood_dirichlet(
            pA, A, observation_tuple, qs, lr=l_rate, modalities=modalities_to_update)
        
        observation_obj_array = utils.process_observation((0, 3, 2), len(num_obs), num_obs)

        pA_updated_3 = learning.update_obs_likelihood_dirichlet(
            pA, A, observation_obj_array, qs, lr=l_rate, modalities=modalities_to_update)

        for modality, _ in enumerate(num_obs):
            
            self.assertTrue(np.allclose(pA_updated_1[modality], pA_updated_2[modality]))
            self.assertTrue(np.allclose(pA_updated_1[modality], pA_updated_3[modality]))
       
        # now do the same for case of single modality

        num_states = [2, 6]
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        num_obs = [3]
        modalities_to_update = "all"
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.dirichlet_like(A)

        observation_int = 2

        pA_updated_1 = learning.update_obs_likelihood_dirichlet(
            pA, A, observation_int, qs, lr=l_rate, modalities=modalities_to_update)

        observation_onehot = utils.onehot(2, num_obs[0])

        pA_updated_2 = learning.update_obs_likelihood_dirichlet(
            pA, A, observation_onehot, qs, lr=l_rate, modalities=modalities_to_update)
        
        self.assertTrue(np.allclose(pA_updated_1[0], pA_updated_2[0]))
    
    def test_update_pA_factorized(self):
        """
        Test for `learning.update_obs_likelihood_dirichlet_factorized`, which is the learning function updating prior Dirichlet parameters over the sensory likelihood (pA) 
        in the case that the generative model is sparse and only some modalities depend on some hidden state factors
        """

        """ Test version with sparse conditional dependency graph (taking advantage of `A_factor_list` argument) """
        num_states = [2, 6, 5]
        num_obs = [3, 4, 5]
        A_factor_list = [[0], [1, 2], [0, 2]]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states, A_factor_list=A_factor_list)
        pA = utils.dirichlet_like(A, scale=1.0)
        observation = [np.random.randint(obs_dim) for obs_dim in num_obs]
        pA_updated_test = learning.update_obs_likelihood_dirichlet_factorized(
            pA, A, observation, qs, A_factor_list
            )

        for modality, obs_dim in enumerate(num_obs):
            update = maths.spm_cross(utils.onehot(observation[modality], obs_dim), qs[A_factor_list[modality]])
            pA_updated_valid_m = pA[modality] +  update
            self.assertTrue(np.allclose(pA_updated_test[modality], pA_updated_valid_m))

        """ Test version with full conditional dependency graph (not taking advantage of `A_factor_list` argument, but including it anyway) """
        num_states = [2, 6, 5]
        num_obs = [3, 4, 5]
        A_factor_list = len(num_obs) * [[0, 1, 2]]
        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)

        modalities_to_update = [0, 2]
        learning_rate = np.random.rand() # sample some positive learning rate

        pA = utils.dirichlet_like(A, scale=1.0)
        observation = [np.random.randint(obs_dim) for obs_dim in num_obs]
        pA_updated_test = learning.update_obs_likelihood_dirichlet_factorized(
            pA, A, observation, qs, A_factor_list, lr=learning_rate, modalities=modalities_to_update
            )

        pA_updated_valid = learning.update_obs_likelihood_dirichlet(
            pA, A, observation, qs, lr=learning_rate, modalities=modalities_to_update
            )

        for modality, obs_dim in enumerate(num_obs):
            self.assertTrue(np.allclose(pA_updated_test[modality], pA_updated_valid[modality]))

    def test_update_pB_single_factor_no_actions(self):
        """
        Test for updating prior Dirichlet parameters over transition likelihood (pB)
        in the case that the one and only hidden state factor is updated, and there 
        are no actions.
        """

        num_states = [3]
        num_controls = [1]  # this is how we encode the fact that there aren't any actions
        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated = learning.update_state_likelihood_dirichlet(
            pB, B, action, qs, qs_prev, lr=l_rate, factors="all"
        )

        validation_pB = utils.obj_array_ones([B_f.shape for B_f in B])
        validation_pB[0][:, :, 0] += (
            l_rate * maths.spm_cross(qs[0], qs_prev[0]) * (B[0][:, :, action[0]] > 0)
        )
        self.assertTrue(np.all(pB_updated[0] == validation_pB[0]))
    
    def test_update_pB_single_factor_with_actions(self):
        """
        Test for updating prior Dirichlet parameters over transition likelihood (pB)
        in the case that the one and only hidden state factor is updated, and there 
        are actions.
        """

        num_states = [3]
        num_controls = [3]
        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated = learning.update_state_likelihood_dirichlet(
            pB, B, action, qs, qs_prev, lr=l_rate, factors="all"
        )

        validation_pB = utils.obj_array_ones([B_f.shape for B_f in B])
        validation_pB[0][:, :, action[0]] += (
            l_rate * maths.spm_cross(qs[0], qs_prev[0]) * (B[0][:, :, action[0]] > 0)
        )
        self.assertTrue(np.all(pB_updated[0] == validation_pB[0]))

    def test_update_pB_multi_factor_no_actions_all_factors(self):
        """
        Test for updating prior Dirichlet parameters over transition likelihood (pB)
        in the case that there are mulitple hidden state factors, and there 
        are no actions. All factors are updated.
        """

        num_states = [3, 4]
        num_controls = [1, 1]
        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated = learning.update_state_likelihood_dirichlet(
            pB, B, action, qs, qs_prev, lr=l_rate, factors="all"
        )

        validation_pB = utils.obj_array_ones([B_f.shape for B_f in B])

        for factor, action_i in enumerate(action):
            validation_pB[factor][:, :, action_i] += (
                l_rate
                * maths.spm_cross(qs[factor], qs_prev[factor])
                * (B[factor][:, :, action_i] > 0)
            )
            self.assertTrue(np.all(pB_updated[factor] == validation_pB[factor]))
    
    def test_update_pB_multi_factor_no_actions_one_factor(self):
        """
        Test for updating prior Dirichlet parameters over transition likelihood (pB)
        in the case that there are mulitple hidden state factors, and there 
        are no actions. One factor is updated
        """

        num_states = [3, 4]
        num_controls = [1, 1]
        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        factors_to_update = [np.random.randint(len(num_states))]

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated = learning.update_state_likelihood_dirichlet(
            pB, B, action, qs, qs_prev, lr=l_rate, factors=factors_to_update
        )

        validation_pB = utils.obj_array_ones([B_f.shape for B_f in B])

        for factor, action_i in enumerate(action):

            if factor in factors_to_update:
                validation_pB[factor][:, :, action_i] += (
                    l_rate
                    * maths.spm_cross(qs[factor], qs_prev[factor])
                    * (B[factor][:, :, action_i] > 0)
                )
            self.assertTrue(np.all(pB_updated[factor] == validation_pB[factor]))
    
    def test_update_pB_multi_factor_no_actions_some_factors(self):
        """
        Test for updating prior Dirichlet parameters over transition likelihood (pB)
        in the case that there are mulitple hidden state factors, and there 
        are no actions. Some factors are updated.
        """

        num_states = [3, 4, 5]
        num_controls = [1, 1, 1]
        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        factors_to_update = [0, 2]

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated = learning.update_state_likelihood_dirichlet(
            pB, B, action, qs, qs_prev, lr=l_rate, factors=factors_to_update
        )

        validation_pB = utils.obj_array_ones([B_f.shape for B_f in B])

        for factor, action_i in enumerate(action):

            if factor in factors_to_update:
                validation_pB[factor][:, :, action_i] += (
                    l_rate
                    * maths.spm_cross(qs[factor], qs_prev[factor])
                    * (B[factor][:, :, action_i] > 0)
                )
            self.assertTrue(np.all(pB_updated[factor] == validation_pB[factor]))
    
    def test_update_pB_multi_factor_with_actions_all_factors(self):
        """
        Test for updating prior Dirichlet parameters over transition likelihood (pB)
        in the case that there are mulitple hidden state factors, and there 
        are actions. All factors are updated
        """

        num_states = [3, 4, 5]
        num_controls = [2, 3, 4]
        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated = learning.update_state_likelihood_dirichlet(
            pB, B, action, qs, qs_prev, lr=l_rate, factors="all"
        )

        validation_pB = utils.obj_array_ones([B_f.shape for B_f in B])

        for factor, action_i in enumerate(action):

            validation_pB[factor][:, :, action_i] += (
                l_rate
                * maths.spm_cross(qs[factor], qs_prev[factor])
                * (B[factor][:, :, action_i] > 0)
            )
            self.assertTrue(np.all(pB_updated[factor] == validation_pB[factor]))
    
    def test_update_pB_multi_factor_with_actions_one_factor(self):
        """
        Test for updating prior Dirichlet parameters over transition likelihood (pB)
        in the case that there are mulitple hidden state factors, and there 
        are actions. One factor is updated
        """

        num_states = [3, 4, 5]
        num_controls = [2, 3, 4]
        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        factors_to_update = [np.random.randint(len(num_states))]

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated = learning.update_state_likelihood_dirichlet(
            pB, B, action, qs, qs_prev, lr=l_rate, factors=factors_to_update
        )

        validation_pB = utils.obj_array_ones([B_f.shape for B_f in B])

        for factor, action_i in enumerate(action):
            
            if factor in factors_to_update:
                validation_pB[factor][:, :, action_i] += (
                    l_rate
                    * maths.spm_cross(qs[factor], qs_prev[factor])
                    * (B[factor][:, :, action_i] > 0)
                )
            self.assertTrue(np.all(pB_updated[factor] == validation_pB[factor]))
    
    def test_update_pB_multi_factor_with_actions_some_factors(self):
        """
        Test for updating prior Dirichlet parameters over transition likelihood (pB)
        in the case that there are mulitple hidden state factors, and there 
        are actions. Some factors are updated
        """

        num_states = [3, 4, 5]
        num_controls = [2, 3, 4]
        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        factors_to_update = [0, 1]

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated = learning.update_state_likelihood_dirichlet(
            pB, B, action, qs, qs_prev, lr=l_rate, factors=factors_to_update
        )

        validation_pB = utils.obj_array_ones([B_f.shape for B_f in B])

        for factor, action_i in enumerate(action):
            
            if factor in factors_to_update:
                validation_pB[factor][:, :, action_i] += (
                    l_rate
                    * maths.spm_cross(qs[factor], qs_prev[factor])
                    * (B[factor][:, :, action_i] > 0)
                )
            self.assertTrue(np.all(pB_updated[factor] == validation_pB[factor]))

    def test_update_pB_multi_factor_some_controllable_some_factors(self):
        """
        Test for updating prior Dirichlet parameters over transition likelihood (pB)
        in the case that there are mulitple hidden state factors, some of which 
        are controllable. Some factors are updated.
        """

        num_states = [3, 4, 5]
        num_controls = [2, 1, 1]
        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        factors_to_update = [0, 1]

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated = learning.update_state_likelihood_dirichlet(
            pB, B, action, qs, qs_prev, lr=l_rate, factors=factors_to_update
        )

        validation_pB = utils.obj_array_ones([B_f.shape for B_f in B])

        for factor, action_i in enumerate(action):
            
            if factor in factors_to_update:
                validation_pB[factor][:, :, action_i] += (
                    l_rate
                    * maths.spm_cross(qs[factor], qs_prev[factor])
                    * (B[factor][:, :, action_i] > 0)
                )
            self.assertTrue(np.all(pB_updated[factor] == validation_pB[factor]))
    
    def test_update_pB_interactions(self):
        """
        Test for `learning.update_state_likelihood_dirichlet_factorized`, which is the learning function updating prior Dirichlet parameters over the transition likelihood (pB) 
        in the case that there are allowable interactions between hidden state factors, i.e. the dynamics of factor `f` may depend on more than just its control factor and its own state.
        """

        """ Test version with interactions """
        num_states = [3, 4, 5]
        num_controls = [2, 1, 1]
        B_factor_list= [[0, 1], [0,1,2], [1, 2]]
        factors_to_update = [0, 1]

        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)

        B = utils.random_B_matrix(num_states, num_controls, B_factor_list=B_factor_list)
        pB = utils.dirichlet_like(B, scale=1.)
        l_rate = np.random.rand() # sample some positive learning rate

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated_test = learning.update_state_likelihood_dirichlet_interactions(
            pB, B, action, qs, qs_prev, B_factor_list, lr=l_rate, factors=factors_to_update
        )

        pB_updated_valid = utils.dirichlet_like(B, scale=1.)

        for factor, action_i in enumerate(action):
            
            if factor in factors_to_update:
                pB_updated_valid[factor][...,action_i] += (
                    l_rate
                    * maths.spm_cross(qs[factor], qs_prev[B_factor_list[factor]])
                    * (B[factor][...,action_i] > 0)
                )
            self.assertTrue(np.all(pB_updated_test[factor] == pB_updated_valid[factor]))

        """ Test version without interactions, but still use the factorized version to test it against the non-interacting version `update_state_likelihood_dirichlet` """
        num_states = [3, 4, 5]
        num_controls = [2, 1, 1]
        B_factor_list= [[0], [1], [2]]
        factors_to_update = [0, 1]

        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)

        B = utils.random_B_matrix(num_states, num_controls, B_factor_list=B_factor_list)
        pB = utils.dirichlet_like(B, scale=1.)
        l_rate = np.random.rand() # sample some positive learning rate

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated_test = learning.update_state_likelihood_dirichlet_interactions(
            pB, B, action, qs, qs_prev, B_factor_list, lr=l_rate, factors=factors_to_update
        )

        pB_updated_valid = learning.update_state_likelihood_dirichlet(
            pB, B, action, qs, qs_prev, lr=l_rate, factors=factors_to_update
        )

        for factor, action_i in enumerate(action):
            self.assertTrue(np.allclose(pB_updated_test[factor], pB_updated_valid[factor]))


    def test_update_pD(self):
        """
        Test updating prior Dirichlet parameters over initial hidden states (pD). 
        Tests different cases
        1. Multiple vs. single hidden state factor
        2. One factor vs. several factors vs. all factors learned
        """

        # 1. Single hidden state factor
        num_states = [3]

        pD = utils.dirichlet_like(utils.random_single_categorical(num_states), scale = 0.5)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        pD_test= learning.update_state_prior_dirichlet(
                        pD, qs, lr=l_rate, factors="all"
                    )
        
        for factor in range(len(num_states)):
            pD_validation_f = pD[factor].copy()
            idx = pD_validation_f > 0
            pD_validation_f[idx] += l_rate * qs[factor][idx]
            self.assertTrue(np.allclose(pD_test[factor], pD_validation_f))

        # 2. Multiple hidden state factors
        num_states = [3, 4, 5]

        pD = utils.dirichlet_like(utils.random_single_categorical(num_states), scale = 0.5)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        pD_test= learning.update_state_prior_dirichlet(
                        pD, qs, lr=l_rate, factors="all"
                    )
        
        for factor in range(len(num_states)):
            pD_validation_f = pD[factor].copy()
            idx = pD_validation_f > 0
            pD_validation_f[idx] += l_rate * qs[factor][idx]
            self.assertTrue(np.allclose(pD_test[factor], pD_validation_f))
        
        # 3. Multiple hidden state factors, only some learned
        num_states = [3, 4, 5]

        factors_to_learn = [0, 2]

        pD = utils.dirichlet_like(utils.random_single_categorical(num_states), scale = 0.5)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        pD_test= learning.update_state_prior_dirichlet(
                        pD, qs, lr=l_rate, factors=factors_to_learn
                    )
        
        pD_validation = deepcopy(pD)

        for factor in range(len(num_states)):

            if factor in factors_to_learn:
                idx = pD_validation[factor] > 0
                pD_validation[factor][idx] += l_rate * qs[factor][idx]

            self.assertTrue(np.allclose(pD_test[factor], pD_validation[factor]))
    
    def test_prune_prior(self):
        """
        Test removing hidden state factor levels and/or observation levels from the priors vectors
        of a generative model, using the `_prune_prior` function of the `learning` module
        """

        """ Test 1a. Testing `_prune_prior()` in case of a single hidden state factor/modality """

        num_levels_total = 4 # this could either be 4 hidden state levels, or 4 observation levels
        test_prior = utils.random_single_categorical([num_levels_total])[0]

        levels_to_remove = [2]

        reduced_prior = learning._prune_prior(test_prior, levels_to_remove)

        self.assertTrue(len(reduced_prior) == (num_levels_total - len(levels_to_remove)))
        self.assertTrue(utils.is_normalized(reduced_prior))

        """ Test 1b. Testing `_prune_prior()` in case of multiple hidden state factors/modalities """

        num_levels_total = [4, 5] # this could either be 4 hidden state levels, or 4 observation levels
        test_prior = utils.random_single_categorical(num_levels_total)

        levels_to_remove = [ [2, 3], []]

        reduced_prior = learning._prune_prior(test_prior, levels_to_remove)

        for f, ns in enumerate(num_levels_total):
            self.assertTrue(len(reduced_prior[f]) == (ns - len(levels_to_remove[f])))
            self.assertTrue(utils.is_normalized(reduced_prior[f]))
        
        """ Test 1c. Testing `_prune_prior()` in case of multiple hidden state factors/modalities, and where you're removing all the levels of a particular factor """

        num_levels_total = [4, 5] # this could either be 4 hidden state levels, or 4 observation levels
        test_prior = utils.random_single_categorical(num_levels_total)

        levels_to_remove = [ [2, 3], list(range(5))]

        reduced_prior = learning._prune_prior(test_prior, levels_to_remove)

        self.assertTrue(len(reduced_prior[0]) == (num_levels_total[0] - len(levels_to_remove[0])))
        self.assertTrue(utils.is_normalized(reduced_prior[0]))
    
        self.assertTrue(len(reduced_prior) == (len(levels_to_remove)-1))
    
    def test_prune_likelihoods(self):
        """
        Test removing hidden state factor levels and/or observation levels from the likelihood arrays 
        of a generative model, using the `_prune_A` and `_prune_B` functions of the `learning` module
        """

        """ Test 1a. Testing `_prune_A()` in case of a single hidden state factor/modality """

        A = utils.random_A_matrix([5], [4])[0]

        obs_levels_to_prune = [2, 3]
        state_levels_to_prune = [1, 3]

        A_pruned = learning._prune_A(A, obs_levels_to_prune, state_levels_to_prune)

        expected_shape = (A.shape[0] - len(obs_levels_to_prune), A.shape[1] - len(state_levels_to_prune))
        self.assertTrue(A_pruned.shape == expected_shape)
        self.assertTrue(utils.is_normalized(A_pruned))

        """ Test 1b. Testing `_prune_A()` in case of a single hidden state factor/modality, where hidden state levels aren't pruned at all """

        A = utils.random_A_matrix([5], [4])[0]

        obs_levels_to_prune = [2, 3]
        state_levels_to_prune = []

        A_pruned = learning._prune_A(A, obs_levels_to_prune, state_levels_to_prune)

        expected_shape = (A.shape[0] - len(obs_levels_to_prune), A.shape[1] - len(state_levels_to_prune))
        self.assertTrue(A_pruned.shape == expected_shape)
        self.assertTrue(utils.is_normalized(A_pruned))

        """ Test 1c. Testing `_prune_A()` in case of a single hidden state factor/modality, where observation levels aren't pruned at all """
        
        A = utils.random_A_matrix([5], [4])[0]

        obs_levels_to_prune = []
        state_levels_to_prune = [2,3]

        A_pruned = learning._prune_A(A, obs_levels_to_prune, state_levels_to_prune)

        expected_shape = (A.shape[0] - len(obs_levels_to_prune), A.shape[1] - len(state_levels_to_prune))
        self.assertTrue(A_pruned.shape == expected_shape)
        self.assertTrue(utils.is_normalized(A_pruned))

        """ Test 1d. Testing `_prune_A()` in case of a multiple hidden state factors/modalities """

        num_obs = [3, 4, 5]
        num_states = [2, 10, 4]
        A = utils.random_A_matrix(num_obs, num_states)

        obs_levels_to_prune = [ [0, 2], [], [1, 2, 3]]
        state_levels_to_prune = [[], [5,6,7,8], [1]]

        A_pruned = learning._prune_A(A, obs_levels_to_prune, state_levels_to_prune)

        expected_lagging_dimensions = []
        for f, ns in enumerate(num_states):
            expected_lagging_dimensions.append(ns - len(state_levels_to_prune[f]))
        for m, no in enumerate(num_obs):
            expected_shape = (no - len(obs_levels_to_prune[m]),) + tuple(expected_lagging_dimensions)
            self.assertTrue(A_pruned[m].shape == expected_shape)
            self.assertTrue(utils.is_normalized(A_pruned[m]))
        
        """ Test 2a. Testing `_prune_B()` in case of a single hidden state factor / control state factor """

        B = utils.random_B_matrix([4], [3])[0]

        state_levels_to_prune = [1, 3]
        action_levels_to_prune = [0, 1]

        B_pruned = learning._prune_B(B, state_levels_to_prune, action_levels_to_prune)

        expected_shape = (B.shape[0] - len(state_levels_to_prune), B.shape[1] - len(state_levels_to_prune), B.shape[2] - len(action_levels_to_prune))
        self.assertTrue(B_pruned.shape == expected_shape)
        self.assertTrue(utils.is_normalized(B_pruned))

        """ Test 2b. Testing `_prune_B()` in case of a single hidden state factor, where control state levels aren't pruned at all """

        B = utils.random_B_matrix([4], [3])[0]

        state_levels_to_prune = [1, 3]
        action_levels_to_prune = []

        B_pruned = learning._prune_B(B, state_levels_to_prune, action_levels_to_prune)

        expected_shape = (B.shape[0] - len(state_levels_to_prune), B.shape[1] - len(state_levels_to_prune), B.shape[2] - len(action_levels_to_prune))
        self.assertTrue(B_pruned.shape == expected_shape)
        self.assertTrue(utils.is_normalized(B_pruned))

        """ Test 1c. Testing `_prune_B()` in case of a single hidden state factor, where hidden state levels aren't pruned at all """
        
        B = utils.random_B_matrix([4], [3])[0]

        state_levels_to_prune = []
        action_levels_to_prune = [0]

        B_pruned = learning._prune_B(B, state_levels_to_prune, action_levels_to_prune)

        expected_shape = (B.shape[0] - len(state_levels_to_prune), B.shape[1] - len(state_levels_to_prune), B.shape[2] - len(action_levels_to_prune))
        self.assertTrue(B_pruned.shape == expected_shape)
        self.assertTrue(utils.is_normalized(B_pruned))
        
        """ Test 1d. Testing `_prune_B()` in case of a multiple hidden state factors """

        num_states = [2, 10, 4]
        num_controls = [5, 3, 4]
        B = utils.random_B_matrix(num_states, num_controls)

        state_levels_to_prune = [ [0, 1], [], [1, 2, 3]]
        action_levels_to_prune = [[], [0, 1], [1]]

        B_pruned = learning._prune_B(B, state_levels_to_prune, action_levels_to_prune)

        for f, ns in enumerate(num_states):
            expected_shape = (ns - len(state_levels_to_prune[f]), ns - len(state_levels_to_prune[f]), num_controls[f] - len(action_levels_to_prune[f]))
            self.assertTrue(B_pruned[f].shape == expected_shape)
            self.assertTrue(utils.is_normalized(B_pruned[f]))

def test_update_pA_single_factor_all(self):
        """
        Test for updating prior Dirichlet parameters over sensory likelihood (pA)
        in the case that all observation modalities are updated and the generative model 
        has a single hidden state factor
        """
        num_states = [3]
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        '''single observation modality'''
        num_obs = [4]
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])
        
        observation = utils.sample(maths.spm_dot(A[0], qs))

        pA_updated = learning.update_obs_likelihood_dirichlet(
            pA, A, observation, qs, lr=l_rate, modalities="all")
        validation_pA = pA[0] + l_rate * maths.spm_cross(utils.onehot(observation, num_obs[0]), qs)
        self.assertTrue(np.all(pA_updated[0] == validation_pA))

        '''multiple observation modalities'''
        num_obs = [3, 4]
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])
        
        observation = [utils.sample(maths.spm_dot(A_m, qs)) for A_m in A]

        pA_updated = learning.update_obs_likelihood_dirichlet(
            pA, A, observation, qs, lr=l_rate, modalities="all")

        for modality, obs_dim in enumerate(num_obs):
            update = maths.spm_cross(utils.onehot(observation[modality], obs_dim), qs)
            validation_pA = pA[modality] + l_rate * update
            self.assertTrue(np.all(pA_updated[modality] == validation_pA))

def test_update_pA_single_factor_one_modality(self):
        """
        Test for updating prior Dirichlet parameters over sensory likelihood (pA)
        in the case that ONE observation modalities is updated and the generative model 
        has a single hidden state factor
        """

        num_states = [3]
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        '''multiple observation modalities'''
        num_obs = [3, 4]

        modality_to_update = [np.random.randint(len(num_obs))]
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])
        
        observation = [utils.sample(maths.spm_dot(A_m, qs)) for A_m in A]

        pA_updated = learning.update_obs_likelihood_dirichlet(
            pA, A, observation, qs, lr=l_rate, modalities=modality_to_update)

        for modality, obs_dim in enumerate(num_obs):
            if modality in modality_to_update:
                update = maths.spm_cross(utils.onehot(observation[modality], obs_dim), qs)
                validation_pA = pA[modality] + l_rate * update
            else:
                validation_pA = pA[modality]
            self.assertTrue(np.all(pA_updated[modality] == validation_pA))

def test_update_pA_single_factor_some_modalities(self):
        """
        Test for updating prior Dirichlet parameters over sensory likelihood (pA)
        in the case that some observation modalities are updated and the generative model 
        has a single hidden state factor
        """
        num_states = [3]
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0
        
        '''multiple observation modalities'''
        num_obs = [3, 4, 5]
        modalities_to_update = [0, 2]
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])

        observation = [utils.sample(maths.spm_dot(A_m, qs)) for A_m in A]

        pA_updated = learning.update_obs_likelihood_dirichlet(
            pA, A, observation, qs, lr=l_rate, modalities=modalities_to_update)

        for modality, obs_dim in enumerate(num_obs):
            if modality in modalities_to_update:
                update = maths.spm_cross(utils.onehot(observation[modality], obs_dim), qs)
                validation_pA = pA[modality] + l_rate * update
            else:
                validation_pA = pA[modality]
            self.assertTrue(np.all(pA_updated[modality] == validation_pA))

def test_update_pA_multi_factor_all(self):
        """
        Test for updating prior Dirichlet parameters over sensory likelihood (pA)
        in the case that all observation modalities are updated and the generative model 
        has multiple hidden state factors
        """
        num_states = [2, 6]
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        # single observation modality
        num_obs = [4]
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])
        observation = [utils.sample(maths.spm_dot(A_m, qs)) for A_m in A]
        pA_updated = learning.update_obs_likelihood_dirichlet(
            pA, A, observation, qs, lr=l_rate, modalities="all")
        update = maths.spm_cross(utils.onehot(observation[0], num_obs[0]), qs)
        validation_pA = pA[0] + l_rate * update
        self.assertTrue(np.all(pA_updated[0] == validation_pA))

        # multiple observation modalities
        num_obs = [3, 4]
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])
        observation = [utils.sample(maths.spm_dot(A_m, qs)) for A_m in A]
        pA_updated = learning.update_obs_likelihood_dirichlet(
            pA, A, observation, qs, lr=l_rate, modalities="all")
        for modality, obs_dim in enumerate(num_obs):
            update = maths.spm_cross(utils.onehot(observation[modality], obs_dim), qs)
            validation_pA = pA[modality] + l_rate * update
            self.assertTrue(np.all(pA_updated[modality] == validation_pA))

def test_update_pA_multi_factor_one_modality(self):
        """
        Test for updating prior Dirichlet parameters over sensory likelihood (pA)
        in the case that ONE observation modalities is updated and the generative model 
        has multiple hidden state factors
        """
        num_states = [2, 6]
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        # multiple observation modalities
        num_obs = [3, 4]
        modality_to_update = [np.random.randint(len(num_obs))]
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])
        observation = [utils.sample(maths.spm_dot(A_m, qs)) for A_m in A]
        pA_updated = learning.update_obs_likelihood_dirichlet(
            pA, A, observation, qs, lr=l_rate, modalities=modality_to_update)

        for modality, obs_dim in enumerate(num_obs):
            if modality in modality_to_update:
                update = maths.spm_cross(utils.onehot(observation[modality], obs_dim), qs)
                validation_pA = pA[modality] + l_rate * update
            else:
                validation_pA = pA[modality]
            self.assertTrue(np.all(pA_updated[modality] == validation_pA))

def test_update_pA_multi_factor_some_modalities(self):
        """
        Test for updating prior Dirichlet parameters over sensory likelihood (pA)
        in the case that SOME observation modalities are updated and the generative model 
        has multiple hidden state factors
        """
        num_states = [2, 6]
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        # multiple observation modalities
        num_obs = [3, 4, 5]
        modalities_to_update = [0, 2]
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])
        observation = [utils.sample(maths.spm_dot(A_m, qs)) for A_m in A]
        pA_updated = learning.update_obs_likelihood_dirichlet(
            pA, A, observation, qs, lr=l_rate, modalities=modalities_to_update)

        for modality, obs_dim in enumerate(num_obs):
            if modality in modalities_to_update:
                update = maths.spm_cross(utils.onehot(observation[modality], obs_dim), qs)
                validation_pA = pA[modality] + l_rate * update
            else:
                validation_pA = pA[modality]
            self.assertTrue(np.all(pA_updated[modality] == validation_pA))

def test_update_pA_diff_observation_formats(self):
        """
        Test for updating prior Dirichlet parameters over sensory likelihood (pA)
        in the case that observation is stored in various formats
        """

        num_states = [2, 6]
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        # multiple observation modalities
        num_obs = [3, 4, 5]
        modalities_to_update = "all"
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.obj_array_ones([A_m.shape for A_m in A])

        observation_list = [0, 3, 2]

        pA_updated_1 = learning.update_obs_likelihood_dirichlet(
            pA, A, observation_list, qs, lr=l_rate, modalities=modalities_to_update)

        observation_tuple = (0, 3, 2)

        pA_updated_2 = learning.update_obs_likelihood_dirichlet(
            pA, A, observation_tuple, qs, lr=l_rate, modalities=modalities_to_update)
        
        observation_obj_array = utils.process_observation((0, 3, 2), len(num_obs), num_obs)

        pA_updated_3 = learning.update_obs_likelihood_dirichlet(
            pA, A, observation_obj_array, qs, lr=l_rate, modalities=modalities_to_update)

        for modality, _ in enumerate(num_obs):
            
            self.assertTrue(np.allclose(pA_updated_1[modality], pA_updated_2[modality]))
            self.assertTrue(np.allclose(pA_updated_1[modality], pA_updated_3[modality]))
       
        # now do the same for case of single modality

        num_states = [2, 6]
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        num_obs = [3]
        modalities_to_update = "all"
        A = utils.random_A_matrix(num_obs, num_states)
        pA = utils.dirichlet_like(A)

        observation_int = 2

        pA_updated_1 = learning.update_obs_likelihood_dirichlet(
            pA, A, observation_int, qs, lr=l_rate, modalities=modalities_to_update)

        observation_onehot = utils.onehot(2, num_obs[0])

        pA_updated_2 = learning.update_obs_likelihood_dirichlet(
            pA, A, observation_onehot, qs, lr=l_rate, modalities=modalities_to_update)
        
        self.assertTrue(np.allclose(pA_updated_1[0], pA_updated_2[0]))

def test_update_pA_factorized(self):
        """
        Test for `learning.update_obs_likelihood_dirichlet_factorized`, which is the learning function updating prior Dirichlet parameters over the sensory likelihood (pA) 
        in the case that the generative model is sparse and only some modalities depend on some hidden state factors
        """

        """ Test version with sparse conditional dependency graph (taking advantage of `A_factor_list` argument) """
        num_states = [2, 6, 5]
        num_obs = [3, 4, 5]
        A_factor_list = [[0], [1, 2], [0, 2]]

        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states, A_factor_list=A_factor_list)
        pA = utils.dirichlet_like(A, scale=1.0)
        observation = [np.random.randint(obs_dim) for obs_dim in num_obs]
        pA_updated_test = learning.update_obs_likelihood_dirichlet_factorized(
            pA, A, observation, qs, A_factor_list
            )

        for modality, obs_dim in enumerate(num_obs):
            update = maths.spm_cross(utils.onehot(observation[modality], obs_dim), qs[A_factor_list[modality]])
            pA_updated_valid_m = pA[modality] +  update
            self.assertTrue(np.allclose(pA_updated_test[modality], pA_updated_valid_m))

        """ Test version with full conditional dependency graph (not taking advantage of `A_factor_list` argument, but including it anyway) """
        num_states = [2, 6, 5]
        num_obs = [3, 4, 5]
        A_factor_list = len(num_obs) * [[0, 1, 2]]
        qs = utils.random_single_categorical(num_states)
        A = utils.random_A_matrix(num_obs, num_states)

        modalities_to_update = [0, 2]
        learning_rate = np.random.rand() # sample some positive learning rate

        pA = utils.dirichlet_like(A, scale=1.0)
        observation = [np.random.randint(obs_dim) for obs_dim in num_obs]
        pA_updated_test = learning.update_obs_likelihood_dirichlet_factorized(
            pA, A, observation, qs, A_factor_list, lr=learning_rate, modalities=modalities_to_update
            )

        pA_updated_valid = learning.update_obs_likelihood_dirichlet(
            pA, A, observation, qs, lr=learning_rate, modalities=modalities_to_update
            )

        for modality, obs_dim in enumerate(num_obs):
            self.assertTrue(np.allclose(pA_updated_test[modality], pA_updated_valid[modality]))

def test_update_pB_single_factor_no_actions(self):
        """
        Test for updating prior Dirichlet parameters over transition likelihood (pB)
        in the case that the one and only hidden state factor is updated, and there 
        are no actions.
        """

        num_states = [3]
        num_controls = [1]  # this is how we encode the fact that there aren't any actions
        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated = learning.update_state_likelihood_dirichlet(
            pB, B, action, qs, qs_prev, lr=l_rate, factors="all"
        )

        validation_pB = utils.obj_array_ones([B_f.shape for B_f in B])
        validation_pB[0][:, :, 0] += (
            l_rate * maths.spm_cross(qs[0], qs_prev[0]) * (B[0][:, :, action[0]] > 0)
        )
        self.assertTrue(np.all(pB_updated[0] == validation_pB[0]))

def test_update_pB_single_factor_with_actions(self):
        """
        Test for updating prior Dirichlet parameters over transition likelihood (pB)
        in the case that the one and only hidden state factor is updated, and there 
        are actions.
        """

        num_states = [3]
        num_controls = [3]
        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated = learning.update_state_likelihood_dirichlet(
            pB, B, action, qs, qs_prev, lr=l_rate, factors="all"
        )

        validation_pB = utils.obj_array_ones([B_f.shape for B_f in B])
        validation_pB[0][:, :, action[0]] += (
            l_rate * maths.spm_cross(qs[0], qs_prev[0]) * (B[0][:, :, action[0]] > 0)
        )
        self.assertTrue(np.all(pB_updated[0] == validation_pB[0]))

def test_update_pB_multi_factor_no_actions_all_factors(self):
        """
        Test for updating prior Dirichlet parameters over transition likelihood (pB)
        in the case that there are mulitple hidden state factors, and there 
        are no actions. All factors are updated.
        """

        num_states = [3, 4]
        num_controls = [1, 1]
        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated = learning.update_state_likelihood_dirichlet(
            pB, B, action, qs, qs_prev, lr=l_rate, factors="all"
        )

        validation_pB = utils.obj_array_ones([B_f.shape for B_f in B])

        for factor, action_i in enumerate(action):
            validation_pB[factor][:, :, action_i] += (
                l_rate
                * maths.spm_cross(qs[factor], qs_prev[factor])
                * (B[factor][:, :, action_i] > 0)
            )
            self.assertTrue(np.all(pB_updated[factor] == validation_pB[factor]))

def test_update_pB_multi_factor_no_actions_one_factor(self):
        """
        Test for updating prior Dirichlet parameters over transition likelihood (pB)
        in the case that there are mulitple hidden state factors, and there 
        are no actions. One factor is updated
        """

        num_states = [3, 4]
        num_controls = [1, 1]
        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        factors_to_update = [np.random.randint(len(num_states))]

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated = learning.update_state_likelihood_dirichlet(
            pB, B, action, qs, qs_prev, lr=l_rate, factors=factors_to_update
        )

        validation_pB = utils.obj_array_ones([B_f.shape for B_f in B])

        for factor, action_i in enumerate(action):

            if factor in factors_to_update:
                validation_pB[factor][:, :, action_i] += (
                    l_rate
                    * maths.spm_cross(qs[factor], qs_prev[factor])
                    * (B[factor][:, :, action_i] > 0)
                )
            self.assertTrue(np.all(pB_updated[factor] == validation_pB[factor]))

def test_update_pB_multi_factor_no_actions_some_factors(self):
        """
        Test for updating prior Dirichlet parameters over transition likelihood (pB)
        in the case that there are mulitple hidden state factors, and there 
        are no actions. Some factors are updated.
        """

        num_states = [3, 4, 5]
        num_controls = [1, 1, 1]
        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        factors_to_update = [0, 2]

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated = learning.update_state_likelihood_dirichlet(
            pB, B, action, qs, qs_prev, lr=l_rate, factors=factors_to_update
        )

        validation_pB = utils.obj_array_ones([B_f.shape for B_f in B])

        for factor, action_i in enumerate(action):

            if factor in factors_to_update:
                validation_pB[factor][:, :, action_i] += (
                    l_rate
                    * maths.spm_cross(qs[factor], qs_prev[factor])
                    * (B[factor][:, :, action_i] > 0)
                )
            self.assertTrue(np.all(pB_updated[factor] == validation_pB[factor]))

def test_update_pB_multi_factor_with_actions_all_factors(self):
        """
        Test for updating prior Dirichlet parameters over transition likelihood (pB)
        in the case that there are mulitple hidden state factors, and there 
        are actions. All factors are updated
        """

        num_states = [3, 4, 5]
        num_controls = [2, 3, 4]
        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated = learning.update_state_likelihood_dirichlet(
            pB, B, action, qs, qs_prev, lr=l_rate, factors="all"
        )

        validation_pB = utils.obj_array_ones([B_f.shape for B_f in B])

        for factor, action_i in enumerate(action):

            validation_pB[factor][:, :, action_i] += (
                l_rate
                * maths.spm_cross(qs[factor], qs_prev[factor])
                * (B[factor][:, :, action_i] > 0)
            )
            self.assertTrue(np.all(pB_updated[factor] == validation_pB[factor]))

def test_update_pB_multi_factor_with_actions_one_factor(self):
        """
        Test for updating prior Dirichlet parameters over transition likelihood (pB)
        in the case that there are mulitple hidden state factors, and there 
        are actions. One factor is updated
        """

        num_states = [3, 4, 5]
        num_controls = [2, 3, 4]
        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        factors_to_update = [np.random.randint(len(num_states))]

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated = learning.update_state_likelihood_dirichlet(
            pB, B, action, qs, qs_prev, lr=l_rate, factors=factors_to_update
        )

        validation_pB = utils.obj_array_ones([B_f.shape for B_f in B])

        for factor, action_i in enumerate(action):
            
            if factor in factors_to_update:
                validation_pB[factor][:, :, action_i] += (
                    l_rate
                    * maths.spm_cross(qs[factor], qs_prev[factor])
                    * (B[factor][:, :, action_i] > 0)
                )
            self.assertTrue(np.all(pB_updated[factor] == validation_pB[factor]))

def test_update_pB_multi_factor_with_actions_some_factors(self):
        """
        Test for updating prior Dirichlet parameters over transition likelihood (pB)
        in the case that there are mulitple hidden state factors, and there 
        are actions. Some factors are updated
        """

        num_states = [3, 4, 5]
        num_controls = [2, 3, 4]
        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        factors_to_update = [0, 1]

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated = learning.update_state_likelihood_dirichlet(
            pB, B, action, qs, qs_prev, lr=l_rate, factors=factors_to_update
        )

        validation_pB = utils.obj_array_ones([B_f.shape for B_f in B])

        for factor, action_i in enumerate(action):
            
            if factor in factors_to_update:
                validation_pB[factor][:, :, action_i] += (
                    l_rate
                    * maths.spm_cross(qs[factor], qs_prev[factor])
                    * (B[factor][:, :, action_i] > 0)
                )
            self.assertTrue(np.all(pB_updated[factor] == validation_pB[factor]))

def test_update_pB_multi_factor_some_controllable_some_factors(self):
        """
        Test for updating prior Dirichlet parameters over transition likelihood (pB)
        in the case that there are mulitple hidden state factors, some of which 
        are controllable. Some factors are updated.
        """

        num_states = [3, 4, 5]
        num_controls = [2, 1, 1]
        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        factors_to_update = [0, 1]

        B = utils.random_B_matrix(num_states, num_controls)
        pB = utils.obj_array_ones([B_f.shape for B_f in B])

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated = learning.update_state_likelihood_dirichlet(
            pB, B, action, qs, qs_prev, lr=l_rate, factors=factors_to_update
        )

        validation_pB = utils.obj_array_ones([B_f.shape for B_f in B])

        for factor, action_i in enumerate(action):
            
            if factor in factors_to_update:
                validation_pB[factor][:, :, action_i] += (
                    l_rate
                    * maths.spm_cross(qs[factor], qs_prev[factor])
                    * (B[factor][:, :, action_i] > 0)
                )
            self.assertTrue(np.all(pB_updated[factor] == validation_pB[factor]))

def test_update_pB_interactions(self):
        """
        Test for `learning.update_state_likelihood_dirichlet_factorized`, which is the learning function updating prior Dirichlet parameters over the transition likelihood (pB) 
        in the case that there are allowable interactions between hidden state factors, i.e. the dynamics of factor `f` may depend on more than just its control factor and its own state.
        """

        """ Test version with interactions """
        num_states = [3, 4, 5]
        num_controls = [2, 1, 1]
        B_factor_list= [[0, 1], [0,1,2], [1, 2]]
        factors_to_update = [0, 1]

        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)

        B = utils.random_B_matrix(num_states, num_controls, B_factor_list=B_factor_list)
        pB = utils.dirichlet_like(B, scale=1.)
        l_rate = np.random.rand() # sample some positive learning rate

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated_test = learning.update_state_likelihood_dirichlet_interactions(
            pB, B, action, qs, qs_prev, B_factor_list, lr=l_rate, factors=factors_to_update
        )

        pB_updated_valid = utils.dirichlet_like(B, scale=1.)

        for factor, action_i in enumerate(action):
            
            if factor in factors_to_update:
                pB_updated_valid[factor][...,action_i] += (
                    l_rate
                    * maths.spm_cross(qs[factor], qs_prev[B_factor_list[factor]])
                    * (B[factor][...,action_i] > 0)
                )
            self.assertTrue(np.all(pB_updated_test[factor] == pB_updated_valid[factor]))

        """ Test version without interactions, but still use the factorized version to test it against the non-interacting version `update_state_likelihood_dirichlet` """
        num_states = [3, 4, 5]
        num_controls = [2, 1, 1]
        B_factor_list= [[0], [1], [2]]
        factors_to_update = [0, 1]

        qs_prev = utils.random_single_categorical(num_states)
        qs = utils.random_single_categorical(num_states)

        B = utils.random_B_matrix(num_states, num_controls, B_factor_list=B_factor_list)
        pB = utils.dirichlet_like(B, scale=1.)
        l_rate = np.random.rand() # sample some positive learning rate

        action = np.array([np.random.randint(c_dim) for c_dim in num_controls])

        pB_updated_test = learning.update_state_likelihood_dirichlet_interactions(
            pB, B, action, qs, qs_prev, B_factor_list, lr=l_rate, factors=factors_to_update
        )

        pB_updated_valid = learning.update_state_likelihood_dirichlet(
            pB, B, action, qs, qs_prev, lr=l_rate, factors=factors_to_update
        )

        for factor, action_i in enumerate(action):
            self.assertTrue(np.allclose(pB_updated_test[factor], pB_updated_valid[factor]))

def test_update_pD(self):
        """
        Test updating prior Dirichlet parameters over initial hidden states (pD). 
        Tests different cases
        1. Multiple vs. single hidden state factor
        2. One factor vs. several factors vs. all factors learned
        """

        # 1. Single hidden state factor
        num_states = [3]

        pD = utils.dirichlet_like(utils.random_single_categorical(num_states), scale = 0.5)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        pD_test= learning.update_state_prior_dirichlet(
                        pD, qs, lr=l_rate, factors="all"
                    )
        
        for factor in range(len(num_states)):
            pD_validation_f = pD[factor].copy()
            idx = pD_validation_f > 0
            pD_validation_f[idx] += l_rate * qs[factor][idx]
            self.assertTrue(np.allclose(pD_test[factor], pD_validation_f))

        # 2. Multiple hidden state factors
        num_states = [3, 4, 5]

        pD = utils.dirichlet_like(utils.random_single_categorical(num_states), scale = 0.5)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        pD_test= learning.update_state_prior_dirichlet(
                        pD, qs, lr=l_rate, factors="all"
                    )
        
        for factor in range(len(num_states)):
            pD_validation_f = pD[factor].copy()
            idx = pD_validation_f > 0
            pD_validation_f[idx] += l_rate * qs[factor][idx]
            self.assertTrue(np.allclose(pD_test[factor], pD_validation_f))
        
        # 3. Multiple hidden state factors, only some learned
        num_states = [3, 4, 5]

        factors_to_learn = [0, 2]

        pD = utils.dirichlet_like(utils.random_single_categorical(num_states), scale = 0.5)
        qs = utils.random_single_categorical(num_states)
        l_rate = 1.0

        pD_test= learning.update_state_prior_dirichlet(
                        pD, qs, lr=l_rate, factors=factors_to_learn
                    )
        
        pD_validation = deepcopy(pD)

        for factor in range(len(num_states)):

            if factor in factors_to_learn:
                idx = pD_validation[factor] > 0
                pD_validation[factor][idx] += l_rate * qs[factor][idx]

            self.assertTrue(np.allclose(pD_test[factor], pD_validation[factor]))

def test_prune_prior(self):
        """
        Test removing hidden state factor levels and/or observation levels from the priors vectors
        of a generative model, using the `_prune_prior` function of the `learning` module
        """

        """ Test 1a. Testing `_prune_prior()` in case of a single hidden state factor/modality """

        num_levels_total = 4 # this could either be 4 hidden state levels, or 4 observation levels
        test_prior = utils.random_single_categorical([num_levels_total])[0]

        levels_to_remove = [2]

        reduced_prior = learning._prune_prior(test_prior, levels_to_remove)

        self.assertTrue(len(reduced_prior) == (num_levels_total - len(levels_to_remove)))
        self.assertTrue(utils.is_normalized(reduced_prior))

        """ Test 1b. Testing `_prune_prior()` in case of multiple hidden state factors/modalities """

        num_levels_total = [4, 5] # this could either be 4 hidden state levels, or 4 observation levels
        test_prior = utils.random_single_categorical(num_levels_total)

        levels_to_remove = [ [2, 3], []]

        reduced_prior = learning._prune_prior(test_prior, levels_to_remove)

        for f, ns in enumerate(num_levels_total):
            self.assertTrue(len(reduced_prior[f]) == (ns - len(levels_to_remove[f])))
            self.assertTrue(utils.is_normalized(reduced_prior[f]))
        
        """ Test 1c. Testing `_prune_prior()` in case of multiple hidden state factors/modalities, and where you're removing all the levels of a particular factor """

        num_levels_total = [4, 5] # this could either be 4 hidden state levels, or 4 observation levels
        test_prior = utils.random_single_categorical(num_levels_total)

        levels_to_remove = [ [2, 3], list(range(5))]

        reduced_prior = learning._prune_prior(test_prior, levels_to_remove)

        self.assertTrue(len(reduced_prior[0]) == (num_levels_total[0] - len(levels_to_remove[0])))
        self.assertTrue(utils.is_normalized(reduced_prior[0]))
    
        self.assertTrue(len(reduced_prior) == (len(levels_to_remove)-1))

def test_prune_likelihoods(self):
        """
        Test removing hidden state factor levels and/or observation levels from the likelihood arrays 
        of a generative model, using the `_prune_A` and `_prune_B` functions of the `learning` module
        """

        """ Test 1a. Testing `_prune_A()` in case of a single hidden state factor/modality """

        A = utils.random_A_matrix([5], [4])[0]

        obs_levels_to_prune = [2, 3]
        state_levels_to_prune = [1, 3]

        A_pruned = learning._prune_A(A, obs_levels_to_prune, state_levels_to_prune)

        expected_shape = (A.shape[0] - len(obs_levels_to_prune), A.shape[1] - len(state_levels_to_prune))
        self.assertTrue(A_pruned.shape == expected_shape)
        self.assertTrue(utils.is_normalized(A_pruned))

        """ Test 1b. Testing `_prune_A()` in case of a single hidden state factor/modality, where hidden state levels aren't pruned at all """

        A = utils.random_A_matrix([5], [4])[0]

        obs_levels_to_prune = [2, 3]
        state_levels_to_prune = []

        A_pruned = learning._prune_A(A, obs_levels_to_prune, state_levels_to_prune)

        expected_shape = (A.shape[0] - len(obs_levels_to_prune), A.shape[1] - len(state_levels_to_prune))
        self.assertTrue(A_pruned.shape == expected_shape)
        self.assertTrue(utils.is_normalized(A_pruned))

        """ Test 1c. Testing `_prune_A()` in case of a single hidden state factor/modality, where observation levels aren't pruned at all """
        
        A = utils.random_A_matrix([5], [4])[0]

        obs_levels_to_prune = []
        state_levels_to_prune = [2,3]

        A_pruned = learning._prune_A(A, obs_levels_to_prune, state_levels_to_prune)

        expected_shape = (A.shape[0] - len(obs_levels_to_prune), A.shape[1] - len(state_levels_to_prune))
        self.assertTrue(A_pruned.shape == expected_shape)
        self.assertTrue(utils.is_normalized(A_pruned))

        """ Test 1d. Testing `_prune_A()` in case of a multiple hidden state factors/modalities """

        num_obs = [3, 4, 5]
        num_states = [2, 10, 4]
        A = utils.random_A_matrix(num_obs, num_states)

        obs_levels_to_prune = [ [0, 2], [], [1, 2, 3]]
        state_levels_to_prune = [[], [5,6,7,8], [1]]

        A_pruned = learning._prune_A(A, obs_levels_to_prune, state_levels_to_prune)

        expected_lagging_dimensions = []
        for f, ns in enumerate(num_states):
            expected_lagging_dimensions.append(ns - len(state_levels_to_prune[f]))
        for m, no in enumerate(num_obs):
            expected_shape = (no - len(obs_levels_to_prune[m]),) + tuple(expected_lagging_dimensions)
            self.assertTrue(A_pruned[m].shape == expected_shape)
            self.assertTrue(utils.is_normalized(A_pruned[m]))
        
        """ Test 2a. Testing `_prune_B()` in case of a single hidden state factor / control state factor """

        B = utils.random_B_matrix([4], [3])[0]

        state_levels_to_prune = [1, 3]
        action_levels_to_prune = [0, 1]

        B_pruned = learning._prune_B(B, state_levels_to_prune, action_levels_to_prune)

        expected_shape = (B.shape[0] - len(state_levels_to_prune), B.shape[1] - len(state_levels_to_prune), B.shape[2] - len(action_levels_to_prune))
        self.assertTrue(B_pruned.shape == expected_shape)
        self.assertTrue(utils.is_normalized(B_pruned))

        """ Test 2b. Testing `_prune_B()` in case of a single hidden state factor, where control state levels aren't pruned at all """

        B = utils.random_B_matrix([4], [3])[0]

        state_levels_to_prune = [1, 3]
        action_levels_to_prune = []

        B_pruned = learning._prune_B(B, state_levels_to_prune, action_levels_to_prune)

        expected_shape = (B.shape[0] - len(state_levels_to_prune), B.shape[1] - len(state_levels_to_prune), B.shape[2] - len(action_levels_to_prune))
        self.assertTrue(B_pruned.shape == expected_shape)
        self.assertTrue(utils.is_normalized(B_pruned))

        """ Test 1c. Testing `_prune_B()` in case of a single hidden state factor, where hidden state levels aren't pruned at all """
        
        B = utils.random_B_matrix([4], [3])[0]

        state_levels_to_prune = []
        action_levels_to_prune = [0]

        B_pruned = learning._prune_B(B, state_levels_to_prune, action_levels_to_prune)

        expected_shape = (B.shape[0] - len(state_levels_to_prune), B.shape[1] - len(state_levels_to_prune), B.shape[2] - len(action_levels_to_prune))
        self.assertTrue(B_pruned.shape == expected_shape)
        self.assertTrue(utils.is_normalized(B_pruned))
        
        """ Test 1d. Testing `_prune_B()` in case of a multiple hidden state factors """

        num_states = [2, 10, 4]
        num_controls = [5, 3, 4]
        B = utils.random_B_matrix(num_states, num_controls)

        state_levels_to_prune = [ [0, 1], [], [1, 2, 3]]
        action_levels_to_prune = [[], [0, 1], [1]]

        B_pruned = learning._prune_B(B, state_levels_to_prune, action_levels_to_prune)

        for f, ns in enumerate(num_states):
            expected_shape = (ns - len(state_levels_to_prune[f]), ns - len(state_levels_to_prune[f]), num_controls[f] - len(action_levels_to_prune[f]))
            self.assertTrue(B_pruned[f].shape == expected_shape)
            self.assertTrue(utils.is_normalized(B_pruned[f]))

class TestUtils(unittest.TestCase):
    def test_obj_array_from_list(self):
        """
        Tests `obj_array_from_list`
        """
        # make arrays with same leading dimensions. naive method trigger numpy broadcasting error.
        arrs = [np.zeros((3, 6)), np.zeros((3, 4, 5))]
        obs_arrs = utils.obj_array_from_list(arrs)
        
        self.assertTrue(all([np.all(a == b) for a, b in zip(arrs, obs_arrs)]))

def test_obj_array_from_list(self):
        """
        Tests `obj_array_from_list`
        """
        # make arrays with same leading dimensions. naive method trigger numpy broadcasting error.
        arrs = [np.zeros((3, 6)), np.zeros((3, 4, 5))]
        obs_arrs = utils.obj_array_from_list(arrs)
        
        self.assertTrue(all([np.all(a == b) for a, b in zip(arrs, obs_arrs)]))

class TestDemos(unittest.TestCase):

    def test_agent_demo(self):
        """
        This unit test runs a more concise version of the
        code in the `agent_demo.ipynb` tutorial Jupyter notebook and the `agent_demo` Python script 
        to make sure the code works whenever we change something.
        """

        A, B, C, control_fac_idx = default_models.generate_epistemic_MAB_model()

        num_obs, num_states, num_modalities, num_factors = utils.get_model_dimensions(A = A, B = C)
       
        agent = Agent(A=A, B=B, C=C, control_fac_idx=control_fac_idx)

        # transition/observation matrices characterising the generative process
        A_gp = copy.deepcopy(A)
        B_gp = copy.deepcopy(B)

        # initial state
        T = 5 # number of timesteps in the simulation
        observation = [2, 2, 0] # initial observation -- no evidence for which arm is rewarding, neutral reward observation, and see themselves in the starting state
        state = [0, 0] # initial (true) state -- the reward condition is highly rewarding, and the true position in the 'start' position

        action_history = []

        for t in range(T):
    
            # update agent
            belief_state = agent.infer_states(observation)
            agent.infer_policies()
            action = agent.sample_action()

            action_history.append(action)
            
            # update environment
            for f, s in enumerate(state):
                state[f] = utils.sample(B_gp[f][:, s, int(action[f])])

            for g, _ in enumerate(observation):
                observation[g] = utils.sample(A_gp[g][:, state[0], state[1]])
        
        # make sure the first action is sampling
        # self.assertEqual(action_history[0][-1], 2) #  @NOTE: Stochastic sampling means this is not always true!!!

        # make sure the last action is playing
        # self.assertEqual(action_history[-1][-1], 1) # @NOTE: Stochastic sampling means this is not always true!!!
    
    def test_tmaze_demo(self):
        """
        This unit test runs the a concise version of the code in the `tmaze_demo.ipynb` tutorial notebook to make sure it works if things are changed
        """

        reward_probabilities = [0.98, 0.02] # probabilities used in the original SPM T-maze demo
        env = TMazeEnv(reward_probs = reward_probabilities)

        '''test plotting of the observation likelihood (just plot one slice)'''
        A_gp = env.get_likelihood_dist()
        # plot_likelihood(A_gp[1][:,:,0],'Reward Right')

        '''test plotting of the transition likelihood (just plot one slice)'''
        B_gp = env.get_transition_dist()
        # plot_likelihood(B_gp[1][:,:,0],'Reward Condition Transitions')

        A_gm = copy.deepcopy(A_gp) # make a copy of the true observation likelihood to initialize the observation model
        B_gm = copy.deepcopy(B_gp)# make a copy of the true transition likelihood to initialize the transition model
        
        control_fac_idx = [0]
        agent = Agent(A=A_gm, B=B_gm, control_fac_idx=control_fac_idx)
        # plot_beliefs(agent.D[0],"Beliefs about initial location")

        agent.C[1][1] = 3.0 # they like reward
        agent.C[1][2] = -3.0 # they don't like loss

        T = 5 # number of timesteps

        obs = env.reset() # reset the environment and get an initial observation

        # these are useful for displaying read-outs during the loop over time
        reward_conditions = ["Right", "Left"]
        location_observations = ['CENTER','RIGHT ARM','LEFT ARM','CUE LOCATION']
        reward_observations = ['No reward','Reward!','Loss!']
        cue_observations = ['Cue Right','Cue Left']
      
        for t in range(T):
            qx = agent.infer_states(obs)

            q_pi, G = agent.infer_policies()

            action = agent.sample_action()

            obs = env.step(action)

            if int(action[0]) == 3:
                
                # if the reward condition is Reward on RIGHT
                if env.reward_condition == 0:
                    self.assertEqual(obs[2], 0) # this tests that the cue observation is 'Cue Right' in case of 'Reward on Right' condition

                # if the reward condition is Reward on RIGHT
                if env.reward_condition == 1:
                    self.assertEqual(obs[2], 1) # this tests that the cue observation is 'Cue Left' in case of 'Reward on Left' condition

            
        # plot_beliefs(qx[1],"Final posterior beliefs about reward condition")
    
    def test_tmaze_learning_demo(self):
        """
        This unit test runs the a concise version of the code in the `tmaze_demo_learning.ipynb` tutorial notebook to make sure it works if things are changed
        """
        
        reward_probabilities = [0.85, 0.15] # the 'true' reward probabilities 
        env = TMazeEnvNullOutcome(reward_probs = reward_probabilities)
        A_gp = env.get_likelihood_dist()
        B_gp = env.get_transition_dist()

        pA = utils.dirichlet_like(A_gp, scale = 1e16)

        pA[1][1:,1:3,:] = 1.0

        A_gm = utils.norm_dist_obj_arr(pA) 

        B_gm = copy.deepcopy(B_gp)

        controllable_indices = [0] # this is a list of the indices of the hidden state factors that are controllable
        learnable_modalities = [1] # this is a list of the modalities that you want to be learn-able 

        agent = Agent(A=A_gm,pA=pA,B=B_gm,
              control_fac_idx=controllable_indices,
              modalities_to_learn=learnable_modalities,
              lr_pA = 0.25,
              use_param_info_gain=True)

        agent.D[0] = utils.onehot(0, agent.num_states[0])
        agent.C[1][1] = 2.0
        agent.C[1][2] = -2.0

        T = 1000 # number of timesteps

        obs = env.reset() # reset the environment and get an initial observation

        for t in range(T):
            agent.infer_states(obs)
            agent.infer_policies()
            action = agent.sample_action()
            agent.update_A(obs)     
            obs = env.step(action)
        
        # make sure they are learning the reward contingencies in the right general direction

        REWARD_ON_RIGHT = 0
        REWARD_ON_LEFT = 1

        REWARD = 1
        PUNISHMENT = 2

        RIGHT_ARM = 1
        LEFT_ARM = 2

        # in case the reward condition is 'Reward on RIGHT' 

        if env.reward_condition == REWARD_ON_RIGHT:

            prob_reward_right = agent.A[1][REWARD,RIGHT_ARM,REWARD_ON_RIGHT]
            prob_punishment_right = agent.A[1][PUNISHMENT,RIGHT_ARM,REWARD_ON_RIGHT]

            self.assertGreater(prob_reward_right, prob_punishment_right)

        # in case the reward condition is 'Reward on LEFT' 

        elif env.reward_condition == REWARD_ON_LEFT:

            prob_reward_left = agent.A[1][REWARD,LEFT_ARM,REWARD_ON_LEFT]
            prob_punishment_left = agent.A[1][PUNISHMENT,LEFT_ARM,REWARD_ON_LEFT]
            self.assertGreater(prob_reward_left, prob_punishment_left)

    def test_gridworld_genmodel_construction(self):
        """
        This unit test runs the a concise version of the code in the `gridworld_tutorial_1.ipynb` tutorial notebook to make sure it works if things are changed
        """

        state_mapping = {0: (0,0), 1: (1,0), 2: (2,0), 3: (0,1), 4: (1,1), 5:(2,1), 6: (0,2), 7:(1,2), 8:(2,2)}

        grid = np.zeros((3,3))
        for linear_index, xy_coordinates in state_mapping.items():
            x, y = xy_coordinates
            grid[y,x] = linear_index # rows are the y-coordinate, columns are the x-coordinate -- so we index into the grid we'll be visualizing using '[y, x]'
        fig = plt.figure(figsize = (3,3))
        sns.set(font_scale=1.5)
        sns.heatmap(grid, annot=True,  cbar = False, fmt='.0f', cmap='crest')

        A = np.eye(9)

        labels = [state_mapping[i] for i in range(A.shape[1])]

        # plot_likelihood(A)

        P = {}
        dim = 3
        actions = {'UP':0, 'RIGHT':1, 'DOWN':2, 'LEFT':3, 'STAY':4}

        for state_index, xy_coordinates in state_mapping.items():
            P[state_index] = {a : [] for a in range(len(actions))}
            x, y = xy_coordinates

            '''if your y-coordinate is all the way at the top (i.e. y == 0), you stay in the same place -- otherwise you move one upwards (achieved by subtracting 3 from your linear state index'''
            P[state_index][actions['UP']] = state_index if y == 0 else state_index - dim 

            '''f your x-coordinate is all the way to the right (i.e. x == 2), you stay in the same place -- otherwise you move one to the right (achieved by adding 1 to your linear state index)'''
            P[state_index][actions["RIGHT"]] = state_index if x == (dim -1) else state_index+1 

            '''if your y-coordinate is all the way at the bottom (i.e. y == 2), you stay in the same place -- otherwise you move one down (achieved by adding 3 to your linear state index)'''
            P[state_index][actions['DOWN']] = state_index if y == (dim -1) else state_index + dim 

            ''' if your x-coordinate is all the way at the left (i.e. x == 0), you stay at the same place -- otherwise, you move one to the left (achieved by subtracting 1 from your linear state index)'''
            P[state_index][actions['LEFT']] = state_index if x == 0 else state_index -1 

            ''' Stay in the same place (self explanatory) '''
            P[state_index][actions['STAY']] = state_index
        
        num_states = 9
        B = np.zeros([num_states, num_states, len(actions)])
        for s in range(num_states):
            for a in range(len(actions)):
                ns = int(P[s][a])
                B[ns, s, a] = 1
        
        self.assertTrue(B.shape[0] == 9)

        # fig, axes = plt.subplots(2,3, figsize = (15,8))
        # a = list(actions.keys())
        # count = 0
        # for i in range(dim-1):
        #     for j in range(dim):
        #         if count >= 5:
        #             break 
        #         g = sns.heatmap(B[:,:,count], cmap = "OrRd", linewidth = 2.5, cbar = False, ax = axes[i,j], xticklabels=labels, yticklabels=labels)
        #         g.set_title(a[count])
        #         count +=1 
        # fig.delaxes(axes.flatten()[5])
        # plt.tight_layout()
    
    def test_gridworld_activeinference(self):
        """
        This unit test runs the a concise version of the code in the `gridworld_tutorial_1.ipynb` tutorial notebook to make sure it works if things are changed
        """

        from pymdp.maths import spm_log_single as log_stable # @NOTE: we use the `spm_log_single` helper function from the `maths` sub-library of pymdp. This is a numerically stable version of np.log()

        state_mapping = {0: (0,0), 1: (1,0), 2: (2,0), 3: (0,1), 4: (1,1), 5:(2,1), 6: (0,2), 7:(1,2), 8:(2,2)}

        A = np.eye(9)
       
        labels = [state_mapping[i] for i in range(A.shape[1])]
       
        # def plot_empirical_prior(B):
        #     fig, axes = plt.subplots(3,2, figsize=(8, 10))
        #     actions = ['UP', 'RIGHT', 'DOWN', 'LEFT', 'STAY']
        #     count = 0
        #     for i in range(3):
        #         for j in range(2):
        #             if count >= 5:
        #                 break
                        
        #             g = sns.heatmap(B[:,:,count], cmap="OrRd", linewidth=2.5, cbar=False, ax=axes[i,j])

        #             g.set_title(actions[count])
        #             count += 1
        #     fig.delaxes(axes.flatten()[5])
        #     plt.tight_layout()
            
        # def plot_transition(B):
        #     fig, axes = plt.subplots(2,3, figsize = (15,8))
        #     a = list(actions.keys())
        #     count = 0
        #     for i in range(dim-1):
        #         for j in range(dim):
        #             if count >= 5:
        #                 break 
        #             g = sns.heatmap(B[:,:,count], cmap = "OrRd", linewidth = 2.5, cbar = False, ax = axes[i,j], xticklabels=labels, yticklabels=labels)
        #             g.set_title(a[count])
        #             count +=1 
        #     fig.delaxes(axes.flatten()[5])
        #     plt.tight_layout()
        
        A = np.eye(9)
        # plot_likelihood(A)

        P = {}
        dim = 3
        actions = {'UP':0, 'RIGHT':1, 'DOWN':2, 'LEFT':3, 'STAY':4}

        for state_index, xy_coordinates in state_mapping.items():
            P[state_index] = {a : [] for a in range(len(actions))}
            x, y = xy_coordinates

            '''if your y-coordinate is all the way at the top (i.e. y == 0), you stay in the same place -- otherwise you move one upwards (achieved by subtracting 3 from your linear state index'''
            P[state_index][actions['UP']] = state_index if y == 0 else state_index - dim 

            '''f your x-coordinate is all the way to the right (i.e. x == 2), you stay in the same place -- otherwise you move one to the right (achieved by adding 1 to your linear state index)'''
            P[state_index][actions["RIGHT"]] = state_index if x == (dim -1) else state_index+1 

            '''if your y-coordinate is all the way at the bottom (i.e. y == 2), you stay in the same place -- otherwise you move one down (achieved by adding 3 to your linear state index)'''
            P[state_index][actions['DOWN']] = state_index if y == (dim -1) else state_index + dim 

            ''' if your x-coordinate is all the way at the left (i.e. x == 0), you stay at the same place -- otherwise, you move one to the left (achieved by subtracting 1 from your linear state index)'''
            P[state_index][actions['LEFT']] = state_index if x == 0 else state_index -1 

            ''' Stay in the same place (self explanatory) '''
            P[state_index][actions['STAY']] = state_index

        
        num_states = 9
        B = np.zeros([num_states, num_states, len(actions)])
        for s in range(num_states):
            for a in range(len(actions)):
                ns = int(P[s][a])
                B[ns, s, a] = 1

        # plot_transition(B)
        
        class GridWorldEnv():
    
            def __init__(self,A,B):
                self.A = deepcopy(A)
                self.B = deepcopy(B)
                self.state = np.zeros(9)
                self.state[2] = 1
            
            def step(self,a):
                self.state = np.dot(self.B[:,:,a], self.state)
                obs = utils.sample(np.dot(self.A, self.state))
                return obs

            def reset(self):
                self.state =np.zeros(9)
                self.state[2] =1 
                obs = utils.sample(np.dot(self.A, self.state))
                return obs
        
        env = GridWorldEnv(A,B)

        def KL_divergence(q,p):
            return np.sum(q * (log_stable(q) - log_stable(p)))

        def compute_free_energy(q,A, B):
            return np.sum(q * (log_stable(q) - log_stable(A) - log_stable(B)))

        def softmax(x):
            return np.exp(x) / np.sum(np.exp(x))

        # def perform_inference(likelihood, prior):
        #     return softmax(log_stable(likelihood) + log_stable(prior))
        
        Qs = np.ones(9) * 1/9
        # plot_beliefs(Qs)

        REWARD_LOCATION = 7
        reward_state = state_mapping[REWARD_LOCATION]

        C = np.zeros(num_states)
        C[REWARD_LOCATION] = 1. 
        # plot_beliefs(C)

        def evaluate_policy(policy, Qs, A, B, C):
            # initialize expected free energy at 0
            G = 0

            # loop over policy
            for t in range(len(policy)):

                # get action entailed by the policy at timestep `t`
                u = int(policy[t].item())

                # work out expected state, given the action
                Qs_pi = B[:,:,u].dot(Qs)

                # work out expected observations, given the action
                Qo_pi = A.dot(Qs_pi)

                # get entropy
                H = - (A * log_stable(A)).sum(axis = 0)

                # get predicted divergence
                # divergence = np.sum(Qo_pi * (log_stable(Qo_pi) - log_stable(C)), axis=0)
                divergence = KL_divergence(Qo_pi, C)
                
                # compute the expected uncertainty or ambiguity 
                uncertainty = H.dot(Qs_pi)

                # increment the expected free energy counter for the policy, using the expected free energy at this timestep
                G += (divergence + uncertainty)

            return -G

        def infer_action(Qs, A, B, C, n_actions, policies):
    
            # initialize the negative expected free energy
            neg_G = np.zeros(len(policies))

            # loop over every possible policy and compute the EFE of each policy
            for i, policy in enumerate(policies):
                neg_G[i] = evaluate_policy(policy, Qs, A, B, C)

            # get distribution over policies
            Q_pi = maths.softmax(neg_G)

            # initialize probabilites of control states (convert from policies to actions)
            Qu = np.zeros(n_actions)

            # sum probabilites of control states or actions 
            for i, policy in enumerate(policies):
                # control state specified by policy
                u = int(policy[0].item())
                # add probability of policy
                Qu[u] += Q_pi[i]

            # normalize action marginal
            utils.norm_dist(Qu)

            # sample control from action marginal
            u = utils.sample(Qu)

            return u

        # number of time steps
        T = 10

        #n_actions = env.n_control
        n_actions = 5

        # length of policies we consider
        policy_len = 4

        # this function generates all possible combinations of policies
        policies = control.construct_policies([B.shape[0]], [n_actions], policy_len)

        # reset environment
        o = env.reset()

        # loop over time
        for t in range(T):

            # infer which action to take
            a = infer_action(Qs, A, B, C, n_actions, policies)
            
            # perform action in the environment and update the environment
            o = env.step(int(a))
            
            # infer new hidden state (this is the same equation as above but with PyMDP functions)
            likelihood = A[o,:]
            prior = B[:,:,int(a)].dot(Qs)

            Qs = maths.softmax(log_stable(likelihood) + log_stable(prior))
            
            # plot_beliefs(Qs, "Beliefs (Qs) at time {}".format(t))

        # self.assertEqual(np.argmax(Qs), REWARD_LOCATION) # @NOTE: This is not always true due to stochastic samplign!!!
        self.assertEqual(Qs.shape[0], B.shape[0])

def test_agent_demo(self):
        """
        This unit test runs a more concise version of the
        code in the `agent_demo.ipynb` tutorial Jupyter notebook and the `agent_demo` Python script 
        to make sure the code works whenever we change something.
        """

        A, B, C, control_fac_idx = default_models.generate_epistemic_MAB_model()

        num_obs, num_states, num_modalities, num_factors = utils.get_model_dimensions(A = A, B = C)
       
        agent = Agent(A=A, B=B, C=C, control_fac_idx=control_fac_idx)

        # transition/observation matrices characterising the generative process
        A_gp = copy.deepcopy(A)
        B_gp = copy.deepcopy(B)

        # initial state
        T = 5 # number of timesteps in the simulation
        observation = [2, 2, 0] # initial observation -- no evidence for which arm is rewarding, neutral reward observation, and see themselves in the starting state
        state = [0, 0] # initial (true) state -- the reward condition is highly rewarding, and the true position in the 'start' position

        action_history = []

        for t in range(T):
    
            # update agent
            belief_state = agent.infer_states(observation)
            agent.infer_policies()
            action = agent.sample_action()

            action_history.append(action)
            
            # update environment
            for f, s in enumerate(state):
                state[f] = utils.sample(B_gp[f][:, s, int(action[f])])

            for g, _ in enumerate(observation):
                observation[g] = utils.sample(A_gp[g][:, state[0], state[1]])

def test_tmaze_demo(self):
        """
        This unit test runs the a concise version of the code in the `tmaze_demo.ipynb` tutorial notebook to make sure it works if things are changed
        """

        reward_probabilities = [0.98, 0.02] # probabilities used in the original SPM T-maze demo
        env = TMazeEnv(reward_probs = reward_probabilities)

        '''test plotting of the observation likelihood (just plot one slice)'''
        A_gp = env.get_likelihood_dist()
        # plot_likelihood(A_gp[1][:,:,0],'Reward Right')

        '''test plotting of the transition likelihood (just plot one slice)'''
        B_gp = env.get_transition_dist()
        # plot_likelihood(B_gp[1][:,:,0],'Reward Condition Transitions')

        A_gm = copy.deepcopy(A_gp) # make a copy of the true observation likelihood to initialize the observation model
        B_gm = copy.deepcopy(B_gp)# make a copy of the true transition likelihood to initialize the transition model
        
        control_fac_idx = [0]
        agent = Agent(A=A_gm, B=B_gm, control_fac_idx=control_fac_idx)
        # plot_beliefs(agent.D[0],"Beliefs about initial location")

        agent.C[1][1] = 3.0 # they like reward
        agent.C[1][2] = -3.0 # they don't like loss

        T = 5 # number of timesteps

        obs = env.reset() # reset the environment and get an initial observation

        # these are useful for displaying read-outs during the loop over time
        reward_conditions = ["Right", "Left"]
        location_observations = ['CENTER','RIGHT ARM','LEFT ARM','CUE LOCATION']
        reward_observations = ['No reward','Reward!','Loss!']
        cue_observations = ['Cue Right','Cue Left']
      
        for t in range(T):
            qx = agent.infer_states(obs)

            q_pi, G = agent.infer_policies()

            action = agent.sample_action()

            obs = env.step(action)

            if int(action[0]) == 3:
                
                # if the reward condition is Reward on RIGHT
                if env.reward_condition == 0:
                    self.assertEqual(obs[2], 0) # this tests that the cue observation is 'Cue Right' in case of 'Reward on Right' condition

                # if the reward condition is Reward on RIGHT
                if env.reward_condition == 1:
                    self.assertEqual(obs[2], 1)

def test_tmaze_learning_demo(self):
        """
        This unit test runs the a concise version of the code in the `tmaze_demo_learning.ipynb` tutorial notebook to make sure it works if things are changed
        """
        
        reward_probabilities = [0.85, 0.15] # the 'true' reward probabilities 
        env = TMazeEnvNullOutcome(reward_probs = reward_probabilities)
        A_gp = env.get_likelihood_dist()
        B_gp = env.get_transition_dist()

        pA = utils.dirichlet_like(A_gp, scale = 1e16)

        pA[1][1:,1:3,:] = 1.0

        A_gm = utils.norm_dist_obj_arr(pA) 

        B_gm = copy.deepcopy(B_gp)

        controllable_indices = [0] # this is a list of the indices of the hidden state factors that are controllable
        learnable_modalities = [1] # this is a list of the modalities that you want to be learn-able 

        agent = Agent(A=A_gm,pA=pA,B=B_gm,
              control_fac_idx=controllable_indices,
              modalities_to_learn=learnable_modalities,
              lr_pA = 0.25,
              use_param_info_gain=True)

        agent.D[0] = utils.onehot(0, agent.num_states[0])
        agent.C[1][1] = 2.0
        agent.C[1][2] = -2.0

        T = 1000 # number of timesteps

        obs = env.reset() # reset the environment and get an initial observation

        for t in range(T):
            agent.infer_states(obs)
            agent.infer_policies()
            action = agent.sample_action()
            agent.update_A(obs)     
            obs = env.step(action)
        
        # make sure they are learning the reward contingencies in the right general direction

        REWARD_ON_RIGHT = 0
        REWARD_ON_LEFT = 1

        REWARD = 1
        PUNISHMENT = 2

        RIGHT_ARM = 1
        LEFT_ARM = 2

        # in case the reward condition is 'Reward on RIGHT' 

        if env.reward_condition == REWARD_ON_RIGHT:

            prob_reward_right = agent.A[1][REWARD,RIGHT_ARM,REWARD_ON_RIGHT]
            prob_punishment_right = agent.A[1][PUNISHMENT,RIGHT_ARM,REWARD_ON_RIGHT]

            self.assertGreater(prob_reward_right, prob_punishment_right)

        # in case the reward condition is 'Reward on LEFT' 

        elif env.reward_condition == REWARD_ON_LEFT:

            prob_reward_left = agent.A[1][REWARD,LEFT_ARM,REWARD_ON_LEFT]
            prob_punishment_left = agent.A[1][PUNISHMENT,LEFT_ARM,REWARD_ON_LEFT]
            self.assertGreater(prob_reward_left, prob_punishment_left)

def test_gridworld_genmodel_construction(self):
        """
        This unit test runs the a concise version of the code in the `gridworld_tutorial_1.ipynb` tutorial notebook to make sure it works if things are changed
        """

        state_mapping = {0: (0,0), 1: (1,0), 2: (2,0), 3: (0,1), 4: (1,1), 5:(2,1), 6: (0,2), 7:(1,2), 8:(2,2)}

        grid = np.zeros((3,3))
        for linear_index, xy_coordinates in state_mapping.items():
            x, y = xy_coordinates
            grid[y,x] = linear_index # rows are the y-coordinate, columns are the x-coordinate -- so we index into the grid we'll be visualizing using '[y, x]'
        fig = plt.figure(figsize = (3,3))
        sns.set(font_scale=1.5)
        sns.heatmap(grid, annot=True,  cbar = False, fmt='.0f', cmap='crest')

        A = np.eye(9)

        labels = [state_mapping[i] for i in range(A.shape[1])]

        # plot_likelihood(A)

        P = {}
        dim = 3
        actions = {'UP':0, 'RIGHT':1, 'DOWN':2, 'LEFT':3, 'STAY':4}

        for state_index, xy_coordinates in state_mapping.items():
            P[state_index] = {a : [] for a in range(len(actions))}
            x, y = xy_coordinates

            '''if your y-coordinate is all the way at the top (i.e. y == 0), you stay in the same place -- otherwise you move one upwards (achieved by subtracting 3 from your linear state index'''
            P[state_index][actions['UP']] = state_index if y == 0 else state_index - dim 

            '''f your x-coordinate is all the way to the right (i.e. x == 2), you stay in the same place -- otherwise you move one to the right (achieved by adding 1 to your linear state index)'''
            P[state_index][actions["RIGHT"]] = state_index if x == (dim -1) else state_index+1 

            '''if your y-coordinate is all the way at the bottom (i.e. y == 2), you stay in the same place -- otherwise you move one down (achieved by adding 3 to your linear state index)'''
            P[state_index][actions['DOWN']] = state_index if y == (dim -1) else state_index + dim 

            ''' if your x-coordinate is all the way at the left (i.e. x == 0), you stay at the same place -- otherwise, you move one to the left (achieved by subtracting 1 from your linear state index)'''
            P[state_index][actions['LEFT']] = state_index if x == 0 else state_index -1 

            ''' Stay in the same place (self explanatory) '''
            P[state_index][actions['STAY']] = state_index
        
        num_states = 9
        B = np.zeros([num_states, num_states, len(actions)])
        for s in range(num_states):
            for a in range(len(actions)):
                ns = int(P[s][a])
                B[ns, s, a] = 1
        
        self.assertTrue(B.shape[0] == 9)

def test_gridworld_activeinference(self):
        """
        This unit test runs the a concise version of the code in the `gridworld_tutorial_1.ipynb` tutorial notebook to make sure it works if things are changed
        """

        from pymdp.maths import spm_log_single as log_stable # @NOTE: we use the `spm_log_single` helper function from the `maths` sub-library of pymdp. This is a numerically stable version of np.log()

        state_mapping = {0: (0,0), 1: (1,0), 2: (2,0), 3: (0,1), 4: (1,1), 5:(2,1), 6: (0,2), 7:(1,2), 8:(2,2)}

        A = np.eye(9)
       
        labels = [state_mapping[i] for i in range(A.shape[1])]
       
        # def plot_empirical_prior(B):
        #     fig, axes = plt.subplots(3,2, figsize=(8, 10))
        #     actions = ['UP', 'RIGHT', 'DOWN', 'LEFT', 'STAY']
        #     count = 0
        #     for i in range(3):
        #         for j in range(2):
        #             if count >= 5:
        #                 break
                        
        #             g = sns.heatmap(B[:,:,count], cmap="OrRd", linewidth=2.5, cbar=False, ax=axes[i,j])

        #             g.set_title(actions[count])
        #             count += 1
        #     fig.delaxes(axes.flatten()[5])
        #     plt.tight_layout()
            
        # def plot_transition(B):
        #     fig, axes = plt.subplots(2,3, figsize = (15,8))
        #     a = list(actions.keys())
        #     count = 0
        #     for i in range(dim-1):
        #         for j in range(dim):
        #             if count >= 5:
        #                 break 
        #             g = sns.heatmap(B[:,:,count], cmap = "OrRd", linewidth = 2.5, cbar = False, ax = axes[i,j], xticklabels=labels, yticklabels=labels)
        #             g.set_title(a[count])
        #             count +=1 
        #     fig.delaxes(axes.flatten()[5])
        #     plt.tight_layout()
        
        A = np.eye(9)
        # plot_likelihood(A)

        P = {}
        dim = 3
        actions = {'UP':0, 'RIGHT':1, 'DOWN':2, 'LEFT':3, 'STAY':4}

        for state_index, xy_coordinates in state_mapping.items():
            P[state_index] = {a : [] for a in range(len(actions))}
            x, y = xy_coordinates

            '''if your y-coordinate is all the way at the top (i.e. y == 0), you stay in the same place -- otherwise you move one upwards (achieved by subtracting 3 from your linear state index'''
            P[state_index][actions['UP']] = state_index if y == 0 else state_index - dim 

            '''f your x-coordinate is all the way to the right (i.e. x == 2), you stay in the same place -- otherwise you move one to the right (achieved by adding 1 to your linear state index)'''
            P[state_index][actions["RIGHT"]] = state_index if x == (dim -1) else state_index+1 

            '''if your y-coordinate is all the way at the bottom (i.e. y == 2), you stay in the same place -- otherwise you move one down (achieved by adding 3 to your linear state index)'''
            P[state_index][actions['DOWN']] = state_index if y == (dim -1) else state_index + dim 

            ''' if your x-coordinate is all the way at the left (i.e. x == 0), you stay at the same place -- otherwise, you move one to the left (achieved by subtracting 1 from your linear state index)'''
            P[state_index][actions['LEFT']] = state_index if x == 0 else state_index -1 

            ''' Stay in the same place (self explanatory) '''
            P[state_index][actions['STAY']] = state_index

        
        num_states = 9
        B = np.zeros([num_states, num_states, len(actions)])
        for s in range(num_states):
            for a in range(len(actions)):
                ns = int(P[s][a])
                B[ns, s, a] = 1

        # plot_transition(B)
        
        class GridWorldEnv():
    
            def __init__(self,A,B):
                self.A = deepcopy(A)
                self.B = deepcopy(B)
                self.state = np.zeros(9)
                self.state[2] = 1
            
            def step(self,a):
                self.state = np.dot(self.B[:,:,a], self.state)
                obs = utils.sample(np.dot(self.A, self.state))
                return obs

            def reset(self):
                self.state =np.zeros(9)
                self.state[2] =1 
                obs = utils.sample(np.dot(self.A, self.state))
                return obs
        
        env = GridWorldEnv(A,B)

        def KL_divergence(q,p):
            return np.sum(q * (log_stable(q) - log_stable(p)))

        def compute_free_energy(q,A, B):
            return np.sum(q * (log_stable(q) - log_stable(A) - log_stable(B)))

        def softmax(x):
            return np.exp(x) / np.sum(np.exp(x))

        # def perform_inference(likelihood, prior):
        #     return softmax(log_stable(likelihood) + log_stable(prior))
        
        Qs = np.ones(9) * 1/9
        # plot_beliefs(Qs)

        REWARD_LOCATION = 7
        reward_state = state_mapping[REWARD_LOCATION]

        C = np.zeros(num_states)
        C[REWARD_LOCATION] = 1. 
        # plot_beliefs(C)

        def evaluate_policy(policy, Qs, A, B, C):
            # initialize expected free energy at 0
            G = 0

            # loop over policy
            for t in range(len(policy)):

                # get action entailed by the policy at timestep `t`
                u = int(policy[t].item())

                # work out expected state, given the action
                Qs_pi = B[:,:,u].dot(Qs)

                # work out expected observations, given the action
                Qo_pi = A.dot(Qs_pi)

                # get entropy
                H = - (A * log_stable(A)).sum(axis = 0)

                # get predicted divergence
                # divergence = np.sum(Qo_pi * (log_stable(Qo_pi) - log_stable(C)), axis=0)
                divergence = KL_divergence(Qo_pi, C)
                
                # compute the expected uncertainty or ambiguity 
                uncertainty = H.dot(Qs_pi)

                # increment the expected free energy counter for the policy, using the expected free energy at this timestep
                G += (divergence + uncertainty)

            return -G

        def infer_action(Qs, A, B, C, n_actions, policies):
    
            # initialize the negative expected free energy
            neg_G = np.zeros(len(policies))

            # loop over every possible policy and compute the EFE of each policy
            for i, policy in enumerate(policies):
                neg_G[i] = evaluate_policy(policy, Qs, A, B, C)

            # get distribution over policies
            Q_pi = maths.softmax(neg_G)

            # initialize probabilites of control states (convert from policies to actions)
            Qu = np.zeros(n_actions)

            # sum probabilites of control states or actions 
            for i, policy in enumerate(policies):
                # control state specified by policy
                u = int(policy[0].item())
                # add probability of policy
                Qu[u] += Q_pi[i]

            # normalize action marginal
            utils.norm_dist(Qu)

            # sample control from action marginal
            u = utils.sample(Qu)

            return u

        # number of time steps
        T = 10

        #n_actions = env.n_control
        n_actions = 5

        # length of policies we consider
        policy_len = 4

        # this function generates all possible combinations of policies
        policies = control.construct_policies([B.shape[0]], [n_actions], policy_len)

        # reset environment
        o = env.reset()

        # loop over time
        for t in range(T):

            # infer which action to take
            a = infer_action(Qs, A, B, C, n_actions, policies)
            
            # perform action in the environment and update the environment
            o = env.step(int(a))
            
            # infer new hidden state (this is the same equation as above but with PyMDP functions)
            likelihood = A[o,:]
            prior = B[:,:,int(a)].dot(Qs)

            Qs = maths.softmax(log_stable(likelihood) + log_stable(prior))
            
            # plot_beliefs(Qs, "Beliefs (Qs) at time {}".format(t))

        # self.assertEqual(np.argmax(Qs), REWARD_LOCATION) # @NOTE: This is not always true due to stochastic samplign!!!
        self.assertEqual(Qs.shape[0], B.shape[0])

class GridWorldEnv():
    
            def __init__(self,A,B):
                self.A = deepcopy(A)
                self.B = deepcopy(B)
                self.state = np.zeros(9)
                self.state[2] = 1
            
            def step(self,a):
                self.state = np.dot(self.B[:,:,a], self.state)
                obs = utils.sample(np.dot(self.A, self.state))
                return obs

            def reset(self):
                self.state =np.zeros(9)
                self.state[2] =1 
                obs = utils.sample(np.dot(self.A, self.state))
                return obs

def KL_divergence(q,p):
            return np.sum(q * (log_stable(q) - log_stable(p)))

def compute_free_energy(q,A, B):
            return np.sum(q * (log_stable(q) - log_stable(A) - log_stable(B)))

def softmax(x):
            return np.exp(x) / np.sum(np.exp(x))

def evaluate_policy(policy, Qs, A, B, C):
            # initialize expected free energy at 0
            G = 0

            # loop over policy
            for t in range(len(policy)):

                # get action entailed by the policy at timestep `t`
                u = int(policy[t].item())

                # work out expected state, given the action
                Qs_pi = B[:,:,u].dot(Qs)

                # work out expected observations, given the action
                Qo_pi = A.dot(Qs_pi)

                # get entropy
                H = - (A * log_stable(A)).sum(axis = 0)

                # get predicted divergence
                # divergence = np.sum(Qo_pi * (log_stable(Qo_pi) - log_stable(C)), axis=0)
                divergence = KL_divergence(Qo_pi, C)
                
                # compute the expected uncertainty or ambiguity 
                uncertainty = H.dot(Qs_pi)

                # increment the expected free energy counter for the policy, using the expected free energy at this timestep
                G += (divergence + uncertainty)

            return -G

def infer_action(Qs, A, B, C, n_actions, policies):
    
            # initialize the negative expected free energy
            neg_G = np.zeros(len(policies))

            # loop over every possible policy and compute the EFE of each policy
            for i, policy in enumerate(policies):
                neg_G[i] = evaluate_policy(policy, Qs, A, B, C)

            # get distribution over policies
            Q_pi = maths.softmax(neg_G)

            # initialize probabilites of control states (convert from policies to actions)
            Qu = np.zeros(n_actions)

            # sum probabilites of control states or actions 
            for i, policy in enumerate(policies):
                # control state specified by policy
                u = int(policy[0].item())
                # add probability of policy
                Qu[u] += Q_pi[i]

            # normalize action marginal
            utils.norm_dist(Qu)

            # sample control from action marginal
            u = utils.sample(Qu)

            return u

def __init__(self,A,B):
                self.A = deepcopy(A)
                self.B = deepcopy(B)
                self.state = np.zeros(9)
                self.state[2] = 1

def step(self,a):
                self.state = np.dot(self.B[:,:,a], self.state)
                obs = utils.sample(np.dot(self.A, self.state))
                return obs

def reset(self):
                self.state =np.zeros(9)
                self.state[2] =1 
                obs = utils.sample(np.dot(self.A, self.state))
                return obs

class TestFPI(unittest.TestCase):

    def test_factorized_fpi_one_factor_one_modality(self):
        """
        Test the sparsified version of `run_vanilla_fpi`, named `run_vanilla_fpi_factorized`
        with single hidden state factor and single observation modality.
        """

        num_states = [3]
        num_obs = [3]       

        prior = utils.random_single_categorical(num_states)

        A = utils.to_obj_array(maths.softmax(np.eye(num_states[0]) * 0.1))

        obs_idx = np.random.choice(num_obs[0])
        obs = utils.onehot(obs_idx, num_obs[0])

        mb_dict = {'A_factor_list': [[0]],
                    'A_modality_list': [[0]]}

        qs_out = run_vanilla_fpi_factorized(A, obs, num_obs, num_states, mb_dict, prior=prior)[0]
        qs_validation_1 = run_vanilla_fpi(A, obs, num_obs, num_states, prior=prior)[0]
        qs_validation_2 = maths.softmax(maths.spm_log_single(A[0][obs_idx,:]) + maths.spm_log_single(prior[0]))

        self.assertTrue(np.isclose(qs_validation_1, qs_out).all())
        self.assertTrue(np.isclose(qs_validation_2, qs_out).all())
    
    def test_factorized_fpi_one_factor_multi_modality(self):
        """
        Test the sparsified version of `run_vanilla_fpi`, named `run_vanilla_fpi_factorized`
        with single hidden state factor and multiple observation modalities.
        """

        num_states = [3]
        num_obs = [3, 2]

        prior = utils.random_single_categorical(num_states)

        A = utils.random_A_matrix(num_obs, num_states)

        obs = utils.obj_array(len(num_obs))
        for m, obs_dim in enumerate(num_obs):
            obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

        mb_dict = {'A_factor_list': [[0], [0]],
                    'A_modality_list': [[0, 1]]}
        
        qs_out = run_vanilla_fpi_factorized(A, obs, num_obs, num_states, mb_dict, prior=prior)[0]
        qs_validation = run_vanilla_fpi(A, obs, num_obs, num_states, prior=prior)[0]

        self.assertTrue(np.isclose(qs_validation, qs_out).all())
    
    def test_factorized_fpi_multi_factor_one_modality(self):
        """
        Test the sparsified version of `run_vanilla_fpi`, named `run_vanilla_fpi_factorized`
        with multiple hidden state factors and one observation modality.
        """

        num_states = [4, 5]
        num_obs = [3]

        prior = utils.random_single_categorical(num_states)

        A = utils.random_A_matrix(num_obs, num_states)

        obs_idx = np.random.choice(num_obs[0])
        obs = utils.onehot(obs_idx, num_obs[0])

        mb_dict = {'A_factor_list': [[0, 1]],
                    'A_modality_list': [[0], [0]]}
        
        qs_out = run_vanilla_fpi_factorized(A, obs, num_obs, num_states, mb_dict, prior=prior)
        qs_validation = run_vanilla_fpi(A, obs, num_obs, num_states, prior=prior)

        for qs_f_val, qs_f_out in zip(qs_validation, qs_out):
            self.assertTrue(np.isclose(qs_f_val, qs_f_out).all())
    
    def test_factorized_fpi_multi_factor_multi_modality(self):
        """
        Test the sparsified version of `run_vanilla_fpi`, named `run_vanilla_fpi_factorized`
        with multiple hidden state factors and multiple observation modalities.
        """

        num_states = [3, 4]
        num_obs = [3, 3, 5]

        prior = utils.random_single_categorical(num_states)

        A = utils.random_A_matrix(num_obs, num_states)

        obs = utils.obj_array(len(num_obs))
        for m, obs_dim in enumerate(num_obs):
            obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

        mb_dict = {'A_factor_list': [[0, 1], [0, 1], [0, 1]],
                    'A_modality_list': [[0, 1, 2], [0, 1, 2]]}
        
        qs_out = run_vanilla_fpi_factorized(A, obs, num_obs, num_states, mb_dict, prior=prior)
        qs_validation = run_vanilla_fpi(A, obs, num_obs, num_states, prior=prior)

        for qs_f_val, qs_f_out in zip(qs_validation, qs_out):
            self.assertTrue(np.isclose(qs_f_val, qs_f_out).all())

        # test it also without computing VFE (i.e. with `compute_vfe=False`)
        qs_out = run_vanilla_fpi_factorized(A, obs, num_obs, num_states, mb_dict, prior=prior, compute_vfe=False)
        qs_validation = run_vanilla_fpi(A, obs, num_obs, num_states, prior=prior, compute_vfe=False)

        for qs_f_val, qs_f_out in zip(qs_validation, qs_out):
            self.assertTrue(np.isclose(qs_f_val, qs_f_out).all())

    def test_factorized_fpi_multi_factor_multi_modality_with_condind(self):
        """
        Test the sparsified version of `run_vanilla_fpi`, named `run_vanilla_fpi_factorized`
        with multiple hidden state factors and multiple observation modalities, where some modalities only depend on some factors.
        """

        num_states = [3, 4]
        num_obs = [3, 3, 5]

        prior = utils.random_single_categorical(num_states)

        obs = utils.obj_array(len(num_obs))
        for m, obs_dim in enumerate(num_obs):
            obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

        mb_dict = {'A_factor_list': [[0], [1], [0, 1]],
                    'A_modality_list': [[0, 2], [1, 2]]}

        A_reduced = utils.random_A_matrix(num_obs, num_states, A_factor_list=mb_dict['A_factor_list'])
        
        qs_out = run_vanilla_fpi_factorized(A_reduced, obs, num_obs, num_states, mb_dict, prior=prior)

        A_full = utils.initialize_empty_A(num_obs, num_states)
        for m, A_m in enumerate(A_full):
            other_factors = list(set(range(len(num_states))) - set(mb_dict['A_factor_list'][m])) # list of the factors that modality `m` does not depend on

            # broadcast or tile the reduced A matrix (`A_reduced`) along the dimensions of corresponding to `other_factors`
            expanded_dims = [num_obs[m]] + [1 if f in other_factors else ns for (f, ns) in enumerate(num_states)]
            tile_dims = [1] + [ns if f in other_factors else 1 for (f, ns) in enumerate(num_states)]
            A_full[m] = np.tile(A_reduced[m].reshape(expanded_dims), tile_dims)

        qs_validation = run_vanilla_fpi(A_full, obs, num_obs, num_states, prior=prior)

        for qs_f_val, qs_f_out in zip(qs_validation, qs_out):
            self.assertTrue(np.isclose(qs_f_val, qs_f_out).all())
    
    def test_factorized_fpi_multi_factor_single_modality_with_condind(self):
        """
        Test the sparsified version of `run_vanilla_fpi`, named `run_vanilla_fpi_factorized`
        with multiple hidden state factors and one observation modality, where the modality only depend on some factors.
        """

        num_states = [3, 4]
        num_obs = [3]

        prior = utils.random_single_categorical(num_states)

        obs = utils.obj_array(len(num_obs))
        for m, obs_dim in enumerate(num_obs):
            obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

        mb_dict = {'A_factor_list': [[0]],
                    'A_modality_list': [[0], []]}

        A_reduced = utils.random_A_matrix(num_obs, num_states, A_factor_list=mb_dict['A_factor_list'])
        
        qs_out = run_vanilla_fpi_factorized(A_reduced, obs, num_obs, num_states, mb_dict, prior=prior)

        A_full = utils.initialize_empty_A(num_obs, num_states)
        for m, A_m in enumerate(A_full):
            other_factors = list(set(range(len(num_states))) - set(mb_dict['A_factor_list'][m])) # list of the factors that modality `m` does not depend on

            # broadcast or tile the reduced A matrix (`A_reduced`) along the dimensions of corresponding to `other_factors`
            expanded_dims = [num_obs[m]] + [1 if f in other_factors else ns for (f, ns) in enumerate(num_states)]
            tile_dims = [1] + [ns if f in other_factors else 1 for (f, ns) in enumerate(num_states)]
            A_full[m] = np.tile(A_reduced[m].reshape(expanded_dims), tile_dims)

        qs_validation = run_vanilla_fpi(A_full, obs, num_obs, num_states, prior=prior)

        for qs_f_val, qs_f_out in zip(qs_validation, qs_out):
            self.assertTrue(np.isclose(qs_f_val, qs_f_out).all())
        
        self.assertTrue(np.isclose(qs_out[1], prior[1]).all())

def test_factorized_fpi_one_factor_one_modality(self):
        """
        Test the sparsified version of `run_vanilla_fpi`, named `run_vanilla_fpi_factorized`
        with single hidden state factor and single observation modality.
        """

        num_states = [3]
        num_obs = [3]       

        prior = utils.random_single_categorical(num_states)

        A = utils.to_obj_array(maths.softmax(np.eye(num_states[0]) * 0.1))

        obs_idx = np.random.choice(num_obs[0])
        obs = utils.onehot(obs_idx, num_obs[0])

        mb_dict = {'A_factor_list': [[0]],
                    'A_modality_list': [[0]]}

        qs_out = run_vanilla_fpi_factorized(A, obs, num_obs, num_states, mb_dict, prior=prior)[0]
        qs_validation_1 = run_vanilla_fpi(A, obs, num_obs, num_states, prior=prior)[0]
        qs_validation_2 = maths.softmax(maths.spm_log_single(A[0][obs_idx,:]) + maths.spm_log_single(prior[0]))

        self.assertTrue(np.isclose(qs_validation_1, qs_out).all())
        self.assertTrue(np.isclose(qs_validation_2, qs_out).all())

def test_factorized_fpi_one_factor_multi_modality(self):
        """
        Test the sparsified version of `run_vanilla_fpi`, named `run_vanilla_fpi_factorized`
        with single hidden state factor and multiple observation modalities.
        """

        num_states = [3]
        num_obs = [3, 2]

        prior = utils.random_single_categorical(num_states)

        A = utils.random_A_matrix(num_obs, num_states)

        obs = utils.obj_array(len(num_obs))
        for m, obs_dim in enumerate(num_obs):
            obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

        mb_dict = {'A_factor_list': [[0], [0]],
                    'A_modality_list': [[0, 1]]}
        
        qs_out = run_vanilla_fpi_factorized(A, obs, num_obs, num_states, mb_dict, prior=prior)[0]
        qs_validation = run_vanilla_fpi(A, obs, num_obs, num_states, prior=prior)[0]

        self.assertTrue(np.isclose(qs_validation, qs_out).all())

def test_factorized_fpi_multi_factor_one_modality(self):
        """
        Test the sparsified version of `run_vanilla_fpi`, named `run_vanilla_fpi_factorized`
        with multiple hidden state factors and one observation modality.
        """

        num_states = [4, 5]
        num_obs = [3]

        prior = utils.random_single_categorical(num_states)

        A = utils.random_A_matrix(num_obs, num_states)

        obs_idx = np.random.choice(num_obs[0])
        obs = utils.onehot(obs_idx, num_obs[0])

        mb_dict = {'A_factor_list': [[0, 1]],
                    'A_modality_list': [[0], [0]]}
        
        qs_out = run_vanilla_fpi_factorized(A, obs, num_obs, num_states, mb_dict, prior=prior)
        qs_validation = run_vanilla_fpi(A, obs, num_obs, num_states, prior=prior)

        for qs_f_val, qs_f_out in zip(qs_validation, qs_out):
            self.assertTrue(np.isclose(qs_f_val, qs_f_out).all())

def test_factorized_fpi_multi_factor_multi_modality(self):
        """
        Test the sparsified version of `run_vanilla_fpi`, named `run_vanilla_fpi_factorized`
        with multiple hidden state factors and multiple observation modalities.
        """

        num_states = [3, 4]
        num_obs = [3, 3, 5]

        prior = utils.random_single_categorical(num_states)

        A = utils.random_A_matrix(num_obs, num_states)

        obs = utils.obj_array(len(num_obs))
        for m, obs_dim in enumerate(num_obs):
            obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

        mb_dict = {'A_factor_list': [[0, 1], [0, 1], [0, 1]],
                    'A_modality_list': [[0, 1, 2], [0, 1, 2]]}
        
        qs_out = run_vanilla_fpi_factorized(A, obs, num_obs, num_states, mb_dict, prior=prior)
        qs_validation = run_vanilla_fpi(A, obs, num_obs, num_states, prior=prior)

        for qs_f_val, qs_f_out in zip(qs_validation, qs_out):
            self.assertTrue(np.isclose(qs_f_val, qs_f_out).all())

        # test it also without computing VFE (i.e. with `compute_vfe=False`)
        qs_out = run_vanilla_fpi_factorized(A, obs, num_obs, num_states, mb_dict, prior=prior, compute_vfe=False)
        qs_validation = run_vanilla_fpi(A, obs, num_obs, num_states, prior=prior, compute_vfe=False)

        for qs_f_val, qs_f_out in zip(qs_validation, qs_out):
            self.assertTrue(np.isclose(qs_f_val, qs_f_out).all())

def test_factorized_fpi_multi_factor_multi_modality_with_condind(self):
        """
        Test the sparsified version of `run_vanilla_fpi`, named `run_vanilla_fpi_factorized`
        with multiple hidden state factors and multiple observation modalities, where some modalities only depend on some factors.
        """

        num_states = [3, 4]
        num_obs = [3, 3, 5]

        prior = utils.random_single_categorical(num_states)

        obs = utils.obj_array(len(num_obs))
        for m, obs_dim in enumerate(num_obs):
            obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

        mb_dict = {'A_factor_list': [[0], [1], [0, 1]],
                    'A_modality_list': [[0, 2], [1, 2]]}

        A_reduced = utils.random_A_matrix(num_obs, num_states, A_factor_list=mb_dict['A_factor_list'])
        
        qs_out = run_vanilla_fpi_factorized(A_reduced, obs, num_obs, num_states, mb_dict, prior=prior)

        A_full = utils.initialize_empty_A(num_obs, num_states)
        for m, A_m in enumerate(A_full):
            other_factors = list(set(range(len(num_states))) - set(mb_dict['A_factor_list'][m])) # list of the factors that modality `m` does not depend on

            # broadcast or tile the reduced A matrix (`A_reduced`) along the dimensions of corresponding to `other_factors`
            expanded_dims = [num_obs[m]] + [1 if f in other_factors else ns for (f, ns) in enumerate(num_states)]
            tile_dims = [1] + [ns if f in other_factors else 1 for (f, ns) in enumerate(num_states)]
            A_full[m] = np.tile(A_reduced[m].reshape(expanded_dims), tile_dims)

        qs_validation = run_vanilla_fpi(A_full, obs, num_obs, num_states, prior=prior)

        for qs_f_val, qs_f_out in zip(qs_validation, qs_out):
            self.assertTrue(np.isclose(qs_f_val, qs_f_out).all())

def test_factorized_fpi_multi_factor_single_modality_with_condind(self):
        """
        Test the sparsified version of `run_vanilla_fpi`, named `run_vanilla_fpi_factorized`
        with multiple hidden state factors and one observation modality, where the modality only depend on some factors.
        """

        num_states = [3, 4]
        num_obs = [3]

        prior = utils.random_single_categorical(num_states)

        obs = utils.obj_array(len(num_obs))
        for m, obs_dim in enumerate(num_obs):
            obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

        mb_dict = {'A_factor_list': [[0]],
                    'A_modality_list': [[0], []]}

        A_reduced = utils.random_A_matrix(num_obs, num_states, A_factor_list=mb_dict['A_factor_list'])
        
        qs_out = run_vanilla_fpi_factorized(A_reduced, obs, num_obs, num_states, mb_dict, prior=prior)

        A_full = utils.initialize_empty_A(num_obs, num_states)
        for m, A_m in enumerate(A_full):
            other_factors = list(set(range(len(num_states))) - set(mb_dict['A_factor_list'][m])) # list of the factors that modality `m` does not depend on

            # broadcast or tile the reduced A matrix (`A_reduced`) along the dimensions of corresponding to `other_factors`
            expanded_dims = [num_obs[m]] + [1 if f in other_factors else ns for (f, ns) in enumerate(num_states)]
            tile_dims = [1] + [ns if f in other_factors else 1 for (f, ns) in enumerate(num_states)]
            A_full[m] = np.tile(A_reduced[m].reshape(expanded_dims), tile_dims)

        qs_validation = run_vanilla_fpi(A_full, obs, num_obs, num_states, prior=prior)

        for qs_f_val, qs_f_out in zip(qs_validation, qs_out):
            self.assertTrue(np.isclose(qs_f_val, qs_f_out).all())
        
        self.assertTrue(np.isclose(qs_out[1], prior[1]).all())

def generate_model_params():
    """
    Generate random model dimensions
    """
    rng_keys = jr.split(jr.PRNGKey(cfg["source_key"]), cfg["num_models"])
    num_factors_list = [ jr.randint(key, (1,), 1, 10)[0].item() for key in rng_keys ]
    num_states_list = [ jr.randint(key, (nf,), 1, 5).tolist() for nf, key in zip(num_factors_list, rng_keys) ]

    rng_keys = jr.split(rng_keys[-1], cfg["num_models"])
    num_modalities_list = [ jr.randint(key, (1,), 1, 10)[0].item() for key in rng_keys ]
    num_obs_list = [ jr.randint(key, (nm,), 1, 5).tolist() for nm, key in zip(num_modalities_list, rng_keys) ]

    rng_keys = jr.split(rng_keys[-1], cfg["num_models"])
    A_deps_list = []
    for nf, nm, model_key in zip(num_factors_list, num_modalities_list, rng_keys):
        keys_model_i = jr.split(model_key, nm)
        A_deps_model_i = [jr.randint(key, (nm,), 0, nf).tolist() for key in keys_model_i]
        A_deps_list.append(A_deps_model_i)
    
    return {'nf_list': num_factors_list, 
            'ns_list': num_states_list, 
            'nm_list': num_modalities_list, 
            'no_list': num_obs_list, 
            'A_deps_list': A_deps_list}

class TestControlJax(unittest.TestCase):

    def test_get_expected_obs_factorized(self):
        """
        Tests the jax-ified version of computations of expected observations under some hidden states and policy
        """
        gm_params = generate_model_params()
        num_factors_list, num_states_list, num_modalities_list, num_obs_list, A_deps_list = gm_params['nf_list'], gm_params['ns_list'], gm_params['nm_list'], gm_params['no_list'], gm_params['A_deps_list']
        for (num_states, num_obs, A_deps) in zip(num_states_list, num_obs_list, A_deps_list):
            
            qs_numpy = utils.random_single_categorical(num_states)
            qs_jax = list(qs_numpy)

            A_np = utils.random_A_matrix(num_obs, num_states, A_factor_list=A_deps)
            A_jax = jtu.tree_map(lambda x: jnp.array(x), list(A_np))   

            qo_test = ctl_jax.compute_expected_obs(qs_jax, A_jax, A_deps) 
            qo_validation = ctl_np.get_expected_obs_factorized([qs_numpy], A_np, A_deps) # need to wrap `qs` in list because `get_expected_obs_factorized` expects a list of `qs` (representing multiple timesteps)

            for qo_m, qo_val_m in zip(qo_test, qo_validation[0]): # need to extract first index of `qo_validation` because `get_expected_obs_factorized` returns a list of `qo` (representing multiple timesteps)
                self.assertTrue(np.allclose(qo_m, qo_val_m))

    def test_info_gain_factorized(self):
        """ 
        Unit test the `calc_states_info_gain_factorized` function by qualitatively checking that in the T-Maze (contextual bandit)
        example, the state info gain is higher for the policy that leads to visiting the cue, which is higher than state info gain
        for visiting the bandit arm, which in turn is higher than the state info gain for the policy that leads to staying in the start state.
        """

        num_states = [2, 3]  
        num_obs = [3, 3, 3]

        A_dependencies = [[0, 1], [0, 1], [1]] 
        A = []
        for m, obs in enumerate(num_obs):
            lagging_dimensions = [ns for i, ns in enumerate(num_states) if i in A_dependencies[m]]
            modality_shape = [obs] + lagging_dimensions
            A.append(np.zeros(modality_shape))
            if m == 0:
                A[m][:, :, 0] = np.ones( (num_obs[m], num_states[0]) ) / num_obs[m]
                A[m][:, :, 1] = np.ones( (num_obs[m], num_states[0]) ) / num_obs[m]
                A[m][:, :, 2] = np.array([[0.9, 0.1], [0.0, 0.0], [0.1, 0.9]]) # cue statistics
            if m == 1:
                A[m][2, :, 0] = np.ones(num_states[0])
                A[m][0:2, :, 1] = np.array([[0.6, 0.4], [0.6, 0.4]]) # bandit statistics (mapping between reward-state (first hidden state factor) and rewards (Good vs Bad))
                A[m][2, :, 2] = np.ones(num_states[0])
            if m == 2:
                A[m] = np.eye(obs)

        qs_start = list(utils.obj_array_uniform(num_states))
        qs_start[1] = np.array([1., 0., 0.]) # agent believes it's in the start state

        A = [jnp.array(A_m) for A_m in A]
        qs_start = [jnp.array(qs) for qs in qs_start]
        qo_start = ctl_jax.compute_expected_obs(qs_start, A, A_dependencies)
        
        start_info_gain = ctl_jax.compute_info_gain(qs_start, qo_start, A, A_dependencies)

        qs_arm = list(utils.obj_array_uniform(num_states))
        qs_arm[1] = np.array([0., 1., 0.]) # agent believes it's in the arm-visiting state
        qs_arm = [jnp.array(qs) for qs in qs_arm]
        qo_arm = ctl_jax.compute_expected_obs(qs_arm, A, A_dependencies)
        
        arm_info_gain = ctl_jax.compute_info_gain(qs_arm, qo_arm, A, A_dependencies)
        
        qs_cue = utils.obj_array_uniform(num_states)
        qs_cue[1] = np.array([0., 0., 1.]) # agent believes it's in the cue-visiting state
        qs_cue = [jnp.array(qs) for qs in qs_cue]
        
        qo_cue = ctl_jax.compute_expected_obs(qs_cue, A, A_dependencies)
        cue_info_gain = ctl_jax.compute_info_gain(qs_cue, qo_cue, A, A_dependencies)
        
        self.assertGreater(arm_info_gain, start_info_gain)
        self.assertGreater(cue_info_gain, arm_info_gain)

        gm_params = generate_model_params()
        num_factors_list, num_states_list, num_modalities_list, num_obs_list, A_deps_list = gm_params['nf_list'], gm_params['ns_list'], gm_params['nm_list'], gm_params['no_list'], gm_params['A_deps_list']
        for (num_states, num_obs, A_deps) in zip(num_states_list, num_obs_list, A_deps_list):

            qs_numpy = utils.random_single_categorical(num_states)
            qs_jax = list(qs_numpy)

            A_np = utils.random_A_matrix(num_obs, num_states, A_factor_list=A_deps)
            A_jax = jtu.tree_map(lambda x: jnp.array(x), list(A_np))   

            qo = ctl_jax.compute_expected_obs(qs_jax, A_jax, A_deps)

            info_gain = ctl_jax.compute_info_gain(qs_jax, qo, A_jax, A_deps)
            info_gain_validation = ctl_np.calc_states_info_gain_factorized(A_np, [qs_numpy],  A_deps)

            self.assertTrue(np.allclose(info_gain, info_gain_validation, atol=1e-5))

def test_get_expected_obs_factorized(self):
        """
        Tests the jax-ified version of computations of expected observations under some hidden states and policy
        """
        gm_params = generate_model_params()
        num_factors_list, num_states_list, num_modalities_list, num_obs_list, A_deps_list = gm_params['nf_list'], gm_params['ns_list'], gm_params['nm_list'], gm_params['no_list'], gm_params['A_deps_list']
        for (num_states, num_obs, A_deps) in zip(num_states_list, num_obs_list, A_deps_list):
            
            qs_numpy = utils.random_single_categorical(num_states)
            qs_jax = list(qs_numpy)

            A_np = utils.random_A_matrix(num_obs, num_states, A_factor_list=A_deps)
            A_jax = jtu.tree_map(lambda x: jnp.array(x), list(A_np))   

            qo_test = ctl_jax.compute_expected_obs(qs_jax, A_jax, A_deps) 
            qo_validation = ctl_np.get_expected_obs_factorized([qs_numpy], A_np, A_deps) # need to wrap `qs` in list because `get_expected_obs_factorized` expects a list of `qs` (representing multiple timesteps)

            for qo_m, qo_val_m in zip(qo_test, qo_validation[0]): # need to extract first index of `qo_validation` because `get_expected_obs_factorized` returns a list of `qo` (representing multiple timesteps)
                self.assertTrue(np.allclose(qo_m, qo_val_m))

def test_info_gain_factorized(self):
        """ 
        Unit test the `calc_states_info_gain_factorized` function by qualitatively checking that in the T-Maze (contextual bandit)
        example, the state info gain is higher for the policy that leads to visiting the cue, which is higher than state info gain
        for visiting the bandit arm, which in turn is higher than the state info gain for the policy that leads to staying in the start state.
        """

        num_states = [2, 3]  
        num_obs = [3, 3, 3]

        A_dependencies = [[0, 1], [0, 1], [1]] 
        A = []
        for m, obs in enumerate(num_obs):
            lagging_dimensions = [ns for i, ns in enumerate(num_states) if i in A_dependencies[m]]
            modality_shape = [obs] + lagging_dimensions
            A.append(np.zeros(modality_shape))
            if m == 0:
                A[m][:, :, 0] = np.ones( (num_obs[m], num_states[0]) ) / num_obs[m]
                A[m][:, :, 1] = np.ones( (num_obs[m], num_states[0]) ) / num_obs[m]
                A[m][:, :, 2] = np.array([[0.9, 0.1], [0.0, 0.0], [0.1, 0.9]]) # cue statistics
            if m == 1:
                A[m][2, :, 0] = np.ones(num_states[0])
                A[m][0:2, :, 1] = np.array([[0.6, 0.4], [0.6, 0.4]]) # bandit statistics (mapping between reward-state (first hidden state factor) and rewards (Good vs Bad))
                A[m][2, :, 2] = np.ones(num_states[0])
            if m == 2:
                A[m] = np.eye(obs)

        qs_start = list(utils.obj_array_uniform(num_states))
        qs_start[1] = np.array([1., 0., 0.]) # agent believes it's in the start state

        A = [jnp.array(A_m) for A_m in A]
        qs_start = [jnp.array(qs) for qs in qs_start]
        qo_start = ctl_jax.compute_expected_obs(qs_start, A, A_dependencies)
        
        start_info_gain = ctl_jax.compute_info_gain(qs_start, qo_start, A, A_dependencies)

        qs_arm = list(utils.obj_array_uniform(num_states))
        qs_arm[1] = np.array([0., 1., 0.]) # agent believes it's in the arm-visiting state
        qs_arm = [jnp.array(qs) for qs in qs_arm]
        qo_arm = ctl_jax.compute_expected_obs(qs_arm, A, A_dependencies)
        
        arm_info_gain = ctl_jax.compute_info_gain(qs_arm, qo_arm, A, A_dependencies)
        
        qs_cue = utils.obj_array_uniform(num_states)
        qs_cue[1] = np.array([0., 0., 1.]) # agent believes it's in the cue-visiting state
        qs_cue = [jnp.array(qs) for qs in qs_cue]
        
        qo_cue = ctl_jax.compute_expected_obs(qs_cue, A, A_dependencies)
        cue_info_gain = ctl_jax.compute_info_gain(qs_cue, qo_cue, A, A_dependencies)
        
        self.assertGreater(arm_info_gain, start_info_gain)
        self.assertGreater(cue_info_gain, arm_info_gain)

        gm_params = generate_model_params()
        num_factors_list, num_states_list, num_modalities_list, num_obs_list, A_deps_list = gm_params['nf_list'], gm_params['ns_list'], gm_params['nm_list'], gm_params['no_list'], gm_params['A_deps_list']
        for (num_states, num_obs, A_deps) in zip(num_states_list, num_obs_list, A_deps_list):

            qs_numpy = utils.random_single_categorical(num_states)
            qs_jax = list(qs_numpy)

            A_np = utils.random_A_matrix(num_obs, num_states, A_factor_list=A_deps)
            A_jax = jtu.tree_map(lambda x: jnp.array(x), list(A_np))   

            qo = ctl_jax.compute_expected_obs(qs_jax, A_jax, A_deps)

            info_gain = ctl_jax.compute_info_gain(qs_jax, qo, A_jax, A_deps)
            info_gain_validation = ctl_np.calc_states_info_gain_factorized(A_np, [qs_numpy],  A_deps)

            self.assertTrue(np.allclose(info_gain, info_gain_validation, atol=1e-5))

class MMP(unittest.TestCase):
   
    def test_mmp_a(self):
        """
        Testing our SPM-ified version of `run_MMP` with
            1 hidden state factor & 1 outcome modality, at a random fixed
            timestep during the generative process
        """

        array_path = os.path.join(os.getcwd(), DATA_PATH + "mmp_a.mat")
        mat_contents = loadmat(file_name=array_path)

        A = mat_contents["A"][0]
        B = mat_contents["B"][0]
        prev_obs = mat_contents["obs_idx"].astype("int64")
        policy = mat_contents["policy"].astype("int64") - 1
        curr_t = mat_contents["t"][0, 0].astype("int64") - 1
        t_horizon = mat_contents["t_horizon"][0, 0].astype("int64")
        prev_actions = mat_contents["previous_actions"].astype("int64") - 1
        result_spm = mat_contents["qs"][0]
        likelihoods = mat_contents["likelihoods"][0]

        num_obs, num_states, _, num_factors = get_model_dimensions(A, B)
        prev_obs = convert_observation_array(
            prev_obs[:, max(0, curr_t - t_horizon) : (curr_t + 1)], num_obs
        )

        prev_actions = prev_actions[(max(0, curr_t - t_horizon) -1) :, :]
        prior = np.empty(num_factors, dtype=object)
        for f in range(num_factors):
            uniform = np.ones(num_states[f]) / num_states[f]
            prior[f] = B[f][:, :, prev_actions[0, f]].dot(uniform)

        lh_seq = get_joint_likelihood_seq(A, prev_obs, num_states)
        qs_seq, _ = run_mmp(
            lh_seq, B, policy, prev_actions[1:], prior=prior, num_iter=5, grad_descent=True
        )

        result_pymdp = qs_seq[-1]
        for f in range(num_factors):
            self.assertTrue(np.isclose(result_spm[f].squeeze(), result_pymdp[f]).all())
   
    def test_mmp_b(self):
        """ Testing our SPM-ified version of `run_MMP` with
        2 hidden state factors & 2 outcome modalities, at a random fixed
        timestep during the generative process"""

        array_path = os.path.join(os.getcwd(), DATA_PATH + "mmp_b.mat")
        mat_contents = loadmat(file_name=array_path)

        A = mat_contents["A"][0]
        B = mat_contents["B"][0]
        prev_obs = mat_contents["obs_idx"].astype("int64")
        policy = mat_contents["policy"].astype("int64") - 1
        curr_t = mat_contents["t"][0, 0].astype("int64") - 1
        t_horizon = mat_contents["t_horizon"][0, 0].astype("int64")
        prev_actions = mat_contents["previous_actions"].astype("int64") - 1
        result_spm = mat_contents["qs"][0]
        likelihoods = mat_contents["likelihoods"][0]

        num_obs, num_states, _, num_factors = get_model_dimensions(A, B)
        prev_obs = convert_observation_array(
            prev_obs[:, max(0, curr_t - t_horizon) : (curr_t + 1)], num_obs
        )

        prev_actions = prev_actions[(max(0, curr_t - t_horizon)) :, :]
        lh_seq = get_joint_likelihood_seq(A, prev_obs, num_states)
        qs_seq, _ = run_mmp(lh_seq, 
             B, policy, prev_actions=prev_actions, prior=None, num_iter=5, grad_descent=True
        )

        result_pymdp = qs_seq[-1]
        for f in range(num_factors):
            self.assertTrue(np.isclose(result_spm[f].squeeze(), result_pymdp[f]).all())

    def test_mmp_c(self):
        """ Testing our SPM-ified version of `run_MMP` with
         2 hidden state factors & 2 outcome modalities, at the very first
         timestep of the generative process (boundary condition test). So there 
         are no previous actions"""

        array_path = os.path.join(os.getcwd(), DATA_PATH + "mmp_c.mat")
        mat_contents = loadmat(file_name=array_path)

        A = mat_contents["A"][0]
        B = mat_contents["B"][0]
        prev_obs = mat_contents["obs_idx"].astype("int64")
        policy = mat_contents["policy"].astype("int64") - 1
        curr_t = mat_contents["t"][0, 0].astype("int64") - 1
        t_horizon = mat_contents["t_horizon"][0, 0].astype("int64")
        # prev_actions = mat_contents["previous_actions"].astype("int64") - 1
        result_spm = mat_contents["qs"][0]
        likelihoods = mat_contents["likelihoods"][0]

        num_obs, num_states, _, num_factors = get_model_dimensions(A, B)
        prev_obs = convert_observation_array(
            prev_obs[:, max(0, curr_t - t_horizon) : (curr_t + 1)], num_obs
        )

        # prev_actions = prev_actions[(max(0, curr_t - t_horizon)) :, :]
        lh_seq = get_joint_likelihood_seq(A, prev_obs, num_states)
        qs_seq, _ = run_mmp(
            lh_seq, B, policy, prev_actions=None, prior=None, num_iter=5, grad_descent=True
        )

        result_pymdp = qs_seq[-1]
        for f in range(num_factors):
            self.assertTrue(np.isclose(result_spm[f].squeeze(), result_pymdp[f]).all())
    
    def test_mmp_d(self):
        """ Testing our SPM-ified version of `run_MMP` with
        2 hidden state factors & 2 outcome modalities, at the final
        timestep of the generative process (boundary condition test)
        @NOTE: mmp_d.mat test has issues with the prediction errors. But the future messages are 
        totally fine (even at the last timestep of variational iteration."""

        array_path = os.path.join(os.getcwd(), DATA_PATH + "mmp_d.mat")
        mat_contents = loadmat(file_name=array_path)

        A = mat_contents["A"][0]
        B = mat_contents["B"][0]
        prev_obs = mat_contents["obs_idx"].astype("int64")
        policy = mat_contents["policy"].astype("int64") - 1
        curr_t = mat_contents["t"][0, 0].astype("int64") - 1
        t_horizon = mat_contents["t_horizon"][0, 0].astype("int64")
        prev_actions = mat_contents["previous_actions"].astype("int64") - 1
        result_spm = mat_contents["qs"][0]
        likelihoods = mat_contents["likelihoods"][0]

        num_obs, num_states, _, num_factors = get_model_dimensions(A, B)
        prev_obs = convert_observation_array(
            prev_obs[:, max(0, curr_t - t_horizon) : (curr_t + 1)], num_obs
        )
        
        prev_actions = prev_actions[(max(0, curr_t - t_horizon) -1) :, :]
        prior = np.empty(num_factors, dtype=object)
        for f in range(num_factors):
            uniform = np.ones(num_states[f]) / num_states[f]
            prior[f] = B[f][:, :, prev_actions[0, f]].dot(uniform)

        lh_seq = get_joint_likelihood_seq(A, prev_obs, num_states)

        qs_seq, _ = run_mmp(
            lh_seq, B, policy, prev_actions[1:], prior=prior, num_iter=5, grad_descent=True, last_timestep=True
        )
    
        result_pymdp = qs_seq[-1] 

        for f in range(num_factors):
            self.assertTrue(np.isclose(result_spm[f].squeeze(), result_pymdp[f]).all())
    
    """"
    @ NOTE (from Conor Heins 07.04.2021)
    Please keep this uncommented code below here. We need to figure out how to re-include optional arguments e.g. `save_vfe_seq` 
    into `run_mmp` so that important tests like these can run again some day. My only dumb solution for now would be to just have a 'UnitTest variant' of the MMP function
    that has extra optional outputs that slow down run-time (e.g. `save_vfe_seq`), and are thus excluded from the deployable version of `pymdp`,
    but are useful for benchmarking the performance/ accuracy of the algorithm
    """

def test_mmp_a(self):
        """
        Testing our SPM-ified version of `run_MMP` with
            1 hidden state factor & 1 outcome modality, at a random fixed
            timestep during the generative process
        """

        array_path = os.path.join(os.getcwd(), DATA_PATH + "mmp_a.mat")
        mat_contents = loadmat(file_name=array_path)

        A = mat_contents["A"][0]
        B = mat_contents["B"][0]
        prev_obs = mat_contents["obs_idx"].astype("int64")
        policy = mat_contents["policy"].astype("int64") - 1
        curr_t = mat_contents["t"][0, 0].astype("int64") - 1
        t_horizon = mat_contents["t_horizon"][0, 0].astype("int64")
        prev_actions = mat_contents["previous_actions"].astype("int64") - 1
        result_spm = mat_contents["qs"][0]
        likelihoods = mat_contents["likelihoods"][0]

        num_obs, num_states, _, num_factors = get_model_dimensions(A, B)
        prev_obs = convert_observation_array(
            prev_obs[:, max(0, curr_t - t_horizon) : (curr_t + 1)], num_obs
        )

        prev_actions = prev_actions[(max(0, curr_t - t_horizon) -1) :, :]
        prior = np.empty(num_factors, dtype=object)
        for f in range(num_factors):
            uniform = np.ones(num_states[f]) / num_states[f]
            prior[f] = B[f][:, :, prev_actions[0, f]].dot(uniform)

        lh_seq = get_joint_likelihood_seq(A, prev_obs, num_states)
        qs_seq, _ = run_mmp(
            lh_seq, B, policy, prev_actions[1:], prior=prior, num_iter=5, grad_descent=True
        )

        result_pymdp = qs_seq[-1]
        for f in range(num_factors):
            self.assertTrue(np.isclose(result_spm[f].squeeze(), result_pymdp[f]).all())

def test_mmp_b(self):
        """ Testing our SPM-ified version of `run_MMP` with
        2 hidden state factors & 2 outcome modalities, at a random fixed
        timestep during the generative process"""

        array_path = os.path.join(os.getcwd(), DATA_PATH + "mmp_b.mat")
        mat_contents = loadmat(file_name=array_path)

        A = mat_contents["A"][0]
        B = mat_contents["B"][0]
        prev_obs = mat_contents["obs_idx"].astype("int64")
        policy = mat_contents["policy"].astype("int64") - 1
        curr_t = mat_contents["t"][0, 0].astype("int64") - 1
        t_horizon = mat_contents["t_horizon"][0, 0].astype("int64")
        prev_actions = mat_contents["previous_actions"].astype("int64") - 1
        result_spm = mat_contents["qs"][0]
        likelihoods = mat_contents["likelihoods"][0]

        num_obs, num_states, _, num_factors = get_model_dimensions(A, B)
        prev_obs = convert_observation_array(
            prev_obs[:, max(0, curr_t - t_horizon) : (curr_t + 1)], num_obs
        )

        prev_actions = prev_actions[(max(0, curr_t - t_horizon)) :, :]
        lh_seq = get_joint_likelihood_seq(A, prev_obs, num_states)
        qs_seq, _ = run_mmp(lh_seq, 
             B, policy, prev_actions=prev_actions, prior=None, num_iter=5, grad_descent=True
        )

        result_pymdp = qs_seq[-1]
        for f in range(num_factors):
            self.assertTrue(np.isclose(result_spm[f].squeeze(), result_pymdp[f]).all())

def test_mmp_c(self):
        """ Testing our SPM-ified version of `run_MMP` with
         2 hidden state factors & 2 outcome modalities, at the very first
         timestep of the generative process (boundary condition test). So there 
         are no previous actions"""

        array_path = os.path.join(os.getcwd(), DATA_PATH + "mmp_c.mat")
        mat_contents = loadmat(file_name=array_path)

        A = mat_contents["A"][0]
        B = mat_contents["B"][0]
        prev_obs = mat_contents["obs_idx"].astype("int64")
        policy = mat_contents["policy"].astype("int64") - 1
        curr_t = mat_contents["t"][0, 0].astype("int64") - 1
        t_horizon = mat_contents["t_horizon"][0, 0].astype("int64")
        # prev_actions = mat_contents["previous_actions"].astype("int64") - 1
        result_spm = mat_contents["qs"][0]
        likelihoods = mat_contents["likelihoods"][0]

        num_obs, num_states, _, num_factors = get_model_dimensions(A, B)
        prev_obs = convert_observation_array(
            prev_obs[:, max(0, curr_t - t_horizon) : (curr_t + 1)], num_obs
        )

        # prev_actions = prev_actions[(max(0, curr_t - t_horizon)) :, :]
        lh_seq = get_joint_likelihood_seq(A, prev_obs, num_states)
        qs_seq, _ = run_mmp(
            lh_seq, B, policy, prev_actions=None, prior=None, num_iter=5, grad_descent=True
        )

        result_pymdp = qs_seq[-1]
        for f in range(num_factors):
            self.assertTrue(np.isclose(result_spm[f].squeeze(), result_pymdp[f]).all())

def test_mmp_d(self):
        """ Testing our SPM-ified version of `run_MMP` with
        2 hidden state factors & 2 outcome modalities, at the final
        timestep of the generative process (boundary condition test)
        @NOTE: mmp_d.mat test has issues with the prediction errors. But the future messages are 
        totally fine (even at the last timestep of variational iteration."""

        array_path = os.path.join(os.getcwd(), DATA_PATH + "mmp_d.mat")
        mat_contents = loadmat(file_name=array_path)

        A = mat_contents["A"][0]
        B = mat_contents["B"][0]
        prev_obs = mat_contents["obs_idx"].astype("int64")
        policy = mat_contents["policy"].astype("int64") - 1
        curr_t = mat_contents["t"][0, 0].astype("int64") - 1
        t_horizon = mat_contents["t_horizon"][0, 0].astype("int64")
        prev_actions = mat_contents["previous_actions"].astype("int64") - 1
        result_spm = mat_contents["qs"][0]
        likelihoods = mat_contents["likelihoods"][0]

        num_obs, num_states, _, num_factors = get_model_dimensions(A, B)
        prev_obs = convert_observation_array(
            prev_obs[:, max(0, curr_t - t_horizon) : (curr_t + 1)], num_obs
        )
        
        prev_actions = prev_actions[(max(0, curr_t - t_horizon) -1) :, :]
        prior = np.empty(num_factors, dtype=object)
        for f in range(num_factors):
            uniform = np.ones(num_states[f]) / num_states[f]
            prior[f] = B[f][:, :, prev_actions[0, f]].dot(uniform)

        lh_seq = get_joint_likelihood_seq(A, prev_obs, num_states)

        qs_seq, _ = run_mmp(
            lh_seq, B, policy, prev_actions[1:], prior=prior, num_iter=5, grad_descent=True, last_timestep=True
        )
    
        result_pymdp = qs_seq[-1] 

        for f in range(num_factors):
            self.assertTrue(np.isclose(result_spm[f].squeeze(), result_pymdp[f]).all())

class TestInference(unittest.TestCase):

    def test_update_posterior_states(self):
        """
        Tests the refactored version of `update_posterior_states`
        """

        '''Test with single hidden state factor and single observation modality'''

        num_states = [3]
        num_obs = [3]       

        prior = utils.random_single_categorical(num_states)

        A = utils.to_obj_array(maths.softmax(np.eye(num_states[0]) * 0.1))

        obs_idx = 1
        obs = utils.onehot(obs_idx, num_obs[0])

        qs_out = inference.update_posterior_states(A, obs, prior=prior)
        qs_validation =  maths.softmax(maths.spm_log_single(A[0][obs_idx,:]) + maths.spm_log_single(prior[0]))

        self.assertTrue(np.isclose(qs_validation, qs_out[0]).all())

        '''Try single modality inference where the observation is passed in as an int'''
        qs_out_2 = inference.update_posterior_states(A, obs_idx, prior=prior)
        self.assertTrue(np.isclose(qs_out_2[0], qs_out[0]).all())

        '''Try single modality inference where the observation is a one-hot stored in an object array'''
        qs_out_3 = inference.update_posterior_states(A, utils.to_obj_array(obs), prior=prior)
        self.assertTrue(np.isclose(qs_out_3[0], qs_out[0]).all())

        '''Test with multiple hidden state factors and single observation modality'''

        num_states = [3, 4]
        num_obs = [3]

        prior = utils.random_single_categorical(num_states)

        A = utils.random_A_matrix(num_obs, num_states)

        obs_idx = 1
        obs = utils.onehot(obs_idx, num_obs[0])

        qs_out = inference.update_posterior_states(A, obs, prior=prior, num_iter = 1)

        # validate with a quick n' dirty implementation of FPI

        # initialize posterior and log prior
        qs_valid_init = utils.obj_array_uniform(num_states)
        log_prior = maths.spm_log_obj_array(prior)

        qs_valid_final = utils.obj_array(len(num_states))

        log_likelihood = maths.spm_log_single(maths.get_joint_likelihood(A, obs, num_states))

        num_factors = len(num_states)

        qs_valid_init_all = qs_valid_init[0]
        for factor in range(num_factors-1):
            qs_valid_init_all = qs_valid_init_all[...,None]*qs_valid_init[factor+1]
        LL_tensor = log_likelihood * qs_valid_init_all

        factor_ids = range(num_factors)

        for factor, qs_f in enumerate(qs_valid_init):
            ax2sum = tuple(set(factor_ids) - set([factor])) # which axes to sum out
            qL = LL_tensor.sum(axis = ax2sum) / qs_f
            qs_valid_final[factor] = maths.softmax(qL + log_prior[factor])

        for factor, qs_f_valid in enumerate(qs_valid_final):
            self.assertTrue(np.isclose(qs_f_valid, qs_out[factor]).all())

        '''Test with multiple hidden state factors and multiple observation modalities, for two different kinds of observation input formats'''
        
        num_states = [3, 4]
        num_obs = [3, 3, 5]

        prior = utils.random_single_categorical(num_states)

        A = utils.random_A_matrix(num_obs, num_states)

        obs_index_tuple = tuple([np.random.randint(obs_dim) for obs_dim in num_obs])

        qs_out1 = inference.update_posterior_states(A, obs_index_tuple, prior=prior)

        obs_onehots = utils.obj_array(len(num_obs))
        for g in range(len(num_obs)):
            obs_onehots[g] = utils.onehot(obs_index_tuple[g], num_obs[g])

        qs_out2 = inference.update_posterior_states(A, obs_onehots, prior=prior)

        for factor in range(len(num_states)):
            self.assertTrue(np.isclose(qs_out1[factor], qs_out2[factor]).all())

    def test_update_posterior_states_factorized_single_factor(self):
        """
        Tests the version of `update_posterior_states` where an `mb_dict` is provided as an argument to factorize
        the fixed-point iteration (FPI) algorithm. Single factor version.
        """
        num_states = [3]
        num_obs = [3]       

        prior = utils.random_single_categorical(num_states)

        A = utils.to_obj_array(maths.softmax(np.eye(num_states[0]) * 0.1))

        obs_idx = 1
        obs = utils.onehot(obs_idx, num_obs[0])

        mb_dict = {'A_factor_list': [[0]],
                    'A_modality_list': [[0]]}

        qs_out = inference.update_posterior_states_factorized(A, obs, num_obs, num_states, mb_dict, prior=prior)
        qs_validation =  maths.softmax(maths.spm_log_single(A[0][obs_idx,:]) + maths.spm_log_single(prior[0]))

        self.assertTrue(np.isclose(qs_validation, qs_out[0]).all())

        '''Try single modality inference where the observation is passed in as an int'''
        qs_out_2 = inference.update_posterior_states_factorized(A, obs_idx, num_obs, num_states, mb_dict, prior=prior)
        self.assertTrue(np.isclose(qs_out_2[0], qs_out[0]).all())

        '''Try single modality inference where the observation is a one-hot stored in an object array'''
        qs_out_3 = inference.update_posterior_states_factorized(A, utils.to_obj_array(obs),num_obs, num_states, mb_dict, prior=prior)
        self.assertTrue(np.isclose(qs_out_3[0], qs_out[0]).all())

    def test_update_posterior_states_factorized(self):
        """
        Tests the version of `update_posterior_states` where an `mb_dict` is provided as an argument to factorize
        the fixed-point iteration (FPI) algorithm.
        """

        num_states = [3, 4]
        num_obs = [3, 3, 5]

        prior = utils.random_single_categorical(num_states)

        obs_index_tuple = tuple([np.random.randint(obs_dim) for obs_dim in num_obs])

        mb_dict = {'A_factor_list': [[0], [1], [0, 1]],
                    'A_modality_list': [[0, 2], [1, 2]]}
        
        A_reduced = utils.random_A_matrix(num_obs, num_states, A_factor_list=mb_dict['A_factor_list'])

        qs_out = inference.update_posterior_states_factorized(A_reduced, obs_index_tuple, num_obs, num_states, mb_dict, prior=prior)

        A_full = utils.initialize_empty_A(num_obs, num_states)
        for m, A_m in enumerate(A_full):
            other_factors = list(set(range(len(num_states))) - set(mb_dict['A_factor_list'][m])) # list of the factors that modality `m` does not depend on

            # broadcast or tile the reduced A matrix (`A_reduced`) along the dimensions of corresponding to `other_factors`
            expanded_dims = [num_obs[m]] + [1 if f in other_factors else ns for (f, ns) in enumerate(num_states)]
            tile_dims = [1] + [ns if f in other_factors else 1 for (f, ns) in enumerate(num_states)]
            A_full[m] = np.tile(A_reduced[m].reshape(expanded_dims), tile_dims)
        
        qs_validation = inference.update_posterior_states(A_full, obs_index_tuple, prior=prior)

        for qs_f_val, qs_f_out in zip(qs_validation, qs_out):
            self.assertTrue(np.isclose(qs_f_val, qs_f_out).all())
    
    def test_update_posterior_states_factorized_noVFE_compute(self):
        """
        Tests the version of `update_posterior_states` where an `mb_dict` is provided as an argument to factorize
        the fixed-point iteration (FPI) algorithm.

        In this version, we always run the total number of iterations because we don't compute the variational free energy over the course of convergence/optimization.
        """

        num_states = [3, 4]
        num_obs = [3, 3, 5]

        prior = utils.random_single_categorical(num_states)

        obs_index_tuple = tuple([np.random.randint(obs_dim) for obs_dim in num_obs])

        mb_dict = {'A_factor_list': [[0], [1], [0, 1]],
                    'A_modality_list': [[0, 2], [1, 2]]}
        
        A_reduced = utils.random_A_matrix(num_obs, num_states, A_factor_list=mb_dict['A_factor_list'])

        qs_out = inference.update_posterior_states_factorized(A_reduced, obs_index_tuple, num_obs, num_states, mb_dict, prior=prior, compute_vfe=False)

        A_full = utils.initialize_empty_A(num_obs, num_states)
        for m, A_m in enumerate(A_full):
            other_factors = list(set(range(len(num_states))) - set(mb_dict['A_factor_list'][m])) # list of the factors that modality `m` does not depend on

            # broadcast or tile the reduced A matrix (`A_reduced`) along the dimensions of corresponding to `other_factors`
            expanded_dims = [num_obs[m]] + [1 if f in other_factors else ns for (f, ns) in enumerate(num_states)]
            tile_dims = [1] + [ns if f in other_factors else 1 for (f, ns) in enumerate(num_states)]
            A_full[m] = np.tile(A_reduced[m].reshape(expanded_dims), tile_dims)
        
        qs_validation = inference.update_posterior_states(A_full, obs_index_tuple, prior=prior, compute_vfe=False)

        for qs_f_val, qs_f_out in zip(qs_validation, qs_out):
            self.assertTrue(np.isclose(qs_f_val, qs_f_out).all())

def test_update_posterior_states(self):
        """
        Tests the refactored version of `update_posterior_states`
        """

        '''Test with single hidden state factor and single observation modality'''

        num_states = [3]
        num_obs = [3]       

        prior = utils.random_single_categorical(num_states)

        A = utils.to_obj_array(maths.softmax(np.eye(num_states[0]) * 0.1))

        obs_idx = 1
        obs = utils.onehot(obs_idx, num_obs[0])

        qs_out = inference.update_posterior_states(A, obs, prior=prior)
        qs_validation =  maths.softmax(maths.spm_log_single(A[0][obs_idx,:]) + maths.spm_log_single(prior[0]))

        self.assertTrue(np.isclose(qs_validation, qs_out[0]).all())

        '''Try single modality inference where the observation is passed in as an int'''
        qs_out_2 = inference.update_posterior_states(A, obs_idx, prior=prior)
        self.assertTrue(np.isclose(qs_out_2[0], qs_out[0]).all())

        '''Try single modality inference where the observation is a one-hot stored in an object array'''
        qs_out_3 = inference.update_posterior_states(A, utils.to_obj_array(obs), prior=prior)
        self.assertTrue(np.isclose(qs_out_3[0], qs_out[0]).all())

        '''Test with multiple hidden state factors and single observation modality'''

        num_states = [3, 4]
        num_obs = [3]

        prior = utils.random_single_categorical(num_states)

        A = utils.random_A_matrix(num_obs, num_states)

        obs_idx = 1
        obs = utils.onehot(obs_idx, num_obs[0])

        qs_out = inference.update_posterior_states(A, obs, prior=prior, num_iter = 1)

        # validate with a quick n' dirty implementation of FPI

        # initialize posterior and log prior
        qs_valid_init = utils.obj_array_uniform(num_states)
        log_prior = maths.spm_log_obj_array(prior)

        qs_valid_final = utils.obj_array(len(num_states))

        log_likelihood = maths.spm_log_single(maths.get_joint_likelihood(A, obs, num_states))

        num_factors = len(num_states)

        qs_valid_init_all = qs_valid_init[0]
        for factor in range(num_factors-1):
            qs_valid_init_all = qs_valid_init_all[...,None]*qs_valid_init[factor+1]
        LL_tensor = log_likelihood * qs_valid_init_all

        factor_ids = range(num_factors)

        for factor, qs_f in enumerate(qs_valid_init):
            ax2sum = tuple(set(factor_ids) - set([factor])) # which axes to sum out
            qL = LL_tensor.sum(axis = ax2sum) / qs_f
            qs_valid_final[factor] = maths.softmax(qL + log_prior[factor])

        for factor, qs_f_valid in enumerate(qs_valid_final):
            self.assertTrue(np.isclose(qs_f_valid, qs_out[factor]).all())

        '''Test with multiple hidden state factors and multiple observation modalities, for two different kinds of observation input formats'''
        
        num_states = [3, 4]
        num_obs = [3, 3, 5]

        prior = utils.random_single_categorical(num_states)

        A = utils.random_A_matrix(num_obs, num_states)

        obs_index_tuple = tuple([np.random.randint(obs_dim) for obs_dim in num_obs])

        qs_out1 = inference.update_posterior_states(A, obs_index_tuple, prior=prior)

        obs_onehots = utils.obj_array(len(num_obs))
        for g in range(len(num_obs)):
            obs_onehots[g] = utils.onehot(obs_index_tuple[g], num_obs[g])

        qs_out2 = inference.update_posterior_states(A, obs_onehots, prior=prior)

        for factor in range(len(num_states)):
            self.assertTrue(np.isclose(qs_out1[factor], qs_out2[factor]).all())

def test_update_posterior_states_factorized_single_factor(self):
        """
        Tests the version of `update_posterior_states` where an `mb_dict` is provided as an argument to factorize
        the fixed-point iteration (FPI) algorithm. Single factor version.
        """
        num_states = [3]
        num_obs = [3]       

        prior = utils.random_single_categorical(num_states)

        A = utils.to_obj_array(maths.softmax(np.eye(num_states[0]) * 0.1))

        obs_idx = 1
        obs = utils.onehot(obs_idx, num_obs[0])

        mb_dict = {'A_factor_list': [[0]],
                    'A_modality_list': [[0]]}

        qs_out = inference.update_posterior_states_factorized(A, obs, num_obs, num_states, mb_dict, prior=prior)
        qs_validation =  maths.softmax(maths.spm_log_single(A[0][obs_idx,:]) + maths.spm_log_single(prior[0]))

        self.assertTrue(np.isclose(qs_validation, qs_out[0]).all())

        '''Try single modality inference where the observation is passed in as an int'''
        qs_out_2 = inference.update_posterior_states_factorized(A, obs_idx, num_obs, num_states, mb_dict, prior=prior)
        self.assertTrue(np.isclose(qs_out_2[0], qs_out[0]).all())

        '''Try single modality inference where the observation is a one-hot stored in an object array'''
        qs_out_3 = inference.update_posterior_states_factorized(A, utils.to_obj_array(obs),num_obs, num_states, mb_dict, prior=prior)
        self.assertTrue(np.isclose(qs_out_3[0], qs_out[0]).all())

def test_update_posterior_states_factorized(self):
        """
        Tests the version of `update_posterior_states` where an `mb_dict` is provided as an argument to factorize
        the fixed-point iteration (FPI) algorithm.
        """

        num_states = [3, 4]
        num_obs = [3, 3, 5]

        prior = utils.random_single_categorical(num_states)

        obs_index_tuple = tuple([np.random.randint(obs_dim) for obs_dim in num_obs])

        mb_dict = {'A_factor_list': [[0], [1], [0, 1]],
                    'A_modality_list': [[0, 2], [1, 2]]}
        
        A_reduced = utils.random_A_matrix(num_obs, num_states, A_factor_list=mb_dict['A_factor_list'])

        qs_out = inference.update_posterior_states_factorized(A_reduced, obs_index_tuple, num_obs, num_states, mb_dict, prior=prior)

        A_full = utils.initialize_empty_A(num_obs, num_states)
        for m, A_m in enumerate(A_full):
            other_factors = list(set(range(len(num_states))) - set(mb_dict['A_factor_list'][m])) # list of the factors that modality `m` does not depend on

            # broadcast or tile the reduced A matrix (`A_reduced`) along the dimensions of corresponding to `other_factors`
            expanded_dims = [num_obs[m]] + [1 if f in other_factors else ns for (f, ns) in enumerate(num_states)]
            tile_dims = [1] + [ns if f in other_factors else 1 for (f, ns) in enumerate(num_states)]
            A_full[m] = np.tile(A_reduced[m].reshape(expanded_dims), tile_dims)
        
        qs_validation = inference.update_posterior_states(A_full, obs_index_tuple, prior=prior)

        for qs_f_val, qs_f_out in zip(qs_validation, qs_out):
            self.assertTrue(np.isclose(qs_f_val, qs_f_out).all())

def test_update_posterior_states_factorized_noVFE_compute(self):
        """
        Tests the version of `update_posterior_states` where an `mb_dict` is provided as an argument to factorize
        the fixed-point iteration (FPI) algorithm.

        In this version, we always run the total number of iterations because we don't compute the variational free energy over the course of convergence/optimization.
        """

        num_states = [3, 4]
        num_obs = [3, 3, 5]

        prior = utils.random_single_categorical(num_states)

        obs_index_tuple = tuple([np.random.randint(obs_dim) for obs_dim in num_obs])

        mb_dict = {'A_factor_list': [[0], [1], [0, 1]],
                    'A_modality_list': [[0, 2], [1, 2]]}
        
        A_reduced = utils.random_A_matrix(num_obs, num_states, A_factor_list=mb_dict['A_factor_list'])

        qs_out = inference.update_posterior_states_factorized(A_reduced, obs_index_tuple, num_obs, num_states, mb_dict, prior=prior, compute_vfe=False)

        A_full = utils.initialize_empty_A(num_obs, num_states)
        for m, A_m in enumerate(A_full):
            other_factors = list(set(range(len(num_states))) - set(mb_dict['A_factor_list'][m])) # list of the factors that modality `m` does not depend on

            # broadcast or tile the reduced A matrix (`A_reduced`) along the dimensions of corresponding to `other_factors`
            expanded_dims = [num_obs[m]] + [1 if f in other_factors else ns for (f, ns) in enumerate(num_states)]
            tile_dims = [1] + [ns if f in other_factors else 1 for (f, ns) in enumerate(num_states)]
            A_full[m] = np.tile(A_reduced[m].reshape(expanded_dims), tile_dims)
        
        qs_validation = inference.update_posterior_states(A_full, obs_index_tuple, prior=prior, compute_vfe=False)

        for qs_f_val, qs_f_out in zip(qs_validation, qs_out):
            self.assertTrue(np.isclose(qs_f_val, qs_f_out).all())

class TestInferenceJax(unittest.TestCase):

    def test_fixed_point_iteration_singlestate_singleobs(self):
        """
        Tests the jax-ified version of mean-field fixed-point iteration against the original numpy version.
        In this version there is one hidden state factor and one observation modality
        """

        num_states_list = [
                            [1],
                            [5],
                            [10]
        ]

        num_obs_list = [
                        [5],
                        [1],
                        [2]
        ]

        for (num_states, num_obs) in zip(num_states_list, num_obs_list):

            # numpy version
            prior = utils.random_single_categorical(num_states)
            A = utils.random_A_matrix(num_obs, num_states)

            obs = utils.obj_array(len(num_obs))
            for m, obs_dim in enumerate(num_obs):
                obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

            qs_numpy = fpi_numpy(A, obs, num_obs, num_states, prior=prior, num_iter=16, dF=1.0, dF_tol=-1.0) # set dF_tol to negative number so numpy version of FPI never stops early due to convergence

            # jax version
            prior = [jnp.array(prior_f) for prior_f in prior]
            A = [jnp.array(a_m) for a_m in A]
            obs = [jnp.array(o_m) for o_m in obs]

            qs_jax = fpi_jax(A, obs, prior, num_iter=16)

            for f, _ in enumerate(qs_jax):
                self.assertTrue(np.allclose(qs_numpy[f], qs_jax[f]))
    
    def test_fixed_point_iteration_singlestate_multiobs(self):
        """
        Tests the jax-ified version of mean-field fixed-point iteration against the original numpy version.
        In this version there is one hidden state factor and multiple observation modalities
        """

        num_states_list = [
                            [1],
                            [5],
                            [10]
        ]

        num_obs_list = [
                        [5, 2],
                        [1, 8, 9],
                        [2, 2, 2]
        ]

        for (num_states, num_obs) in zip(num_states_list, num_obs_list):

            # numpy version
            prior = utils.random_single_categorical(num_states)
            A = utils.random_A_matrix(num_obs, num_states)

            obs = utils.obj_array(len(num_obs))
            for m, obs_dim in enumerate(num_obs):
                obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

            qs_numpy = fpi_numpy(A, obs, num_obs, num_states, prior=prior, num_iter=16, dF=1.0, dF_tol=-1.0) # set dF_tol to negative number so numpy version of FPI never stops early due to convergence

            # jax version
            prior = [jnp.array(prior_f) for prior_f in prior]
            A = [jnp.array(a_m) for a_m in A]
            obs = [jnp.array(o_m) for o_m in obs]

            qs_jax = fpi_jax(A, obs, prior, num_iter=16)

            for f, _ in enumerate(qs_jax):
                self.assertTrue(np.allclose(qs_numpy[f], qs_jax[f]))
    
    def test_fixed_point_iteration_multistate_singleobs(self):
        """
        Tests the jax-ified version of mean-field fixed-point iteration against the original numpy version.
        In this version there are multiple hidden state factors and a single observation modality
        """

        num_states_list = [
                            [1, 10, 2],
                            [5, 5, 10, 2],
                            [10, 2]
        ]

        num_obs_list = [
                        [5],
                        [1],
                        [10]
        ]

        for (num_states, num_obs) in zip(num_states_list, num_obs_list):

            # numpy version
            prior = utils.random_single_categorical(num_states)
            A = utils.random_A_matrix(num_obs, num_states)

            obs = utils.obj_array(len(num_obs))
            for m, obs_dim in enumerate(num_obs):
                obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

            qs_numpy = fpi_numpy(A, obs, num_obs, num_states, prior=prior, num_iter=16, dF=1.0, dF_tol=-1.0) # set dF_tol to negative number so numpy version of FPI never stops early due to convergence

            # jax version
            prior = [jnp.array(prior_f) for prior_f in prior]
            A = [jnp.array(a_m) for a_m in A]
            obs = [jnp.array(o_m) for o_m in obs]

            qs_jax = fpi_jax(A, obs, prior, num_iter=16)

            for f, _ in enumerate(qs_jax):
                self.assertTrue(np.allclose(qs_numpy[f], qs_jax[f]))


    def test_fixed_point_iteration_multistate_multiobs(self):
        """
        Tests the jax-ified version of mean-field fixed-point iteration against the original numpy version.
        In this version there are multiple hidden state factors and multiple observation modalities
        """

        ''' Start by creating a collection of random generative models with different 
        cardinalities and dimensionalities of hidden state factors and observation modalities'''

        num_states_list = [ 
                         [2, 2, 5],
                         [2, 2, 2],
                         [4, 4]
        ]

        num_obs_list = [
                        [5, 10],
                        [4, 3, 2],
                        [5, 10, 6]
        ]

        for (num_states, num_obs) in zip(num_states_list, num_obs_list):

            # numpy version
            prior = utils.random_single_categorical(num_states)
            A = utils.random_A_matrix(num_obs, num_states)

            obs = utils.obj_array(len(num_obs))
            for m, obs_dim in enumerate(num_obs):
                obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

            qs_numpy = fpi_numpy(A, obs, num_obs, num_states, prior=prior, num_iter=16, dF=1.0, dF_tol=-1.0) # set dF_tol to negative number so numpy version of FPI never stops early due to convergence

            # jax version
            prior = [jnp.array(prior_f) for prior_f in prior]
            A = [jnp.array(a_m) for a_m in A]
            obs = [jnp.array(o_m) for o_m in obs]

            qs_jax = fpi_jax(A, obs, prior, num_iter=16)

            for f, _ in enumerate(qs_jax):
                self.assertTrue(np.allclose(qs_numpy[f], qs_jax[f]))
    
    def test_fixed_point_iteration_index_observations(self):
        """
        Tests the jax-ified version of mean-field fixed-point iteration against the original NumPy version.
        In this version there are multiple hidden state factors and multiple observation modalities.

        Test the jax version with index-based observations (not one-hots)
        """

        ''' Start by creating a collection of random generative models with different 
        cardinalities and dimensionalities of hidden state factors and observation modalities'''

        num_states_list = [ 
                         [2, 2, 5],
                         [2, 2, 2],
                         [4, 4]
        ]

        num_obs_list = [
                        [5, 10],
                        [4, 3, 2],
                        [5, 10, 6]
        ]

        for (num_states, num_obs) in zip(num_states_list, num_obs_list):

            # numpy version
            prior = utils.random_single_categorical(num_states)
            A = utils.random_A_matrix(num_obs, num_states)

            obs = utils.obj_array(len(num_obs))
            for m, obs_dim in enumerate(num_obs):
                obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

            qs_numpy = fpi_numpy(A, obs, num_obs, num_states, prior=prior, num_iter=16, dF=1.0, dF_tol=-1.0) # set dF_tol to negative number so numpy version of FPI never stops early due to convergence

            obs_idx = []
            for ob in obs:
                obs_idx.append(np.where(ob)[0][0])
            
            # jax version
            prior = [jnp.array(prior_f) for prior_f in prior]
            A = [jnp.array(a_m) for a_m in A]
            # obs = [jnp.array(o_m) for o_m in obs]

            qs_jax = fpi_jax(A, obs_idx, prior, num_iter=16, distr_obs=False)

            for f, _ in enumerate(qs_jax):
                self.assertTrue(np.allclose(qs_numpy[f], qs_jax[f]))

def test_fixed_point_iteration_singlestate_singleobs(self):
        """
        Tests the jax-ified version of mean-field fixed-point iteration against the original numpy version.
        In this version there is one hidden state factor and one observation modality
        """

        num_states_list = [
                            [1],
                            [5],
                            [10]
        ]

        num_obs_list = [
                        [5],
                        [1],
                        [2]
        ]

        for (num_states, num_obs) in zip(num_states_list, num_obs_list):

            # numpy version
            prior = utils.random_single_categorical(num_states)
            A = utils.random_A_matrix(num_obs, num_states)

            obs = utils.obj_array(len(num_obs))
            for m, obs_dim in enumerate(num_obs):
                obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

            qs_numpy = fpi_numpy(A, obs, num_obs, num_states, prior=prior, num_iter=16, dF=1.0, dF_tol=-1.0) # set dF_tol to negative number so numpy version of FPI never stops early due to convergence

            # jax version
            prior = [jnp.array(prior_f) for prior_f in prior]
            A = [jnp.array(a_m) for a_m in A]
            obs = [jnp.array(o_m) for o_m in obs]

            qs_jax = fpi_jax(A, obs, prior, num_iter=16)

            for f, _ in enumerate(qs_jax):
                self.assertTrue(np.allclose(qs_numpy[f], qs_jax[f]))

def test_fixed_point_iteration_singlestate_multiobs(self):
        """
        Tests the jax-ified version of mean-field fixed-point iteration against the original numpy version.
        In this version there is one hidden state factor and multiple observation modalities
        """

        num_states_list = [
                            [1],
                            [5],
                            [10]
        ]

        num_obs_list = [
                        [5, 2],
                        [1, 8, 9],
                        [2, 2, 2]
        ]

        for (num_states, num_obs) in zip(num_states_list, num_obs_list):

            # numpy version
            prior = utils.random_single_categorical(num_states)
            A = utils.random_A_matrix(num_obs, num_states)

            obs = utils.obj_array(len(num_obs))
            for m, obs_dim in enumerate(num_obs):
                obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

            qs_numpy = fpi_numpy(A, obs, num_obs, num_states, prior=prior, num_iter=16, dF=1.0, dF_tol=-1.0) # set dF_tol to negative number so numpy version of FPI never stops early due to convergence

            # jax version
            prior = [jnp.array(prior_f) for prior_f in prior]
            A = [jnp.array(a_m) for a_m in A]
            obs = [jnp.array(o_m) for o_m in obs]

            qs_jax = fpi_jax(A, obs, prior, num_iter=16)

            for f, _ in enumerate(qs_jax):
                self.assertTrue(np.allclose(qs_numpy[f], qs_jax[f]))

def test_fixed_point_iteration_multistate_singleobs(self):
        """
        Tests the jax-ified version of mean-field fixed-point iteration against the original numpy version.
        In this version there are multiple hidden state factors and a single observation modality
        """

        num_states_list = [
                            [1, 10, 2],
                            [5, 5, 10, 2],
                            [10, 2]
        ]

        num_obs_list = [
                        [5],
                        [1],
                        [10]
        ]

        for (num_states, num_obs) in zip(num_states_list, num_obs_list):

            # numpy version
            prior = utils.random_single_categorical(num_states)
            A = utils.random_A_matrix(num_obs, num_states)

            obs = utils.obj_array(len(num_obs))
            for m, obs_dim in enumerate(num_obs):
                obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

            qs_numpy = fpi_numpy(A, obs, num_obs, num_states, prior=prior, num_iter=16, dF=1.0, dF_tol=-1.0) # set dF_tol to negative number so numpy version of FPI never stops early due to convergence

            # jax version
            prior = [jnp.array(prior_f) for prior_f in prior]
            A = [jnp.array(a_m) for a_m in A]
            obs = [jnp.array(o_m) for o_m in obs]

            qs_jax = fpi_jax(A, obs, prior, num_iter=16)

            for f, _ in enumerate(qs_jax):
                self.assertTrue(np.allclose(qs_numpy[f], qs_jax[f]))

def test_fixed_point_iteration_multistate_multiobs(self):
        """
        Tests the jax-ified version of mean-field fixed-point iteration against the original numpy version.
        In this version there are multiple hidden state factors and multiple observation modalities
        """

        ''' Start by creating a collection of random generative models with different 
        cardinalities and dimensionalities of hidden state factors and observation modalities'''

        num_states_list = [ 
                         [2, 2, 5],
                         [2, 2, 2],
                         [4, 4]
        ]

        num_obs_list = [
                        [5, 10],
                        [4, 3, 2],
                        [5, 10, 6]
        ]

        for (num_states, num_obs) in zip(num_states_list, num_obs_list):

            # numpy version
            prior = utils.random_single_categorical(num_states)
            A = utils.random_A_matrix(num_obs, num_states)

            obs = utils.obj_array(len(num_obs))
            for m, obs_dim in enumerate(num_obs):
                obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

            qs_numpy = fpi_numpy(A, obs, num_obs, num_states, prior=prior, num_iter=16, dF=1.0, dF_tol=-1.0) # set dF_tol to negative number so numpy version of FPI never stops early due to convergence

            # jax version
            prior = [jnp.array(prior_f) for prior_f in prior]
            A = [jnp.array(a_m) for a_m in A]
            obs = [jnp.array(o_m) for o_m in obs]

            qs_jax = fpi_jax(A, obs, prior, num_iter=16)

            for f, _ in enumerate(qs_jax):
                self.assertTrue(np.allclose(qs_numpy[f], qs_jax[f]))

def test_fixed_point_iteration_index_observations(self):
        """
        Tests the jax-ified version of mean-field fixed-point iteration against the original NumPy version.
        In this version there are multiple hidden state factors and multiple observation modalities.

        Test the jax version with index-based observations (not one-hots)
        """

        ''' Start by creating a collection of random generative models with different 
        cardinalities and dimensionalities of hidden state factors and observation modalities'''

        num_states_list = [ 
                         [2, 2, 5],
                         [2, 2, 2],
                         [4, 4]
        ]

        num_obs_list = [
                        [5, 10],
                        [4, 3, 2],
                        [5, 10, 6]
        ]

        for (num_states, num_obs) in zip(num_states_list, num_obs_list):

            # numpy version
            prior = utils.random_single_categorical(num_states)
            A = utils.random_A_matrix(num_obs, num_states)

            obs = utils.obj_array(len(num_obs))
            for m, obs_dim in enumerate(num_obs):
                obs[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

            qs_numpy = fpi_numpy(A, obs, num_obs, num_states, prior=prior, num_iter=16, dF=1.0, dF_tol=-1.0) # set dF_tol to negative number so numpy version of FPI never stops early due to convergence

            obs_idx = []
            for ob in obs:
                obs_idx.append(np.where(ob)[0][0])
            
            # jax version
            prior = [jnp.array(prior_f) for prior_f in prior]
            A = [jnp.array(a_m) for a_m in A]
            # obs = [jnp.array(o_m) for o_m in obs]

            qs_jax = fpi_jax(A, obs_idx, prior, num_iter=16, distr_obs=False)

            for f, _ in enumerate(qs_jax):
                self.assertTrue(np.allclose(qs_numpy[f], qs_jax[f]))

class TestLearningJax(unittest.TestCase):

    def test_update_observation_likelihood_fullyconnected(self):
        """
        Testing JAX-ified version of updating Dirichlet posterior over observation likelihood parameters (qA is posterior, pA is prior, and A is expectation
        of likelihood wrt to current posterior over A, i.e. $A = E_{Q(A)}[P(o|s,A)]$.

        This is the so-called 'fully-connected' version where all hidden state factors drive each modality (i.e. A_dependencies is a list of lists of hidden state factors)
        """

        num_obs_list = [ [5], 
                        [10, 3, 2], 
                        [2, 4, 4, 2],
                        [10]
                        ]
        num_states_list = [ [2,3,4], 
                        [2], 
                        [4,5],
                        [3] 
                        ]

        A_dependencies_list = [ [ [0,1,2] ],
                                [ [0], [0], [0] ],
                                [ [0,1], [0,1], [0,1], [0,1] ],
                                [ [0] ]
                                ]

        for (num_obs, num_states, A_dependencies) in zip(num_obs_list, num_states_list, A_dependencies_list):
            # create numpy arrays to test numpy version of learning

            # create A matrix initialization (expected initial value of P(o|s, A)) and prior over A (pA)
            A_np = utils.random_A_matrix(num_obs, num_states)
            pA_np = utils.dirichlet_like(A_np, scale = 3.0)

            # create random observations 
            obs_np = utils.obj_array(len(num_obs))
            for m, obs_dim in enumerate(num_obs):
                obs_np[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

            # create random state posterior
            qs_np = utils.random_single_categorical(num_states)

            l_rate = 1.0

            # run numpy version of learning
            qA_np_test = update_pA_numpy(pA_np, A_np, obs_np, qs_np, lr=l_rate)

            pA_jax = jtu.tree_map(lambda x: jnp.array(x), list(pA_np))
            A_jax = jtu.tree_map(lambda x: jnp.array(x), list(A_np))
            obs_jax = jtu.tree_map(lambda x: jnp.array(x)[None], list(obs_np))
            qs_jax = jtu.tree_map(lambda x: jnp.array(x)[None], list(qs_np))

            qA_jax_test, E_qA_jax_test = update_pA_jax(
                pA_jax,
                A_jax,
                obs_jax,
                qs_jax,
                A_dependencies=A_dependencies,
                onehot_obs=True,
                num_obs=num_obs,
                lr=l_rate
            )

            for modality, obs_dim in enumerate(num_obs):
                self.assertTrue(np.allclose(qA_jax_test[modality], qA_np_test[modality]))

    def test_update_observation_likelihood_factorized(self):
        """
        Testing JAX-ified version of updating Dirichlet posterior over observation likelihood parameters (qA is posterior, pA is prior, and A is expectation
        of likelihood wrt to current posterior over A, i.e. $A = E_{Q(A)}[P(o|s,A)]$.

        This is the factorized version where only some hidden state factors drive each modality (i.e. A_dependencies is a list of lists of hidden state factors)
        """

        num_obs_list = [ [5], 
                        [10, 3, 2], 
                        [2, 4, 4, 2],
                        [10]
                        ]
        num_states_list = [ [2,3,4], 
                        [2, 5, 2], 
                        [4,5],
                        [3] 
                        ]

        A_dependencies_list = [ [ [0,1] ],
                                [ [0, 1], [1], [1, 2] ],
                                [ [0,1], [0], [0,1], [1] ],
                                [ [0] ]
                                ]

        for (num_obs, num_states, A_dependencies) in zip(num_obs_list, num_states_list, A_dependencies_list):
            # create numpy arrays to test numpy version of learning

            # create A matrix initialization (expected initial value of P(o|s, A)) and prior over A (pA)
            A_np = utils.random_A_matrix(num_obs, num_states, A_factor_list=A_dependencies)
            pA_np = utils.dirichlet_like(A_np, scale = 3.0)

            # create random observations 
            obs_np = utils.obj_array(len(num_obs))
            for m, obs_dim in enumerate(num_obs):
                obs_np[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

            # create random state posterior
            qs_np = utils.random_single_categorical(num_states)

            l_rate = 1.0

            # run numpy version of learning
            qA_np_test = update_pA_numpy_factorized(pA_np, A_np, obs_np, qs_np, A_dependencies, lr=l_rate)

            pA_jax = jtu.tree_map(lambda x: jnp.array(x), list(pA_np))
            A_jax = jtu.tree_map(lambda x: jnp.array(x), list(A_np))
            obs_jax = jtu.tree_map(lambda x: jnp.array(x)[None], list(obs_np))
            qs_jax = jtu.tree_map(lambda x: jnp.array(x)[None], list(qs_np))

            qA_jax_test, E_qA_jax_test = update_pA_jax(
                pA_jax,
                A_jax,
                obs_jax,
                qs_jax,
                A_dependencies=A_dependencies,
                onehot_obs=True,
                num_obs=num_obs,
                lr=l_rate
            )

            for modality, obs_dim in enumerate(num_obs):
                self.assertTrue(np.allclose(qA_jax_test[modality],qA_np_test[modality]))

def test_update_observation_likelihood_fullyconnected(self):
        """
        Testing JAX-ified version of updating Dirichlet posterior over observation likelihood parameters (qA is posterior, pA is prior, and A is expectation
        of likelihood wrt to current posterior over A, i.e. $A = E_{Q(A)}[P(o|s,A)]$.

        This is the so-called 'fully-connected' version where all hidden state factors drive each modality (i.e. A_dependencies is a list of lists of hidden state factors)
        """

        num_obs_list = [ [5], 
                        [10, 3, 2], 
                        [2, 4, 4, 2],
                        [10]
                        ]
        num_states_list = [ [2,3,4], 
                        [2], 
                        [4,5],
                        [3] 
                        ]

        A_dependencies_list = [ [ [0,1,2] ],
                                [ [0], [0], [0] ],
                                [ [0,1], [0,1], [0,1], [0,1] ],
                                [ [0] ]
                                ]

        for (num_obs, num_states, A_dependencies) in zip(num_obs_list, num_states_list, A_dependencies_list):
            # create numpy arrays to test numpy version of learning

            # create A matrix initialization (expected initial value of P(o|s, A)) and prior over A (pA)
            A_np = utils.random_A_matrix(num_obs, num_states)
            pA_np = utils.dirichlet_like(A_np, scale = 3.0)

            # create random observations 
            obs_np = utils.obj_array(len(num_obs))
            for m, obs_dim in enumerate(num_obs):
                obs_np[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

            # create random state posterior
            qs_np = utils.random_single_categorical(num_states)

            l_rate = 1.0

            # run numpy version of learning
            qA_np_test = update_pA_numpy(pA_np, A_np, obs_np, qs_np, lr=l_rate)

            pA_jax = jtu.tree_map(lambda x: jnp.array(x), list(pA_np))
            A_jax = jtu.tree_map(lambda x: jnp.array(x), list(A_np))
            obs_jax = jtu.tree_map(lambda x: jnp.array(x)[None], list(obs_np))
            qs_jax = jtu.tree_map(lambda x: jnp.array(x)[None], list(qs_np))

            qA_jax_test, E_qA_jax_test = update_pA_jax(
                pA_jax,
                A_jax,
                obs_jax,
                qs_jax,
                A_dependencies=A_dependencies,
                onehot_obs=True,
                num_obs=num_obs,
                lr=l_rate
            )

            for modality, obs_dim in enumerate(num_obs):
                self.assertTrue(np.allclose(qA_jax_test[modality], qA_np_test[modality]))

def test_update_observation_likelihood_factorized(self):
        """
        Testing JAX-ified version of updating Dirichlet posterior over observation likelihood parameters (qA is posterior, pA is prior, and A is expectation
        of likelihood wrt to current posterior over A, i.e. $A = E_{Q(A)}[P(o|s,A)]$.

        This is the factorized version where only some hidden state factors drive each modality (i.e. A_dependencies is a list of lists of hidden state factors)
        """

        num_obs_list = [ [5], 
                        [10, 3, 2], 
                        [2, 4, 4, 2],
                        [10]
                        ]
        num_states_list = [ [2,3,4], 
                        [2, 5, 2], 
                        [4,5],
                        [3] 
                        ]

        A_dependencies_list = [ [ [0,1] ],
                                [ [0, 1], [1], [1, 2] ],
                                [ [0,1], [0], [0,1], [1] ],
                                [ [0] ]
                                ]

        for (num_obs, num_states, A_dependencies) in zip(num_obs_list, num_states_list, A_dependencies_list):
            # create numpy arrays to test numpy version of learning

            # create A matrix initialization (expected initial value of P(o|s, A)) and prior over A (pA)
            A_np = utils.random_A_matrix(num_obs, num_states, A_factor_list=A_dependencies)
            pA_np = utils.dirichlet_like(A_np, scale = 3.0)

            # create random observations 
            obs_np = utils.obj_array(len(num_obs))
            for m, obs_dim in enumerate(num_obs):
                obs_np[m] = utils.onehot(np.random.randint(obs_dim), obs_dim)

            # create random state posterior
            qs_np = utils.random_single_categorical(num_states)

            l_rate = 1.0

            # run numpy version of learning
            qA_np_test = update_pA_numpy_factorized(pA_np, A_np, obs_np, qs_np, A_dependencies, lr=l_rate)

            pA_jax = jtu.tree_map(lambda x: jnp.array(x), list(pA_np))
            A_jax = jtu.tree_map(lambda x: jnp.array(x), list(A_np))
            obs_jax = jtu.tree_map(lambda x: jnp.array(x)[None], list(obs_np))
            qs_jax = jtu.tree_map(lambda x: jnp.array(x)[None], list(qs_np))

            qA_jax_test, E_qA_jax_test = update_pA_jax(
                pA_jax,
                A_jax,
                obs_jax,
                qs_jax,
                A_dependencies=A_dependencies,
                onehot_obs=True,
                num_obs=num_obs,
                lr=l_rate
            )

            for modality, obs_dim in enumerate(num_obs):
                self.assertTrue(np.allclose(qA_jax_test[modality],qA_np_test[modality]))

def update_posterior_policies_full(
    qs_seq_pi,
    A,
    B,
    C,
    policies,
    use_utility=True,
    use_states_info_gain=True,
    use_param_info_gain=False,
    prior=None,
    pA=None,
    pB=None,
    F=None,
    E=None,
    I=None,
    gamma=16.0
):  
    """
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
    """

    num_obs, num_states, num_modalities, num_factors = utils.get_model_dimensions(A, B)
    horizon = len(qs_seq_pi[0])
    num_policies = len(qs_seq_pi)

    qo_seq = utils.obj_array(horizon)
    for t in range(horizon):
        qo_seq[t] = utils.obj_array_zeros(num_obs)

    # initialise expected observations
    qo_seq_pi = utils.obj_array(num_policies)

    # initialize (negative) expected free energies for all policies
    G = np.zeros(num_policies)

    if F is None:
        F = spm_log_single(np.ones(num_policies) / num_policies)

    if E is None:
        lnE = spm_log_single(np.ones(num_policies) / num_policies)
    else:
        lnE = spm_log_single(E) 

    if I is not None:
        init_qs_all_pi = [qs_seq_pi[p][0] for p in range(num_policies)]
        qs_bma = average_states_over_policies(init_qs_all_pi, softmax(E))

    for p_idx, policy in enumerate(policies):

        qo_seq_pi[p_idx] = get_expected_obs(qs_seq_pi[p_idx], A)

        if use_utility:
            G[p_idx] += calc_expected_utility(qo_seq_pi[p_idx], C)
        
        if use_states_info_gain:
            G[p_idx] += calc_states_info_gain(A, qs_seq_pi[p_idx])
        
        if use_param_info_gain:
            if pA is not None:
                G[p_idx] += calc_pA_info_gain(pA, qo_seq_pi[p_idx], qs_seq_pi[p_idx])
            if pB is not None:
                G[p_idx] += calc_pB_info_gain(pB, qs_seq_pi[p_idx], prior, policy)
        
        if I is not None:
            G[p_idx] += calc_inductive_cost(qs_bma, qs_seq_pi[p_idx], I)

    q_pi = softmax(G * gamma - F + lnE)
    
    return q_pi, G

def update_posterior_policies_full_factorized(
    qs_seq_pi,
    A,
    B,
    C,
    A_factor_list,
    B_factor_list,
    policies,
    use_utility=True,
    use_states_info_gain=True,
    use_param_info_gain=False,
    prior=None,
    pA=None,
    pB=None,
    F=None,
    E=None,
    I=None,
    gamma=16.0
):  
    """
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
    """

    num_obs, num_states, num_modalities, num_factors = utils.get_model_dimensions(A, B)
    horizon = len(qs_seq_pi[0])
    num_policies = len(qs_seq_pi)

    qo_seq = utils.obj_array(horizon)
    for t in range(horizon):
        qo_seq[t] = utils.obj_array_zeros(num_obs)

    # initialise expected observations
    qo_seq_pi = utils.obj_array(num_policies)

    # initialize (negative) expected free energies for all policies
    G = np.zeros(num_policies)

    if F is None:
        F = spm_log_single(np.ones(num_policies) / num_policies)

    if E is None:
        lnE = spm_log_single(np.ones(num_policies) / num_policies)
    else:
        lnE = spm_log_single(E) 

    if I is not None:
        init_qs_all_pi = [qs_seq_pi[p][0] for p in range(num_policies)]
        qs_bma = average_states_over_policies(init_qs_all_pi, softmax(E))

    for p_idx, policy in enumerate(policies):

        qo_seq_pi[p_idx] = get_expected_obs_factorized(qs_seq_pi[p_idx], A, A_factor_list)

        if use_utility:
            G[p_idx] += calc_expected_utility(qo_seq_pi[p_idx], C)
        
        if use_states_info_gain:
            G[p_idx] += calc_states_info_gain_factorized(A, qs_seq_pi[p_idx], A_factor_list)
        
        if use_param_info_gain:
            if pA is not None:
                G[p_idx] += calc_pA_info_gain_factorized(pA, qo_seq_pi[p_idx], qs_seq_pi[p_idx], A_factor_list)
            if pB is not None:
                G[p_idx] += calc_pB_info_gain_interactions(pB, qs_seq_pi[p_idx], qs_seq_pi[p_idx], B_factor_list, policy)
        
        if I is not None:
            G[p_idx] += calc_inductive_cost(qs_bma, qs_seq_pi[p_idx], I)
            
    q_pi = softmax(G * gamma - F + lnE)
    
    return q_pi, G

def update_posterior_policies(
    qs,
    A,
    B,
    C,
    policies,
    use_utility=True,
    use_states_info_gain=True,
    use_param_info_gain=False,
    pA=None,
    pB=None,
    E=None,
    I=None,
    gamma=16.0
):
    """
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
    """

    n_policies = len(policies)
    G = np.zeros(n_policies)
    q_pi = np.zeros((n_policies, 1))

    if E is None:
        lnE = spm_log_single(np.ones(n_policies) / n_policies)
    else:
        lnE = spm_log_single(E) 

    for idx, policy in enumerate(policies):
        qs_pi = get_expected_states(qs, B, policy)
        qo_pi = get_expected_obs(qs_pi, A)

        if use_utility:
            G[idx] += calc_expected_utility(qo_pi, C)

        if use_states_info_gain:
            G[idx] += calc_states_info_gain(A, qs_pi)

        if use_param_info_gain:
            if pA is not None:
                G[idx] += calc_pA_info_gain(pA, qo_pi, qs_pi).item()
            if pB is not None:
                G[idx] += calc_pB_info_gain(pB, qs_pi, qs, policy).item()
        
        if I is not None:
            G[idx] += calc_inductive_cost(qs, qs_pi, I)

    q_pi = softmax(G * gamma + lnE)    

    return q_pi, G

def update_posterior_policies_factorized(
    qs,
    A,
    B,
    C,
    A_factor_list,
    B_factor_list,
    policies,
    use_utility=True,
    use_states_info_gain=True,
    use_param_info_gain=False,
    pA=None,
    pB=None,
    E=None,
    I=None,
    gamma=16.0
):
    """
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
    """

    n_policies = len(policies)
    G = np.zeros(n_policies)
    q_pi = np.zeros((n_policies, 1))

    if E is None:
        lnE = spm_log_single(np.ones(n_policies) / n_policies)
    else:
        lnE = spm_log_single(E) 

    for idx, policy in enumerate(policies):
        qs_pi = get_expected_states_interactions(qs, B, B_factor_list, policy)
        qo_pi = get_expected_obs_factorized(qs_pi, A, A_factor_list)

        if use_utility:
            G[idx] += calc_expected_utility(qo_pi, C)

        if use_states_info_gain:
            G[idx] += calc_states_info_gain_factorized(A, qs_pi, A_factor_list)

        if use_param_info_gain:
            if pA is not None:
                G[idx] += calc_pA_info_gain_factorized(pA, qo_pi, qs_pi, A_factor_list).item()
            if pB is not None:
                G[idx] += calc_pB_info_gain_interactions(pB, qs_pi, qs, B_factor_list, policy).item()
        
        if I is not None:
            G[idx] += calc_inductive_cost(qs, qs_pi, I)

    q_pi = softmax(G * gamma + lnE)    

    return q_pi, G

def get_expected_states(qs, B, policy):
    """
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
    """
    n_steps = policy.shape[0]
    n_factors = policy.shape[1]

    # initialise posterior predictive density as a list of beliefs over time, including current posterior beliefs about hidden states as the first element
    qs_pi = [qs] + [utils.obj_array(n_factors) for t in range(n_steps)]
    
    # get expected states over time
    for t in range(n_steps):
        for control_factor, action in enumerate(policy[t,:]):
            qs_pi[t+1][control_factor] = B[control_factor][:,:,int(action)].dot(qs_pi[t][control_factor])

    return qs_pi[1:]

def get_expected_states_interactions(qs, B, B_factor_list, policy):
    """
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
    """
    n_steps = policy.shape[0]
    n_factors = policy.shape[1]

    # initialise posterior predictive density as a list of beliefs over time, including current posterior beliefs about hidden states as the first element
    qs_pi = [qs] + [utils.obj_array(n_factors) for t in range(n_steps)]
    
    # get expected states over time
    for t in range(n_steps):
        for control_factor, action in enumerate(policy[t,:]):
            factor_idx = B_factor_list[control_factor] # list of the hidden state factor indices that the dynamics of `qs[control_factor]` depend on
            qs_pi[t+1][control_factor] = spm_dot(B[control_factor][...,int(action)], qs_pi[t][factor_idx])

    return qs_pi[1:]

def get_expected_obs(qs_pi, A):
    """
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
    """

    n_steps = len(qs_pi) # each element of the list is the PPD at a different timestep

    # initialise expected observations
    qo_pi = []

    for t in range(n_steps):
        qo_pi_t = utils.obj_array(len(A))
        qo_pi.append(qo_pi_t)

    # compute expected observations over time
    for t in range(n_steps):
        for modality, A_m in enumerate(A):
            qo_pi[t][modality] = spm_dot(A_m, qs_pi[t])

    return qo_pi

def get_expected_obs_factorized(qs_pi, A, A_factor_list):
    """
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
    """

    n_steps = len(qs_pi) # each element of the list is the PPD at a different timestep

    # initialise expected observations
    qo_pi = []

    for t in range(n_steps):
        qo_pi_t = utils.obj_array(len(A))
        qo_pi.append(qo_pi_t)

    # compute expected observations over time
    for t in range(n_steps):
        for modality, A_m in enumerate(A):
            factor_idx = A_factor_list[modality] # list of the hidden state factor indices that observation modality with the index `modality` depends on
            qo_pi[t][modality] = spm_dot(A_m, qs_pi[t][factor_idx])

    return qo_pi

def calc_expected_utility(qo_pi, C):
    """
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
    """
    n_steps = len(qo_pi)
    
    # initialise expected utility
    expected_util = 0

    # loop over time points and modalities
    num_modalities = len(C)

    # reformat C to be tiled across timesteps, if it's not already
    modalities_to_tile = [modality_i for modality_i in range(num_modalities) if C[modality_i].ndim == 1]

    # make a deepcopy of C where it has been tiled across timesteps
    C_tiled = copy.deepcopy(C)
    for modality in modalities_to_tile:
        C_tiled[modality] = np.tile(C[modality][:,None], (1, n_steps) )
    
    C_prob = softmax_obj_arr(C_tiled) # convert relative log probabilities into proper probability distribution

    for t in range(n_steps):
        for modality in range(num_modalities):

            lnC = spm_log_single(C_prob[modality][:, t])
            expected_util += qo_pi[t][modality].dot(lnC)

    return expected_util

def calc_states_info_gain(A, qs_pi):
    """
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
    """

    n_steps = len(qs_pi)

    states_surprise = 0
    for t in range(n_steps):
        states_surprise += spm_MDP_G(A, qs_pi[t])

    return states_surprise

def calc_states_info_gain_factorized(A, qs_pi, A_factor_list):
    """
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
    """

    n_steps = len(qs_pi)

    states_surprise = 0
    for t in range(n_steps):
        for m, A_m in enumerate(A):
            factor_idx = A_factor_list[m] # list of the hidden state factor indices that observation modality with the index `m` depends on
            states_surprise += spm_MDP_G(A_m, qs_pi[t][factor_idx])

    return states_surprise

def calc_pA_info_gain(pA, qo_pi, qs_pi):
    """
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
    """

    n_steps = len(qo_pi)
    
    num_modalities = len(pA)
    wA = utils.obj_array(num_modalities)
    for modality, pA_m in enumerate(pA):
        wA[modality] = spm_wnorm(pA[modality])

    pA_infogain = 0
    
    for modality in range(num_modalities):
        wA_modality = wA[modality] * (pA[modality] > 0).astype("float")
        for t in range(n_steps):
            pA_infogain -= qo_pi[t][modality].dot(spm_dot(wA_modality, qs_pi[t])[:, np.newaxis])

    return pA_infogain

def calc_pA_info_gain_factorized(pA, qo_pi, qs_pi, A_factor_list):
    """
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
    """

    n_steps = len(qo_pi)
    
    num_modalities = len(pA)
    wA = utils.obj_array(num_modalities)
    for modality, pA_m in enumerate(pA):
        wA[modality] = spm_wnorm(pA[modality])

    pA_infogain = 0
    
    for modality in range(num_modalities):
        wA_modality = wA[modality] * (pA[modality] > 0).astype("float")
        factor_idx = A_factor_list[modality]
        for t in range(n_steps):
            pA_infogain -= qo_pi[t][modality].dot(spm_dot(wA_modality, qs_pi[t][factor_idx])[:, np.newaxis])

    return pA_infogain

def calc_pB_info_gain(pB, qs_pi, qs_prev, policy):
    """
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
    """

    n_steps = len(qs_pi)

    num_factors = len(pB)
    wB = utils.obj_array(num_factors)
    for factor, pB_f in enumerate(pB):
        wB[factor] = spm_wnorm(pB_f)

    pB_infogain = 0

    for t in range(n_steps):
        # the 'past posterior' used for the information gain about pB here is the posterior
        # over expected states at the timestep previous to the one under consideration
        # if we're on the first timestep, we just use the latest posterior in the
        # entire action-perception cycle as the previous posterior
        if t == 0:
            previous_qs = qs_prev
        # otherwise, we use the expected states for the timestep previous to the timestep under consideration
        else:
            previous_qs = qs_pi[t - 1]

        # get the list of action-indices for the current timestep
        policy_t = policy[t, :]
        for factor, a_i in enumerate(policy_t):
            wB_factor_t = wB[factor][:, :, int(a_i)] * (pB[factor][:, :, int(a_i)] > 0).astype("float")
            pB_infogain -= qs_pi[t][factor].dot(wB_factor_t.dot(previous_qs[factor]))

    return pB_infogain

def calc_pB_info_gain_interactions(pB, qs_pi, qs_prev, B_factor_list, policy):
    """
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
    """

    n_steps = len(qs_pi)

    num_factors = len(pB)
    wB = utils.obj_array(num_factors)
    for factor, pB_f in enumerate(pB):
        wB[factor] = spm_wnorm(pB_f)

    pB_infogain = 0

    for t in range(n_steps):
        # the 'past posterior' used for the information gain about pB here is the posterior
        # over expected states at the timestep previous to the one under consideration
        # if we're on the first timestep, we just use the latest posterior in the
        # entire action-perception cycle as the previous posterior
        if t == 0:
            previous_qs = qs_prev
        # otherwise, we use the expected states for the timestep previous to the timestep under consideration
        else:
            previous_qs = qs_pi[t - 1]

        # get the list of action-indices for the current timestep
        policy_t = policy[t, :]
        for factor, a_i in enumerate(policy_t):
            wB_factor_t = wB[factor][...,int(a_i)] * (pB[factor][...,int(a_i)] > 0).astype("float")
            f_idx = B_factor_list[factor]
            pB_infogain -= qs_pi[t][factor].dot(spm_dot(wB_factor_t, previous_qs[f_idx]))

    return pB_infogain

def calc_inductive_cost(qs, qs_pi, I, epsilon=1e-3):
    """
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
    """
    n_steps = len(qs_pi)
    
    # initialise inductive cost
    inductive_cost = 0

    # loop over time points and modalities
    num_factors = len(I)

    for t in range(n_steps):
        for factor in range(num_factors):
            # we also assume precise beliefs here?!
            idx = np.argmax(qs[factor])
            # m = arg max_n p_n < sup p
            # i.e. find first I idx equals 1 and m is the index before
            m = np.where(I[factor][:, idx] == 1)[0]
            # we might find no path to goal (i.e. when no goal specified)
            if len(m) > 0:
                m = max(m[0]-1, 0)
                I_m = (1-I[factor][m, :]) * np.log(epsilon)
                inductive_cost += I_m.dot(qs_pi[t][factor])
                
    return inductive_cost

def construct_policies(num_states, num_controls = None, policy_len=1, control_fac_idx=None):
    """
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
    """

    num_factors = len(num_states)
    if control_fac_idx is None:
        if num_controls is not None:
            control_fac_idx = [f for f, n_c in enumerate(num_controls) if n_c > 1]
        else:
            control_fac_idx = list(range(num_factors))

    if num_controls is None:
        num_controls = [num_states[c_idx] if c_idx in control_fac_idx else 1 for c_idx in range(num_factors)]
        
    x = num_controls * policy_len
    policies = list(itertools.product(*[list(range(i)) for i in x]))
    for pol_i in range(len(policies)):
        policies[pol_i] = np.array(policies[pol_i]).reshape(policy_len, num_factors)

    return policies

def get_num_controls_from_policies(policies):
    """
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
    """

    return list(np.max(np.vstack(policies), axis = 0) + 1)

def sample_action(q_pi, policies, num_controls, action_selection="deterministic", alpha = 16.0):
    """
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
    """

    num_factors = len(num_controls)

    action_marginals = utils.obj_array_zeros(num_controls)

    # weight each action according to its integrated posterior probability under all policies at the current timestep
    for pol_idx, policy in enumerate(policies):
        for factor_i, action_i in enumerate(policy[0, :]):
            action_marginals[factor_i][action_i] += q_pi[pol_idx]
    
    action_marginals = utils.norm_dist_obj_arr(action_marginals)

    selected_policy = np.zeros(num_factors)
    for factor_i in range(num_factors):

        # Either you do this:
        if action_selection == 'deterministic':
            selected_policy[factor_i] = select_highest(action_marginals[factor_i])
        elif action_selection == 'stochastic':
            log_marginal_f = spm_log_single(action_marginals[factor_i])
            p_actions = softmax(log_marginal_f * alpha)
            selected_policy[factor_i] = utils.sample(p_actions)

    return selected_policy

def _sample_action_test(q_pi, policies, num_controls, action_selection="deterministic", alpha = 16.0, seed=None):
    """
    Computes the marginal posterior over actions and then samples an action from it, one action per control factor.
    Internal testing version that returns the marginal posterior over actions, and also has a seed argument for reproducibility.

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
    alpha: float, default 16.0
        Action selection precision -- the inverse temperature of the softmax that is used to scale the 
        action marginals before sampling. This is only used if ``action_selection`` argument is "stochastic"
    seed: ``int``, default None
        The seed can be set to control the random sampling that occurs when ``action_selection`` is "deterministic" but there are more than one actions with the same maximum posterior probability.


    Returns
    ----------
    selected_policy: 1D ``numpy.ndarray``
        Vector containing the indices of the actions for each control factor
    p_actions: ``numpy.ndarray`` of dtype object
        Marginal posteriors over actions, after softmaxing and scaling with action precision. This distribution will be used to sample actions,
        if``action_selection`` argument is "stochastic"
    """

    num_factors = len(num_controls)

    action_marginals = utils.obj_array_zeros(num_controls)
    
    # weight each action according to its integrated posterior probability under all policies at the current timestep
    for pol_idx, policy in enumerate(policies):
        for factor_i, action_i in enumerate(policy[0, :]):
            action_marginals[factor_i][action_i] += q_pi[pol_idx]
    
    action_marginals = utils.norm_dist_obj_arr(action_marginals)

    selected_policy = np.zeros(num_factors)
    p_actions = utils.obj_array_zeros(num_controls)
    for factor_i in range(num_factors):
        if action_selection == 'deterministic':
            p_actions[factor_i] = action_marginals[factor_i]
            selected_policy[factor_i] = _select_highest_test(p_actions[factor_i], seed=seed)
        elif action_selection == 'stochastic':
            log_marginal_f = spm_log_single(action_marginals[factor_i])
            p_actions[factor_i] = softmax(log_marginal_f * alpha)
            selected_policy[factor_i] = utils.sample(p_actions[factor_i])

    return selected_policy, p_actions

def sample_policy(q_pi, policies, num_controls, action_selection="deterministic", alpha = 16.0):
    """
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
    """

    num_factors = len(num_controls)

    if action_selection == "deterministic":
        policy_idx = select_highest(q_pi)
    elif action_selection == "stochastic":
        log_qpi = spm_log_single(q_pi)
        p_policies = softmax(log_qpi * alpha)
        policy_idx = utils.sample(p_policies)

    selected_policy = np.zeros(num_factors)
    for factor_i in range(num_factors):
        selected_policy[factor_i] = policies[policy_idx][0, factor_i]

    return selected_policy

def _sample_policy_test(q_pi, policies, num_controls, action_selection="deterministic", alpha = 16.0, seed=None):
    """
    Test version of sampling a policy from the posterior over policies, taking the action (per control factor) entailed by the first timestep of the selected policy.
    This test version also returns the probability distribution over policies, and also has a seed argument for reproducibility.
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
    seed: ``int``, default None
        The seed can be set to control the random sampling that occurs when ``action_selection`` is "deterministic" but there are more than one actions with the same maximum posterior probability.

   
    Returns
    ----------
    selected_policy: 1D ``numpy.ndarray``
        Vector containing the indices of the actions for each control factor
    """

    num_factors = len(num_controls)

    if action_selection == "deterministic":
        p_policies = q_pi
        policy_idx = _select_highest_test(p_policies, seed=seed)
    elif action_selection == "stochastic":
        log_qpi = spm_log_single(q_pi)
        p_policies = softmax(log_qpi * alpha)
        policy_idx = utils.sample(p_policies)

    selected_policy = np.zeros(num_factors)
    for factor_i in range(num_factors):
        selected_policy[factor_i] = policies[policy_idx][0, factor_i]

    return selected_policy, p_policies

def select_highest(options_array):
    """
    Selects the highest value among the provided ones. If the higher value is more than once and they're closer than 1e-5, a random choice is made.
    Parameters
    ----------
    options_array: ``numpy.ndarray``
        The array to examine

    Returns
    -------
    The highest value in the given list
    """
    options_with_idx = np.array(list(enumerate(options_array)))
    same_prob = options_with_idx[
                    abs(options_with_idx[:, 1] - np.amax(options_with_idx[:, 1])) <= 1e-8][:, 0]
    if len(same_prob) > 1:
        # If some of the most likely actions have nearly equal probability, sample from this subset of actions, instead of using argmax
        return int(same_prob[np.random.choice(len(same_prob))])

    return int(same_prob[0])

def _select_highest_test(options_array, seed=None):
    """
    (Test version with seed argument for reproducibility) Selects the highest value among the provided ones. If the higher value is more than once and they're closer than 1e-8, a random choice is made.
    Parameters
    ----------
    options_array: ``numpy.ndarray``
        The array to examine

    Returns
    -------
    The highest value in the given list
    """
    options_with_idx = np.array(list(enumerate(options_array)))
    same_prob = options_with_idx[
                    abs(options_with_idx[:, 1] - np.amax(options_with_idx[:, 1])) <= 1e-8][:, 0]
    if len(same_prob) > 1:
        # If some of the most likely actions have nearly equal probability, sample from this subset of actions, instead of using argmax
        rng = np.random.default_rng(seed)
        return int(same_prob[rng.choice(len(same_prob))])

    return int(same_prob[0])

def backwards_induction(H, B, B_factor_list, threshold, depth):
    """
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
    """
    # TODO can this be done with arbitrary B_factor_list?
    
    num_factors = len(H)
    I = utils.obj_array(num_factors)
    for factor in range(num_factors):
        I[factor] = np.zeros((depth, H[factor].shape[0]))
        I[factor][0, :] = H[factor]

        bf = factor
        if B_factor_list is not None:
            if len(B_factor_list[factor]) > 1:
                raise ValueError("Backwards induction with factorized transition model not yet implemented")
            bf = B_factor_list[factor][0]

        num_states, _, _ = B[bf].shape
        b = np.zeros((num_states, num_states))
        
        for state in range(num_states):
            for next_state in range(num_states):
                # If there exists an action that allows transitioning 
                # from state to next_state, with probability larger than threshold
                # set b[state, next_state] to 1
                if np.any(B[bf][next_state, state, :] > threshold):
                    b[next_state, state] = 1

        for i in range(1, depth):
            I[factor][i, :] = np.dot(b, I[factor][i-1, :])
            I[factor][i, :] = np.where(I[factor][i, :] > 0.1, 1.0, 0.0)
            # TODO stop when all 1s?

    return I

def calc_ambiguity_factorized(qs_pi, A, A_factor_list):
    """
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
    """

    n_steps = len(qs_pi)

    ambiguity = 0
    # TODO check if we do this correctly!
    H = entropy(A)
    for t in range(n_steps):
        for m, H_m in enumerate(H):
            factor_idx = A_factor_list[m]
            # TODO why does spm_dot return an array here?
            # joint_x = maths.spm_cross(qs_pi[t][factor_idx])
            # ambiguity += (H_m * joint_x).sum()
            ambiguity += np.sum(spm_dot(H_m, qs_pi[t][factor_idx]))

    return ambiguity

def sophisticated_inference_search(qs, policies, A, B, C, A_factor_list, B_factor_list, I=None, horizon=1,
                                   policy_prune_threshold=1/16, state_prune_threshold=1/16, prune_penalty=512, gamma=16,
                                   inference_params = {"num_iter": 10, "dF": 1.0, "dF_tol": 0.001, "compute_vfe": False}, n=0):
    """
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
    """

    n_policies = len(policies)
    G = np.zeros(n_policies)
    q_pi = np.zeros((n_policies, 1))
    qs_pi = utils.obj_array(n_policies)
    qo_pi = utils.obj_array(n_policies)

    for idx, policy in enumerate(policies):
        qs_pi[idx] = get_expected_states_interactions(qs, B, B_factor_list, policy)
        qo_pi[idx] = get_expected_obs_factorized(qs_pi[idx], A, A_factor_list)

        G[idx] += calc_expected_utility(qo_pi[idx], C)
        G[idx] += calc_states_info_gain_factorized(A, qs_pi[idx], A_factor_list)

        if I is not None:
            G[idx] += calc_inductive_cost(qs, qs_pi[idx], I)

    q_pi = softmax(G * gamma)

    if n < horizon - 1:
        # ignore low probability actions in the search tree
        # TODO shouldnt we have to add extra penalty for branches no longer considered?
        # or assume these are already low EFE (high NEFE) anyway?
        policies_to_consider = list(np.where(q_pi >= policy_prune_threshold)[0])
        for idx in range(n_policies):
            if idx not in policies_to_consider:
                G[idx] -= prune_penalty
            else :
                # average over outcomes
                qo_next = qo_pi[idx][0]
                for k in itertools.product(*[range(s.shape[0]) for s in qo_next]):
                    prob = 1.0
                    for i in range(len(k)):
                        prob *= qo_pi[idx][0][i][k[i]]
                    
                    # ignore low probability states in the search tree
                    if prob < state_prune_threshold:
                        continue

                    qo_one_hot = utils.obj_array(len(qo_next))
                    for i in range(len(qo_one_hot)):
                        qo_one_hot[i] = utils.onehot(k[i], qo_next[i].shape[0])
                    
                    num_obs = [A[m].shape[0] for m in range(len(A))]
                    num_states = [B[f].shape[0] for f in range(len(B))]
                    A_modality_list = []
                    for f in range(len(B)):
                        A_modality_list.append( [m for m in range(len(A)) if f in A_factor_list[m]] )
                    mb_dict = {
                        'A_factor_list': A_factor_list,
                        'A_modality_list': A_modality_list
                        }
                    qs_next = update_posterior_states_factorized(A, qo_one_hot, num_obs, num_states, mb_dict, qs_pi[idx][0], **inference_params)
                    q_pi_next, G_next = sophisticated_inference_search(qs_next, policies, A, B, C, A_factor_list, B_factor_list, I,
                                                                       horizon, policy_prune_threshold, state_prune_threshold,
                                                                       prune_penalty, gamma, inference_params, n+1)
                    G_weighted = np.dot(q_pi_next, G_next) * prob
                    G[idx] += G_weighted

    q_pi = softmax(G * gamma)
    return q_pi, G

class Dimensions(object):
    """
    The Dimensions class stores all data related to the size and shape of a model.
    """
    def __init__(
        self,
        num_observations=None,
        num_observation_modalities=0,
        num_states=None,
        num_state_factors=0,
        num_controls=None,
        num_control_factors=0,
    ):
        self.num_observations=num_observations
        self.num_observation_modalities=num_observation_modalities
        self.num_states=num_states
        self.num_state_factors=num_state_factors
        self.num_controls=num_controls
        self.num_control_factors=num_control_factors

def sample(probabilities):
    probabilities = probabilities.squeeze() if len(probabilities) > 1 else probabilities
    sample_onehot = np.random.multinomial(1, probabilities)
    return np.where(sample_onehot == 1)[0][0]

def sample_obj_array(arr):
    """ 
    Sample from set of Categorical distributions, stored in the sub-arrays of an object array 
    """
    
    samples = [sample(arr_i) for arr_i in arr]

    return samples

def obj_array(num_arr):
    """
    Creates a generic object array with the desired number of sub-arrays, given by `num_arr`
    """
    return np.empty(num_arr, dtype=object)

def obj_array_zeros(shape_list):
    """ 
    Creates a numpy object array whose sub-arrays are 1-D vectors
    filled with zeros, with shapes given by shape_list[i]
    """
    arr = obj_array(len(shape_list))
    for i, shape in enumerate(shape_list):
        arr[i] = np.zeros(shape)
    return arr

def initialize_empty_A(num_obs, num_states):
    """ 
    Initializes an empty observation likelihood array or `A` array using a list of observation-modality dimensions (`num_obs`)
    and hidden state factor dimensions (`num_states`)
    """

    A_shape_list = [ [no] + num_states for no in num_obs]
    return obj_array_zeros(A_shape_list)

def initialize_empty_B(num_states, num_controls):
    """ 
    Initializes an empty (controllable) transition likelihood array or `B` array using a list of hidden state factor dimensions (`num_states`)
    and control factor dimensions (`num_controls)
    """

    B_shape_list = [ [ns, ns, num_controls[f]] for f, ns in enumerate(num_states)]
    return obj_array_zeros(B_shape_list)

def obj_array_uniform(shape_list):
    """ 
    Creates a numpy object array whose sub-arrays are uniform Categorical
    distributions with shapes given by shape_list[i]. The shapes (elements of shape_list)
    can either be tuples or lists.
    """
    arr = obj_array(len(shape_list))
    for i, shape in enumerate(shape_list):
        arr[i] = norm_dist(np.ones(shape))
    return arr

def obj_array_ones(shape_list, scale = 1.0):
    arr = obj_array(len(shape_list))
    for i, shape in enumerate(shape_list):
        arr[i] = scale * np.ones(shape)
    
    return arr

def onehot(value, num_values):
    arr = np.zeros(num_values)
    arr[value] = 1.0
    return arr

def random_A_matrix(num_obs, num_states, A_factor_list=None):
    if type(num_obs) is int:
        num_obs = [num_obs]
    if type(num_states) is int:
        num_states = [num_states]
    num_modalities = len(num_obs)

    if A_factor_list is None:
        num_factors = len(num_states)
        A_factor_list = [list(range(num_factors))] * num_modalities

    A = obj_array(num_modalities)
    for modality, modality_obs in enumerate(num_obs):
        # lagging_dimensions = [ns for i, ns in enumerate(num_states) if i in A_factor_list[modality]] # enforces sortedness of A_factor_list
        lagging_dimensions = [num_states[idx] for idx in A_factor_list[modality]]
        modality_shape = [modality_obs] + lagging_dimensions
        modality_dist = np.random.rand(*modality_shape)
        A[modality] = norm_dist(modality_dist)
    return A

def random_B_matrix(num_states, num_controls, B_factor_list=None):
    if type(num_states) is int:
        num_states = [num_states]
    if type(num_controls) is int:
        num_controls = [num_controls]
    num_factors = len(num_states)
    assert len(num_controls) == len(num_states)

    if B_factor_list is None:
        B_factor_list = [[f] for f in range(num_factors)]

    B = obj_array(num_factors)
    for factor in range(num_factors):
        lagging_shape = [ns for i, ns in enumerate(num_states) if i in B_factor_list[factor]]
        factor_shape = [num_states[factor]] + lagging_shape + [num_controls[factor]]
        # factor_shape = (num_states[factor], num_states[factor], num_controls[factor])
        factor_dist = np.random.rand(*factor_shape)
        B[factor] = norm_dist(factor_dist)
    return B

def random_single_categorical(shape_list):
    """
    Creates a random 1-D categorical distribution (or set of 1-D categoricals, e.g. multiple marginals of different factors) and returns them in an object array 
    """
    
    num_sub_arrays = len(shape_list)

    out = obj_array(num_sub_arrays)

    for arr_idx, shape_i  in enumerate(shape_list):
        out[arr_idx] = norm_dist(np.random.rand(shape_i))
    
    return out

def construct_controllable_B(num_states, num_controls):
    """
    Generates a fully controllable transition likelihood array, where each 
    action (control state) corresponds to a move to the n-th state from any 
    other state, for each control factor
    """

    num_factors = len(num_states)

    B = obj_array(num_factors)
    for factor, c_dim in enumerate(num_controls):
        tmp = np.eye(c_dim)[:, :, np.newaxis]
        tmp = np.tile(tmp, (1, 1, c_dim))
        B[factor] = tmp.transpose(1, 2, 0)

    return B

def dirichlet_like(template_categorical, scale = 1.0):
    """
    Helper function to construct a Dirichlet distribution based on an existing Categorical distribution
    """ 

    if not is_obj_array(template_categorical):
        warnings.warn(
                    "Input array is not an object array...\
                    Casting the input to an object array"
                )
        template_categorical = to_obj_array(template_categorical)

    n_sub_arrays = len(template_categorical)

    dirichlet_out = obj_array(n_sub_arrays)
    
    for i, arr in enumerate(template_categorical):
        dirichlet_out[i] = scale * arr

    return dirichlet_out

def get_model_dimensions(A=None, B=None, factorized=False):

    if A is None and B is None:
        raise ValueError(
                    "Must provide either `A` or `B`"
                )

    if A is not None:
        num_obs = [a.shape[0] for a in A] if is_obj_array(A) else [A.shape[0]]
        num_modalities = len(num_obs)
    else:
        num_obs, num_modalities = None, None
    
    if B is not None:
        num_states = [b.shape[0] for b in B] if is_obj_array(B) else [B.shape[0]]
        num_factors = len(num_states)
    else:
        if A is not None:
            if not factorized:
                num_states = list(A[0].shape[1:]) if is_obj_array(A) else list(A.shape[1:])
                num_factors = len(num_states)
            else:
                raise ValueError(
                    "`A` array is factorized and  cannot be used to infer `num_states`"
                )
        else:
            num_states, num_factors = None, None
    
    return num_obs, num_states, num_modalities, num_factors

def get_model_dimensions_from_labels(model_labels):

    modalities = model_labels['observations']
    factors = model_labels['states']

    res = Dimensions(
        num_observations=[len(modalities[modality]) for modality in modalities.keys()],
        num_observation_modalities=len(modalities.keys()),
        num_states=[len(factors[factor]) for factor in factors.keys()],
        num_state_factors=len(factors.keys()),
    )

    if 'actions' in model_labels.keys():
        controls = model_labels['actions']
        res.num_controls=[len(controls[cfac]) for cfac in controls.keys()]
        res.num_control_factors=len(controls.keys())

    return res

def norm_dist(dist):
    """ Normalizes a Categorical probability distribution (or set of them) assuming sufficient statistics are stored in leading dimension"""
    return np.divide(dist, dist.sum(axis=0))

def norm_dist_obj_arr(obj_arr):
    """ Normalizes a multi-factor or -modality collection of Categorical probability distributions, assuming sufficient statistics of each conditional distribution
    are stored in the leading dimension"""
    normed_obj_array = obj_array(len(obj_arr))
    for i, arr in enumerate(obj_arr):
        normed_obj_array[i] = norm_dist(arr)
    
    return normed_obj_array

def is_normalized(dist):
    """
    Utility function for checking whether a single distribution or set of conditional categorical distributions is normalized.
    Returns True if all distributions integrate to 1.0
    """

    if is_obj_array(dist):
        normed_arrays = []
        for i, arr in enumerate(dist):
            column_sums = arr.sum(axis=0)
            normed_arrays.append(np.allclose(column_sums, np.ones_like(column_sums)))
        out = all(normed_arrays)
    else:
        column_sums = dist.sum(axis=0)
        out = np.allclose(column_sums, np.ones_like(column_sums))
    
    return out

def is_obj_array(arr):
    return arr.dtype == "object"

def to_obj_array(arr):
    if is_obj_array(arr):
        return arr
    obj_array_out = obj_array(1)
    obj_array_out[0] = arr.squeeze()
    return obj_array_out

def obj_array_from_list(list_input):
    """
    Takes a list of `numpy.ndarray` and converts them to a `numpy.ndarray` of `dtype = object`
    """
    arr = obj_array(len(list_input))
    for i, item in enumerate(list_input):
        arr[i] = item
    return arr

def process_observation_seq(obs_seq, n_modalities, n_observations):
    """
    Helper function for formatting observations    

        Observations can either be `int` (converted to one-hot)
        or `tuple` (obs for each modality), or `list` (obs for each modality)
        If list, the entries could be object arrays of one-hots, in which
        case this function returns `obs_seq` as is.
    """
    proc_obs_seq = obj_array(len(obs_seq))
    for t, obs_t in enumerate(obs_seq):
        proc_obs_seq[t] = process_observation(obs_t, n_modalities, n_observations)
    return proc_obs_seq

def process_observation(obs, num_modalities, num_observations):
    """
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
    """

    if isinstance(obs, np.ndarray) and not is_obj_array(obs):
        assert num_modalities == 1, "If `obs` is a 1D numpy array, `num_modalities` must be equal to 1"
        assert len(np.where(obs)[0]) == 1, "If `obs` is a 1D numpy array, it must be a one hot vector (e.g. np.array([0.0, 1.0, 0.0, ....]))"

    if isinstance(obs, (int, np.integer)):
        obs = onehot(obs, num_observations[0])

    if isinstance(obs, tuple) or isinstance(obs,list):
        obs_arr_arr = obj_array(num_modalities)
        for m in range(num_modalities):
            obs_arr_arr[m] = onehot(obs[m], num_observations[m])
        obs = obs_arr_arr

    return obs

def convert_observation_array(obs, num_obs):
    """
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
    """

    T = obs.shape[1]
    num_modalities = len(num_obs)

    # Initialise the output
    obs_t = []
    # Case of one modality
    if num_modalities == 1:
        for t in range(T):
            obs_t.append(onehot(obs[0, t] - 1, num_obs[0]))
    else:
        for t in range(T):
            obs_AoA = obj_array(num_modalities)
            for g in range(num_modalities):
                # Subtract obs[g,t] by 1 to account for MATLAB vs. Python indexing
                # (MATLAB is 1-indexed)
                obs_AoA[g] = onehot(obs[g, t] - 1, num_obs[g])
            obs_t.append(obs_AoA)

    return obs_t

def insert_multiple(s, indices, items):
    for idx in range(len(items)):
        s.insert(indices[idx], items[idx])
    return s

def reduce_a_matrix(A):
    """
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
    """

    o_dim, num_states = A.shape[0], A.shape[1:]
    idx_vec_s = [slice(0, o_dim)]  + [slice(ns) for _, ns in enumerate(num_states)]

    original_factor_idx = []
    excluded_factor_idx = [] # the indices of the hidden state factors that are independent of the observation and thus marginalized away
    for factor_i, ns in enumerate(num_states):

        level_counter = 0
        break_flag = False
        while level_counter < ns and break_flag is False:
            idx_vec_i = idx_vec_s.copy()
            idx_vec_i[factor_i+1] = slice(level_counter,level_counter+1,None)
            if not np.isclose(A.mean(axis=factor_i+1), A[tuple(idx_vec_i)].squeeze()).all():
                break_flag = True # this means they're not independent
                original_factor_idx.append(factor_i)
            else:
                level_counter += 1
        
        if break_flag is False:
            excluded_factor_idx.append(factor_i+1)
    
    A_reduced = A.mean(axis=tuple(excluded_factor_idx)).squeeze()

    return A_reduced, original_factor_idx

def construct_full_a(A_reduced, original_factor_idx, num_states):
    """
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
    """

    o_dim = A_reduced.shape[0] # dimensionality of the support of the likelihood distribution (i.e. the number of observation levels)
    full_dimensionality = [o_dim] + num_states # full dimensionality of the output (`A`)
    fill_indices = [0] +  [f+1 for f in original_factor_idx] # these are the indices of the dimensions we need to fill for this modality
    fill_dimensions = np.delete(full_dimensionality, fill_indices) 

    original_factor_dims = [num_states[f] for f in original_factor_idx] # dimensionalities of the relevant factors
    prefilled_slices = [slice(0, o_dim)] + [slice(0, ns) for ns in original_factor_dims] # these are the slices that are filled out by the provided `A_reduced`

    A = np.zeros(full_dimensionality)

    for item in itertools.product(*[list(range(d)) for d in fill_dimensions]):
        slice_ = list(item)
        A_indices = insert_multiple(slice_, fill_indices, prefilled_slices) #here we insert the correct values for the fill indices for this slice                    
        A[tuple(A_indices)] = A_reduced
    
    return A

def build_xn_vn_array(xn):

    """
    This function constructs array-ified (not nested) versions
    of the posterior xn (beliefs) or vn (prediction error) arrays, that are separated 
    by iteration, hidden state factor, timepoint, and policy
    """

    num_policies = len(xn)
    num_itr = len(xn[0])
    num_factors = len(xn[0][0])

    if num_factors > 1:
        xn_array = obj_array(num_factors)
        for factor in range(num_factors):
            num_states, infer_len = xn[0][0][factor].shape
            xn_array[factor] = np.zeros( (num_itr, num_states, infer_len, num_policies) )
        for policy_i in range(num_policies):
            for itr in range(num_itr):
                for factor in range(num_factors):
                    xn_array[factor][itr,:,:,policy_i] = xn[policy_i][itr][factor]
    else:
        num_states, infer_len  = xn[0][0][0].shape
        xn_array = np.zeros( (num_itr, num_states, infer_len, num_policies) )
        for policy_i in range(num_policies):
            for itr in range(num_itr):
                xn_array[itr,:,:,policy_i] = xn[policy_i][itr][0] 
    
    return xn_array

def plot_beliefs(belief_dist, title=""):
    """
    Utility function that plots a bar chart of a categorical probability distribution,
    with each bar height corresponding to the probability of one of the elements of the categorical
    probability vector.
    """

    plt.grid(zorder=0)
    plt.bar(range(belief_dist.shape[0]), belief_dist, color='r', zorder=3)
    plt.xticks(range(belief_dist.shape[0]))
    plt.title(title)
    plt.show()

def plot_likelihood(A, title=""):
    """
    Utility function that shows a heatmap of a 2-D likelihood (hidden causes in the columns, observations in the rows),
    with hotter colors indicating higher probability.
    """

    ax = sns.heatmap(A, cmap="OrRd", linewidth=2.5)
    plt.xticks(range(A.shape[1]+1))
    plt.yticks(range(A.shape[0]+1))
    plt.title(title)
    plt.show()

def __init__(
        self,
        num_observations=None,
        num_observation_modalities=0,
        num_states=None,
        num_state_factors=0,
        num_controls=None,
        num_control_factors=0,
    ):
        self.num_observations=num_observations
        self.num_observation_modalities=num_observation_modalities
        self.num_states=num_states
        self.num_state_factors=num_state_factors
        self.num_controls=num_controls
        self.num_control_factors=num_control_factors

def spm_dot(X, x, dims_to_omit=None):
    """ Dot product of a multidimensional array with `x`. The dimensions in `dims_to_omit` 
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
    """

    # Construct dims to perform dot product on
    if utils.is_obj_array(x):
        # dims = list((np.arange(0, len(x)) + X.ndim - len(x)).astype(int))
        dims = list(range(X.ndim - len(x),len(x)+X.ndim - len(x)))
        # dims = list(range(X.ndim))
    else:
        dims = [1]
        x = utils.to_obj_array(x)

    if dims_to_omit is not None:
        arg_list = [X, list(range(X.ndim))] + list(chain(*([x[xdim_i],[dims[xdim_i]]] for xdim_i in range(len(x)) if xdim_i not in dims_to_omit))) + [dims_to_omit]
    else:
        arg_list = [X, list(range(X.ndim))] + list(chain(*([x[xdim_i],[dims[xdim_i]]] for xdim_i in range(len(x))))) + [[0]]

    Y = np.einsum(*arg_list)

    # check to see if `Y` is a scalar
    if np.prod(Y.shape) <= 1.0:
        Y = Y.item()
        Y = np.array([Y]).astype("float64")

    return Y

def spm_dot_classic(X, x, dims_to_omit=None):
    """ Dot product of a multidimensional array with `x`. The dimensions in `dims_to_omit` 
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
    """

    # Construct dims to perform dot product on
    if utils.is_obj_array(x):
        dims = (np.arange(0, len(x)) + X.ndim - len(x)).astype(int)
    else:
        dims = np.array([1], dtype=int)
        x = utils.to_obj_array(x)

    # delete ignored dims
    if dims_to_omit is not None:
        if not isinstance(dims_to_omit, list):
            raise ValueError("`dims_to_omit` must be a `list` of `int`")
        dims = np.delete(dims, dims_to_omit)
        if len(x) == 1:
            x = np.empty([0], dtype=object)
        else:
            x = np.delete(x, dims_to_omit)

    # compute dot product
    for d in range(len(x)):
        s = np.ones(np.ndim(X), dtype=int)
        s[dims[d]] = np.shape(x[d])[0]
        X = X * x[d].reshape(tuple(s))
        # X = np.sum(X, axis=dims[d], keepdims=True)

    Y = np.sum(X, axis=tuple(dims.astype(int))).squeeze()
    # Y = np.squeeze(X)

    # check to see if `Y` is a scalar
    if np.prod(Y.shape) <= 1.0:
        Y = Y.item()
        Y = np.array([Y]).astype("float64")

    return Y

def factor_dot_flex(M, xs, dims, keep_dims=None):
    """ Dot product of a multidimensional array with `x`.
    
    Parameters
    ----------
    - `M` [numpy.ndarray] - tensor
    - 'xs' [list of numpyr.ndarray] - list of tensors
    - 'dims' [list of tuples] - list of dimensions of xs tensors in tensor M
    - 'keep_dims' [tuple] - tuple of integers denoting dimesions to keep
    Returns 
    -------
    - `Y` [1D numpy.ndarray] - the result of the dot product
    """
    all_dims = tuple(range(M.ndim))
    matrix = [[xs[f], dims[f]] for f in range(len(xs))]
    args = [M, all_dims]
    for row in matrix:
        args.extend(row)

    args += [keep_dims]
    return contract(*args, backend='numpy')

def spm_dot_old(X, x, dims_to_omit=None, obs_mode=False):
    """ Dot product of a multidimensional array with `x`. The dimensions in `dims_to_omit` 
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
    """

    # Construct dims to perform dot product on
    if utils.is_obj_array(x):
        dims = (np.arange(0, len(x)) + X.ndim - len(x)).astype(int)
    else:
        if obs_mode is True:
            """
            @NOTE Case when you're getting the likelihood of an observation under 
                  the generative model. Equivalent to something like self.values[np.where(x),:]
                  when `x` is a discrete 'one-hot' observation vector
            """
            dims = np.array([0], dtype=int)
        else:
            """
            @NOTE Case when `x` leading dimension matches the lagging dimension of `values`
                  E.g. a more 'classical' dot product of a likelihood with hidden states
            """
            dims = np.array([1], dtype=int)

        x = utils.to_obj_array(x)

    # delete ignored dims
    if dims_to_omit is not None:
        if not isinstance(dims_to_omit, list):
            raise ValueError("`dims_to_omit` must be a `list` of `int`")
        dims = np.delete(dims, dims_to_omit)
        if len(x) == 1:
            x = np.empty([0], dtype=object)
        else:
            x = np.delete(x, dims_to_omit)

    # compute dot product
    for d in range(len(x)):
        s = np.ones(np.ndim(X), dtype=int)
        s[dims[d]] = np.shape(x[d])[0]
        X = X * x[d].reshape(tuple(s))
        # X = np.sum(X, axis=dims[d], keepdims=True)

    Y = np.sum(X, axis=tuple(dims.astype(int))).squeeze()
    # Y = np.squeeze(X)

    # check to see if `Y` is a scalar
    if np.prod(Y.shape) <= 1.0:
        Y = Y.item()
        Y = np.array([Y]).astype("float64")

    return Y

def spm_cross(x, y=None, *args):
    """ Multi-dimensional outer product
    
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
    """

    if len(args) == 0 and y is None:
        if utils.is_obj_array(x):
            z = spm_cross(*list(x))
        elif np.issubdtype(x.dtype, np.number):
            z = x
        else:
            raise ValueError(f"Invalid input to spm_cross ({x})")
        return z

    if utils.is_obj_array(x):
        x = spm_cross(*list(x))

    if y is not None and utils.is_obj_array(y):
        y = spm_cross(*list(y))

    A = np.expand_dims(x, tuple(range(-y.ndim, 0)))
    B = np.expand_dims(y, tuple(range(x.ndim)))
    z = A * B

    for x in args:
        z = spm_cross(z, x)
    return z

def dot_likelihood(A,obs):

    s = np.ones(np.ndim(A), dtype = int)
    s[0] = obs.shape[0]
    X = A * obs.reshape(tuple(s))
    X = np.sum(X, axis=0, keepdims=True)
    LL = np.squeeze(X)

    # check to see if `LL` is a scalar
    if np.prod(LL.shape) <= 1.0:
        LL = LL.item()
        LL = np.array([LL]).astype("float64")

    return LL

def get_joint_likelihood(A, obs, num_states):
    # deal with single modality case
    if type(num_states) is int:
        num_states = [num_states]
    A = utils.to_obj_array(A)
    obs = utils.to_obj_array(obs)
    ll = np.ones(tuple(num_states))
    for modality in range(len(A)):
        ll = ll * dot_likelihood(A[modality], obs[modality])
    return ll

def get_joint_likelihood_seq(A, obs, num_states):
    ll_seq = utils.obj_array(len(obs))
    for t, obs_t in enumerate(obs):
        ll_seq[t] = get_joint_likelihood(A, obs_t, num_states)
    return ll_seq

def get_joint_likelihood_seq_by_modality(A, obs, num_states):
    """
    Returns joint likelihoods for each modality separately
    """

    ll_seq = utils.obj_array(len(obs))
    n_modalities = len(A)

    for t, obs_t in enumerate(obs):
        likelihood = utils.obj_array(n_modalities)
        obs_t_obj = utils.to_obj_array(obs_t)
        for (m, A_m) in enumerate(A):
            likelihood[m] = dot_likelihood(A_m, obs_t_obj[m])
        ll_seq[t] = likelihood
    
    return ll_seq

def spm_norm(A):
    """ 
    Returns normalization of Categorical distribution, 
    stored in the columns of A.
    """
    A = A + EPS_VAL
    normed_A = np.divide(A, A.sum(axis=0))
    return normed_A

def spm_log_single(arr):
    """
    Adds small epsilon value to an array before natural logging it
    """
    return np.log(arr + EPS_VAL)

def spm_log_obj_array(obj_arr):
    """
    Applies `spm_log_single` to multiple elements of a numpy object array
    """

    obj_arr_logged = utils.obj_array(len(obj_arr))
    for idx, arr in enumerate(obj_arr):
        obj_arr_logged[idx] = spm_log_single(arr)

    return obj_arr_logged

def spm_wnorm(A):
    """ 
    Returns Expectation of logarithm of Dirichlet parameters over a set of 
    Categorical distributions, stored in the columns of A.
    """
    A = A + EPS_VAL
    norm = np.divide(1.0, np.sum(A, axis=0))
    avg = np.divide(1.0, A)
    wA = norm - avg
    return wA

def spm_betaln(z):
    """ Log of the multivariate beta function of a vector.
     @NOTE this function computes across columns if `z` is a matrix
    """
    return special.gammaln(z).sum(axis=0) - special.gammaln(z.sum(axis=0))

def dirichlet_log_evidence(q_dir, p_dir, r_dir):
    """
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
    """

    # change in free energy or log model evidence
    s_dir = q_dir + r_dir - p_dir
    F  = spm_betaln(q_dir) + spm_betaln(r_dir) - spm_betaln(p_dir) - spm_betaln(s_dir)

    return F, s_dir

def softmax(dist):
    """ 
    Computes the softmax function on a set of values
    """

    output = dist - dist.max(axis=0)
    output = np.exp(output)
    output = output / np.sum(output, axis=0)
    return output

def softmax_obj_arr(arr):

    output = utils.obj_array(len(arr))

    for i, arr_i in enumerate(arr):
        output[i] = softmax(arr_i)
    
    return output

def compute_accuracy(log_likelihood, qs):
    """
    Function that computes the accuracy term of the variational free energy. This is essentially a stripped down version of `spm_dot` above,
    with fewer conditions / dimension handling in the beginning.
    """ 

    ndims_ll, n_factors = log_likelihood.ndim, len(qs)

    dims = list(range(ndims_ll - n_factors,n_factors+ndims_ll - n_factors))
    arg_list = [log_likelihood, list(range(ndims_ll))] + list(chain(*([qs[xdim_i],[dims[xdim_i]]] for xdim_i in range(n_factors))))

    return np.einsum(*arg_list)

def calc_free_energy(qs, prior, n_factors, likelihood=None):
    """ Calculate variational free energy
    @TODO Primarily used in FPI algorithm, needs to be made general
    """
    free_energy = 0
    for factor in range(n_factors):
        # Neg-entropy of posterior marginal H(q[f])
        negH_qs = qs[factor].dot(np.log(qs[factor][:, np.newaxis] + 1e-16))
        # Cross entropy of posterior marginal with prior marginal H(q[f],p[f])
        xH_qp = -qs[factor].dot(prior[factor][:, np.newaxis])
        free_energy += negH_qs + xH_qp

    if likelihood is not None:
        free_energy -= compute_accuracy(likelihood, qs)
    return free_energy

def spm_calc_qo_entropy(A, x):
    """ 
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
    """

    num_modalities = len(A)

    # Probability distribution over the hidden causes: i.e., Q(x)
    qx = spm_cross(x)
    qo = 0
    idx = np.array(np.where(qx > np.exp(-16))).T

    if utils.is_obj_array(A):
        # Accumulate expectation of entropy: i.e., E_{Q(o, x)}[lnP(o|x)] = E_{P(o|x)Q(x)}[lnP(o|x)] = E_{Q(x)}[P(o|x)lnP(o|x)] = E_{Q(x)}[H[P(o|x)]]
        for i in idx:
            # Probability over outcomes for this combination of causes
            po = np.ones(1)
            for modality_idx, A_m in enumerate(A):
                index_vector = [slice(0, A_m.shape[0])] + list(i)
                po = spm_cross(po, A_m[tuple(index_vector)])
            po = po.ravel()
            qo += qx[tuple(i)] * po
    else:
        for i in idx:
            po = np.ones(1)
            index_vector = [slice(0, A.shape[0])] + list(i)
            po = spm_cross(po, A[tuple(index_vector)])
            po = po.ravel()
            qo += qx[tuple(i)] * po
   
    # Compute entropy of expectations: i.e., -E_{Q(o)}[lnQ(o)]
    H = - qo.dot(spm_log_single(qo))

    return H

def spm_calc_neg_ambig(A, x):
    """
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
    """

    num_modalities = len(A)

    # Probability distribution over the hidden causes: i.e., Q(x)
    qx = spm_cross(x)
    G = 0
    qo = 0
    idx = np.array(np.where(qx > np.exp(-16))).T

    if utils.is_obj_array(A):
        # Accumulate expectation of entropy: i.e., E_{Q(o, x)}[lnP(o|x)] = E_{P(o|x)Q(x)}[lnP(o|x)] = E_{Q(x)}[P(o|x)lnP(o|x)] = E_{Q(x)}[H[P(o|x)]]
        for i in idx:
            # Probability over outcomes for this combination of causes
            po = np.ones(1)
            for modality_idx, A_m in enumerate(A):
                index_vector = [slice(0, A_m.shape[0])] + list(i)
                po = spm_cross(po, A_m[tuple(index_vector)])

            po = po.ravel()
            qo += qx[tuple(i)] * po
            G += qx[tuple(i)] * po.dot(np.log(po + np.exp(-16)))
    else:
        for i in idx:
            po = np.ones(1)
            index_vector = [slice(0, A.shape[0])] + list(i)
            po = spm_cross(po, A[tuple(index_vector)])
            po = po.ravel()
            qo += qx[tuple(i)] * po
            G += qx[tuple(i)] * po.dot(np.log(po + np.exp(-16)))

    return G

def spm_MDP_G(A, x):
    """
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
    """

    num_modalities = len(A)

    # Probability distribution over the hidden causes: i.e., Q(x)
    qx = spm_cross(x)
    G = 0
    qo = 0
    idx = np.array(np.where(qx > np.exp(-16))).T

    if utils.is_obj_array(A):
        # Accumulate expectation of entropy: i.e., E_{Q(o, x)}[lnP(o|x)] = E_{P(o|x)Q(x)}[lnP(o|x)] = E_{Q(x)}[P(o|x)lnP(o|x)] = E_{Q(x)}[H[P(o|x)]]
        for i in idx:
            # Probability over outcomes for this combination of causes
            po = np.ones(1)
            for modality_idx, A_m in enumerate(A):
                index_vector = [slice(0, A_m.shape[0])] + list(i)
                po = spm_cross(po, A_m[tuple(index_vector)])
            
            po = po.ravel()
            qo += qx[tuple(i)] * po
            G += qx[tuple(i)] * po.dot(np.log(po + np.exp(-16)))
    else:
        for i in idx:
            po = np.ones(1)
            index_vector = [slice(0, A.shape[0])] + list(i)
            po = spm_cross(po, A[tuple(index_vector)])
            po = po.ravel()
            qo += qx[tuple(i)] * po
            G += qx[tuple(i)] * po.dot(np.log(po + np.exp(-16)))
   
    # Subtract negative entropy of expectations: i.e., E_{Q(o)}[lnQ(o)]
    G = G - qo.dot(spm_log_single(qo))  # type: ignore

    return G

def kl_div(P,Q):
    """
    Parameters
    ----------
    P : Categorical probability distribution
    Q : Categorical probability distribution

    Returns
    -------
    The KL-divergence of P and Q

    """
    dkl = 0
    for i in range(len(P)):
        dkl += np.dot(P[i], np.log(P[i] + EPS_VAL) - np.log(Q[i] + EPS_VAL))
    return(dkl)

def entropy(A):
    """
    Compute the entropy term H of the likelihood matrix,
    i.e. one entropy value per column
    """
    entropies = np.empty(len(A), dtype=object)
    for i in range(len(A)):
        if len(A[i].shape) > 2:
            obs_dim = A[i].shape[0]
            s_dim = A[i].size // obs_dim
            A_merged = A[i].reshape(obs_dim, s_dim)
        else:
            A_merged = A[i]

        H = - np.diag(np.matmul(A_merged.T, np.log(A_merged + EPS_VAL)))
        entropies[i] = H.reshape(*A[i].shape[1:])
    return entropies

def generate_epistemic_MAB_model():
    '''
    Create the generative model matrices (A, B, C, D) for the 'epistemic multi-armed bandit',
    used in the `agent_demo.py` Python file and the `agent_demo.ipynb` notebook.
    ''' 
    
    num_states = [2, 3]  
    num_obs = [3, 3, 3]
    num_controls = [1, 3] 
    A = utils.obj_array_zeros([[o] + num_states for _, o in enumerate(num_obs)])

    """
    MODALITY 0 -- INFORMATION-ABOUT-REWARD-STATE MODALITY
    """

    A[0][:, :, 0] = np.ones( (num_obs[0], num_states[0]) ) / num_obs[0]
    A[0][:, :, 1] = np.ones( (num_obs[0], num_states[0]) ) / num_obs[0]
    A[0][:, :, 2] = np.array([[0.8, 0.2], [0.0, 0.0], [0.2, 0.8]])

    """
    MODALITY 1 -- REWARD MODALITY
    """

    A[1][2, :, 0] = np.ones(num_states[0])
    A[1][0:2, :, 1] = maths.softmax(np.eye(num_obs[1] - 1)) # bandit statistics (mapping between reward-state (first hidden state factor) and rewards (Good vs Bad))
    A[1][2, :, 2] = np.ones(num_states[0])

    """
    MODALITY 2 -- LOCATION-OBSERVATION MODALITY
    """
    A[2][0,:,0] = 1.0
    A[2][1,:,1] = 1.0
    A[2][2,:,2] = 1.0

    control_fac_idx = [1] # this is the controllable control state factor, where there will be a >1-dimensional control state along this factor
    B = utils.obj_array_zeros([[n_s, n_s, num_controls[f]] for f, n_s in enumerate(num_states)])

    """
    FACTOR 0 -- REWARD STATE DYNAMICS
    """

    p_stoch = 0.0

    # we cannot influence factor zero, set up the 'default' stationary dynamics - 
    # one state just maps to itself at the next timestep with very high probability, by default. So this means the reward state can
    # change from one to another with some low probability (p_stoch)

    B[0][0, 0, 0] = 1.0 - p_stoch
    B[0][1, 0, 0] = p_stoch

    B[0][1, 1, 0] = 1.0 - p_stoch
    B[0][0, 1, 0] = p_stoch
    
    """
    FACTOR 1 -- CONTROLLABLE LOCATION DYNAMICS
    """
    # setup our controllable factor.
    B[1] = utils.construct_controllable_B(num_states, num_controls)[1]

    C = utils.obj_array_zeros(num_obs)
    C[1][0] = 1.0  # make the observation we've a priori named `REWARD` actually desirable, by building a high prior expectation of encountering it 
    C[1][1] = -1.0    # make the observation we've a prior named `PUN` actually aversive,by building a low prior expectation of encountering it

    control_fac_idx = [1]

    return A, B, C, control_fac_idx

def generate_grid_world_transitions(action_labels, num_rows = 3, num_cols = 3):
    """ 
    Wrapper code for creating the controllable transition matrix 
    that an agent can use to navigate in a 2-dimensional grid world
    """

    num_grid_locs = num_rows * num_cols

    transition_matrix = np.zeros( (num_grid_locs, num_grid_locs, len(action_labels)) )

    grid = np.arange(num_grid_locs).reshape(num_rows, num_cols)
    it = np.nditer(grid, flags=["multi_index"])

    loc_list = []
    while not it.finished:
        loc_list.append(it.multi_index)
        it.iternext()

    for action_id, action_label in enumerate(action_labels):

        for curr_state, grid_location in enumerate(loc_list):

            curr_row, curr_col = grid_location
            
            if action_label == "LEFT":
                next_col = curr_col - 1 if curr_col > 0 else curr_col 
                next_row = curr_row
            elif action_label == "DOWN":
                next_row = curr_row + 1 if curr_row < (num_rows-1) else curr_row 
                next_col = curr_col
            elif action_label == "RIGHT":
                next_col = curr_col + 1 if curr_col < (num_cols-1) else curr_col 
                next_row = curr_row
            elif action_label == "UP":
                next_row = curr_row - 1 if curr_row > 0 else curr_row 
                next_col = curr_col
            elif action_label == "STAY":
                next_row, next_col = curr_row, curr_col

            new_location = (next_row, next_col)
            next_state = loc_list.index(new_location)
            transition_matrix[next_state, curr_state, action_id] = 1.0
    
    return transition_matrix

class Agent(object):
    """ 
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
    """

    def __init__(
        self,
        A,
        B,
        C=None,
        D=None,
        E=None,
        H=None,
        pA=None,
        pB=None,
        pD=None,
        num_controls=None,
        policy_len=1,
        inference_horizon=1,
        control_fac_idx=None,
        policies=None,
        gamma=16.0,
        alpha=16.0,
        use_utility=True,
        use_states_info_gain=True,
        use_param_info_gain=False,
        action_selection="deterministic",
        sampling_mode = "marginal", # whether to sample from full posterior over policies ("full") or from marginal posterior over actions ("marginal")
        inference_algo="VANILLA",
        inference_params=None,
        modalities_to_learn="all",
        lr_pA=1.0,
        factors_to_learn="all",
        lr_pB=1.0,
        lr_pD=1.0,
        use_BMA=True,
        policy_sep_prior=False,
        save_belief_hist=False,
        A_factor_list=None,
        B_factor_list=None,
        sophisticated=False,
        si_horizon=3,
        si_policy_prune_threshold=1/16,
        si_state_prune_threshold=1/16,
        si_prune_penalty=512,
        ii_depth=10,
        ii_threshold=1/16,
    ):

        ### Constant parameters ###

        # policy parameters
        self.policy_len = policy_len
        self.gamma = gamma
        self.alpha = alpha
        self.action_selection = action_selection
        self.sampling_mode = sampling_mode
        self.use_utility = use_utility
        self.use_states_info_gain = use_states_info_gain
        self.use_param_info_gain = use_param_info_gain

        # learning parameters
        self.modalities_to_learn = modalities_to_learn
        self.lr_pA = lr_pA
        self.factors_to_learn = factors_to_learn
        self.lr_pB = lr_pB
        self.lr_pD = lr_pD

        # sophisticated inference parameters
        self.sophisticated = sophisticated
        if self.sophisticated:
            assert self.policy_len == 1, "Sophisticated inference only works with policy_len = 1"
        self.si_horizon = si_horizon
        self.si_policy_prune_threshold = si_policy_prune_threshold
        self.si_state_prune_threshold = si_state_prune_threshold
        self.si_prune_penalty = si_prune_penalty

        # Initialise observation model (A matrices)
        if not isinstance(A, np.ndarray):
            raise TypeError(
                'A matrix must be a numpy array'
            )

        self.A = utils.to_obj_array(A)

        assert utils.is_normalized(self.A), "A matrix is not normalized (i.e. A[m].sum(axis = 0) must all equal 1.0 for all modalities)"

        # Determine number of observation modalities and their respective dimensions
        self.num_obs = [self.A[m].shape[0] for m in range(len(self.A))]
        self.num_modalities = len(self.num_obs)

        # Assigning prior parameters on observation model (pA matrices)
        self.pA = pA

        # Initialise transition model (B matrices)
        if not isinstance(B, np.ndarray):
            raise TypeError(
                'B matrix must be a numpy array'
            )

        self.B = utils.to_obj_array(B)

        assert utils.is_normalized(self.B), "B matrix is not normalized (i.e. B[f].sum(axis = 0) must all equal 1.0 for all factors)"

        # Determine number of hidden state factors and their dimensionalities
        self.num_states = [self.B[f].shape[0] for f in range(len(self.B))]
        self.num_factors = len(self.num_states)

        # Assigning prior parameters on transition model (pB matrices) 
        self.pB = pB

        # If no `num_controls` are given, then this is inferred from the shapes of the input B matrices
        if num_controls == None:
            self.num_controls = [self.B[f].shape[-1] for f in range(self.num_factors)]
        else:
            inferred_num_controls = [self.B[f].shape[-1] for f in range(self.num_factors)]
            assert num_controls == inferred_num_controls, "num_controls must be consistent with the shapes of the input B matrices"
            self.num_controls = num_controls

        # checking that `A_factor_list` and `B_factor_list` are consistent with `num_factors`, `num_states`, and lagging dimensions of `A` and `B` tensors
        self.factorized = False
        if A_factor_list == None:
            self.A_factor_list = self.num_modalities * [list(range(self.num_factors))] # defaults to having all modalities depend on all factors
            for m in range(self.num_modalities):
                factor_dims = tuple([self.num_states[f] for f in self.A_factor_list[m]])
                assert self.A[m].shape[1:] == factor_dims, f"Please input an `A_factor_list` whose {m}-th indices pick out the hidden state factors that line up with lagging dimensions of A{m}..." 
                if self.pA is not None:
                    assert self.pA[m].shape[1:] == factor_dims, f"Please input an `A_factor_list` whose {m}-th indices pick out the hidden state factors that line up with lagging dimensions of pA{m}..." 
        else:
            self.factorized = True
            for m in range(self.num_modalities):
                assert max(A_factor_list[m]) <= (self.num_factors - 1), f"Check modality {m} of A_factor_list - must be consistent with `num_states` and `num_factors`..."
                factor_dims = tuple([self.num_states[f] for f in A_factor_list[m]])
                assert self.A[m].shape[1:] == factor_dims, f"Check modality {m} of A_factor_list. It must coincide with lagging dimensions of A{m}..." 
                if self.pA is not None:
                    assert self.pA[m].shape[1:] == factor_dims, f"Check modality {m} of A_factor_list. It must coincide with lagging dimensions of pA{m}..."
            self.A_factor_list = A_factor_list

        # generate a list of the modalities that depend on each factor 
        A_modality_list = []
        for f in range(self.num_factors):
            A_modality_list.append( [m for m in range(self.num_modalities) if f in self.A_factor_list[m]] )

        # Store thee `A_factor_list` and the `A_modality_list` in a Markov blanket dictionary
        self.mb_dict = {
                        'A_factor_list': self.A_factor_list,
                        'A_modality_list': A_modality_list
                        }

        if B_factor_list == None:
            self.B_factor_list = [[f] for f in range(self.num_factors)] # defaults to having all factors depend only on themselves
            for f in range(self.num_factors):
                factor_dims = tuple([self.num_states[f] for f in self.B_factor_list[f]])
                assert self.B[f].shape[1:-1] == factor_dims, f"Please input a `B_factor_list` whose {f}-th indices pick out the hidden state factors that line up with the all-but-final lagging dimensions of B{f}..." 
                if self.pB is not None:
                    assert self.pB[f].shape[1:-1] == factor_dims, f"Please input a `B_factor_list` whose {f}-th indices pick out the hidden state factors that line up with the all-but-final lagging dimensions of pB{f}..." 
        else:
            self.factorized = True
            for f in range(self.num_factors):
                assert max(B_factor_list[f]) <= (self.num_factors - 1), f"Check factor {f} of B_factor_list - must be consistent with `num_states` and `num_factors`..."
                factor_dims = tuple([self.num_states[f] for f in B_factor_list[f]])
                assert self.B[f].shape[1:-1] == factor_dims, f"Check factor {f} of B_factor_list. It must coincide with all-but-final lagging dimensions of B{f}..." 
                if self.pB is not None:
                    assert self.pB[f].shape[1:-1] == factor_dims, f"Check factor {f} of B_factor_list. It must coincide with all-but-final lagging dimensions of pB{f}..."
            self.B_factor_list = B_factor_list

        # Users have the option to make only certain factors controllable.
        # default behaviour is to make all hidden state factors controllable, i.e. `self.num_factors == len(self.num_controls)`
        if control_fac_idx == None:
            self.control_fac_idx = [f for f in range(self.num_factors) if self.num_controls[f] > 1]
        else:

            assert max(control_fac_idx) <= (self.num_factors - 1), "Check control_fac_idx - must be consistent with `num_states` and `num_factors`..."
            self.control_fac_idx = control_fac_idx

            for factor_idx in self.control_fac_idx:
                assert self.num_controls[factor_idx] > 1, "Control factor (and B matrix) dimensions are not consistent with user-given control_fac_idx"

        # Again, the use can specify a set of possible policies, or
        # all possible combinations of actions and timesteps will be considered
        if policies is None:
            policies = self._construct_policies()
        self.policies = policies

        assert all([len(self.num_controls) == policy.shape[1] for policy in self.policies]), "Number of control states is not consistent with policy dimensionalities"
        
        all_policies = np.vstack(self.policies)

        assert all([n_c >= max_action for (n_c, max_action) in zip(self.num_controls, list(np.max(all_policies, axis =0)+1))]), "Maximum number of actions is not consistent with `num_controls`"

        # Construct prior preferences (uniform if not specified)

        if C is not None:
            if not isinstance(C, np.ndarray):
                raise TypeError(
                    'C vector must be a numpy array'
                )
            self.C = utils.to_obj_array(C)

            assert len(self.C) == self.num_modalities, f"Check C vector: number of sub-arrays must be equal to number of observation modalities: {self.num_modalities}"

            for modality, c_m in enumerate(self.C):
                assert c_m.shape[0] == self.num_obs[modality], f"Check C vector: number of rows of C vector for modality {modality} should be equal to {self.num_obs[modality]}"
        else:
            self.C = self._construct_C_prior()

        # Construct prior over hidden states (uniform if not specified)
    
        if D is not None:
            if not isinstance(D, np.ndarray):
                raise TypeError(
                    'D vector must be a numpy array'
                )
            self.D = utils.to_obj_array(D)

            assert len(self.D) == self.num_factors, f"Check D vector: number of sub-arrays must be equal to number of hidden state factors: {self.num_factors}"

            for f, d_f in enumerate(self.D):
                assert d_f.shape[0] == self.num_states[f], f"Check D vector: number of entries of D vector for factor {f} should be equal to {self.num_states[f]}"
        else:
            if pD is not None:
                self.D = utils.norm_dist_obj_arr(pD)
            else:
                self.D = self._construct_D_prior()

        assert utils.is_normalized(self.D), "D vector is not normalized (i.e. D[f].sum() must all equal 1.0 for all factors)"

        # Assigning prior parameters on initial hidden states (pD vectors)
        self.pD = pD

        # Construct prior over policies (uniform if not specified) 
        if E is not None:
            if not isinstance(E, np.ndarray):
                raise TypeError(
                    'E vector must be a numpy array'
                )
            self.E = E

            assert len(self.E) == len(self.policies), f"Check E vector: length of E must be equal to number of policies: {len(self.policies)}"

        else:
            self.E = self._construct_E_prior()
        
        # Construct I for backwards induction (if H specified)
        if H is not None:
            self.H = H
            self.I = control.backwards_induction(H, B, B_factor_list, threshold=ii_threshold, depth=ii_depth)
        else:
            self.H = None
            self.I = None

        self.edge_handling_params = {}
        self.edge_handling_params['use_BMA'] = use_BMA # creates a 'D-like' moving prior
        self.edge_handling_params['policy_sep_prior'] = policy_sep_prior # carries forward last timesteps posterior, in a policy-conditioned way

        # use_BMA and policy_sep_prior can both be False, but both cannot be simultaneously be True. If one of them is True, the other must be False
        if policy_sep_prior:
            if use_BMA:
                warnings.warn(
                    "Inconsistent choice of `policy_sep_prior` and `use_BMA`.\
                    You have set `policy_sep_prior` to True, so we are setting `use_BMA` to False"
                )
                self.edge_handling_params['use_BMA'] = False
        
        if inference_algo == None:
            self.inference_algo = "VANILLA"
            self.inference_params = self._get_default_params()
            if inference_horizon > 1:
                warnings.warn(
                    "If `inference_algo` is VANILLA, then inference_horizon must be 1\n. \
                    Setting inference_horizon to default value of 1...\n"
                    )
                self.inference_horizon = 1
            else:
                self.inference_horizon = 1
        else:
            self.inference_algo = inference_algo
            self.inference_params = self._get_default_params()
            self.inference_horizon = inference_horizon

        if save_belief_hist:
            self.qs_hist = []
            self.q_pi_hist = []
        
        self.prev_obs = []
        self.reset()
        
        self.action = None
        self.prev_actions = None

    def _construct_C_prior(self):
        
        C = utils.obj_array_zeros(self.num_obs)

        return C

    def _construct_D_prior(self):

        D = utils.obj_array_uniform(self.num_states)

        return D

    def _construct_policies(self):
        
        policies =  control.construct_policies(
            self.num_states, self.num_controls, self.policy_len, self.control_fac_idx
        )

        return policies

    def _construct_num_controls(self):
        num_controls = control.get_num_controls_from_policies(
            self.policies
        )
        
        return num_controls
    
    def _construct_E_prior(self):
        E = np.ones(len(self.policies)) / len(self.policies)
        return E

    def reset(self, init_qs=None):
        """
        Resets the posterior beliefs about hidden states of the agent to a uniform distribution, and resets time to first timestep of the simulation's temporal horizon.
        Returns the posterior beliefs about hidden states.

        Returns
        ---------
        qs: ``numpy.ndarray`` of dtype object
           Initialized posterior over hidden states. Depending on the inference algorithm chosen and other parameters (such as the parameters stored within ``edge_handling_paramss),
           the resulting ``qs`` variable will have additional sub-structure to reflect whether beliefs are additionally conditioned on timepoint and policy.
            For example, in case the ``self.inference_algo == 'MMP' `, the indexing structure of ``qs`` is policy->timepoint-->factor, so that 
            ``qs[p_idx][t_idx][f_idx]`` refers to beliefs about marginal factor ``f_idx`` expected under policy ``p_idx`` 
            at timepoint ``t_idx``. In this case, the returned ``qs`` will only have entries filled out for the first timestep, i.e. for ``q[p_idx][0]``, for all 
            policy-indices ``p_idx``. Subsequent entries ``q[:][1, 2, ...]`` will be initialized to empty ``numpy.ndarray`` objects.
        """

        self.curr_timestep = 0

        if init_qs is None:
            if self.inference_algo == 'VANILLA':
                self.qs = utils.obj_array_uniform(self.num_states)
            else: # in the case you're doing MMP (i.e. you have an inference_horizon > 1), we have to account for policy- and timestep-conditioned posterior beliefs
                self.qs = utils.obj_array(len(self.policies))
                for p_i, _ in enumerate(self.policies):
                    self.qs[p_i] = utils.obj_array(self.inference_horizon + self.policy_len + 1) # + 1 to include belief about current timestep
                    self.qs[p_i][0] = utils.obj_array_uniform(self.num_states)
                
                first_belief = utils.obj_array(len(self.policies))
                for p_i, _ in enumerate(self.policies):
                    first_belief[p_i] = copy.deepcopy(self.D) 
                
                if self.edge_handling_params['policy_sep_prior']:
                    self.set_latest_beliefs(last_belief = first_belief)
                else:
                    self.set_latest_beliefs(last_belief = self.D)
            
        else:
            self.qs = init_qs
        
        if self.pA is not None:
            self.A = utils.norm_dist_obj_arr(self.pA)
        
        if self.pB is not None:
            self.B = utils.norm_dist_obj_arr(self.pB)

        return self.qs

    def step_time(self):
        """
        Advances time by one step. This involves updating the ``self.prev_actions``, and in the case of a moving
        inference horizon, this also shifts the history of post-dictive beliefs forward in time (using ``self.set_latest_beliefs()``),
        so that the penultimate belief before the beginning of the horizon is correctly indexed.

        Returns
        ---------
        curr_timestep: ``int``
            The index in absolute simulation time of the current timestep.
        """

        if self.prev_actions is None:
            self.prev_actions = [self.action]
        else:
            self.prev_actions.append(self.action)

        self.curr_timestep += 1

        if self.inference_algo == "MMP" and (self.curr_timestep - self.inference_horizon) >= 0:
            self.set_latest_beliefs()
        
        return self.curr_timestep
    
    def set_latest_beliefs(self,last_belief=None):
        """
        Both sets and returns the penultimate belief before the first timestep of the backwards inference horizon. 
        In the case that the inference horizon includes the first timestep of the simulation, then the ``latest_belief`` is
        simply the first belief of the whole simulation, or the prior (``self.D``). The particular structure of the ``latest_belief``
        depends on the value of ``self.edge_handling_params['use_BMA']``.

        Returns
        ---------
        latest_belief: ``numpy.ndarray`` of dtype object
            Penultimate posterior beliefs over hidden states at the timestep just before the first timestep of the inference horizon. 
            Depending on the value of ``self.edge_handling_params['use_BMA']``, the shape of this output array will differ.
            If ``self.edge_handling_params['use_BMA'] == True``, then ``latest_belief`` will be a Bayesian model average 
            of beliefs about hidden states, where the average is taken with respect to posterior beliefs about policies.
            Otherwise, `latest_belief`` will be the full, policy-conditioned belief about hidden states, and will have indexing structure
            policies->factors, such that ``latest_belief[p_idx][f_idx]`` refers to the penultimate belief about marginal factor ``f_idx``
            under policy ``p_idx``.
        """

        if last_belief is None:
            last_belief = utils.obj_array(len(self.policies))
            for p_i, _ in enumerate(self.policies):
                last_belief[p_i] = copy.deepcopy(self.qs[p_i][0])

        begin_horizon_step = self.curr_timestep - self.inference_horizon
        if self.edge_handling_params['use_BMA'] and (begin_horizon_step >= 0):
            if hasattr(self, "q_pi_hist"):
                self.latest_belief = inference.average_states_over_policies(last_belief, self.q_pi_hist[begin_horizon_step]) # average the earliest marginals together using contemporaneous posterior over policies (`self.q_pi_hist[0]`)
            else:
                self.latest_belief = inference.average_states_over_policies(last_belief, self.q_pi) # average the earliest marginals together using posterior over policies (`self.q_pi`)
        else:
            self.latest_belief = last_belief

        return self.latest_belief
    
    def get_future_qs(self):
        """
        Returns the last ``self.policy_len`` timesteps of each policy-conditioned belief
        over hidden states. This is a step of pre-processing that needs to be done before computing
        the expected free energy of policies. We do this to avoid computing the expected free energy of 
        policies using beliefs about hidden states in the past (so-called "post-dictive" beliefs).

        Returns
        ---------
        future_qs_seq: ``numpy.ndarray`` of dtype object
            Posterior beliefs over hidden states under a policy, in the future. This is a nested ``numpy.ndarray`` object array, with one
            sub-array ``future_qs_seq[p_idx]`` for each policy. The indexing structure is policy->timepoint-->factor, so that 
            ``future_qs_seq[p_idx][t_idx][f_idx]`` refers to beliefs about marginal factor ``f_idx`` expected under policy ``p_idx`` 
            at future timepoint ``t_idx``, relative to the current timestep.
        """
        
        future_qs_seq = utils.obj_array(len(self.qs))
        for p_idx in range(len(self.qs)):
            future_qs_seq[p_idx] = self.qs[p_idx][-(self.policy_len+1):] # this grabs only the last `policy_len`+1 beliefs about hidden states, under each policy

        return future_qs_seq


    def infer_states(self, observation, distr_obs=False):
        """
        Update approximate posterior over hidden states by solving variational inference problem, given an observation.

        Parameters
        ----------
        observation: ``list`` or ``tuple`` of ints
            The observation input. Each entry ``observation[m]`` stores the index of the discrete
            observation for modality ``m``.
        distr_obs: ``bool``
            Whether the observation is a distribution over possible observations, rather than a single observation.

        Returns
        ---------
        qs: ``numpy.ndarray`` of dtype object
            Posterior beliefs over hidden states. Depending on the inference algorithm chosen, the resulting ``qs`` variable will have additional sub-structure to reflect whether
            beliefs are additionally conditioned on timepoint and policy.
            For example, in case the ``self.inference_algo == 'MMP' `` indexing structure is policy->timepoint-->factor, so that 
            ``qs[p_idx][t_idx][f_idx]`` refers to beliefs about marginal factor ``f_idx`` expected under policy ``p_idx`` 
            at timepoint ``t_idx``.
        """

        observation = tuple(observation) if not distr_obs else observation

        if not hasattr(self, "qs"):
            self.reset()

        if self.inference_algo == "VANILLA":
            if self.action is not None:
                empirical_prior = control.get_expected_states_interactions(
                    self.qs, self.B, self.B_factor_list, self.action.reshape(1, -1) 
                )[0]
            else:
                empirical_prior = self.D
            qs = inference.update_posterior_states_factorized(
                self.A,
                observation,
                self.num_obs,
                self.num_states,
                self.mb_dict,
                empirical_prior,
                **self.inference_params
            )
        elif self.inference_algo == "MMP":

            self.prev_obs.append(observation)
            if len(self.prev_obs) > self.inference_horizon:
                latest_obs = self.prev_obs[-self.inference_horizon:]
                latest_actions = self.prev_actions[-(self.inference_horizon-1):]
            else:
                latest_obs = self.prev_obs
                latest_actions = self.prev_actions

            qs, F = inference.update_posterior_states_full_factorized(
                self.A,
                self.mb_dict,
                self.B,
                self.B_factor_list,
                latest_obs,
                self.policies, 
                latest_actions, 
                prior = self.latest_belief, 
                policy_sep_prior = self.edge_handling_params['policy_sep_prior'],
                **self.inference_params
            )

            self.F = F # variational free energy of each policy  

        if hasattr(self, "qs_hist"):
            self.qs_hist.append(qs)
        self.qs = qs

        return qs

    def _infer_states_test(self, observation, distr_obs=False):
        """
        Test version of ``infer_states()`` that additionally returns intermediate variables of MMP, such as
        the prediction errors and intermediate beliefs from the optimization. Used for benchmarking against SPM outputs.
        """
        observation = tuple(observation) if not distr_obs else observation

        if not hasattr(self, "qs"):
            self.reset()

        if self.inference_algo == "VANILLA":
            if self.action is not None:
                empirical_prior = control.get_expected_states(
                    self.qs, self.B, self.action.reshape(1, -1) 
                )[0]
            else:
                empirical_prior = self.D
            qs = inference.update_posterior_states(
                self.A,
                observation,
                empirical_prior,
                **self.inference_params
            )
        elif self.inference_algo == "MMP":

            self.prev_obs.append(observation)
            if len(self.prev_obs) > self.inference_horizon:
                latest_obs = self.prev_obs[-self.inference_horizon:]
                latest_actions = self.prev_actions[-(self.inference_horizon-1):]
            else:
                latest_obs = self.prev_obs
                latest_actions = self.prev_actions

            qs, F, xn, vn = inference._update_posterior_states_full_test(
                self.A,
                self.B, 
                latest_obs,
                self.policies, 
                latest_actions, 
                prior = self.latest_belief, 
                policy_sep_prior = self.edge_handling_params['policy_sep_prior'],
                **self.inference_params
            )

            self.F = F # variational free energy of each policy  

        if hasattr(self, "qs_hist"):
            self.qs_hist.append(qs)

        self.qs = qs

        if self.inference_algo == "MMP":
            return qs, xn, vn
        else:
            return qs
    
    def infer_policies(self):
        """
        Perform policy inference by optimizing a posterior (categorical) distribution over policies.
        This distribution is computed as the softmax of ``G * gamma + lnE`` where ``G`` is the negative expected
        free energy of policies, ``gamma`` is a policy precision and ``lnE`` is the (log) prior probability of policies.
        This function returns the posterior over policies as well as the negative expected free energy of each policy.
        In this version of the function, the expected free energy of policies is computed using known factorized structure 
        in the model, which speeds up computation (particular the state information gain calculations).

        Returns
        ----------
        q_pi: 1D ``numpy.ndarray``
            Posterior beliefs over policies, i.e. a vector containing one posterior probability per policy.
        G: 1D ``numpy.ndarray``
            Negative expected free energies of each policy, i.e. a vector containing one negative expected free energy per policy.
        """

        if self.inference_algo == "VANILLA":
            if self.sophisticated:
                q_pi, G = control.sophisticated_inference_search(
                    self.qs, 
                    self.policies, 
                    self.A, 
                    self.B, 
                    self.C, 
                    self.A_factor_list, 
                    self.B_factor_list, 
                    self.I,
                    self.si_horizon,
                    self.si_policy_prune_threshold, 
                    self.si_state_prune_threshold, 
                    self.si_prune_penalty,
                    1.0,
                    self.inference_params,
                    n=0
                )
            else:
                q_pi, G = control.update_posterior_policies_factorized(
                    self.qs,
                    self.A,
                    self.B,
                    self.C,
                    self.A_factor_list,
                    self.B_factor_list,
                    self.policies,
                    self.use_utility,
                    self.use_states_info_gain,
                    self.use_param_info_gain,
                    self.pA,
                    self.pB,
                    E = self.E,
                    I = self.I,
                    gamma = self.gamma
                )
        elif self.inference_algo == "MMP":

            future_qs_seq = self.get_future_qs()

            q_pi, G = control.update_posterior_policies_full_factorized(
                future_qs_seq,
                self.A,
                self.B,
                self.C,
                self.A_factor_list,
                self.B_factor_list,
                self.policies,
                self.use_utility,
                self.use_states_info_gain,
                self.use_param_info_gain,
                self.latest_belief,
                self.pA,
                self.pB,
                F=self.F,
                E=self.E,
                I=self.I,
                gamma=self.gamma
            )

        if hasattr(self, "q_pi_hist"):
            self.q_pi_hist.append(q_pi)
            if len(self.q_pi_hist) > self.inference_horizon:
                self.q_pi_hist = self.q_pi_hist[-(self.inference_horizon-1):]

        self.q_pi = q_pi
        self.G = G
        return q_pi, G

    def sample_action(self):
        """
        Sample or select a discrete action from the posterior over control states.
        This function both sets or cachés the action as an internal variable with the agent and returns it.
        This function also updates time variable (and thus manages consequences of updating the moving reference frame of beliefs)
        using ``self.step_time()``.

        
        Returns
        ----------
        action: 1D ``numpy.ndarray``
            Vector containing the indices of the actions for each control factor
        """

        if self.sampling_mode == "marginal":
            action = control.sample_action(
                self.q_pi, self.policies, self.num_controls, action_selection = self.action_selection, alpha = self.alpha
            )
        elif self.sampling_mode == "full":
            action = control.sample_policy(self.q_pi, self.policies, self.num_controls,
                                           action_selection=self.action_selection, alpha=self.alpha)

        self.action = action

        self.step_time()

        return action
    
    def _sample_action_test(self):
        """
        Sample or select a discrete action from the posterior over control states.
        This function both sets or cachés the action as an internal variable with the agent and returns it.
        This function also updates time variable (and thus manages consequences of updating the moving reference frame of beliefs)
        using ``self.step_time()``.
        
        Returns
        ----------
        action: 1D ``numpy.ndarray``
            Vector containing the indices of the actions for each control factor
        """

        if self.sampling_mode == "marginal":
            action, p_dist = control._sample_action_test(self.q_pi, self.policies, self.num_controls,
                                                         action_selection=self.action_selection, alpha=self.alpha)
        elif self.sampling_mode == "full":
            action, p_dist = control._sample_policy_test(self.q_pi, self.policies, self.num_controls,
                                                         action_selection=self.action_selection, alpha=self.alpha)

        self.action = action

        self.step_time()

        return action, p_dist

    def update_A(self, obs):
        """
        Update approximate posterior beliefs about Dirichlet parameters that parameterise the observation likelihood or ``A`` array.

        Parameters
        ----------
        observation: ``list`` or ``tuple`` of ints
            The observation input. Each entry ``observation[m]`` stores the index of the discrete
            observation for modality ``m``.

        Returns
        -----------
        qA: ``numpy.ndarray`` of dtype object
            Posterior Dirichlet parameters over observation model (same shape as ``A``), after having updated it with observations.
        """

        qA = learning.update_obs_likelihood_dirichlet_factorized(
            self.pA, 
            self.A, 
            obs, 
            self.qs, 
            self.A_factor_list,
            self.lr_pA, 
            self.modalities_to_learn
        )

        self.pA = qA # set new prior to posterior
        self.A = utils.norm_dist_obj_arr(qA) # take expected value of posterior Dirichlet parameters to calculate posterior over A array

        return qA

    def _update_A_old(self, obs):
        """
        Update approximate posterior beliefs about Dirichlet parameters that parameterise the observation likelihood or ``A`` array.

        Parameters
        ----------
        observation: ``list`` or ``tuple`` of ints
            The observation input. Each entry ``observation[m]`` stores the index of the discrete
            observation for modality ``m``.

        Returns
        -----------
        qA: ``numpy.ndarray`` of dtype object
            Posterior Dirichlet parameters over observation model (same shape as ``A``), after having updated it with observations.
        """

        qA = learning.update_obs_likelihood_dirichlet(
            self.pA, 
            self.A, 
            obs, 
            self.qs, 
            self.lr_pA, 
            self.modalities_to_learn
        )

        self.pA = qA # set new prior to posterior
        self.A = utils.norm_dist_obj_arr(qA) # take expected value of posterior Dirichlet parameters to calculate posterior over A array

        return qA

    def update_B(self, qs_prev):
        """
        Update posterior beliefs about Dirichlet parameters that parameterise the transition likelihood 
        
        Parameters
        -----------
        qs_prev: 1D ``numpy.ndarray`` or ``numpy.ndarray`` of dtype object
            Marginal posterior beliefs over hidden states at previous timepoint.
    
        Returns
        -----------
        qB: ``numpy.ndarray`` of dtype object
            Posterior Dirichlet parameters over transition model (same shape as ``B``), after having updated it with state beliefs and actions.
        """

        qB = learning.update_state_likelihood_dirichlet_interactions(
            self.pB,
            self.B,
            self.action,
            self.qs,
            qs_prev,
            self.B_factor_list,
            self.lr_pB,
            self.factors_to_learn
        )

        self.pB = qB # set new prior to posterior
        self.B = utils.norm_dist_obj_arr(qB)  # take expected value of posterior Dirichlet parameters to calculate posterior over B array

        return qB
    
    def _update_B_old(self, qs_prev):
        """
        Update posterior beliefs about Dirichlet parameters that parameterise the transition likelihood 
        
        Parameters
        -----------
        qs_prev: 1D ``numpy.ndarray`` or ``numpy.ndarray`` of dtype object
            Marginal posterior beliefs over hidden states at previous timepoint.
    
        Returns
        -----------
        qB: ``numpy.ndarray`` of dtype object
            Posterior Dirichlet parameters over transition model (same shape as ``B``), after having updated it with state beliefs and actions.
        """

        qB = learning.update_state_likelihood_dirichlet(
            self.pB,
            self.B,
            self.action,
            self.qs,
            qs_prev,
            self.lr_pB,
            self.factors_to_learn
        )

        self.pB = qB # set new prior to posterior
        self.B = utils.norm_dist_obj_arr(qB)  # take expected value of posterior Dirichlet parameters to calculate posterior over B array

        return qB
    
    def update_D(self, qs_t0 = None):
        """
        Update Dirichlet parameters of the initial hidden state distribution 
        (prior beliefs about hidden states at the beginning of the inference window).

        Parameters
        -----------
        qs_t0: 1D ``numpy.ndarray``, ``numpy.ndarray`` of dtype object, or ``None``
            Marginal posterior beliefs over hidden states at current timepoint. If ``None``, the 
            value of ``qs_t0`` is set to ``self.qs_hist[0]`` (i.e. the initial hidden state beliefs at the first timepoint).
            If ``self.inference_algo == "MMP"``, then ``qs_t0`` is set to be the Bayesian model average of beliefs about hidden states
            at the first timestep of the backwards inference horizon, where the average is taken with respect to posterior beliefs about policies.
      
        Returns
        -----------
        qD: ``numpy.ndarray`` of dtype object
            Posterior Dirichlet parameters over initial hidden state prior (same shape as ``qs_t0``), after having updated it with state beliefs.
        """
        
        if self.inference_algo == "VANILLA":
            
            if qs_t0 is None:
                
                try:
                    qs_t0 = self.qs_hist[0]
                except ValueError:
                    print("qs_t0 must either be passed as argument to `update_D` or `save_belief_hist` must be set to True!")             

        elif self.inference_algo == "MMP":
            
            if self.edge_handling_params['use_BMA']:
                qs_t0 = self.latest_belief
            elif self.edge_handling_params['policy_sep_prior']:
              
                qs_pi_t0 = self.latest_belief

                # get beliefs about policies at the time at the beginning of the inference horizon
                if hasattr(self, "q_pi_hist"):
                    begin_horizon_step = max(0, self.curr_timestep - self.inference_horizon)
                    q_pi_t0 = np.copy(self.q_pi_hist[begin_horizon_step])
                else:
                    q_pi_t0 = np.copy(self.q_pi)
            
                qs_t0 = inference.average_states_over_policies(qs_pi_t0,q_pi_t0) # beliefs about hidden states at the first timestep of the inference horizon
        
        qD = learning.update_state_prior_dirichlet(self.pD, qs_t0, self.lr_pD, factors = self.factors_to_learn)
        
        self.pD = qD # set new prior to posterior
        self.D = utils.norm_dist_obj_arr(qD) # take expected value of posterior Dirichlet parameters to calculate posterior over D array

        return qD

    def _get_default_params(self):
        method = self.inference_algo
        default_params = None
        if method == "VANILLA":
            default_params = {"num_iter": 10, "dF": 1.0, "dF_tol": 0.001, "compute_vfe": True}
        elif method == "MMP":
            default_params = {"num_iter": 10, "grad_descent": True, "tau": 0.25}
        elif method == "VMP":
            raise NotImplementedError("VMP is not implemented")
        elif method == "BP":
            raise NotImplementedError("BP is not implemented")
        elif method == "EP":
            raise NotImplementedError("EP is not implemented")
        elif method == "CV":
            raise NotImplementedError("CV is not implemented")

        return default_params

def __init__(
        self,
        A,
        B,
        C=None,
        D=None,
        E=None,
        H=None,
        pA=None,
        pB=None,
        pD=None,
        num_controls=None,
        policy_len=1,
        inference_horizon=1,
        control_fac_idx=None,
        policies=None,
        gamma=16.0,
        alpha=16.0,
        use_utility=True,
        use_states_info_gain=True,
        use_param_info_gain=False,
        action_selection="deterministic",
        sampling_mode = "marginal", # whether to sample from full posterior over policies ("full") or from marginal posterior over actions ("marginal")
        inference_algo="VANILLA",
        inference_params=None,
        modalities_to_learn="all",
        lr_pA=1.0,
        factors_to_learn="all",
        lr_pB=1.0,
        lr_pD=1.0,
        use_BMA=True,
        policy_sep_prior=False,
        save_belief_hist=False,
        A_factor_list=None,
        B_factor_list=None,
        sophisticated=False,
        si_horizon=3,
        si_policy_prune_threshold=1/16,
        si_state_prune_threshold=1/16,
        si_prune_penalty=512,
        ii_depth=10,
        ii_threshold=1/16,
    ):

        ### Constant parameters ###

        # policy parameters
        self.policy_len = policy_len
        self.gamma = gamma
        self.alpha = alpha
        self.action_selection = action_selection
        self.sampling_mode = sampling_mode
        self.use_utility = use_utility
        self.use_states_info_gain = use_states_info_gain
        self.use_param_info_gain = use_param_info_gain

        # learning parameters
        self.modalities_to_learn = modalities_to_learn
        self.lr_pA = lr_pA
        self.factors_to_learn = factors_to_learn
        self.lr_pB = lr_pB
        self.lr_pD = lr_pD

        # sophisticated inference parameters
        self.sophisticated = sophisticated
        if self.sophisticated:
            assert self.policy_len == 1, "Sophisticated inference only works with policy_len = 1"
        self.si_horizon = si_horizon
        self.si_policy_prune_threshold = si_policy_prune_threshold
        self.si_state_prune_threshold = si_state_prune_threshold
        self.si_prune_penalty = si_prune_penalty

        # Initialise observation model (A matrices)
        if not isinstance(A, np.ndarray):
            raise TypeError(
                'A matrix must be a numpy array'
            )

        self.A = utils.to_obj_array(A)

        assert utils.is_normalized(self.A), "A matrix is not normalized (i.e. A[m].sum(axis = 0) must all equal 1.0 for all modalities)"

        # Determine number of observation modalities and their respective dimensions
        self.num_obs = [self.A[m].shape[0] for m in range(len(self.A))]
        self.num_modalities = len(self.num_obs)

        # Assigning prior parameters on observation model (pA matrices)
        self.pA = pA

        # Initialise transition model (B matrices)
        if not isinstance(B, np.ndarray):
            raise TypeError(
                'B matrix must be a numpy array'
            )

        self.B = utils.to_obj_array(B)

        assert utils.is_normalized(self.B), "B matrix is not normalized (i.e. B[f].sum(axis = 0) must all equal 1.0 for all factors)"

        # Determine number of hidden state factors and their dimensionalities
        self.num_states = [self.B[f].shape[0] for f in range(len(self.B))]
        self.num_factors = len(self.num_states)

        # Assigning prior parameters on transition model (pB matrices) 
        self.pB = pB

        # If no `num_controls` are given, then this is inferred from the shapes of the input B matrices
        if num_controls == None:
            self.num_controls = [self.B[f].shape[-1] for f in range(self.num_factors)]
        else:
            inferred_num_controls = [self.B[f].shape[-1] for f in range(self.num_factors)]
            assert num_controls == inferred_num_controls, "num_controls must be consistent with the shapes of the input B matrices"
            self.num_controls = num_controls

        # checking that `A_factor_list` and `B_factor_list` are consistent with `num_factors`, `num_states`, and lagging dimensions of `A` and `B` tensors
        self.factorized = False
        if A_factor_list == None:
            self.A_factor_list = self.num_modalities * [list(range(self.num_factors))] # defaults to having all modalities depend on all factors
            for m in range(self.num_modalities):
                factor_dims = tuple([self.num_states[f] for f in self.A_factor_list[m]])
                assert self.A[m].shape[1:] == factor_dims, f"Please input an `A_factor_list` whose {m}-th indices pick out the hidden state factors that line up with lagging dimensions of A{m}..." 
                if self.pA is not None:
                    assert self.pA[m].shape[1:] == factor_dims, f"Please input an `A_factor_list` whose {m}-th indices pick out the hidden state factors that line up with lagging dimensions of pA{m}..." 
        else:
            self.factorized = True
            for m in range(self.num_modalities):
                assert max(A_factor_list[m]) <= (self.num_factors - 1), f"Check modality {m} of A_factor_list - must be consistent with `num_states` and `num_factors`..."
                factor_dims = tuple([self.num_states[f] for f in A_factor_list[m]])
                assert self.A[m].shape[1:] == factor_dims, f"Check modality {m} of A_factor_list. It must coincide with lagging dimensions of A{m}..." 
                if self.pA is not None:
                    assert self.pA[m].shape[1:] == factor_dims, f"Check modality {m} of A_factor_list. It must coincide with lagging dimensions of pA{m}..."
            self.A_factor_list = A_factor_list

        # generate a list of the modalities that depend on each factor 
        A_modality_list = []
        for f in range(self.num_factors):
            A_modality_list.append( [m for m in range(self.num_modalities) if f in self.A_factor_list[m]] )

        # Store thee `A_factor_list` and the `A_modality_list` in a Markov blanket dictionary
        self.mb_dict = {
                        'A_factor_list': self.A_factor_list,
                        'A_modality_list': A_modality_list
                        }

        if B_factor_list == None:
            self.B_factor_list = [[f] for f in range(self.num_factors)] # defaults to having all factors depend only on themselves
            for f in range(self.num_factors):
                factor_dims = tuple([self.num_states[f] for f in self.B_factor_list[f]])
                assert self.B[f].shape[1:-1] == factor_dims, f"Please input a `B_factor_list` whose {f}-th indices pick out the hidden state factors that line up with the all-but-final lagging dimensions of B{f}..." 
                if self.pB is not None:
                    assert self.pB[f].shape[1:-1] == factor_dims, f"Please input a `B_factor_list` whose {f}-th indices pick out the hidden state factors that line up with the all-but-final lagging dimensions of pB{f}..." 
        else:
            self.factorized = True
            for f in range(self.num_factors):
                assert max(B_factor_list[f]) <= (self.num_factors - 1), f"Check factor {f} of B_factor_list - must be consistent with `num_states` and `num_factors`..."
                factor_dims = tuple([self.num_states[f] for f in B_factor_list[f]])
                assert self.B[f].shape[1:-1] == factor_dims, f"Check factor {f} of B_factor_list. It must coincide with all-but-final lagging dimensions of B{f}..." 
                if self.pB is not None:
                    assert self.pB[f].shape[1:-1] == factor_dims, f"Check factor {f} of B_factor_list. It must coincide with all-but-final lagging dimensions of pB{f}..."
            self.B_factor_list = B_factor_list

        # Users have the option to make only certain factors controllable.
        # default behaviour is to make all hidden state factors controllable, i.e. `self.num_factors == len(self.num_controls)`
        if control_fac_idx == None:
            self.control_fac_idx = [f for f in range(self.num_factors) if self.num_controls[f] > 1]
        else:

            assert max(control_fac_idx) <= (self.num_factors - 1), "Check control_fac_idx - must be consistent with `num_states` and `num_factors`..."
            self.control_fac_idx = control_fac_idx

            for factor_idx in self.control_fac_idx:
                assert self.num_controls[factor_idx] > 1, "Control factor (and B matrix) dimensions are not consistent with user-given control_fac_idx"

        # Again, the use can specify a set of possible policies, or
        # all possible combinations of actions and timesteps will be considered
        if policies is None:
            policies = self._construct_policies()
        self.policies = policies

        assert all([len(self.num_controls) == policy.shape[1] for policy in self.policies]), "Number of control states is not consistent with policy dimensionalities"
        
        all_policies = np.vstack(self.policies)

        assert all([n_c >= max_action for (n_c, max_action) in zip(self.num_controls, list(np.max(all_policies, axis =0)+1))]), "Maximum number of actions is not consistent with `num_controls`"

        # Construct prior preferences (uniform if not specified)

        if C is not None:
            if not isinstance(C, np.ndarray):
                raise TypeError(
                    'C vector must be a numpy array'
                )
            self.C = utils.to_obj_array(C)

            assert len(self.C) == self.num_modalities, f"Check C vector: number of sub-arrays must be equal to number of observation modalities: {self.num_modalities}"

            for modality, c_m in enumerate(self.C):
                assert c_m.shape[0] == self.num_obs[modality], f"Check C vector: number of rows of C vector for modality {modality} should be equal to {self.num_obs[modality]}"
        else:
            self.C = self._construct_C_prior()

        # Construct prior over hidden states (uniform if not specified)
    
        if D is not None:
            if not isinstance(D, np.ndarray):
                raise TypeError(
                    'D vector must be a numpy array'
                )
            self.D = utils.to_obj_array(D)

            assert len(self.D) == self.num_factors, f"Check D vector: number of sub-arrays must be equal to number of hidden state factors: {self.num_factors}"

            for f, d_f in enumerate(self.D):
                assert d_f.shape[0] == self.num_states[f], f"Check D vector: number of entries of D vector for factor {f} should be equal to {self.num_states[f]}"
        else:
            if pD is not None:
                self.D = utils.norm_dist_obj_arr(pD)
            else:
                self.D = self._construct_D_prior()

        assert utils.is_normalized(self.D), "D vector is not normalized (i.e. D[f].sum() must all equal 1.0 for all factors)"

        # Assigning prior parameters on initial hidden states (pD vectors)
        self.pD = pD

        # Construct prior over policies (uniform if not specified) 
        if E is not None:
            if not isinstance(E, np.ndarray):
                raise TypeError(
                    'E vector must be a numpy array'
                )
            self.E = E

            assert len(self.E) == len(self.policies), f"Check E vector: length of E must be equal to number of policies: {len(self.policies)}"

        else:
            self.E = self._construct_E_prior()
        
        # Construct I for backwards induction (if H specified)
        if H is not None:
            self.H = H
            self.I = control.backwards_induction(H, B, B_factor_list, threshold=ii_threshold, depth=ii_depth)
        else:
            self.H = None
            self.I = None

        self.edge_handling_params = {}
        self.edge_handling_params['use_BMA'] = use_BMA # creates a 'D-like' moving prior
        self.edge_handling_params['policy_sep_prior'] = policy_sep_prior # carries forward last timesteps posterior, in a policy-conditioned way

        # use_BMA and policy_sep_prior can both be False, but both cannot be simultaneously be True. If one of them is True, the other must be False
        if policy_sep_prior:
            if use_BMA:
                warnings.warn(
                    "Inconsistent choice of `policy_sep_prior` and `use_BMA`.\
                    You have set `policy_sep_prior` to True, so we are setting `use_BMA` to False"
                )
                self.edge_handling_params['use_BMA'] = False
        
        if inference_algo == None:
            self.inference_algo = "VANILLA"
            self.inference_params = self._get_default_params()
            if inference_horizon > 1:
                warnings.warn(
                    "If `inference_algo` is VANILLA, then inference_horizon must be 1\n. \
                    Setting inference_horizon to default value of 1...\n"
                    )
                self.inference_horizon = 1
            else:
                self.inference_horizon = 1
        else:
            self.inference_algo = inference_algo
            self.inference_params = self._get_default_params()
            self.inference_horizon = inference_horizon

        if save_belief_hist:
            self.qs_hist = []
            self.q_pi_hist = []
        
        self.prev_obs = []
        self.reset()
        
        self.action = None
        self.prev_actions = None

def _construct_C_prior(self):
        
        C = utils.obj_array_zeros(self.num_obs)

        return C

def _construct_D_prior(self):

        D = utils.obj_array_uniform(self.num_states)

        return D

def _construct_policies(self):
        
        policies =  control.construct_policies(
            self.num_states, self.num_controls, self.policy_len, self.control_fac_idx
        )

        return policies

def _construct_num_controls(self):
        num_controls = control.get_num_controls_from_policies(
            self.policies
        )
        
        return num_controls

def _construct_E_prior(self):
        E = np.ones(len(self.policies)) / len(self.policies)
        return E

def reset(self, init_qs=None):
        """
        Resets the posterior beliefs about hidden states of the agent to a uniform distribution, and resets time to first timestep of the simulation's temporal horizon.
        Returns the posterior beliefs about hidden states.

        Returns
        ---------
        qs: ``numpy.ndarray`` of dtype object
           Initialized posterior over hidden states. Depending on the inference algorithm chosen and other parameters (such as the parameters stored within ``edge_handling_paramss),
           the resulting ``qs`` variable will have additional sub-structure to reflect whether beliefs are additionally conditioned on timepoint and policy.
            For example, in case the ``self.inference_algo == 'MMP' `, the indexing structure of ``qs`` is policy->timepoint-->factor, so that 
            ``qs[p_idx][t_idx][f_idx]`` refers to beliefs about marginal factor ``f_idx`` expected under policy ``p_idx`` 
            at timepoint ``t_idx``. In this case, the returned ``qs`` will only have entries filled out for the first timestep, i.e. for ``q[p_idx][0]``, for all 
            policy-indices ``p_idx``. Subsequent entries ``q[:][1, 2, ...]`` will be initialized to empty ``numpy.ndarray`` objects.
        """

        self.curr_timestep = 0

        if init_qs is None:
            if self.inference_algo == 'VANILLA':
                self.qs = utils.obj_array_uniform(self.num_states)
            else: # in the case you're doing MMP (i.e. you have an inference_horizon > 1), we have to account for policy- and timestep-conditioned posterior beliefs
                self.qs = utils.obj_array(len(self.policies))
                for p_i, _ in enumerate(self.policies):
                    self.qs[p_i] = utils.obj_array(self.inference_horizon + self.policy_len + 1) # + 1 to include belief about current timestep
                    self.qs[p_i][0] = utils.obj_array_uniform(self.num_states)
                
                first_belief = utils.obj_array(len(self.policies))
                for p_i, _ in enumerate(self.policies):
                    first_belief[p_i] = copy.deepcopy(self.D) 
                
                if self.edge_handling_params['policy_sep_prior']:
                    self.set_latest_beliefs(last_belief = first_belief)
                else:
                    self.set_latest_beliefs(last_belief = self.D)
            
        else:
            self.qs = init_qs
        
        if self.pA is not None:
            self.A = utils.norm_dist_obj_arr(self.pA)
        
        if self.pB is not None:
            self.B = utils.norm_dist_obj_arr(self.pB)

        return self.qs

def step_time(self):
        """
        Advances time by one step. This involves updating the ``self.prev_actions``, and in the case of a moving
        inference horizon, this also shifts the history of post-dictive beliefs forward in time (using ``self.set_latest_beliefs()``),
        so that the penultimate belief before the beginning of the horizon is correctly indexed.

        Returns
        ---------
        curr_timestep: ``int``
            The index in absolute simulation time of the current timestep.
        """

        if self.prev_actions is None:
            self.prev_actions = [self.action]
        else:
            self.prev_actions.append(self.action)

        self.curr_timestep += 1

        if self.inference_algo == "MMP" and (self.curr_timestep - self.inference_horizon) >= 0:
            self.set_latest_beliefs()
        
        return self.curr_timestep

def set_latest_beliefs(self,last_belief=None):
        """
        Both sets and returns the penultimate belief before the first timestep of the backwards inference horizon. 
        In the case that the inference horizon includes the first timestep of the simulation, then the ``latest_belief`` is
        simply the first belief of the whole simulation, or the prior (``self.D``). The particular structure of the ``latest_belief``
        depends on the value of ``self.edge_handling_params['use_BMA']``.

        Returns
        ---------
        latest_belief: ``numpy.ndarray`` of dtype object
            Penultimate posterior beliefs over hidden states at the timestep just before the first timestep of the inference horizon. 
            Depending on the value of ``self.edge_handling_params['use_BMA']``, the shape of this output array will differ.
            If ``self.edge_handling_params['use_BMA'] == True``, then ``latest_belief`` will be a Bayesian model average 
            of beliefs about hidden states, where the average is taken with respect to posterior beliefs about policies.
            Otherwise, `latest_belief`` will be the full, policy-conditioned belief about hidden states, and will have indexing structure
            policies->factors, such that ``latest_belief[p_idx][f_idx]`` refers to the penultimate belief about marginal factor ``f_idx``
            under policy ``p_idx``.
        """

        if last_belief is None:
            last_belief = utils.obj_array(len(self.policies))
            for p_i, _ in enumerate(self.policies):
                last_belief[p_i] = copy.deepcopy(self.qs[p_i][0])

        begin_horizon_step = self.curr_timestep - self.inference_horizon
        if self.edge_handling_params['use_BMA'] and (begin_horizon_step >= 0):
            if hasattr(self, "q_pi_hist"):
                self.latest_belief = inference.average_states_over_policies(last_belief, self.q_pi_hist[begin_horizon_step]) # average the earliest marginals together using contemporaneous posterior over policies (`self.q_pi_hist[0]`)
            else:
                self.latest_belief = inference.average_states_over_policies(last_belief, self.q_pi) # average the earliest marginals together using posterior over policies (`self.q_pi`)
        else:
            self.latest_belief = last_belief

        return self.latest_belief

def get_future_qs(self):
        """
        Returns the last ``self.policy_len`` timesteps of each policy-conditioned belief
        over hidden states. This is a step of pre-processing that needs to be done before computing
        the expected free energy of policies. We do this to avoid computing the expected free energy of 
        policies using beliefs about hidden states in the past (so-called "post-dictive" beliefs).

        Returns
        ---------
        future_qs_seq: ``numpy.ndarray`` of dtype object
            Posterior beliefs over hidden states under a policy, in the future. This is a nested ``numpy.ndarray`` object array, with one
            sub-array ``future_qs_seq[p_idx]`` for each policy. The indexing structure is policy->timepoint-->factor, so that 
            ``future_qs_seq[p_idx][t_idx][f_idx]`` refers to beliefs about marginal factor ``f_idx`` expected under policy ``p_idx`` 
            at future timepoint ``t_idx``, relative to the current timestep.
        """
        
        future_qs_seq = utils.obj_array(len(self.qs))
        for p_idx in range(len(self.qs)):
            future_qs_seq[p_idx] = self.qs[p_idx][-(self.policy_len+1):] # this grabs only the last `policy_len`+1 beliefs about hidden states, under each policy

        return future_qs_seq

def infer_states(self, observation, distr_obs=False):
        """
        Update approximate posterior over hidden states by solving variational inference problem, given an observation.

        Parameters
        ----------
        observation: ``list`` or ``tuple`` of ints
            The observation input. Each entry ``observation[m]`` stores the index of the discrete
            observation for modality ``m``.
        distr_obs: ``bool``
            Whether the observation is a distribution over possible observations, rather than a single observation.

        Returns
        ---------
        qs: ``numpy.ndarray`` of dtype object
            Posterior beliefs over hidden states. Depending on the inference algorithm chosen, the resulting ``qs`` variable will have additional sub-structure to reflect whether
            beliefs are additionally conditioned on timepoint and policy.
            For example, in case the ``self.inference_algo == 'MMP' `` indexing structure is policy->timepoint-->factor, so that 
            ``qs[p_idx][t_idx][f_idx]`` refers to beliefs about marginal factor ``f_idx`` expected under policy ``p_idx`` 
            at timepoint ``t_idx``.
        """

        observation = tuple(observation) if not distr_obs else observation

        if not hasattr(self, "qs"):
            self.reset()

        if self.inference_algo == "VANILLA":
            if self.action is not None:
                empirical_prior = control.get_expected_states_interactions(
                    self.qs, self.B, self.B_factor_list, self.action.reshape(1, -1) 
                )[0]
            else:
                empirical_prior = self.D
            qs = inference.update_posterior_states_factorized(
                self.A,
                observation,
                self.num_obs,
                self.num_states,
                self.mb_dict,
                empirical_prior,
                **self.inference_params
            )
        elif self.inference_algo == "MMP":

            self.prev_obs.append(observation)
            if len(self.prev_obs) > self.inference_horizon:
                latest_obs = self.prev_obs[-self.inference_horizon:]
                latest_actions = self.prev_actions[-(self.inference_horizon-1):]
            else:
                latest_obs = self.prev_obs
                latest_actions = self.prev_actions

            qs, F = inference.update_posterior_states_full_factorized(
                self.A,
                self.mb_dict,
                self.B,
                self.B_factor_list,
                latest_obs,
                self.policies, 
                latest_actions, 
                prior = self.latest_belief, 
                policy_sep_prior = self.edge_handling_params['policy_sep_prior'],
                **self.inference_params
            )

            self.F = F # variational free energy of each policy  

        if hasattr(self, "qs_hist"):
            self.qs_hist.append(qs)
        self.qs = qs

        return qs

def _infer_states_test(self, observation, distr_obs=False):
        """
        Test version of ``infer_states()`` that additionally returns intermediate variables of MMP, such as
        the prediction errors and intermediate beliefs from the optimization. Used for benchmarking against SPM outputs.
        """
        observation = tuple(observation) if not distr_obs else observation

        if not hasattr(self, "qs"):
            self.reset()

        if self.inference_algo == "VANILLA":
            if self.action is not None:
                empirical_prior = control.get_expected_states(
                    self.qs, self.B, self.action.reshape(1, -1) 
                )[0]
            else:
                empirical_prior = self.D
            qs = inference.update_posterior_states(
                self.A,
                observation,
                empirical_prior,
                **self.inference_params
            )
        elif self.inference_algo == "MMP":

            self.prev_obs.append(observation)
            if len(self.prev_obs) > self.inference_horizon:
                latest_obs = self.prev_obs[-self.inference_horizon:]
                latest_actions = self.prev_actions[-(self.inference_horizon-1):]
            else:
                latest_obs = self.prev_obs
                latest_actions = self.prev_actions

            qs, F, xn, vn = inference._update_posterior_states_full_test(
                self.A,
                self.B, 
                latest_obs,
                self.policies, 
                latest_actions, 
                prior = self.latest_belief, 
                policy_sep_prior = self.edge_handling_params['policy_sep_prior'],
                **self.inference_params
            )

            self.F = F # variational free energy of each policy  

        if hasattr(self, "qs_hist"):
            self.qs_hist.append(qs)

        self.qs = qs

        if self.inference_algo == "MMP":
            return qs, xn, vn
        else:
            return qs

def infer_policies(self):
        """
        Perform policy inference by optimizing a posterior (categorical) distribution over policies.
        This distribution is computed as the softmax of ``G * gamma + lnE`` where ``G`` is the negative expected
        free energy of policies, ``gamma`` is a policy precision and ``lnE`` is the (log) prior probability of policies.
        This function returns the posterior over policies as well as the negative expected free energy of each policy.
        In this version of the function, the expected free energy of policies is computed using known factorized structure 
        in the model, which speeds up computation (particular the state information gain calculations).

        Returns
        ----------
        q_pi: 1D ``numpy.ndarray``
            Posterior beliefs over policies, i.e. a vector containing one posterior probability per policy.
        G: 1D ``numpy.ndarray``
            Negative expected free energies of each policy, i.e. a vector containing one negative expected free energy per policy.
        """

        if self.inference_algo == "VANILLA":
            if self.sophisticated:
                q_pi, G = control.sophisticated_inference_search(
                    self.qs, 
                    self.policies, 
                    self.A, 
                    self.B, 
                    self.C, 
                    self.A_factor_list, 
                    self.B_factor_list, 
                    self.I,
                    self.si_horizon,
                    self.si_policy_prune_threshold, 
                    self.si_state_prune_threshold, 
                    self.si_prune_penalty,
                    1.0,
                    self.inference_params,
                    n=0
                )
            else:
                q_pi, G = control.update_posterior_policies_factorized(
                    self.qs,
                    self.A,
                    self.B,
                    self.C,
                    self.A_factor_list,
                    self.B_factor_list,
                    self.policies,
                    self.use_utility,
                    self.use_states_info_gain,
                    self.use_param_info_gain,
                    self.pA,
                    self.pB,
                    E = self.E,
                    I = self.I,
                    gamma = self.gamma
                )
        elif self.inference_algo == "MMP":

            future_qs_seq = self.get_future_qs()

            q_pi, G = control.update_posterior_policies_full_factorized(
                future_qs_seq,
                self.A,
                self.B,
                self.C,
                self.A_factor_list,
                self.B_factor_list,
                self.policies,
                self.use_utility,
                self.use_states_info_gain,
                self.use_param_info_gain,
                self.latest_belief,
                self.pA,
                self.pB,
                F=self.F,
                E=self.E,
                I=self.I,
                gamma=self.gamma
            )

        if hasattr(self, "q_pi_hist"):
            self.q_pi_hist.append(q_pi)
            if len(self.q_pi_hist) > self.inference_horizon:
                self.q_pi_hist = self.q_pi_hist[-(self.inference_horizon-1):]

        self.q_pi = q_pi
        self.G = G
        return q_pi, G

def sample_action(self):
        """
        Sample or select a discrete action from the posterior over control states.
        This function both sets or cachés the action as an internal variable with the agent and returns it.
        This function also updates time variable (and thus manages consequences of updating the moving reference frame of beliefs)
        using ``self.step_time()``.

        
        Returns
        ----------
        action: 1D ``numpy.ndarray``
            Vector containing the indices of the actions for each control factor
        """

        if self.sampling_mode == "marginal":
            action = control.sample_action(
                self.q_pi, self.policies, self.num_controls, action_selection = self.action_selection, alpha = self.alpha
            )
        elif self.sampling_mode == "full":
            action = control.sample_policy(self.q_pi, self.policies, self.num_controls,
                                           action_selection=self.action_selection, alpha=self.alpha)

        self.action = action

        self.step_time()

        return action

def _sample_action_test(self):
        """
        Sample or select a discrete action from the posterior over control states.
        This function both sets or cachés the action as an internal variable with the agent and returns it.
        This function also updates time variable (and thus manages consequences of updating the moving reference frame of beliefs)
        using ``self.step_time()``.
        
        Returns
        ----------
        action: 1D ``numpy.ndarray``
            Vector containing the indices of the actions for each control factor
        """

        if self.sampling_mode == "marginal":
            action, p_dist = control._sample_action_test(self.q_pi, self.policies, self.num_controls,
                                                         action_selection=self.action_selection, alpha=self.alpha)
        elif self.sampling_mode == "full":
            action, p_dist = control._sample_policy_test(self.q_pi, self.policies, self.num_controls,
                                                         action_selection=self.action_selection, alpha=self.alpha)

        self.action = action

        self.step_time()

        return action, p_dist

def update_A(self, obs):
        """
        Update approximate posterior beliefs about Dirichlet parameters that parameterise the observation likelihood or ``A`` array.

        Parameters
        ----------
        observation: ``list`` or ``tuple`` of ints
            The observation input. Each entry ``observation[m]`` stores the index of the discrete
            observation for modality ``m``.

        Returns
        -----------
        qA: ``numpy.ndarray`` of dtype object
            Posterior Dirichlet parameters over observation model (same shape as ``A``), after having updated it with observations.
        """

        qA = learning.update_obs_likelihood_dirichlet_factorized(
            self.pA, 
            self.A, 
            obs, 
            self.qs, 
            self.A_factor_list,
            self.lr_pA, 
            self.modalities_to_learn
        )

        self.pA = qA # set new prior to posterior
        self.A = utils.norm_dist_obj_arr(qA) # take expected value of posterior Dirichlet parameters to calculate posterior over A array

        return qA

def _update_A_old(self, obs):
        """
        Update approximate posterior beliefs about Dirichlet parameters that parameterise the observation likelihood or ``A`` array.

        Parameters
        ----------
        observation: ``list`` or ``tuple`` of ints
            The observation input. Each entry ``observation[m]`` stores the index of the discrete
            observation for modality ``m``.

        Returns
        -----------
        qA: ``numpy.ndarray`` of dtype object
            Posterior Dirichlet parameters over observation model (same shape as ``A``), after having updated it with observations.
        """

        qA = learning.update_obs_likelihood_dirichlet(
            self.pA, 
            self.A, 
            obs, 
            self.qs, 
            self.lr_pA, 
            self.modalities_to_learn
        )

        self.pA = qA # set new prior to posterior
        self.A = utils.norm_dist_obj_arr(qA) # take expected value of posterior Dirichlet parameters to calculate posterior over A array

        return qA

def update_B(self, qs_prev):
        """
        Update posterior beliefs about Dirichlet parameters that parameterise the transition likelihood 
        
        Parameters
        -----------
        qs_prev: 1D ``numpy.ndarray`` or ``numpy.ndarray`` of dtype object
            Marginal posterior beliefs over hidden states at previous timepoint.
    
        Returns
        -----------
        qB: ``numpy.ndarray`` of dtype object
            Posterior Dirichlet parameters over transition model (same shape as ``B``), after having updated it with state beliefs and actions.
        """

        qB = learning.update_state_likelihood_dirichlet_interactions(
            self.pB,
            self.B,
            self.action,
            self.qs,
            qs_prev,
            self.B_factor_list,
            self.lr_pB,
            self.factors_to_learn
        )

        self.pB = qB # set new prior to posterior
        self.B = utils.norm_dist_obj_arr(qB)  # take expected value of posterior Dirichlet parameters to calculate posterior over B array

        return qB

def _update_B_old(self, qs_prev):
        """
        Update posterior beliefs about Dirichlet parameters that parameterise the transition likelihood 
        
        Parameters
        -----------
        qs_prev: 1D ``numpy.ndarray`` or ``numpy.ndarray`` of dtype object
            Marginal posterior beliefs over hidden states at previous timepoint.
    
        Returns
        -----------
        qB: ``numpy.ndarray`` of dtype object
            Posterior Dirichlet parameters over transition model (same shape as ``B``), after having updated it with state beliefs and actions.
        """

        qB = learning.update_state_likelihood_dirichlet(
            self.pB,
            self.B,
            self.action,
            self.qs,
            qs_prev,
            self.lr_pB,
            self.factors_to_learn
        )

        self.pB = qB # set new prior to posterior
        self.B = utils.norm_dist_obj_arr(qB)  # take expected value of posterior Dirichlet parameters to calculate posterior over B array

        return qB

def update_D(self, qs_t0 = None):
        """
        Update Dirichlet parameters of the initial hidden state distribution 
        (prior beliefs about hidden states at the beginning of the inference window).

        Parameters
        -----------
        qs_t0: 1D ``numpy.ndarray``, ``numpy.ndarray`` of dtype object, or ``None``
            Marginal posterior beliefs over hidden states at current timepoint. If ``None``, the 
            value of ``qs_t0`` is set to ``self.qs_hist[0]`` (i.e. the initial hidden state beliefs at the first timepoint).
            If ``self.inference_algo == "MMP"``, then ``qs_t0`` is set to be the Bayesian model average of beliefs about hidden states
            at the first timestep of the backwards inference horizon, where the average is taken with respect to posterior beliefs about policies.
      
        Returns
        -----------
        qD: ``numpy.ndarray`` of dtype object
            Posterior Dirichlet parameters over initial hidden state prior (same shape as ``qs_t0``), after having updated it with state beliefs.
        """
        
        if self.inference_algo == "VANILLA":
            
            if qs_t0 is None:
                
                try:
                    qs_t0 = self.qs_hist[0]
                except ValueError:
                    print("qs_t0 must either be passed as argument to `update_D` or `save_belief_hist` must be set to True!")             

        elif self.inference_algo == "MMP":
            
            if self.edge_handling_params['use_BMA']:
                qs_t0 = self.latest_belief
            elif self.edge_handling_params['policy_sep_prior']:
              
                qs_pi_t0 = self.latest_belief

                # get beliefs about policies at the time at the beginning of the inference horizon
                if hasattr(self, "q_pi_hist"):
                    begin_horizon_step = max(0, self.curr_timestep - self.inference_horizon)
                    q_pi_t0 = np.copy(self.q_pi_hist[begin_horizon_step])
                else:
                    q_pi_t0 = np.copy(self.q_pi)
            
                qs_t0 = inference.average_states_over_policies(qs_pi_t0,q_pi_t0) # beliefs about hidden states at the first timestep of the inference horizon
        
        qD = learning.update_state_prior_dirichlet(self.pD, qs_t0, self.lr_pD, factors = self.factors_to_learn)
        
        self.pD = qD # set new prior to posterior
        self.D = utils.norm_dist_obj_arr(qD) # take expected value of posterior Dirichlet parameters to calculate posterior over D array

        return qD

def _get_default_params(self):
        method = self.inference_algo
        default_params = None
        if method == "VANILLA":
            default_params = {"num_iter": 10, "dF": 1.0, "dF_tol": 0.001, "compute_vfe": True}
        elif method == "MMP":
            default_params = {"num_iter": 10, "grad_descent": True, "tau": 0.25}
        elif method == "VMP":
            raise NotImplementedError("VMP is not implemented")
        elif method == "BP":
            raise NotImplementedError("BP is not implemented")
        elif method == "EP":
            raise NotImplementedError("EP is not implemented")
        elif method == "CV":
            raise NotImplementedError("CV is not implemented")

        return default_params

def update_posterior_states_full(
    A,
    B,
    prev_obs,
    policies,
    prev_actions=None,
    prior=None,
    policy_sep_prior = True,
    **kwargs,
):
    """
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
    """

    num_obs, num_states, num_modalities, num_factors = utils.get_model_dimensions(A, B)
    
    prev_obs = utils.process_observation_seq(prev_obs, num_modalities, num_obs)
   
    lh_seq = get_joint_likelihood_seq(A, prev_obs, num_states)

    if prev_actions is not None:
        prev_actions = np.stack(prev_actions,0)

    qs_seq_pi = utils.obj_array(len(policies))
    F = np.zeros(len(policies)) # variational free energy of policies

    for p_idx, policy in enumerate(policies):

            # get sequence and the free energy for policy
            qs_seq_pi[p_idx], F[p_idx] = run_mmp(
                lh_seq,
                B,
                policy,
                prev_actions=prev_actions,
                prior= prior[p_idx] if policy_sep_prior else prior, 
                **kwargs
            )

    return qs_seq_pi, F

def update_posterior_states_full_factorized(
    A,
    mb_dict,
    B,
    B_factor_list,
    prev_obs,
    policies,
    prev_actions=None,
    prior=None,
    policy_sep_prior = True,
    **kwargs,
):
    """
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
    """

    num_obs, num_states, num_modalities, num_factors = utils.get_model_dimensions(A, B)
    
    prev_obs = utils.process_observation_seq(prev_obs, num_modalities, num_obs)
   
    lh_seq = get_joint_likelihood_seq_by_modality(A, prev_obs, num_states)

    if prev_actions is not None:
        prev_actions = np.stack(prev_actions,0)

    qs_seq_pi = utils.obj_array(len(policies))
    F = np.zeros(len(policies)) # variational free energy of policies

    for p_idx, policy in enumerate(policies):

            # get sequence and the free energy for policy
            qs_seq_pi[p_idx], F[p_idx] = run_mmp_factorized(
                lh_seq,
                mb_dict,
                B,
                B_factor_list,
                policy,
                prev_actions=prev_actions,
                prior= prior[p_idx] if policy_sep_prior else prior, 
                **kwargs
            )

    return qs_seq_pi, F

def _update_posterior_states_full_test(
    A,
    B,
    prev_obs,
    policies,
    prev_actions=None,
    prior=None,
    policy_sep_prior = True,
    **kwargs,
):
    """
    Update posterior over hidden states using marginal message passing (TEST VERSION, with extra returns for benchmarking).

    Parameters
    ----------
    A: ``numpy.ndarray`` of dtype object
        Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
        stores an ``np.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
        the probability of observation level ``i`` given hidden state levels ``j, k, ...``
    B: ``numpy.ndarray`` of dtype object
        Dynamics likelihood mapping or 'transition model', mapping from hidden states at ``t`` to hidden states at ``t+1``, given some control state ``u``.
        Each element ``B[f]`` of this object array stores a 3-D tensor for hidden state factor ``f``, whose entries ``B[f][s, v, u]`` store the probability
        of hidden state level ``s`` at the current time, given hidden state level ``v`` and action ``u`` at the previous time.
    prev_obs: list
        List of observations over time. Each observation in the list can be an ``int``, a ``list`` of ints, a ``tuple`` of ints, a one-hot vector or an object array of one-hot vectors.
    prior: ``numpy.ndarray`` of dtype object, default None
        If provided, this a ``numpy.ndarray`` of dtype object, with one sub-array per hidden state factor, that stores the prior beliefs about initial states. 
        If ``None``, this defaults to a flat (uninformative) prior over hidden states.
    policy_sep_prior: Bool, default True
        Flag determining whether the prior beliefs from the past are unconditioned on policy, or separated by /conditioned on the policy variable.
    **kwargs: keyword arguments
        Optional keyword arguments for the function ``algos.mmp.run_mmp``

    Returns
    --------
    qs_seq_pi: ``numpy.ndarray`` of dtype object
        Posterior beliefs over hidden states for each policy. Nesting structure is policies, timepoints, factors,
        where e.g. ``qs_seq_pi[p][t][f]`` stores the marginal belief about factor ``f`` at timepoint ``t`` under policy ``p``.
    F: 1D ``numpy.ndarray``
        Vector of variational free energies for each policy
    xn_seq_pi: ``numpy.ndarray`` of dtype object
        Posterior beliefs over hidden states for each policy, for each iteration of marginal message passing.
        Nesting structure is policy, iteration, factor, so ``xn_seq_p[p][itr][f]`` stores the ``num_states x infer_len`` 
        array of beliefs about hidden states at different time points of inference horizon.
    vn_seq_pi: `numpy.ndarray`` of dtype object
        Prediction errors over hidden states for each policy, for each iteration of marginal message passing.
        Nesting structure is policy, iteration, factor, so ``vn_seq_p[p][itr][f]`` stores the ``num_states x infer_len`` 
        array of beliefs about hidden states at different time points of inference horizon.
    """

    num_obs, num_states, num_modalities, num_factors = utils.get_model_dimensions(A, B)

    prev_obs = utils.process_observation_seq(prev_obs, num_modalities, num_obs)
    
    lh_seq = get_joint_likelihood_seq(A, prev_obs, num_states)

    if prev_actions is not None:
        prev_actions = np.stack(prev_actions,0)

    qs_seq_pi = utils.obj_array(len(policies))
    xn_seq_pi = utils.obj_array(len(policies))
    vn_seq_pi = utils.obj_array(len(policies))
    F = np.zeros(len(policies)) # variational free energy of policies

    for p_idx, policy in enumerate(policies):

            # get sequence and the free energy for policy
            qs_seq_pi[p_idx], F[p_idx], xn_seq_pi[p_idx], vn_seq_pi[p_idx] = _run_mmp_testing(
                lh_seq,
                B,
                policy,
                prev_actions=prev_actions,
                prior=prior[p_idx] if policy_sep_prior else prior, 
                **kwargs
            )

    return qs_seq_pi, F, xn_seq_pi, vn_seq_pi

def average_states_over_policies(qs_pi, q_pi):
    """
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
    """

    num_factors = len(qs_pi[0]) # get the number of hidden state factors using the shape of the first-policy-conditioned posterior
    num_states = [qs_f.shape[0] for qs_f in qs_pi[0]] # get the dimensionalities of each hidden state factor 

    qs_bma = utils.obj_array(num_factors)
    for f in range(num_factors):
        qs_bma[f] = np.zeros(num_states[f])

    for p_idx, policy_weight in enumerate(q_pi):

        for f in range(num_factors):

            qs_bma[f] += qs_pi[p_idx][f] * policy_weight

    return qs_bma

def update_posterior_states(A, obs, prior=None, **kwargs):
    """
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
    """

    num_obs, num_states, num_modalities, _ = utils.get_model_dimensions(A = A)
    
    obs = utils.process_observation(obs, num_modalities, num_obs)

    if prior is not None:
        prior = utils.to_obj_array(prior)

    return run_vanilla_fpi(A, obs, num_obs, num_states, prior, **kwargs)

def update_posterior_states_factorized(A, obs, num_obs, num_states, mb_dict, prior=None, **kwargs):
    """
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
    """
    
    num_modalities = len(num_obs)
    
    obs = utils.process_observation(obs, num_modalities, num_obs)

    if prior is not None:
        prior = utils.to_obj_array(prior)

    return run_vanilla_fpi_factorized(A, obs, num_obs, num_states, mb_dict, prior, **kwargs)

def update_obs_likelihood_dirichlet(pA, A, obs, qs, lr=1.0, modalities="all"):
    """ 
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
    """


    num_modalities = len(pA)
    num_observations = [pA[modality].shape[0] for modality in range(num_modalities)]

    obs_processed = utils.process_observation(obs, num_modalities, num_observations)
    obs = utils.to_obj_array(obs_processed)

    if modalities == "all":
        modalities = list(range(num_modalities))

    qA = copy.deepcopy(pA)
        
    for modality in modalities:
        dfda = maths.spm_cross(obs[modality], qs)
        dfda = dfda * (A[modality] > 0).astype("float")
        qA[modality] = qA[modality] + (lr * dfda)

    return qA

def update_obs_likelihood_dirichlet_factorized(pA, A, obs, qs, A_factor_list, lr=1.0, modalities="all"):
    """ 
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
    """

    num_modalities = len(pA)
    num_observations = [pA[modality].shape[0] for modality in range(num_modalities)]

    obs_processed = utils.process_observation(obs, num_modalities, num_observations)
    obs = utils.to_obj_array(obs_processed)

    if modalities == "all":
        modalities = list(range(num_modalities))

    qA = copy.deepcopy(pA)
        
    for modality in modalities:
        dfda = maths.spm_cross(obs[modality], qs[A_factor_list[modality]])
        dfda = dfda * (A[modality] > 0).astype("float")
        qA[modality] = qA[modality] + (lr * dfda)

    return qA

def update_state_likelihood_dirichlet(
    pB, B, actions, qs, qs_prev, lr=1.0, factors="all"
):
    """
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
    """

    num_factors = len(pB)

    qB = copy.deepcopy(pB)
   
    if factors == "all":
        factors = list(range(num_factors))

    for factor in factors:
        dfdb = maths.spm_cross(qs[factor], qs_prev[factor])
        dfdb *= (B[factor][:, :, int(actions[factor])] > 0).astype("float")
        qB[factor][:,:,int(actions[factor])] += (lr*dfdb)

    return qB

def update_state_likelihood_dirichlet_interactions(
    pB, B, actions, qs, qs_prev, B_factor_list, lr=1.0, factors="all"
):
    """
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
    """

    num_factors = len(pB)

    qB = copy.deepcopy(pB)
   
    if factors == "all":
        factors = list(range(num_factors))

    for factor in factors:
        dfdb = maths.spm_cross(qs[factor], qs_prev[B_factor_list[factor]])
        dfdb *= (B[factor][...,int(actions[factor])] > 0).astype("float")
        qB[factor][...,int(actions[factor])] += (lr*dfdb)

    return qB

def update_state_prior_dirichlet(
    pD, qs, lr=1.0, factors="all"
):
    """
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
    """

    num_factors = len(pD)

    qD = copy.deepcopy(pD)
   
    if factors == "all":
        factors = list(range(num_factors))

    for factor in factors:
        idx = pD[factor] > 0 # only update those state level indices that have some prior probability
        qD[factor][idx] += (lr * qs[factor][idx])
       
    return qD

def _prune_prior(prior, levels_to_remove, dirichlet = False):
    """
    Function for pruning a prior Categorical distribution (e.g. C, D)

    Parameters
    -----------
    prior: 1D ``numpy.ndarray`` or ``numpy.ndarray`` of dtype object
        The vector(s) containing the priors over hidden states of a generative model, e.g. the prior over hidden states (``D`` vector). 
    levels_to_remove: ``list`` of ``int``, ``list`` of ``list``
        A ``list`` of the levels (indices of the support) to remove. If the prior in question has multiple hidden state factors / multiple observation modalities, 
        then this will be a ``list`` of ``list``, where each sub-list within ``levels_to_remove`` will contain the levels to prune for a particular hidden state factor or modality 
    dirichlet: ``Bool``, default ``False``
        A Boolean flag indicating whether the input vector(s) is/are a Dirichlet distribution, and therefore should not be normalized at the end. 
        @TODO: Instead, the dirichlet parameters from the pruned levels should somehow be re-distributed among the remaining levels

    Returns
    -----------
    reduced_prior: 1D ``numpy.ndarray`` or ``numpy.ndarray`` of dtype object
        The prior vector(s), after pruning, that lacks the hidden state or modality levels indexed by ``levels_to_remove``
    """

    if utils.is_obj_array(prior): # in case of multiple hidden state factors

        assert all([type(levels) == list for levels in levels_to_remove])

        num_factors = len(prior)

        reduced_prior = utils.obj_array(num_factors)

        factors_to_remove = []
        for f, s_i in enumerate(prior): # loop over factors (or modalities)
            
            ns = len(s_i)
            levels_to_keep = list(set(range(ns)) - set(levels_to_remove[f]))
            if len(levels_to_keep) == 0:
                print(f'Warning... removing ALL levels of factor {f} - i.e. the whole hidden state factor is being removed\n')
                factors_to_remove.append(f)
            else:
                if not dirichlet:
                    reduced_prior[f] = utils.norm_dist(s_i[levels_to_keep])
                else:
                    raise(NotImplementedError("Need to figure out how to re-distribute concentration parameters from pruned levels, across remaining levels"))


        if len(factors_to_remove) > 0:
            factors_to_keep = list(set(range(num_factors)) - set(factors_to_remove))
            reduced_prior = reduced_prior[factors_to_keep]

    else: # in case of one hidden state factor

        assert all([type(level_i) == int for level_i in levels_to_remove])

        ns = len(prior)
        levels_to_keep = list(set(range(ns)) - set(levels_to_remove))

        if not dirichlet:
            reduced_prior = utils.norm_dist(prior[levels_to_keep])
        else:
            raise(NotImplementedError("Need to figure out how to re-distribute concentration parameters from pruned levels, across remaining levels"))

    return reduced_prior

def _prune_A(A, obs_levels_to_prune, state_levels_to_prune, dirichlet = False):
    """
    Function for pruning a observation likelihood model (with potentially multiple hidden state factors)
    :meta private:
    Parameters
    -----------
    A: ``numpy.ndarray`` with ``ndim >= 2``, or ``numpy.ndarray`` of dtype object
        Sensory likelihood mapping or 'observation model', mapping from hidden states to observations. Each element ``A[m]`` of
        stores an ``numpy.ndarray`` multidimensional array for observation modality ``m``, whose entries ``A[m][i, j, k, ...]`` store 
        the probability of observation level ``i`` given hidden state levels ``j, k, ...``
    obs_levels_to_prune: ``list`` of int or ``list`` of ``list``: 
        A ``list`` of the observation levels to remove. If the likelihood in question has multiple observation modalities, 
        then this will be a ``list`` of ``list``, where each sub-list within ``obs_levels_to_prune`` will contain the observation levels 
        to remove for a particular observation modality 
    state_levels_to_prune: ``list`` of ``int``
        A ``list`` of the hidden state levels to remove (this will be the same across modalities)
    dirichlet: ``Bool``, default ``False``
        A Boolean flag indicating whether the input array(s) is/are a Dirichlet distribution, and therefore should not be normalized at the end. 
        @TODO: Instead, the dirichlet parameters from the pruned columns should somehow be re-distributed among the remaining columns

    Returns
    -----------
    reduced_A: ``numpy.ndarray`` with ndim >= 2, or ``numpy.ndarray ``of dtype object
        The observation model, after pruning, which lacks the observation or hidden state levels given by the arguments ``obs_levels_to_prune`` and ``state_levels_to_prune``
    """

    columns_to_keep_list = []
    if utils.is_obj_array(A):
        num_states = A[0].shape[1:]
        for f, ns in enumerate(num_states):
            indices_f = np.array( list(set(range(ns)) - set(state_levels_to_prune[f])), dtype = np.intp)
            columns_to_keep_list.append(indices_f)
    else:
        num_states = A.shape[1]
        indices = np.array( list(set(range(num_states)) - set(state_levels_to_prune)), dtype = np.intp )
        columns_to_keep_list.append(indices)

    if utils.is_obj_array(A): # in case of multiple observation modality

        assert all([type(o_m_levels) == list for o_m_levels in obs_levels_to_prune])

        num_modalities = len(A)

        reduced_A = utils.obj_array(num_modalities)
        
        for m, A_i in enumerate(A): # loop over modalities
            
            no = A_i.shape[0]
            rows_to_keep = np.array(list(set(range(no)) - set(obs_levels_to_prune[m])), dtype = np.intp)
            
            reduced_A[m] = A_i[np.ix_(rows_to_keep, *columns_to_keep_list)]
        if not dirichlet:    
            reduced_A = utils.norm_dist_obj_arr(reduced_A)
        else:
            raise(NotImplementedError("Need to figure out how to re-distribute concentration parameters from pruned rows/columns, across remaining rows/columns"))
    else: # in case of one observation modality

        assert all([type(o_levels_i) == int for o_levels_i in obs_levels_to_prune])

        no = A.shape[0]
        rows_to_keep = np.array(list(set(range(no)) - set(obs_levels_to_prune)), dtype = np.intp)
            
        reduced_A = A[np.ix_(rows_to_keep, *columns_to_keep_list)]

        if not dirichlet:
            reduced_A = utils.norm_dist(reduced_A)
        else:
            raise(NotImplementedError("Need to figure out how to re-distribute concentration parameters from pruned rows/columns, across remaining rows/columns"))

    return reduced_A

def _prune_B(B, state_levels_to_prune, action_levels_to_prune, dirichlet = False):
    """
    Function for pruning a transition likelihood model (with potentially multiple hidden state factors)

    Parameters
    -----------
    B: ``numpy.ndarray`` of ``ndim == 3`` or ``numpy.ndarray`` of dtype object
        Dynamics likelihood mapping or 'transition model', mapping from hidden states at `t` to hidden states at `t+1`, given some control state `u`.
        Each element B[f] of this object array stores a 3-D tensor for hidden state factor `f`, whose entries `B[f][s, v, u] store the probability
        of hidden state level `s` at the current time, given hidden state level `v` and action `u` at the previous time.
    state_levels_to_prune: ``list`` of ``int`` or ``list`` of ``list`` 
        A ``list`` of the state levels to remove. If the likelihood in question has multiple hidden state factors, 
        then this will be a ``list`` of ``list``, where each sub-list within ``state_levels_to_prune`` will contain the state levels 
        to remove for a particular hidden state factor 
    action_levels_to_prune: ``list`` of ``int`` or ``list`` of ``list`` 
        A ``list`` of the control state or action levels to remove. If the likelihood in question has multiple control state factors, 
        then this will be a ``list`` of ``list``, where each sub-list within ``action_levels_to_prune`` will contain the control state levels 
        to remove for a particular control state factor 
    dirichlet: ``Bool``, default ``False``
        A Boolean flag indicating whether the input array(s) is/are a Dirichlet distribution, and therefore should not be normalized at the end. 
        @TODO: Instead, the dirichlet parameters from the pruned rows/columns should somehow be re-distributed among the remaining rows/columns

    Returns
    -----------
    reduced_B: ``numpy.ndarray`` of `ndim == 3` or ``numpy.ndarray`` of dtype object
        The transition model, after pruning, which lacks the hidden state levels/action levels given by the arguments ``state_levels_to_prune`` and ``action_levels_to_prune``
    """

    slices_to_keep_list = []

    if utils.is_obj_array(B):

        num_controls = [B_arr.shape[2] for _, B_arr in enumerate(B)]

        for c, nc in enumerate(num_controls):
            indices_c = np.array( list(set(range(nc)) - set(action_levels_to_prune[c])), dtype = np.intp)
            slices_to_keep_list.append(indices_c)
    else:
        num_controls = B.shape[2]
        slices_to_keep = np.array( list(set(range(num_controls)) - set(action_levels_to_prune)), dtype = np.intp )

    if utils.is_obj_array(B): # in case of multiple hidden state factors

        assert all([type(ns_f_levels) == list for ns_f_levels in state_levels_to_prune])

        num_factors = len(B)

        reduced_B = utils.obj_array(num_factors)
        
        for f, B_f in enumerate(B): # loop over modalities
            
            ns = B_f.shape[0]
            states_to_keep = np.array(list(set(range(ns)) - set(state_levels_to_prune[f])), dtype = np.intp)
            
            reduced_B[f] = B_f[np.ix_(states_to_keep, states_to_keep, slices_to_keep_list[f])]

        if not dirichlet:    
            reduced_B = utils.norm_dist_obj_arr(reduced_B)
        else:
            raise(NotImplementedError("Need to figure out how to re-distribute concentration parameters from pruned rows/columns, across remaining rows/columns"))

    else: # in case of one hidden state factor

        assert all([type(state_level_i) == int for state_level_i in state_levels_to_prune])

        ns = B.shape[0]
        states_to_keep = np.array(list(set(range(ns)) - set(state_levels_to_prune)), dtype = np.intp)
            
        reduced_B = B[np.ix_(states_to_keep, states_to_keep, slices_to_keep)]

        if not dirichlet:
            reduced_B = utils.norm_dist(reduced_B)
        else:
            raise(NotImplementedError("Need to figure out how to re-distribute concentration parameters from pruned rows/columns, across remaining rows/columns"))

    return reduced_B

def run_vanilla_fpi(A, obs, num_obs, num_states, prior=None, num_iter=10, dF=1.0, dF_tol=0.001, compute_vfe=True):
    """
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
    """

    # get model dimensions
    n_modalities = len(num_obs)
    n_factors = len(num_states)

    """
    =========== Step 1 ===========
        Loop over the observation modalities and use assumption of independence 
        among observation modalitiesto multiply each modality-specific likelihood 
        onto a single joint likelihood over hidden factors [size num_states]
    """

    likelihood = get_joint_likelihood(A, obs, num_states)

    likelihood = spm_log_single(likelihood)

    """
    =========== Step 2 ===========
        Create a flat posterior (and prior if necessary)
    """

    qs = obj_array_uniform(num_states)

    """
    If prior is not provided, initialise prior to be identical to posterior 
    (namely, a flat categorical distribution). Take the logarithm of it (required for 
    FPI algorithm below).
    """
    if prior is None:
        prior = obj_array_uniform(num_states)
        
    prior = spm_log_obj_array(prior) # log the prior


    """
    =========== Step 3 ===========
        Initialize initial free energy
    """
    if compute_vfe:
        prev_vfe = calc_free_energy(qs, prior, n_factors)

    """
    =========== Step 4 ===========
        If we have a single factor, we can just add prior and likelihood because there is a unique FE minimum that can reached instantaneously,
        otherwise we run fixed point iteration
    """

    if n_factors == 1:

        qL = spm_dot(likelihood, qs, [0])

        return to_obj_array(softmax(qL + prior[0]))

    else:
        """
        =========== Step 5 ===========
        Run the FPI scheme
        """

        # change stop condition for fixed point iterations based on whether we are computing the variational free energy or not
        condition_check_both = lambda curr_iter, dF: curr_iter < num_iter and dF >= dF_tol
        condition_check_just_numiter = lambda curr_iter, dF: curr_iter < num_iter
        check_stop_condition = condition_check_both if compute_vfe else condition_check_just_numiter

        curr_iter = 0

        while check_stop_condition(curr_iter, dF):
            # Initialise variational free energy
            vfe = 0

            # arg_list = [likelihood, list(range(n_factors))]
            # arg_list = arg_list + list(chain(*([qs_i,[i]] for i, qs_i in enumerate(qs)))) + [list(range(n_factors))]
            # LL_tensor = np.einsum(*arg_list)

            qs_all = qs[0]
            for factor in range(n_factors-1):
                qs_all = qs_all[...,None]*qs[factor+1]
            LL_tensor = likelihood * qs_all

            for factor, qs_i in enumerate(qs):
                # qL = np.einsum(LL_tensor, list(range(n_factors)), 1.0/qs_i, [factor], [factor])
                qL = np.einsum(LL_tensor, list(range(n_factors)), [factor])/qs_i
                qs[factor] = softmax(qL + prior[factor])

            # print(f'Posteriors at iteration {curr_iter}:\n')
            # print(qs[0])
            # print(qs[1])
            # List of orders in which marginal posteriors are sequentially multiplied into the joint likelihood:
            # First order loops over factors starting at index = 0, second order goes in reverse
            # factor_orders = [range(n_factors), range((n_factors - 1), -1, -1)]

            # iteratively marginalize out each posterior marginal from the joint log-likelihood
            # except for the one associated with a given factor
            # for factor_order in factor_orders:
            #     for factor in factor_order:
            #         qL = spm_dot(likelihood, qs, [factor])
            #         qs[factor] = softmax(qL + prior[factor])

            if compute_vfe:
                # calculate new free energy
                vfe = calc_free_energy(qs, prior, n_factors, likelihood)

                # print(f'VFE at iteration {curr_iter}: {vfe}\n')
                # stopping condition - time derivative of free energy
                dF = np.abs(prev_vfe - vfe)
                prev_vfe = vfe

            curr_iter += 1

        return qs

def run_vanilla_fpi_factorized(A, obs, num_obs, num_states, mb_dict, prior=None, num_iter=10, dF=1.0, dF_tol=0.001, compute_vfe=True):
    """
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
    """

    # get model dimensions
    n_modalities = len(num_obs)
    n_factors = len(num_states)

    """
    =========== Step 1 ===========
        Generate modality-specific log-likelihood tensors (will be tensors of different-shapes,
        where `likelihood[m].ndim` will be equal to  `len(mb_dict['A_factor_list'][m])`
    """

    likelihood = obj_array(n_modalities)
    obs = to_obj_array(obs)
    for (m, A_m) in enumerate(A):
        likelihood[m] = dot_likelihood(A_m, obs[m])

    log_likelihood = spm_log_obj_array(likelihood)

    """
    =========== Step 2 ===========
        Create a flat posterior (and prior if necessary)
    """

    qs = obj_array_uniform(num_states)

    """
    If prior is not provided, initialise prior to be identical to posterior 
    (namely, a flat categorical distribution). Take the logarithm of it (required for 
    FPI algorithm below).
    """
    if prior is None:
        prior = obj_array_uniform(num_states)
        
    prior = spm_log_obj_array(prior) # log the prior


    """
    =========== Step 3 ===========
        Initialize initial free energy
    """
    prev_vfe = calc_free_energy(qs, prior, n_factors)

    """
    =========== Step 4 ===========
        If we have a single factor, we can just add prior and likelihood because there is a unique FE minimum that can reached instantaneously,
        otherwise we run fixed point iteration
    """

    if n_factors == 1:

        joint_loglikelihood = np.zeros(tuple(num_states))
        for m in range(n_modalities):
            joint_loglikelihood += log_likelihood[m] # add up all the log-likelihoods, since we know they will all have the same dimension in the case of a single hidden state factor
        qL = spm_dot(joint_loglikelihood, qs, [0])

        qs = to_obj_array(softmax(qL + prior[0]))

    else:
        """
        =========== Step 5 ===========
        Run the factorized FPI scheme
        """

        A_factor_list, A_modality_list = mb_dict['A_factor_list'], mb_dict['A_modality_list']

        if compute_vfe:
            joint_loglikelihood = np.zeros(tuple(num_states))
            for m in range(n_modalities):
                reshape_dims = n_factors*[1]
                for _f_id in A_factor_list[m]:
                    reshape_dims[_f_id] = num_states[_f_id]

                joint_loglikelihood += log_likelihood[m].reshape(reshape_dims) # add up all the log-likelihoods after reshaping them to the global common dimensions of all hidden state factors

        curr_iter = 0

        # change stop condition for fixed point iterations based on whether we are computing the variational free energy or not
        condition_check_both = lambda curr_iter, dF: curr_iter < num_iter and dF >= dF_tol
        condition_check_just_numiter = lambda curr_iter, dF: curr_iter < num_iter
        check_stop_condition = condition_check_both if compute_vfe else condition_check_just_numiter

        while check_stop_condition(curr_iter, dF):
            
            # vfe = 0 

            qs_new = obj_array(n_factors)
            for f in range(n_factors):
            
                '''
                Sum the expected log likelihoods E_q(s_i/f)[ln P(o=obs[m]|s)] for independent modalities together,
                since they may have differing dimension. This obtains a marginal log-likelihood for the current factor index `factor`,
                which includes the evidence for that particular factor afforded by the different modalities. 
                '''
            
                qL = np.zeros(num_states[f])

                for ii, m in enumerate(A_modality_list[f]):
                
                    qL += spm_dot(log_likelihood[m], qs[A_factor_list[m]], [A_factor_list[m].index(f)])

                qs_new[f] = softmax(qL + prior[f])

                # vfe -= qL.sum() # accuracy part of vfe, sum of factor-level expected energies E_q(s_i/f)[ln P(o=obs|s)]
            
            qs = deepcopy(qs_new)
            # print(f'Posteriors at iteration {curr_iter}:\n')
            # print(qs[0])
            # print(qs[1])
            # calculate new free energy, leaving out the accuracy term
            # vfe += calc_free_energy(qs, prior, n_factors)

            if compute_vfe:
                vfe = calc_free_energy(qs, prior, n_factors, likelihood=joint_loglikelihood)

                # print(f'VFE at iteration {curr_iter}: {vfe}\n')
                # stopping condition - time derivative of free energy
                dF = np.abs(prev_vfe - vfe)
                prev_vfe = vfe

            curr_iter += 1
            
    return qs

def _run_vanilla_fpi_faster(A, obs, n_observations, n_states, prior=None, num_iter=10, dF=1.0, dF_tol=0.001):
    """
    Update marginal posterior beliefs about hidden states
    using a new version of variational fixed point iteration (FPI). 
    @NOTE (Conor, 26.02.2020):
    This method uses a faster algorithm than the traditional 'spm_dot' approach. Instead of
    separately computing a conditional joint log likelihood of an outcome, under the
    posterior probabilities of a certain marginal, instead all marginals are multiplied into one 
    joint tensor that gives the joint likelihood of an observation under all hidden states, 
    that is then sequentially (and *parallelizably*) marginalized out to get each marginal posterior. 
    This method is less RAM-intensive, admits heavy parallelization, and runs (about 2x) faster.
    @NOTE (Conor, 28.02.2020):
    After further testing, discovered interesting differences between this version and the 
    original version. It appears that the
    original version (simple 'run_vanilla_fpi') shows mean-field biases or 'explaining away' 
    effects, whereas this version spreads probabilities more 'fairly' among possibilities.
    To summarize: it actually matters what order you do the summing across the joint likelihood tensor. 
    In this verison, all marginals are multiplied into the likelihood tensor before summing out, 
    whereas in the previous version, marginals are recursively multiplied and summed out.
    @NOTE (Conor, 24.04.2020): I would expect that the factor_order approach used above would help 
    ameliorate the effects of the mean-field bias. I would also expect that the use of a factor_order 
    below is unnnecessary, since the marginalisation w.r.t. each factor is done only after all marginals 
    are multiplied into the larger tensor.

    Parameters
    ----------
    - 'A' [numpy nd.array (matrix or tensor or array-of-arrays)]:
        Observation likelihood of the generative model, mapping from hidden states to observations. 
        Used to invert generative model to obtain marginal likelihood over hidden states, 
        given the observation
    - 'obs' [numpy 1D array or array of arrays (with 1D numpy array entries)]:
        The observation (generated by the environment). If single modality, this can be a 1D array 
        (one-hot vector representation). If multi-modality, this can be an array of arrays 
        (whose entries are 1D one-hot vectors).
    - 'n_observations' [int or list of ints]
    - 'n_states' [int or list of ints]
    - 'prior' [numpy 1D array, array of arrays (with 1D numpy array entries) or None]:
        Prior beliefs of the agent, to be integrated with the marginal likelihood to obtain posterior. 
        If absent, prior is set to be a uniform distribution over hidden states 
        (identical to the initialisation of the posterior)
    -'num_iter' [int]:
        Number of variational fixed-point iterations to run.
    -'dF' [float]:
        Starting free energy gradient (dF/dt) before updating in the course of gradient descent.
    -'dF_tol' [float]:
        Threshold value of the gradient of the variational free energy (dF/dt), 
        to be checked at each iteration. If dF <= dF_tol, the iterations are halted pre-emptively 
        and the final marginal posterior belief(s) is(are) returned
    Returns
    ----------
    -'qs' [numpy 1D array or array of arrays (with 1D numpy array entries):
        Marginal posterior beliefs over hidden states (single- or multi-factor) achieved 
        via variational fixed point iteration (mean-field)
    """

    # get model dimensions
    n_modalities = len(n_observations)
    n_factors = len(n_states)

    """
    =========== Step 1 ===========
        Loop over the observation modalities and use assumption of independence 
        among observation modalities to multiply each modality-specific likelihood 
        onto a single joint likelihood over hidden factors [size n_states]
    """

    # likelihood = np.ones(tuple(n_states))

    # if n_modalities is 1:
    #     likelihood *= spm_dot(A, obs, obs_mode=True)
    # else:
    #     for modality in range(n_modalities):
    #         likelihood *= spm_dot(A[modality], obs[modality], obs_mode=True)
    likelihood = get_joint_likelihood(A, obs, n_states)
    likelihood = np.log(likelihood + 1e-16)

    """
    =========== Step 2 ===========
        Create a flat posterior (and prior if necessary)
    """

    qs = np.empty(n_factors, dtype=object)
    for factor in range(n_factors):
        qs[factor] = np.ones(n_states[factor]) / n_states[factor]

    """
    If prior is not provided, initialise prior to be identical to posterior 
    (namely, a flat categorical distribution). Take the logarithm of it 
    (required for FPI algorithm below).
    """
    if prior is None:
        prior = np.empty(n_factors, dtype=object)
        for factor in range(n_factors):
            prior[factor] = np.log(np.ones(n_states[factor]) / n_states[factor] + 1e-16)

    """
    =========== Step 3 ===========
        Initialize initial free energy
    """
    prev_vfe = calc_free_energy(qs, prior, n_factors)

    """
    =========== Step 4 ===========
        If we have a single factor, we can just add prior and likelihood,
        otherwise we run FPI
    """

    if n_factors == 1:
        qL = spm_dot(likelihood, qs, [0])
        return softmax(qL + prior[0])

    else:
        """
        =========== Step 5 ===========
        Run the revised fixed-point iteration scheme
        """

        curr_iter = 0

        while curr_iter < num_iter and dF >= dF_tol:
            # Initialise variational free energy
            vfe = 0

            # List of orders in which marginal posteriors are sequentially 
            # multiplied into the joint likelihood: First order loops over 
            # factors starting at index = 0, second order goes in reverse
            factor_orders = [range(n_factors), range((n_factors - 1), -1, -1)]

            for factor_order in factor_orders:
                # reset the log likelihood
                L = likelihood.copy()

                # multiply each marginal onto a growing single joint distribution
                for factor in factor_order:
                    s = np.ones(np.ndim(L), dtype=int)
                    s[factor] = len(qs[factor])
                    L *= qs[factor].reshape(tuple(s))

                # now loop over factors again, and this time divide out the 
                # appropriate marginal before summing out.
                # !!! KEY DIFFERENCE BETWEEN THIS AND 'VANILLA' FPI, 
                # WHERE THE ORDER OF THE MARGINALIZATION MATTERS !!!
                for f in factor_order:
                    s = np.ones(np.ndim(L), dtype=int)
                    s[factor] = len(qs[factor])  # type: ignore

                    # divide out the factor we multiplied into X already
                    temp = L * (1.0 / qs[factor]).reshape(tuple(s))  # type: ignore
                    dims2sum = tuple(np.where(np.arange(n_factors) != f)[0])
                    qL = np.sum(temp, dims2sum)

                    temp = L * (1.0 / qs[factor]).reshape(tuple(s))  # type: ignore
                    qs[factor] = softmax(qL + prior[factor])  # type: ignore

            # calculate new free energy
            vfe = calc_free_energy(qs, prior, n_factors, likelihood)

            # stopping condition - time derivative of free energy
            dF = np.abs(prev_vfe - vfe)
            prev_vfe = vfe

            curr_iter += 1

        return qs

def run_mmp(
    lh_seq, B, policy, prev_actions=None, prior=None, num_iter=10, grad_descent=True, tau=0.25, last_timestep = False):
    """
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
    """

    # window
    past_len = len(lh_seq)
    future_len = policy.shape[0]

    if last_timestep:
        infer_len = past_len + future_len - 1
    else:
        infer_len = past_len + future_len
    
    future_cutoff = past_len + future_len - 2

    # dimensions
    _, num_states, _, num_factors = get_model_dimensions(A=None, B=B)

    # beliefs
    qs_seq = obj_array(infer_len)
    for t in range(infer_len):
        qs_seq[t] = obj_array_uniform(num_states)

    # last message
    qs_T = obj_array_zeros(num_states)

    # prior
    if prior is None:
        prior = obj_array_uniform(num_states)

    # transposed transition
    trans_B = obj_array(num_factors)
        
    for f in range(num_factors):
        trans_B[f] = spm_norm(np.swapaxes(B[f],0,1))

    if prev_actions is not None:
        policy = np.vstack((prev_actions, policy))

    for itr in range(num_iter):
        F = 0.0 # reset variational free energy (accumulated over time and factors, but reset per iteration)
        for t in range(infer_len):
            for f in range(num_factors):
                # likelihood
                if t < past_len:
                    lnA = spm_log_single(spm_dot(lh_seq[t], qs_seq[t], [f]))
                    print(f'Enumerated version: lnA at time {t}: {lnA}')    
                else:
                    lnA = np.zeros(num_states[f])
                
                # past message
                if t == 0:
                    lnB_past = spm_log_single(prior[f])
                else:
                    past_msg = B[f][:, :, int(policy[t - 1, f])].dot(qs_seq[t - 1][f])
                    lnB_past = spm_log_single(past_msg)

                # future message
                if t >= future_cutoff:
                    lnB_future = qs_T[f]
                else:
                    future_msg = trans_B[f][:, :, int(policy[t, f])].dot(qs_seq[t + 1][f])
                    lnB_future = spm_log_single(future_msg)
                
                # inference
                if grad_descent:
                    sx = qs_seq[t][f] # save this as a separate variable so that it can be used in VFE computation
                    lnqs = spm_log_single(sx)
                    coeff = 1 if (t >= future_cutoff) else 2
                    err = (coeff * lnA + lnB_past + lnB_future) - coeff * lnqs
                    lnqs = lnqs + tau * (err - err.mean()) # for numerical stability, before passing into the softmax
                    qs_seq[t][f] = softmax(lnqs)
                    if (t == 0) or (t == (infer_len-1)):
                        F += sx.dot(0.5*err)
                    else:
                        F += sx.dot(0.5*(err - (num_factors - 1)*lnA/num_factors)) # @NOTE: not sure why Karl does this in SPM_MDP_VB_X, we should look into this
                else:
                    qs_seq[t][f] = softmax(lnA + lnB_past + lnB_future)
            
            if not grad_descent:

                if t < past_len:
                    F += calc_free_energy(qs_seq[t], prior, num_factors, likelihood = spm_log_single(lh_seq[t]) )
                else:
                    F += calc_free_energy(qs_seq[t], prior, num_factors)

    return qs_seq, F

def run_mmp_factorized(
    lh_seq, mb_dict, B, B_factor_list, policy, prev_actions=None, prior=None, num_iter=10, grad_descent=True, tau=0.25, last_timestep = False):
    """
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
    """

    # window
    past_len = len(lh_seq)
    future_len = policy.shape[0]

    if last_timestep:
        infer_len = past_len + future_len - 1
    else:
        infer_len = past_len + future_len
    
    future_cutoff = past_len + future_len - 2

    # dimensions
    _, num_states, _, num_factors = get_model_dimensions(A=None, B=B)

    # beliefs
    qs_seq = obj_array(infer_len)
    for t in range(infer_len):
        qs_seq[t] = obj_array_uniform(num_states)

    # last message
    qs_T = obj_array_zeros(num_states)

    # prior
    if prior is None:
        prior = obj_array_uniform(num_states)

    # transposed transition
    trans_B = obj_array(num_factors)
        
    for f in range(num_factors):
        trans_B[f] = spm_norm(np.swapaxes(B[f],0,1))

    if prev_actions is not None:
        policy = np.vstack((prev_actions, policy))

    A_factor_list, A_modality_list = mb_dict['A_factor_list'], mb_dict['A_modality_list']

    joint_lh_seq = obj_array(len(lh_seq))
    num_modalities = len(A_factor_list)
    for t in range(len(lh_seq)):
        joint_loglikelihood = np.zeros(tuple(num_states))
        for m in range(num_modalities):
            reshape_dims = num_factors*[1]
            for _f_id in A_factor_list[m]:
                reshape_dims[_f_id] = num_states[_f_id]
            joint_loglikelihood += lh_seq[t][m].reshape(reshape_dims) # add up all the log-likelihoods after reshaping them to the global common dimensions of all hidden state factors
        joint_lh_seq[t] = joint_loglikelihood

    # compute inverse B dependencies, which is a list that for each hidden state factor, lists the indices of the other hidden state factors that it 'drives' or is a parent of in the HMM graphical model
    inv_B_deps = [[i for i, d in enumerate(B_factor_list) if f in d] for f in range(num_factors)]
    for itr in range(num_iter):
        F = 0.0 # reset variational free energy (accumulated over time and factors, but reset per iteration)
        for t in range(infer_len):
            for f in range(num_factors):
                # likelihood
                lnA = np.zeros(num_states[f])
                if t < past_len:
                    for m in A_modality_list[f]:
                        lnA += spm_log_single(spm_dot(lh_seq[t][m], qs_seq[t][A_factor_list[m]], [A_factor_list[m].index(f)]))  
                    print(f'Factorized version: lnA at time {t}: {lnA}')                
                
                # past message
                if t == 0:
                    lnB_past = spm_log_single(prior[f])
                else:
                    past_msg = spm_dot(B[f][...,int(policy[t - 1, f])], qs_seq[t-1][B_factor_list[f]])
                    lnB_past = spm_log_single(past_msg)

                # future message
                if t >= future_cutoff:
                    lnB_future = qs_T[f]
                else:
                    # list of future_msgs, one for each of the factors that factor f is driving

                    B_marg_list = [] # list of the marginalized B matrices, that correspond to mapping between the factor of interest `f` and each of its children factors `i`
                    for i in inv_B_deps[f]: #loop over all the hidden state factors that are driven by f
                        b = B[i][...,int(policy[t,i])]
                        keep_dims = (0,1+B_factor_list[i].index(f))
                        dims = []
                        idxs = []
                        for j, d in enumerate(B_factor_list[i]): # loop over the list of factors that drive each child `i` of factor-of-interest `f` (i.e. the co-parents of `f`, with respect to child `i`)
                            if f != d:
                                dims.append((1 + j,))
                                idxs.append(d)
                        xs = [qs_seq[t+1][f_i] for f_i in idxs]
                        B_marg_list.append( factor_dot_flex(b, xs, tuple(dims), keep_dims=keep_dims) ) # marginalize out all parents of `i` besides `f`

                    lnB_future = np.zeros(num_states[f])
                    for i, b in enumerate(B_marg_list):
                        b_norm_T = spm_norm(b.T)
                        lnB_future += spm_log_single(b_norm_T.dot(qs_seq[t + 1][inv_B_deps[f][i]]))
                    
                    
                    lnB_future *= 0.5
                
                # inference
                if grad_descent:
                    sx = qs_seq[t][f] # save this as a separate variable so that it can be used in VFE computation
                    lnqs = spm_log_single(sx)
                    coeff = 1 if (t >= future_cutoff) else 2
                    err = (coeff * lnA + lnB_past + lnB_future) - coeff * lnqs
                    lnqs = lnqs + tau * (err - err.mean())
                    qs_seq[t][f] = softmax(lnqs)
                    if (t == 0) or (t == (infer_len-1)):
                        F += sx.dot(0.5*err)
                    else:
                        F += sx.dot(0.5*(err - (num_factors - 1)*lnA/num_factors)) # @NOTE: not sure why Karl does this in SPM_MDP_VB_X, we should look into this
                else:
                    qs_seq[t][f] = softmax(lnA + lnB_past + lnB_future)
            
            if not grad_descent:

                if t < past_len:
                    F += calc_free_energy(qs_seq[t], prior, num_factors, likelihood = spm_log_single(joint_lh_seq[t]) )
                else:
                    F += calc_free_energy(qs_seq[t], prior, num_factors)

    return qs_seq, F

def _run_mmp_testing(
    lh_seq, B, policy, prev_actions=None, prior=None, num_iter=10, grad_descent=True, tau=0.25, last_timestep = False):
    """
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
    xn: list
        The sequence of beliefs as they're computed across iterations of marginal message passing (used for benchmarking). Nesting structure is iteration, factor, so ``xn[itr][f]`` 
        stores the ``num_states x infer_len`` array of beliefs about hidden states at different time points of inference horizon.
    vn: list
        The sequence of prediction errors as they're computed across iterations of marginal message passing (used for benchmarking). Nesting structure is iteration, factor, so ``vn[itr][f]`` 
        stores the ``num_states x infer_len`` array of prediction errors for hidden states at different time points of inference horizon.
    """

    # window
    past_len = len(lh_seq)
    future_len = policy.shape[0]

    if last_timestep:
        infer_len = past_len + future_len - 1
    else:
        infer_len = past_len + future_len
    
    future_cutoff = past_len + future_len - 2

    # dimensions
    _, num_states, _, num_factors = get_model_dimensions(A=None, B=B)

    # beliefs
    qs_seq = obj_array(infer_len)
    for t in range(infer_len):
        qs_seq[t] = obj_array_uniform(num_states)

    # last message
    qs_T = obj_array_zeros(num_states)

    # prior
    if prior is None:
        prior = obj_array_uniform(num_states)

    # transposed transition
    trans_B = obj_array(num_factors)
        
    for f in range(num_factors):
        trans_B[f] = spm_norm(np.swapaxes(B[f],0,1))

    if prev_actions is not None:
        policy = np.vstack((prev_actions, policy))

    xn = [] # list for storing beliefs across iterations
    vn = [] # list for storing prediction errors across iterations

    shape_list = [ [num_states[f], infer_len] for f in range(num_factors) ]
    
    for itr in range(num_iter):

        xn_itr_all_factors = obj_array_zeros(shape_list) # temporary cache for storing beliefs across different hidden state factors, for a fixed iteration of the belief updating scheme
        vn_itr_all_factors = obj_array_zeros(shape_list) # temporary cache for storing prediction errors across different hidden state factors, for a fixed iteration of the belief updating scheme

        F = 0.0 # reset variational free energy (accumulated over time and factors, but reset per iteration)
        for t in range(infer_len):

            if t == (infer_len - 1):
                debug_flag = True

            for f in range(num_factors):
                # likelihood
                if t < past_len:
                    # if itr == 0:
                    #     print(f'obs from timestep {t}\n')
                    lnA = spm_log_single(spm_dot(lh_seq[t], qs_seq[t], [f]))
                else:
                    lnA = np.zeros(num_states[f])
                
                # past message
                if t == 0:
                    lnB_past = spm_log_single(prior[f])
                else:
                    past_msg = B[f][:, :, int(policy[t - 1, f])].dot(qs_seq[t - 1][f])
                    lnB_past = spm_log_single(past_msg)

                # future message
                if t >= future_cutoff:
                    lnB_future = qs_T[f]
                else:
                    future_msg = trans_B[f][:, :, int(policy[t, f])].dot(qs_seq[t + 1][f])
                    lnB_future = spm_log_single(future_msg)

                # inference
                if grad_descent:
                    sx = qs_seq[t][f] # save this as a separate variable so that it can be used in VFE computation
                    lnqs = spm_log_single(sx)
                    coeff = 1 if (t >= future_cutoff) else 2
                    err = (coeff * lnA + lnB_past + lnB_future) - coeff * lnqs
                    vn_tmp = err - err.mean()
                    lnqs = lnqs + tau * vn_tmp
                    qs_seq[t][f] = softmax(lnqs)
                    if (t == 0) or (t == (infer_len-1)):
                        F += sx.dot(0.5*err)
                    else:
                        F += sx.dot(0.5*(err - (num_factors - 1)*lnA/num_factors)) # @NOTE: not sure why Karl does this in SPM_MDP_VB_X, we should look into this
                    
                    xn_itr_all_factors[f][:,t] = np.copy(qs_seq[t][f])
                    vn_itr_all_factors[f][:,t] = np.copy(vn_tmp)

                else:
                    qs_seq[t][f] = softmax(lnA + lnB_past + lnB_future)
            
            if not grad_descent:

                if t < past_len:
                    F += calc_free_energy(qs_seq[t], prior, num_factors, likelihood = spm_log_single(lh_seq[t]) )
                else:
                    F += calc_free_energy(qs_seq[t], prior, num_factors)
        xn.append(xn_itr_all_factors)
        vn.append(vn_itr_all_factors)

    return qs_seq, F, xn, vn

def run_mmp_old(
    A,
    B,
    obs_t,
    policy,
    curr_t,
    t_horizon,
    T,
    qs_bma=None,
    prior=None,
    num_iter=10,
    dF=1.0,
    dF_tol=0.001,
    previous_actions=None,
    use_gradient_descent=False,
    tau=0.25,
):
    """
    Optimise marginal posterior beliefs about hidden states using marginal message-passing scheme (MMP) developed
    by Thomas Parr and colleagues, see https://github.com/tejparr/nmpassing
   
    Parameters
    ----------
    - 'A' [numpy nd.array (matrix or tensor or array-of-arrays)]:
        Observation likelihood of the generative model, mapping from hidden states to observations. 
        Used in inference to get the likelihood of an observation, under different hidden state configurations.
    - 'B' [numpy.ndarray (tensor or array-of-arrays)]:
        Transition likelihood of the generative model, mapping from hidden states at t to hidden states at t+1.
        Used in inference to get expected future (or past) hidden states, given past (or future) hidden 
        states (or expectations thereof).
    - 'obs_t' [list of length t_horizon of numpy 1D array or array of arrays (with 1D numpy array entries)]:
        Sequence of observations sampled from beginning of time horizon the current timestep t. 
        The first observation (the start of the time horizon) is either the first timestep of the generative 
        process or the first timestep of the policy horizon (whichever is closer to 'curr_t' in time).
        The observations over time are stored as a list of numpy arrays, where in case of multi-modalities 
        each numpy array is an array-of-arrays, with one 1D numpy.ndarray for each modality. 
        In the case of a single modality, each observation is a single 1D numpy.ndarray.
    - 'policy' [2D np.ndarray]:
        Array of actions constituting a single policy. Policy is a shape 
        (n_steps, n_control_factors) numpy.ndarray, the values of which indicate actions along a given control 
        factor (column index) at a given timestep (row index).
    - 'curr_t' [int]:
        Current timestep (relative to the 'absolute' time of the generative process).
    - 't_horizon'[int]:
        Temporal horizon of inference for states and policies.
    - 'T' [int]:
        Temporal horizon of the generative process (absolute time)
    - `qs_bma` [numpy 1D array, array of arrays (with 1D numpy array entries) or None]:
    - 'prior' [numpy 1D array, array of arrays (with 1D numpy array entries) or None]:
        Prior beliefs of the agent at the beginning of the time horizon, to be integrated 
        with the marginal likelihood to obtain posterior at the first timestep.
        If absent, prior is set to be a uniform distribution over hidden states (identical to the 
        initialisation of the posterior.
    -'num_iter' [int]:
        Number of variational iterations to run. (optional)
    -'dF' [float]:
        Starting free energy gradient (dF/dt) before updating in the course of gradient descent. (optional)
    -'dF_tol' [float]:
        Threshold value of the gradient of the variational free energy (dF/dt), to be checked 
        at each iteration. If dF <= dF_tol, the iterations are halted pre-emptively and the final 
        marginal posterior belief(s) is(are) returned.  (optional)
    -'previous_actions' [numpy.ndarray with shape (num_steps, n_control_factors) or None]:
        Array of previous actions, which can be used to constrain the 'past' messages in inference 
        to only consider states of affairs that were possible under actions that are known to have been taken. 
        The first dimension of previous-arrays (previous_actions.shape[0]) encodes how far back in time the agent is 
        considering. The first timestep of this either corresponds to either the first timestep of the generative 
        process or the first timestep of the policy horizon (whichever is sooner in time).  (optional)
    -'use_gradient_descent' [bool]:
        Flag to indicate whether to use gradient descent to optimise posterior beliefs.
    -'tau' [float]:
        Learning rate for gradient descent (only used if use_gradient_descent is True)
 
  
    Returns
    ----------
    -'qs' [list of length T of numpy 1D arrays or array of arrays (with 1D numpy array entries):
        Marginal posterior beliefs over hidden states (single- or multi-factor) achieved 
        via marginal message pasing
    -'qss' [list of lists of length T of numpy 1D arrays or array of arrays (with 1D numpy array entries):
        Marginal posterior beliefs about hidden states (single- or multi-factor) held at 
        each timepoint, *about* each timepoint of the observation
        sequence
    -'F' [2D np.ndarray]:
        Variational free energy of beliefs about hidden states, indexed by time point and variational iteration
    -'F_pol' [float]:
        Total free energy of the policy under consideration.
    """

    # get temporal window for inference
    min_time = max(0, curr_t - t_horizon)
    max_time = min(T, curr_t + t_horizon)
    window_idxs = np.array([t for t in range(min_time, max_time)])
    window_len = len(window_idxs)
    # TODO: needs a better name - the point at which we ignore future messages
    future_cutoff = window_len - 1
    inference_len = window_len + 1
    obs_seq_len = len(obs_t)

    # get relevant observations, given our current time point
    if curr_t == 0:
        obs_range = [0]
    else:
        min_obs_idx = max(0, curr_t - t_horizon)
        max_obs_idx = curr_t + 1
        obs_range = range(min_obs_idx, max_obs_idx)

    # get model dimensions
    # TODO: make a general function in `utils` for extracting model dimensions
    if utils.is_obj_array(obs_t[0]):
        num_obs = [obs.shape[0] for obs in obs_t[0]]
    else:
        num_obs = [obs_t[0].shape[0]]

    if utils.is_obj_array(B):
        num_states = [b.shape[0] for b in B]
    else:
        num_states = [B[0].shape[0]]
        B = utils.to_obj_array(B)

    num_modalities = len(num_obs)
    num_factors = len(num_states)

    """
    =========== Step 1 ===========
        Calculate likelihood
        Loop over modalities and use assumption of independence among observation modalities
        to combine each modality-specific likelihood into a single joint likelihood over hidden states 
    """

    # likelihood of observations under configurations of hidden states (over time)
    likelihood = np.empty(len(obs_range), dtype=object)
    for t, obs in enumerate(obs_range):
        # likelihood_t = np.ones(tuple(num_states))

        # if num_modalities == 1:
        #     likelihood_t *= spm_dot(A[0], obs_t[obs], obs_mode=True)
        # else:
        #     for modality in range(num_modalities):
        #         likelihood_t *= spm_dot(A[modality], obs_t[obs][modality], obs_mode=True)
        
        likelihood_t = get_joint_likelihood(A, obs_t, num_states)

        # The Thomas Parr MMP version, you log the likelihood first
        # likelihood[t] = np.log(likelihood_t + 1e-16)

        # Karl SPM version, logging doesn't happen until *after* the dotting with the posterior
        likelihood[t] = likelihood_t

    """
    =========== Step 2 ===========
        Initialise a flat posterior (and prior if necessary)
        If a prior is not provided, initialise a uniform prior
    """

    qs = [np.empty(num_factors, dtype=object) for i in range(inference_len)]

    for t in range(inference_len):
        # if t == window_len:
        #     # final message is zeros - has no effect on inference
        #     # TODO: this may be redundant now that we skip last step
        #     for f in range(num_factors):
        #         qs[t][f] = np.zeros(num_states[f])
        # else:
            # for f in range(num_factors):
            #     qs[t][f] = np.ones(num_states[f]) / num_states[f]
        for f in range(num_factors):
                qs[t][f] = np.ones(num_states[f]) / num_states[f]

    if prior is None:
        prior = np.empty(num_factors, dtype=object)
        for f in range(num_factors):
            prior[f] = np.ones(num_states[f]) / num_states[f]

    """ 
    =========== Step 3 ===========
        Create a normalized transpose of the transition distribution `B_transposed`
        Used for computing backwards messages 'from the future'
    """

    B_transposed = np.empty(num_factors, dtype=object)
    for f in range(num_factors):
        B_transposed[f] = np.zeros_like(B[f])
        for u in range(B[f].shape[2]):
            B_transposed[f][:, :, u] = spm_norm(B[f][:, :, u].T)

    # zero out final message
    # TODO: may be redundant now we skip final step
    last_message = np.empty(num_factors, dtype=object)
    for f in range(num_factors):
        last_message[f] = np.zeros(num_states[f])

    # if previous actions not given, zero out to stop any influence on inference
    if previous_actions is None:
        previous_actions = np.zeros((1, policy.shape[1]))

    full_policy = np.vstack((previous_actions, policy))

    # print(full_policy.shape)

    """
    =========== Step 3 ===========
        Loop over time indices of time window, updating posterior as we go
        This includes past time steps and future time steps
    """

    qss = [[] for i in range(num_iter)]
    free_energy = np.zeros((len(qs), num_iter))
    free_energy_pol = 0.0

    # print(obs_seq_len)

    print('Full policy history')
    print('------------------')
    print(full_policy)

    for n in range(num_iter):
        for t in range(inference_len):

            lnB_past_tensor = np.empty(num_factors, dtype=object)
            for f in range(num_factors):

                # if t == 0 and n == 0:
                #     print(f"qs at time t = {t}, factor f = {f}, iteration i = {n}: {qs[t][f]}")

                """
                =========== Step 3.a ===========
                    Calculate likelihood
                """
                if t < len(obs_range):
                    # if t < len(obs_seq_len):
                    # Thomas Parr MMP version
                    # lnA = spm_dot(likelihood[t], qs[t], [f])

                    # Karl SPM version
                    lnA = np.log(spm_dot(likelihood[t], qs[t], [f]) + 1e-16)
                else:
                    lnA = np.zeros(num_states[f])

                if t == 1 and n == 0:
                    # pass
                    print(f"lnA at time t = {t}, factor f = {f}, iteration i = {n}: {lnA}")

                # print(f"lnA at time t = {t}, factor f = {f}, iteration i = {n}: {lnA}")

                """
                =========== Step 3.b ===========
                    Calculate past message
                """
                if t == 0 and window_idxs[0] == 0:
                    lnB_past = np.log(prior[f] + 1e-16)
                else:
                    # Thomas Parr MMP version
                    # lnB_past = 0.5 * np.log(B[f][:, :, full_policy[t - 1, f]].dot(qs[t - 1][f]) + 1e-16)

                    # Karl SPM version
                    if t == 1 and n == 0 and f == 1:
                        print('past action:')
                        print('-------------')
                        print(full_policy[t - 1, :])
                        print(B[f][:,:,0])
                        print(B[f][:,:,1])
                        print(qs[t - 1][f])
                    lnB_past = np.log(B[f][:, :, full_policy[t - 1, f]].dot(qs[t - 1][f]) + 1e-16)
                    # if t == 0:
                    # print(
                    # f"qs_t_1 at time t = {t}, factor f = {f}, iteration i = {n}: {qs[t - 1][f]}"
                    # )

                if t == 1 and n == 0:
                    print(
                        f"lnB_past at time t = {t}, factor f = {f}, iteration i = {n}: {lnB_past}"
                    )

                """
                =========== Step 3.c ===========
                    Calculate future message
                """
                if t >= future_cutoff:
                    # TODO: this is redundant - not used in code
                    lnB_future = last_message[f]
                else:
                    # Thomas Parr MMP version
                    # B_future = B_transposed[f][:, :, int(full_policy[t, f])].dot(qs[t + 1][f])
                    # lnB_future = 0.5 * np.log(B_future + 1e-16)

                    # Karl Friston SPM version
                    B_future = B_transposed[f][:, :, int(full_policy[t, f])].dot(qs[t + 1][f])
                    lnB_future = np.log(B_future + 1e-16)
                
                # Thomas Parr MMP version
                # lnB_past_tensor[f] = 2 * lnBpast
                # Karl SPM version
                lnB_past_tensor[f] = lnB_past

                """
                =========== Step 3.d ===========
                    Update posterior
                """
                if use_gradient_descent:
                    lns = np.log(qs[t][f] + 1e-16)

                    # Thomas Parr MMP version
                    # error = (lnA + lnBpast + lnBfuture) - lns

                    # Karl SPM version
                    if t >= future_cutoff:
                        error = lnA + lnB_past - lns

                    else:
                        error = (2 * lnA + lnB_past + lnB_future) - 2 * lns
                        

                    # print(f"prediction error at time t = {t}, factor f = {f}, iteration i = {n}: {error}")
                    # print(f"OG {t} {f} {error}")
                    error -= error.mean()
                    lns = lns + tau * error
                    qs_t_f = softmax(lns)
                    free_energy_pol += 0.5 * qs[t][f].dot(error)
                    qs[t][f] = qs_t_f
                else:
                    qs[t][f] = softmax(lnA + lnB_past + lnB_future)

            # TODO: probably works anyways
            # free_energy[t, n] = calc_free_energy(qs[t], lnB_past_tensor, num_factors, likelihood[t])
            # free_energy_pol += F[t, n]
        qss[n].append(qs)

    return qs, qss, free_energy, free_energy_pol

def get_marginals(q_pi, policies, num_controls):
    """
    Computes the marginal posterior(s) over actions by integrating their posterior probability under the policies that they appear within.

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
    
    Returns
    ----------
    action_marginals: ``list`` of ``jax.numpy.ndarrays``
       List of arrays corresponding to marginal probability of each action possible action
    """
    num_factors = len(num_controls)    

    action_marginals = []
    for factor_i in range(num_factors):
        actions = jnp.arange(num_controls[factor_i])[:, None]
        action_marginals.append(jnp.where(actions==policies[:, 0, factor_i], q_pi, 0).sum(-1))
    
    return action_marginals

def sample_action(policies, num_controls, q_pi, action_selection="deterministic", alpha=16.0, rng_key=None):
    """
    Samples an action from posterior marginals, one action per control factor.

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
        String indicating whether whether the selected action is chosen as the maximum of the posterior over actions,
        or whether it's sampled from the posterior marginal over actions
    alpha: float, default 16.0
        Action selection precision -- the inverse temperature of the softmax that is used to scale the 
        action marginals before sampling. This is only used if ``action_selection`` argument is "stochastic"

    Returns
    ----------
    selected_policy: 1D ``numpy.ndarray``
        Vector containing the indices of the actions for each control factor
    """

    marginal = get_marginals(q_pi, policies, num_controls)
    
    if action_selection == 'deterministic':
        selected_policy = jtu.tree_map(lambda x: jnp.argmax(x, -1), marginal)
    elif action_selection == 'stochastic':
        logits = lambda x: alpha * log_stable(x)
        selected_policy = jtu.tree_map(lambda x: jr.categorical(rng_key, logits(x)), marginal)
    else:
        raise NotImplementedError

    return jnp.array(selected_policy)

def sample_policy(policies, q_pi, action_selection="deterministic", alpha = 16.0, rng_key=None):

    if action_selection == "deterministic":
        policy_idx = jnp.argmax(q_pi)
    elif action_selection == "stochastic":
        log_p_policies = log_stable(q_pi) * alpha
        policy_idx = jr.categorical(rng_key, log_p_policies)

    selected_multiaction = policies[policy_idx, 0]
    return selected_multiaction

def construct_policies(num_states, num_controls = None, policy_len=1, control_fac_idx=None):
    """
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
    """

    num_factors = len(num_states)
    if control_fac_idx is None:
        if num_controls is not None:
            control_fac_idx = [f for f, n_c in enumerate(num_controls) if n_c > 1]
        else:
            control_fac_idx = list(range(num_factors))

    if num_controls is None:
        num_controls = [num_states[c_idx] if c_idx in control_fac_idx else 1 for c_idx in range(num_factors)]
        
    x = num_controls * policy_len
    policies = list(itertools.product(*[list(range(i)) for i in x]))
    
    for pol_i in range(len(policies)):
        policies[pol_i] = jnp.array(policies[pol_i]).reshape(policy_len, num_factors)

    return jnp.stack(policies)

def update_posterior_policies(policy_matrix, qs_init, A, B, C, E, pA, pB, A_dependencies, B_dependencies, gamma=16.0, use_utility=True, use_states_info_gain=True, use_param_info_gain=False):
    # policy --> n_levels_factor_f x 1
    # factor --> n_levels_factor_f x n_policies
    ## vmap across policies
    compute_G_fixed_states = partial(compute_G_policy, qs_init, A, B, C, pA, pB, A_dependencies, B_dependencies,
                                     use_utility=use_utility, use_states_info_gain=use_states_info_gain, use_param_info_gain=use_param_info_gain)

    # only in the case of policy-dependent qs_inits
    # in_axes_list = (1,) * n_factors
    # all_efe_of_policies = vmap(compute_G_policy, in_axes=(in_axes_list, 0))(qs_init_pi, policy_matrix)

    # policies needs to be an NDarray of shape (n_policies, n_timepoints, n_control_factors)
    neg_efe_all_policies = vmap(compute_G_fixed_states)(policy_matrix)

    return nn.softmax(gamma * neg_efe_all_policies + log_stable(E)), neg_efe_all_policies

def compute_expected_state(qs_prior, B, u_t, B_dependencies=None): 
    """
    Compute posterior over next state, given belief about previous state, transition model and action...
    """
    #Note: this algorithm is only correct if each factor depends only on itself. For any interactions, 
    # we will have empirical priors with codependent factors. 
    assert len(u_t) == len(B)  
    qs_next = []
    for B_f, u_f, deps in zip(B, u_t, B_dependencies):
        relevant_factors = [qs_prior[idx] for idx in deps]
        qs_next_f = factor_dot(B_f[...,u_f], relevant_factors, keep_dims=(0,))
        qs_next.append(qs_next_f)
        
    # P(s'|s, u) = \sum_{s, u} P(s'|s) P(s|u) P(u|pi)P(pi) because u </-> pi
    return qs_next

def compute_expected_state_and_Bs(qs_prior, B, u_t): 
    """
    Compute posterior over next state, given belief about previous state, transition model and action...
    """
    assert len(u_t) == len(B)  
    qs_next = []
    Bs = []
    for qs_f, B_f, u_f in zip(qs_prior, B, u_t):
        qs_next.append( B_f[..., u_f].dot(qs_f) )
        Bs.append(B_f[..., u_f])
    
    return qs_next, Bs

def compute_expected_obs(qs, A, A_dependencies):
    """
    New version of expected observation (computation of Q(o|pi)) that takes into account sparse dependencies between observation
    modalities and hidden state factors
    """
        
    def compute_expected_obs_modality(A_m, m):
        deps = A_dependencies[m]
        relevant_factors = [qs[idx] for idx in deps]
        return factor_dot(A_m, relevant_factors, keep_dims=(0,))

    return jtu.tree_map(compute_expected_obs_modality, A, list(range(len(A))))

def compute_info_gain(qs, qo, A, A_dependencies):
    """
    New version of expected information gain that takes into account sparse dependencies between observation modalities and hidden state factors.
    """

    def compute_info_gain_for_modality(qo_m, A_m, m):
        H_qo = stable_entropy(qo_m)
        H_A_m = - stable_xlogx(A_m).sum(0)
        deps = A_dependencies[m]
        relevant_factors = [qs[idx] for idx in deps]
        qs_H_A_m = factor_dot(H_A_m, relevant_factors)
        return H_qo - qs_H_A_m
    
    info_gains_per_modality = jtu.tree_map(compute_info_gain_for_modality, qo, A, list(range(len(A))))
        
    return jtu.tree_reduce(lambda x,y: x+y, info_gains_per_modality)

def compute_expected_utility(t, qo, C):
    
    util = 0.
    for o_m, C_m in zip(qo, C):
        if C_m.ndim > 1:
            util += (o_m * C_m[t]).sum()
        else:
            util += (o_m * C_m).sum()
    
    return util

def calc_pA_info_gain(pA, qo, qs, A_dependencies):
    """
    Compute expected Dirichlet information gain about parameters ``pA`` for a given posterior predictive distribution over observations ``qo`` and states ``qs``.

    Parameters
    ----------
    pA: ``numpy.ndarray`` of dtype object
        Dirichlet parameters over observation model (same shape as ``A``)
    qo: ``list`` of ``numpy.ndarray`` of dtype object
        Predictive posterior beliefs over observations; stores the beliefs about
        observations expected under the policy at some arbitrary time ``t``
    qs: ``list`` of ``numpy.ndarray`` of dtype object
        Predictive posterior beliefs over hidden states, stores the beliefs about
        hidden states expected under the policy at some arbitrary time ``t``

    Returns
    -------
    infogain_pA: float
        Surprise (about Dirichlet parameters) expected for the pair of posterior predictive distributions ``qo`` and ``qs``
    """

    def infogain_per_modality(pa_m, qo_m, m):
        wa_m = spm_wnorm(pa_m) * (pa_m > 0.)
        fd = factor_dot(wa_m, [s for f, s in enumerate(qs) if f in A_dependencies[m]], keep_dims=(0,))[..., None]
        return qo_m.dot(fd)

    pA_infogain_per_modality = jtu.tree_map(
        infogain_per_modality, pA, qo, list(range(len(qo)))
    )
    
    infogain_pA = jtu.tree_reduce(lambda x, y: x + y, pA_infogain_per_modality)
    return infogain_pA.squeeze(-1)

def calc_pB_info_gain(pB, qs_t, qs_t_minus_1, B_dependencies, u_t_minus_1):
    """
    Compute expected Dirichlet information gain about parameters ``pB`` under a given policy

    Parameters
    ----------
    pB: ``Array`` of dtype object
        Dirichlet parameters over transition model (same shape as ``B``)
    qs_t: ``list`` of ``Array`` of dtype object
        Predictive posterior beliefs over hidden states expected under the policy at time ``t``
    qs_t_minus_1: ``list`` of ``Array`` of dtype object
        Posterior over hidden states at time ``t-1`` (before receiving observations)
    u_t_minus_1: "Array"
        Actions in time step t-1 for each factor

    Returns
    -------
    infogain_pB: float
        Surprise (about Dirichlet parameters) expected under the policy in question
    """
    
    wB = lambda pb:  spm_wnorm(pb) * (pb > 0.)
    fd = lambda x, i: factor_dot(x, [s for f, s in enumerate(qs_t_minus_1) if f in B_dependencies[i]], keep_dims=(0,))[..., None]
    
    pB_infogain_per_factor = jtu.tree_map(lambda pb, qs, f: qs.dot(fd(wB(pb[..., u_t_minus_1[f]]), f)), pB, qs_t, list(range(len(qs_t))))
    infogain_pB = jtu.tree_reduce(lambda x, y: x + y, pB_infogain_per_factor)[0]
    return infogain_pB

def compute_G_policy(qs_init, A, B, C, pA, pB, A_dependencies, B_dependencies, policy_i, use_utility=True, use_states_info_gain=True, use_param_info_gain=False):
    """ Write a version of compute_G_policy that does the same computations as `compute_G_policy` but using `lax.scan` instead of a for loop. """

    def scan_body(carry, t):

        qs, neg_G = carry

        qs_next = compute_expected_state(qs, B, policy_i[t], B_dependencies)

        qo = compute_expected_obs(qs_next, A, A_dependencies)

        info_gain = compute_info_gain(qs_next, qo, A, A_dependencies) if use_states_info_gain else 0.

        utility = compute_expected_utility(qo, C) if use_utility else 0.

        param_info_gain = calc_pA_info_gain(pA, qo, qs_next) if use_param_info_gain else 0.
        param_info_gain += calc_pB_info_gain(pB, qs_next, qs, policy_i[t]) if use_param_info_gain else 0.

        neg_G += info_gain + utility + param_info_gain

        return (qs_next, neg_G), None

    qs = qs_init
    neg_G = 0.
    final_state, _ = lax.scan(scan_body, (qs, neg_G), jnp.arange(policy_i.shape[0]))
    qs_final, neg_G = final_state
    return neg_G

def compute_G_policy_inductive(qs_init, A, B, C, pA, pB, A_dependencies, B_dependencies, I, policy_i, inductive_epsilon=1e-3, use_utility=True, use_states_info_gain=True, use_param_info_gain=False, use_inductive=False):
    """ 
    Write a version of compute_G_policy that does the same computations as `compute_G_policy` but using `lax.scan` instead of a for loop.
    This one further adds computations used for inductive planning.
    """

    def scan_body(carry, t):

        qs, neg_G = carry

        qs_next = compute_expected_state(qs, B, policy_i[t], B_dependencies)

        qo = compute_expected_obs(qs_next, A, A_dependencies)

        info_gain = compute_info_gain(qs_next, qo, A, A_dependencies) if use_states_info_gain else 0.

        utility = compute_expected_utility(t, qo, C) if use_utility else 0.

        inductive_value = calc_inductive_value_t(qs_init, qs_next, I, epsilon=inductive_epsilon) if use_inductive else 0.

        param_info_gain = 0.
        if pA is not None:
            param_info_gain += calc_pA_info_gain(pA, qo, qs_next, A_dependencies) if use_param_info_gain else 0.
        if pB is not None:
            param_info_gain += calc_pB_info_gain(pB, qs_next, qs, B_dependencies, policy_i[t]) if use_param_info_gain else 0.

        neg_G += info_gain + utility - param_info_gain + inductive_value

        return (qs_next, neg_G), None

    qs = qs_init
    neg_G = 0.
    final_state, _ = lax.scan(scan_body, (qs, neg_G), jnp.arange(policy_i.shape[0]))
    _, neg_G = final_state
    return neg_G

def update_posterior_policies_inductive(policy_matrix, qs_init, A, B, C, E, pA, pB, A_dependencies, B_dependencies, I, gamma=16.0, inductive_epsilon=1e-3, use_utility=True, use_states_info_gain=True, use_param_info_gain=False, use_inductive=True):
    # policy --> n_levels_factor_f x 1
    # factor --> n_levels_factor_f x n_policies
    ## vmap across policies
    compute_G_fixed_states = partial(compute_G_policy_inductive, qs_init, A, B, C, pA, pB, A_dependencies, B_dependencies, I, inductive_epsilon=inductive_epsilon,
                                     use_utility=use_utility,  use_states_info_gain=use_states_info_gain, use_param_info_gain=use_param_info_gain, use_inductive=use_inductive)

    # only in the case of policy-dependent qs_inits
    # in_axes_list = (1,) * n_factors
    # all_efe_of_policies = vmap(compute_G_policy, in_axes=(in_axes_list, 0))(qs_init_pi, policy_matrix)

    # policies needs to be an NDarray of shape (n_policies, n_timepoints, n_control_factors)
    neg_efe_all_policies = vmap(compute_G_fixed_states)(policy_matrix)

    return nn.softmax(gamma * neg_efe_all_policies + log_stable(E)), neg_efe_all_policies

def generate_I_matrix(H: List[Array], B: List[Array], threshold: float, depth: int):
    """ 
    Generates the `I` matrices used in inductive planning. These matrices stores the probability of reaching the goal state backwards from state j (columns) after i (rows) steps.
    Parameters
    ----------    
    H: ``list`` of ``jax.numpy.ndarray``
        Constraints over desired states (1 if you want to reach that state, 0 otherwise)
    B: ``list`` of ``jax.numpy.ndarray``
        Dynamics likelihood mapping or 'transition model', mapping from hidden states at ``t`` to hidden states at ``t+1``, given some control state ``u``.
        Each element ``B[f]`` of this object array stores a 3-D tensor for hidden state factor ``f``, whose entries ``B[f][s, v, u]`` store the probability
        of hidden state level ``s`` at the current time, given hidden state level ``v`` and action ``u`` at the previous time.
    threshold: ``float``
        The threshold for pruning transitions that are below a certain probability
    depth: ``int``
        The temporal depth of the backward induction

    Returns
    ----------
    I: ``numpy.ndarray`` of dtype object
        For each state factor, contains a 2D ``numpy.ndarray`` whose element i,j yields the probability 
        of reaching the goal state backwards from state j after i steps.
    """
    
    num_factors = len(H)
    I = []
    for f in range(num_factors):
        """
        For each factor, we need to compute the probability of reaching the goal state
        """

        # If there exists an action that allows transitioning 
        # from state to next_state, with probability larger than threshold
        # set b_reachable[current_state, previous_state] to 1
        b_reachable = jnp.where(B[f] > threshold, 1.0, 0.0).sum(axis=-1)
        b_reachable = jnp.where(b_reachable > 0., 1.0, 0.0)

        def step_fn(carry, i):
            I_prev = carry
            I_next = jnp.dot(b_reachable, I_prev)
            I_next = jnp.where(I_next > 0.1, 1.0, 0.0) # clamp I_next to 1.0 if it's above 0.1, 0 otherwise
            return I_next, I_next
    
        _, I_f = lax.scan(step_fn, H[f], jnp.arange(depth-1))
        I_f = jnp.concatenate([H[f][None,...], I_f], axis=0)

        I.append(I_f)
    
    return I

def calc_inductive_value_t(qs, qs_next, I, epsilon=1e-3):
    """
    Computes the inductive value of a state at a particular time (translation of @tverbele's `numpy` implementation of inductive planning, formerly
    called `calc_inductive_cost`).

    Parameters
    ----------
    qs: ``list`` of ``jax.numpy.ndarray`` 
        Marginal posterior beliefs over hidden states at a given timepoint.
    qs_next: ```list`` of ``jax.numpy.ndarray`` 
        Predictive posterior beliefs over hidden states expected under the policy.
    I: ``numpy.ndarray`` of dtype object
        For each state factor, contains a 2D ``numpy.ndarray`` whose element i,j yields the probability 
        of reaching the goal state backwards from state j after i steps.
    epsilon: ``float``
        Value that tunes the strength of the inductive value (how much it contributes to the expected free energy of policies)

    Returns
    -------
    inductive_val: float
        Value (negative inductive cost) of visiting this state using backwards induction under the policy in question
    """
    
    # initialise inductive value
    inductive_val = 0.

    log_eps = log_stable(epsilon)
    for f in range(len(qs)):
        # we also assume precise beliefs here?!
        idx = jnp.argmax(qs[f])
        # m = arg max_n p_n < sup p

        # i.e. find first entry at which I_idx equals 1, and then m is the index before that
        m = jnp.maximum(jnp.argmax(I[f][:, idx])-1, 0)
        I_m = (1. - I[f][m, :]) * log_eps
        path_available = jnp.clip(I[f][:, idx].sum(0), min=0, max=1) # if there are any 1's at all in that column of I, then this == 1, otherwise 0
        inductive_val += path_available * I_m.dot(qs_next[f]) # scaling by path_available will nullify the addition of inductive value in the case we find no path to goal (i.e. when no goal specified)

    return inductive_val

def compute_expected_obs_modality(A_m, m):
        deps = A_dependencies[m]
        relevant_factors = [qs[idx] for idx in deps]
        return factor_dot(A_m, relevant_factors, keep_dims=(0,))

def compute_info_gain_for_modality(qo_m, A_m, m):
        H_qo = stable_entropy(qo_m)
        H_A_m = - stable_xlogx(A_m).sum(0)
        deps = A_dependencies[m]
        relevant_factors = [qs[idx] for idx in deps]
        qs_H_A_m = factor_dot(H_A_m, relevant_factors)
        return H_qo - qs_H_A_m

def infogain_per_modality(pa_m, qo_m, m):
        wa_m = spm_wnorm(pa_m) * (pa_m > 0.)
        fd = factor_dot(wa_m, [s for f, s in enumerate(qs) if f in A_dependencies[m]], keep_dims=(0,))[..., None]
        return qo_m.dot(fd)

def scan_body(carry, t):

        qs, neg_G = carry

        qs_next = compute_expected_state(qs, B, policy_i[t], B_dependencies)

        qo = compute_expected_obs(qs_next, A, A_dependencies)

        info_gain = compute_info_gain(qs_next, qo, A, A_dependencies) if use_states_info_gain else 0.

        utility = compute_expected_utility(qo, C) if use_utility else 0.

        param_info_gain = calc_pA_info_gain(pA, qo, qs_next) if use_param_info_gain else 0.
        param_info_gain += calc_pB_info_gain(pB, qs_next, qs, policy_i[t]) if use_param_info_gain else 0.

        neg_G += info_gain + utility + param_info_gain

        return (qs_next, neg_G), None

def scan_body(carry, t):

        qs, neg_G = carry

        qs_next = compute_expected_state(qs, B, policy_i[t], B_dependencies)

        qo = compute_expected_obs(qs_next, A, A_dependencies)

        info_gain = compute_info_gain(qs_next, qo, A, A_dependencies) if use_states_info_gain else 0.

        utility = compute_expected_utility(t, qo, C) if use_utility else 0.

        inductive_value = calc_inductive_value_t(qs_init, qs_next, I, epsilon=inductive_epsilon) if use_inductive else 0.

        param_info_gain = 0.
        if pA is not None:
            param_info_gain += calc_pA_info_gain(pA, qo, qs_next, A_dependencies) if use_param_info_gain else 0.
        if pB is not None:
            param_info_gain += calc_pB_info_gain(pB, qs_next, qs, B_dependencies, policy_i[t]) if use_param_info_gain else 0.

        neg_G += info_gain + utility - param_info_gain + inductive_value

        return (qs_next, neg_G), None

def step_fn(carry, i):
            I_prev = carry
            I_next = jnp.dot(b_reachable, I_prev)
            I_next = jnp.where(I_next > 0.1, 1.0, 0.0) # clamp I_next to 1.0 if it's above 0.1, 0 otherwise
            return I_next, I_next

def norm_dist(dist: Tensor) -> Tensor:
    """ Normalizes a Categorical probability distribution"""
    return dist/dist.sum(0)

def list_array_uniform(shape_list: ShapeList) -> Vector:
    """ 
    Creates a list of jax arrays representing uniform Categorical
    distributions with shapes given by shape_list[i]. The shapes (elements of shape_list)
    can either be tuples or lists.
    """
    arr = []
    for shape in shape_list:
        arr.append( norm_dist(jnp.ones(shape)) )
    return arr

def list_array_zeros(shape_list: ShapeList) -> Vector:
    """ 
    Creates a list of 1-D jax arrays filled with zeros, with shapes given by shape_list[i]
    """
    arr = []
    for shape in shape_list:
        arr.append( jnp.zeros(shape) )
    return arr

def list_array_scaled(shape_list: ShapeList, scale: float=1.0) -> Vector:
    """ 
    Creates a list of 1-D jax arrays filled with scale, with shapes given by shape_list[i]
    """
    arr = []
    for shape in shape_list:
        arr.append( scale * jnp.ones(shape) )
    
    return arr

def evolve_trials(agent, data):

    def step_fn(carry, xs):
        empirical_prior = carry
        outcomes = xs['outcomes']
        qs = agent.infer_states(outcomes, empirical_prior)
        q_pi, _ = agent.infer_policies(qs)

        probs = agent.action_probabilities(q_pi)

        actions = xs['actions']
        empirical_prior = agent.update_empirical_prior(actions, qs)
        #TODO: if outcomes and actions are None, generate samples
        return empirical_prior, (probs, outcomes, actions)

    prior = agent.D
    _, res = lax.scan(step_fn, prior, data)

    return res

def aif_likelihood(Nb, Nt, Na, data, agent):
    # Na -> batch dimension - number of different subjects/agents
    # Nb -> number of experimental blocks
    # Nt -> number of trials within each block

    def step_fn(carry, xs):
        probs, outcomes, actions = evolve_trials(agent, xs)

        deterministic('outcomes', outcomes)

        with plate('num_agents', Na):
            with plate('num_trials', Nt):
                sample('actions', dist.Categorical(logits=probs).to_event(1), obs=actions)
        
        return None, None
    
    # TODO: See if some information has to be passed from one block to the next and change init and carry accordingly
    init = None
    scan(step_fn, init, data, length=Nb)

def step_fn(carry, xs):
        empirical_prior = carry
        outcomes = xs['outcomes']
        qs = agent.infer_states(outcomes, empirical_prior)
        q_pi, _ = agent.infer_policies(qs)

        probs = agent.action_probabilities(q_pi)

        actions = xs['actions']
        empirical_prior = agent.update_empirical_prior(actions, qs)
        #TODO: if outcomes and actions are None, generate samples
        return empirical_prior, (probs, outcomes, actions)

def step_fn(carry, xs):
        probs, outcomes, actions = evolve_trials(agent, xs)

        deterministic('outcomes', outcomes)

        with plate('num_agents', Na):
            with plate('num_trials', Nt):
                sample('actions', dist.Categorical(logits=probs).to_event(1), obs=actions)
        
        return None, None

def add(x, y):
    return x + y

def marginal_log_likelihood(qs, log_likelihood, i):
    xs = [q for j, q in enumerate(qs) if j != i]
    return factor_dot(log_likelihood, xs, keep_dims=(i,))

def all_marginal_log_likelihood(qs, log_likelihoods, all_factor_lists):
    qL_marginals = jtu.tree_map(lambda ll_m, factor_list_m: mll_factors(qs, ll_m, factor_list_m), log_likelihoods, all_factor_lists)
    
    num_factors = len(qs)

    # insted of a double loop we could have a list defining m to f mapping
    # which could be resolved with a single tree_map cast
    qL_all = [jnp.zeros(1)] * num_factors
    for m, factor_list_m in enumerate(all_factor_lists):
        for l, f in enumerate(factor_list_m):
            qL_all[f] += qL_marginals[m][l]

    return qL_all

def mll_factors(qs, ll_m, factor_list_m) -> List:
    relevant_factors = [qs[f] for f in factor_list_m]
    marginal_ll_f = jtu.Partial(marginal_log_likelihood, relevant_factors, ll_m)
    loc_nf = len(factor_list_m)
    loc_factors = list(range(loc_nf))
    return jtu.tree_map(marginal_ll_f, loc_factors)

def run_vanilla_fpi(A, obs, prior, num_iter=1, distr_obs=True):
    """ Vanilla fixed point iteration (jaxified) """

    nf = len(prior)
    factors = list(range(nf))
    # Step 1: Compute log likelihoods for each factor
    ll = compute_log_likelihood(obs, A, distr_obs=distr_obs)
    # log_likelihoods = [ll] * nf

    # Step 2: Map prior to log space and create initial log-posterior
    log_prior = jtu.tree_map(log_stable, prior)
    log_q = jtu.tree_map(jnp.zeros_like, prior)

    # Step 3: Iterate until convergence
    def scan_fn(carry, t):
        log_q = carry
        q = jtu.tree_map(nn.softmax, log_q)
        mll = jtu.Partial(marginal_log_likelihood, q, ll)
        marginal_ll = jtu.tree_map(mll, factors)
        log_q = jtu.tree_map(add, marginal_ll, log_prior)

        return log_q, None

    res, _ = lax.scan(scan_fn, log_q, jnp.arange(num_iter))

    # Step 4: Map result to factorised posterior
    qs = jtu.tree_map(nn.softmax, res)
    return qs

def run_factorized_fpi(A, obs, prior, A_dependencies, num_iter=1):
    """
    Run the fixed point iteration algorithm with sparse dependencies between factors and outcomes (stored in `A_dependencies`)
    """

    # Step 1: Compute log likelihoods for each factor
    log_likelihoods = compute_log_likelihood_per_modality(obs, A)

    # Step 2: Map prior to log space and create initial log-posterior
    log_prior = jtu.tree_map(log_stable, prior)
    log_q = jtu.tree_map(jnp.zeros_like, prior)

    # Step 3: Iterate until convergence
    def scan_fn(carry, t):
        log_q = carry
        q = jtu.tree_map(nn.softmax, log_q)
        marginal_ll = all_marginal_log_likelihood(q, log_likelihoods, A_dependencies)
        log_q = jtu.tree_map(add, marginal_ll, log_prior)

        return log_q, None

    res, _ = lax.scan(scan_fn, log_q, jnp.arange(num_iter))

    # Step 4: Map result to factorised posterior
    qs = jtu.tree_map(nn.softmax, res)
    return qs

def mirror_gradient_descent_step(tau, ln_A, lnB_past, lnB_future, ln_qs):
    """
    u_{k+1} = u_{k} - \nabla_p F_k
    p_k = softmax(u_k)
    """
    err = ln_A - ln_qs + lnB_past + lnB_future
    ln_qs = ln_qs + tau * err
    qs = nn.softmax(ln_qs - ln_qs.mean(axis=-1, keepdims=True))

    return qs

def update_marginals(get_messages, obs, A, B, prior, A_dependencies, B_dependencies, num_iter=1, tau=1.,):
    """" Version of marginal update that uses a sparse dependency matrix for A """

    T = obs[0].shape[0]
    ln_B = jtu.tree_map(log_stable, B)
    # log likelihoods -> $\ln(A)$ for all time steps
    # for $k > t$ we have $\ln(A) = 0$

    def get_log_likelihood(obs_t, A):
       # # mapping over batch dimension
       # return vmap(compute_log_likelihood_per_modality)(obs_t, A)
       return compute_log_likelihood_per_modality(obs_t, A)

    # mapping over time dimension of obs array
    log_likelihoods = vmap(get_log_likelihood, (0, None))(obs, A) # this gives a sequence of log-likelihoods (one for each `t`)

    # log marginals -> $\ln(q(s_t))$ for all time steps and factors
    ln_qs = jtu.tree_map( lambda p: jnp.broadcast_to(jnp.zeros_like(p), (T,) + p.shape), prior)

    # log prior -> $\ln(p(s_t))$ for all factors
    ln_prior = jtu.tree_map(log_stable, prior)

    qs = jtu.tree_map(nn.softmax, ln_qs)

    def scan_fn(carry, iter):
        qs = carry

        ln_qs = jtu.tree_map(log_stable, qs)
        # messages from future $m_+(s_t)$ and past $m_-(s_t)$ for all time steps and factors. For t = T we have that $m_+(s_T) = 0$
        
        lnB_past, lnB_future = get_messages(ln_B, B, qs, ln_prior, B_dependencies)

        mgds = jtu.Partial(mirror_gradient_descent_step, tau)

        ln_As = vmap(all_marginal_log_likelihood, in_axes=(0, 0, None))(qs, log_likelihoods, A_dependencies)

        qs = jtu.tree_map(mgds, ln_As, lnB_past, lnB_future, ln_qs)

        return qs, None

    qs, _ = lax.scan(scan_fn, qs, jnp.arange(num_iter))

    return qs

def variational_filtering_step(prior, Bs, ln_As, A_dependencies):

    ln_prior = jtu.tree_map(log_stable, prior)
    
    #TODO: put this inside scan
    ####
    marg_ln_As = all_marginal_log_likelihood(prior, ln_As, A_dependencies)

    # compute posterior q(z_t) -> n x 1 x d
    post = jtu.tree_map( 
            lambda x, y: nn.softmax(x + y, -1), marg_ln_As, ln_prior 
        )
    ####

    # compute prediction p(z_{t+1}) = \int p(z_{t+1}|z_t) q(z_t) -> n x d x 1
    pred = jtu.tree_map(
            lambda x, y: jnp.sum(x * jnp.expand_dims(y, -2), -1), Bs, post
        )
    
    # compute reverse conditional distribution q(z_t|z_{t+1})
    cond = jtu.tree_map(
        lambda x, y, z: x * jnp.expand_dims(y, -2) / jnp.expand_dims(z, -1),
        Bs,
        post, 
        pred
    )

    return post, pred, cond

def update_variational_filtering(obs, A, B, prior, A_dependencies, **kwargs):
    """Online variational filtering belief update that uses a sparse dependency matrix for A"""

    T = obs[0].shape[0]
    def pad(x):
        npad = [(0, 0)] * jnp.ndim(x)
        npad[0] = (0, 1)
        return jnp.pad(x, npad, constant_values=1.)
    
    B = jtu.tree_map(pad, B)
 
    def get_log_likelihood(obs_t, A):
        # mapping over batch dimension
        return vmap(compute_log_likelihood_per_modality)(obs_t, A)

    # mapping over time dimension of obs array
    log_likelihoods = vmap(get_log_likelihood, (0, None))(obs, A) # this gives a sequence of log-likelihoods (one for each `t`)
    
    def scan_fn(carry, iter):
        _, prior = carry
        Bs, ln_As = iter

        post, pred, cond = variational_filtering_step(prior, Bs, ln_As, A_dependencies)
        
        return (post, pred), cond

    init = (prior, prior)
    iterator = (B, log_likelihoods)
    # get q_T(s_t), p_T(s_{t+1}) and the history q_{T}(s_{t}|s_{t+1})q_{T-1}(s_{t-1}|s_{t}) ...
    (qs, ps), qss = lax.scan(scan_fn, init, iterator)

    return qs, ps, qss

def get_vmp_messages(ln_B, B, qs, ln_prior, B_dependencies):
    
    num_factors = len(qs)
    factors = list(range(num_factors))
    get_deps = lambda x, f_idx: [x[f] for f in f_idx] # function that effectively "slices" a list with a set of indices `f_idx`

    # make a list of lists, where each list contains all dependencies of a factor except itself
    all_deps_except_f = jtu.tree_map( 
        lambda f: [d for d in B_dependencies[f] if d != f], 
        factors
    )

    # make list of integers, where each integer is the position of the self-factor in its dependencies list
    position = jtu.tree_map(
        lambda f: B_dependencies[f].index(f),
        factors
    )

    if ln_B is not None:
        ln_B_marg = jtu.tree_map( # this is a list of matrices, where each matrix is the marginal transition tensor for factor f
            lambda b, f: factor_dot(b, get_deps(qs, all_deps_except_f[f]), keep_dims=(0, 1, 2 + position[f])), 
            ln_B, 
            factors
        )  # shape = (T, states_f_{t+1}, states_f_{t})
    else:
        ln_B_marg = None

    def forward(ln_b, q, ln_prior):
        msg = vmap(lambda x, y: y @ x)(q[:-1], ln_b) # ln_b has shape (num_states, num_states) qs[:-1] has shape (T-1, num_states)
        return jnp.concatenate([jnp.expand_dims(ln_prior, 0), msg], axis=0)
    
    def backward(ln_b, q):
        # q_i B_ij
        msg = vmap(lambda x, y: x @ y)(q[1:], ln_b)
        return jnp.pad(msg, ((0, 1), (0, 0)))

    if ln_B_marg is not None:
        lnB_future = jtu.tree_map(forward, ln_B_marg, qs, ln_prior)
        lnB_past = jtu.tree_map(backward, ln_B_marg, qs)
    else:
        lnB_future = jtu.tree_map(lambda x: 0., qs)
        lnB_past = jtu.tree_map(lambda x: 0., qs)
    
    return lnB_future, lnB_past

def run_vmp(A, B, obs, prior, A_dependencies, B_dependencies, num_iter=1, tau=1.):
    '''
    Run variational message passing (VMP) on a sequence of observations
    '''

    qs = update_marginals(
        get_vmp_messages, 
        obs, 
        A, 
        B, 
        prior, 
        A_dependencies, 
        B_dependencies, 
        num_iter=num_iter, 
        tau=tau
    )
    return qs

def get_mmp_messages(ln_B, B, qs, ln_prior, B_deps):
    
    num_factors = len(qs)
    factors = list(range(num_factors))

    get_deps_forw = lambda x, f_idx: [x[f][:-1] for f in f_idx]
    get_deps_back = lambda x, f_idx: [x[f][1:] for f in f_idx]

    def forward(b, ln_prior, f):
        xs = get_deps_forw(qs, B_deps[f])
        dims = tuple((0, 2 + i) for i in range(len(B_deps[f])))
        msg = log_stable(factor_dot_flex(b, xs, dims, keep_dims=(0, 1) ))
        # append log_prior as a first message 
        msg = jnp.concatenate([jnp.expand_dims(ln_prior, 0), msg], axis=0)
        # mutliply with 1/2 all but the last msg
        T = len(msg)
        if T > 1:
            msg = msg * jnp.pad( 0.5 * jnp.ones(T - 1), (0, 1), constant_values=1.)[:, None]

        return msg
    
    def backward(Bs, xs):
        msg = 0.
        for i, b in enumerate(Bs):
            b_norm = b / (b.sum(-1, keepdims=True) + 1e-16)
            msg += log_stable(vmap(lambda x, y: y @ x)(b_norm, xs[i])) * .5
        
        return jnp.pad(msg, ((0, 1), (0, 0)))

    def marg(inv_deps, f):
        B_marg = []
        for i in inv_deps:
            b = B[i]
            keep_dims = (0, 1, 2 + B_deps[i].index(f))
            dims = []
            idxs = []
            for j, d in enumerate(B_deps[i]):
                if f != d:
                    dims.append((0, 2 + j))
                    idxs.append(d)
            xs = get_deps_forw(qs, idxs)
            B_marg.append( factor_dot_flex(b, xs, tuple(dims), keep_dims=keep_dims) )
        
        return B_marg

    if B is not None:
        inv_B_deps = [[i for i, d in enumerate(B_deps) if f in d] for f in factors]
        B_marg = jtu.tree_map(lambda f: marg(inv_B_deps[f], f), factors)
        lnB_future = jtu.tree_map(forward, B, ln_prior, factors) 
        lnB_past = jtu.tree_map(lambda f: backward(B_marg[f], get_deps_back(qs, inv_B_deps[f])), factors)
    else: 
        lnB_future = jtu.tree_map(lambda x: jnp.expand_dims(x, 0), ln_prior)
        lnB_past = jtu.tree_map(lambda x: 0., qs)

    return lnB_future, lnB_past

def run_mmp(A, B, obs, prior, A_dependencies, B_dependencies, num_iter=1, tau=1.):
    qs = update_marginals(
        get_mmp_messages, 
        obs, 
        A, 
        B, 
        prior, 
        A_dependencies, 
        B_dependencies, 
        num_iter=num_iter, 
        tau=tau
    )
    return qs

def run_online_filtering(A, B, obs, prior, A_dependencies, num_iter=1, tau=1.):
    """Runs online filtering (HAVE TO REPLACE WITH OVF CODE)"""
    qs = update_marginals(get_mmp_messages, obs, A, B, prior, A_dependencies, num_iter=num_iter, tau=tau)
    return qs

def scan_fn(carry, t):
        log_q = carry
        q = jtu.tree_map(nn.softmax, log_q)
        mll = jtu.Partial(marginal_log_likelihood, q, ll)
        marginal_ll = jtu.tree_map(mll, factors)
        log_q = jtu.tree_map(add, marginal_ll, log_prior)

        return log_q, None

def scan_fn(carry, t):
        log_q = carry
        q = jtu.tree_map(nn.softmax, log_q)
        marginal_ll = all_marginal_log_likelihood(q, log_likelihoods, A_dependencies)
        log_q = jtu.tree_map(add, marginal_ll, log_prior)

        return log_q, None

def get_log_likelihood(obs_t, A):
       # # mapping over batch dimension
       # return vmap(compute_log_likelihood_per_modality)(obs_t, A)
       return compute_log_likelihood_per_modality(obs_t, A)

def scan_fn(carry, iter):
        qs = carry

        ln_qs = jtu.tree_map(log_stable, qs)
        # messages from future $m_+(s_t)$ and past $m_-(s_t)$ for all time steps and factors. For t = T we have that $m_+(s_T) = 0$
        
        lnB_past, lnB_future = get_messages(ln_B, B, qs, ln_prior, B_dependencies)

        mgds = jtu.Partial(mirror_gradient_descent_step, tau)

        ln_As = vmap(all_marginal_log_likelihood, in_axes=(0, 0, None))(qs, log_likelihoods, A_dependencies)

        qs = jtu.tree_map(mgds, ln_As, lnB_past, lnB_future, ln_qs)

        return qs, None

def pad(x):
        npad = [(0, 0)] * jnp.ndim(x)
        npad[0] = (0, 1)
        return jnp.pad(x, npad, constant_values=1.)

def get_log_likelihood(obs_t, A):
        # mapping over batch dimension
        return vmap(compute_log_likelihood_per_modality)(obs_t, A)

def scan_fn(carry, iter):
        _, prior = carry
        Bs, ln_As = iter

        post, pred, cond = variational_filtering_step(prior, Bs, ln_As, A_dependencies)
        
        return (post, pred), cond

def forward(ln_b, q, ln_prior):
        msg = vmap(lambda x, y: y @ x)(q[:-1], ln_b) # ln_b has shape (num_states, num_states) qs[:-1] has shape (T-1, num_states)
        return jnp.concatenate([jnp.expand_dims(ln_prior, 0), msg], axis=0)

def backward(ln_b, q):
        # q_i B_ij
        msg = vmap(lambda x, y: x @ y)(q[1:], ln_b)
        return jnp.pad(msg, ((0, 1), (0, 0)))

def forward(b, ln_prior, f):
        xs = get_deps_forw(qs, B_deps[f])
        dims = tuple((0, 2 + i) for i in range(len(B_deps[f])))
        msg = log_stable(factor_dot_flex(b, xs, dims, keep_dims=(0, 1) ))
        # append log_prior as a first message 
        msg = jnp.concatenate([jnp.expand_dims(ln_prior, 0), msg], axis=0)
        # mutliply with 1/2 all but the last msg
        T = len(msg)
        if T > 1:
            msg = msg * jnp.pad( 0.5 * jnp.ones(T - 1), (0, 1), constant_values=1.)[:, None]

        return msg

def backward(Bs, xs):
        msg = 0.
        for i, b in enumerate(Bs):
            b_norm = b / (b.sum(-1, keepdims=True) + 1e-16)
            msg += log_stable(vmap(lambda x, y: y @ x)(b_norm, xs[i])) * .5
        
        return jnp.pad(msg, ((0, 1), (0, 0)))

def marg(inv_deps, f):
        B_marg = []
        for i in inv_deps:
            b = B[i]
            keep_dims = (0, 1, 2 + B_deps[i].index(f))
            dims = []
            idxs = []
            for j, d in enumerate(B_deps[i]):
                if f != d:
                    dims.append((0, 2 + j))
                    idxs.append(d)
            xs = get_deps_forw(qs, idxs)
            B_marg.append( factor_dot_flex(b, xs, tuple(dims), keep_dims=keep_dims) )
        
        return B_marg

def sum_prod(prior):
        qs = jnp.concatenate(run_vanilla_fpi(A, obs, prior))
        return (qs * log_stable(qs)).sum()

def stable_xlogx(x):
    return xlogy(x, jnp.clip(x, MINVAL))

def stable_entropy(x):
    return - stable_xlogx(x).sum()

def stable_cross_entropy(x, y):
    return - xlogy(x, y).sum()

def log_stable(x):
    return jnp.log(jnp.clip(x, min=MINVAL))

def factor_dot(M, xs, keep_dims: Optional[Tuple[int]] = None):
    """ Dot product of a multidimensional array with `x`.
    
    Parameters
    ----------
    - `qs` [list of 1D numpy.ndarray] - list of jnp.ndarrays
    
    Returns 
    -------
    - `Y` [1D numpy.ndarray] - the result of the dot product
    """
    d = len(keep_dims) if keep_dims is not None else 0
    assert M.ndim == len(xs) + d
    keep_dims = () if keep_dims is None else keep_dims
    dims = tuple((i,) for i in range(M.ndim) if i not in keep_dims)
    return factor_dot_flex(M, xs, dims, keep_dims=keep_dims)

def factor_dot_flex(M, xs, dims: List[Tuple[int]], keep_dims: Optional[Tuple[int]] = None):
    """ Dot product of a multidimensional array with `x`.
    
    Parameters
    ----------
    - `M` [numpy.ndarray] - tensor
    - 'xs' [list of numpyr.ndarray] - list of tensors
    - 'dims' [list of tuples] - list of dimensions of xs tensors in tensor M
    - 'keep_dims' [tuple] - tuple of integers denoting dimesions to keep
    Returns 
    -------
    - `Y` [1D numpy.ndarray] - the result of the dot product
    """
    all_dims = tuple(range(M.ndim))
    matrix = [[xs[f], dims[f]] for f in range(len(xs))]
    args = [M, all_dims]
    for row in matrix:
        args.extend(row)

    args += [keep_dims]
    return contract(*args, backend='jax')

def get_likelihood_single_modality(o_m, A_m, distr_obs=True):
    """Return observation likelihood for a single observation modality m"""
    if distr_obs:
        expanded_obs = jnp.expand_dims(o_m, tuple(range(1, A_m.ndim)))
        likelihood = (expanded_obs * A_m).sum(axis=0)
    else:
        likelihood = A_m[o_m]

    return likelihood

def compute_log_likelihood_single_modality(o_m, A_m, distr_obs=True):
    """Compute observation log-likelihood for a single modality"""
    return log_stable(get_likelihood_single_modality(o_m, A_m, distr_obs=distr_obs))

def compute_log_likelihood(obs, A, distr_obs=True):
    """ Compute likelihood over hidden states across observations from different modalities """
    result = tree_util.tree_map(lambda o, a: compute_log_likelihood_single_modality(o, a, distr_obs=distr_obs), obs, A)
    ll = jnp.sum(jnp.stack(result), 0)

    return ll

def compute_log_likelihood_per_modality(obs, A, distr_obs=True):
    """ Compute likelihood over hidden states across observations from different modalities, and return them per modality """
    ll_all = tree_util.tree_map(lambda o, a: compute_log_likelihood_single_modality(o, a, distr_obs=distr_obs), obs, A)

    return ll_all

def compute_accuracy(qs, obs, A):
    """ Compute the accuracy portion of the variational free energy (expected log likelihood under the variational posterior) """

    log_likelihood = compute_log_likelihood(obs, A)

    x = qs[0]
    for q in qs[1:]:
        x = jnp.expand_dims(x, -1) * q

    joint = log_likelihood * x
    return joint.sum()

def compute_free_energy(qs, prior, obs, A):
    """ 
    Calculate variational free energy by breaking its computation down into three steps:
    1. computation of the negative entropy of the posterior -H[Q(s)]
    2. computation of the cross entropy of the posterior with the prior H_{Q(s)}[P(s)]
    3. computation of the accuracy E_{Q(s)}[lnP(o|s)] 
    
    Then add them all together -- except subtract the accuracy
    """

    vfe = 0.0 # initialize variational free energy
    for q, p in zip(qs, prior):
        negH_qs = - stable_entropy(q)
        xH_qp = stable_cross_entropy(q, p)
        vfe += (negH_qs + xH_qp)
    
    vfe -= compute_accuracy(qs, obs, A)

    return vfe

def multidimensional_outer(arrs):
    """ Compute the outer product of a list of arrays by iteratively expanding the first array and multiplying it with the next array """

    x = arrs[0]
    for q in arrs[1:]:
        x = jnp.expand_dims(x, -1) * q

    return x

def spm_wnorm(A):
    """ 
    Returns Expectation of logarithm of Dirichlet parameters over a set of 
    Categorical distributions, stored in the columns of A.
    """
    norm = 1. / A.sum(axis=0)
    avg = 1. / (A + MINVAL)
    wA = norm - avg
    return wA

def dirichlet_expected_value(dir_arr):
    """ 
    Returns Expectation of Dirichlet parameters over a set of 
    Categorical distributions, stored in the columns of A.
    """
    dir_arr = jnp.clip(dir_arr, min=MINVAL)
    expected_val = jnp.divide(dir_arr, dir_arr.sum(axis=0, keepdims=True))
    return expected_val

class Agent(Module):
    """ 
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
    """

    A: List[Array]
    B: List[Array]
    C: List[Array] 
    D: List[Array]
    E: Array
    # empirical_prior: List
    gamma: Array
    alpha: Array
    qs: Optional[List[Array]]
    q_pi: Optional[List[Array]]

    # parameters used for inductive inference
    inductive_threshold: Array # threshold for inductive inference (the threshold for pruning transitions that are below a certain probability)
    inductive_epsilon: Array # epsilon for inductive inference (trade-off/weight for how much inductive value contributes to EFE of policies)

    H: List[Array] # H vectors (one per hidden state factor) used for inductive inference -- these encode goal states or constraints
    I: List[Array] # I matrices (one per hidden state factor) used for inductive inference -- these encode the 'reachability' matrices of goal states encoded in `self.H`

    pA: List[Array]
    pB: List[Array]

    policies: Array # matrix of all possible policies (each row is a policy of shape (num_controls[0], num_controls[1], ..., num_controls[num_control_factors-1])
    
    # static parameters not leaves of the PyTree
    A_dependencies: Optional[List[int]] = field(static=True)
    B_dependencies: Optional[List[int]] = field(static=True)
    batch_size: int = field(static=True)
    num_iter: int = field(static=True)
    num_obs: List[int] = field(static=True)
    num_modalities: int = field(static=True)
    num_states: List[int] = field(static=True)
    num_factors: int = field(static=True)
    num_controls: List[int] = field(static=True)
    control_fac_idx: Optional[List[int]] = field(static=True)
    policy_len: int = field(static=True) # depth of planning during roll-outs (i.e. number of timesteps to look ahead when computing expected free energy of policies)
    inductive_depth: int = field(static=True) # depth of inductive inference (i.e. number of future timesteps to use when computing inductive `I` matrix)
    use_utility: bool = field(static=True) # flag for whether to use expected utility ("reward" or "preference satisfaction") when computing expected free energy
    use_states_info_gain: bool = field(static=True) # flag for whether to use state information gain ("salience") when computing expected free energy
    use_param_info_gain: bool = field(static=True)  # flag for whether to use parameter information gain ("novelty") when computing expected free energy
    use_inductive: bool = field(static=True)   # flag for whether to use inductive inference ("intentional inference") when computing expected free energy
    onehot_obs: bool = field(static=True)
    action_selection: str = field(static=True) # determinstic or stochastic action selection 
    sampling_mode : str = field(static=True) # whether to sample from full posterior over policies ("full") or from marginal posterior over actions ("marginal")
    inference_algo: str = field(static=True) # fpi, vmp, mmp, ovf

    learn_A: bool = field(static=True)
    learn_B: bool = field(static=True)
    learn_C: bool = field(static=True)
    learn_D: bool = field(static=True)
    learn_E: bool = field(static=True)

    def __init__(
        self,
        A,
        B,
        C,
        D,
        E,
        pA,
        pB,
        A_dependencies=None,
        B_dependencies=None,
        qs=None,
        q_pi=None,
        H=None,
        I=None,
        policy_len=1,
        control_fac_idx=None,
        policies=None,
        gamma=1.0,
        alpha=1.0,
        inductive_depth=1,
        inductive_threshold=0.1,
        inductive_epsilon=1e-3,
        use_utility=True,
        use_states_info_gain=True,
        use_param_info_gain=False,
        use_inductive=False,
        onehot_obs=False,
        action_selection="deterministic",
        sampling_mode="full",
        inference_algo="fpi",
        num_iter=16,
        learn_A=True,
        learn_B=True,
        learn_C=False,
        learn_D=True,
        learn_E=False
    ):
        ### PyTree leaves
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        # self.empirical_prior = D
        self.H = H
        self.pA = pA
        self.pB = pB
        self.qs = qs
        self.q_pi = q_pi

        self.onehot_obs = onehot_obs

        element_size = lambda x: x.shape[1]
        self.num_factors = len(self.B)
        self.num_states = jtu.tree_map(element_size, self.B) 

        self.num_modalities = len(self.A)
        self.num_obs = jtu.tree_map(element_size, self.A)

        # Ensure consistency of A_dependencies with num_states and num_factors
        if A_dependencies is not None:
            self.A_dependencies = A_dependencies
        else:
            # assume full dependence of A matrices and state factors
            self.A_dependencies = [list(range(self.num_factors)) for _ in range(self.num_modalities)]
        
        for m in range(self.num_modalities):
            factor_dims = tuple([self.num_states[f] for f in self.A_dependencies[m]])
            assert self.A[m].shape[2:] == factor_dims, f"Please input an `A_dependencies` whose {m}-th indices correspond to the hidden state factors that line up with lagging dimensions of A[{m}]..." 
            if self.pA != None:
                assert self.pA[m].shape[2:] == factor_dims if self.pA[m] is not None else True, f"Please input an `A_dependencies` whose {m}-th indices correspond to the hidden state factors that line up with lagging dimensions of pA[{m}]..." 
            assert max(self.A_dependencies[m]) <= (self.num_factors - 1), f"Check modality {m} of `A_dependencies` - must be consistent with `num_states` and `num_factors`..."
           
        # Ensure consistency of B_dependencies with num_states and num_factors
        if B_dependencies is not None:
            self.B_dependencies = B_dependencies
        else:
            self.B_dependencies = [[f] for f in range(self.num_factors)] # defaults to having all factors depend only on themselves

        for f in range(self.num_factors):
            factor_dims = tuple([self.num_states[f] for f in self.B_dependencies[f]])
            assert self.B[f].shape[2:-1] == factor_dims, f"Please input a `B_dependencies` whose {f}-th indices pick out the hidden state factors that line up with the all-but-final lagging dimensions of B[{f}]..." 
            if self.pB != None:
                assert self.pB[f].shape[2:-1] == factor_dims, f"Please input a `B_dependencies` whose {f}-th indices pick out the hidden state factors that line up with the all-but-final lagging dimensions of pB[{f}]..." 
            assert max(self.B_dependencies[f]) <= (self.num_factors - 1), f"Check factor {f} of `B_dependencies` - must be consistent with `num_states` and `num_factors`..."

        self.batch_size = self.A[0].shape[0]

        self.gamma = jnp.broadcast_to(gamma, (self.batch_size,))
        self.alpha = jnp.broadcast_to(alpha, (self.batch_size,))
        self.inductive_threshold = jnp.broadcast_to(inductive_threshold, (self.batch_size,))
        self.inductive_epsilon = jnp.broadcast_to(inductive_epsilon, (self.batch_size,))

        ### Static parameters ###
        self.num_iter = num_iter
        self.inference_algo = inference_algo
        self.inductive_depth = inductive_depth

        # policy parameters
        self.policy_len = policy_len
        self.action_selection = action_selection
        self.sampling_mode = sampling_mode
        self.use_utility = use_utility
        self.use_states_info_gain = use_states_info_gain
        self.use_param_info_gain = use_param_info_gain
        self.use_inductive = use_inductive

        if self.use_inductive and self.H is not None:
            # print("Using inductive inference...")
            self.I = self._construct_I()
        elif self.use_inductive and I is not None:
            self.I = I
        else:
            self.I = jtu.tree_map(lambda x: jnp.expand_dims(jnp.zeros_like(x), 1), self.D)

        # learning parameters
        self.learn_A = learn_A
        self.learn_B = learn_B
        self.learn_C = learn_C
        self.learn_D = learn_D
        self.learn_E = learn_E

        """ Determine number of observation modalities and their respective dimensions """
        self.num_obs = [self.A[m].shape[1] for m in range(len(self.A))]
        self.num_modalities = len(self.num_obs)

        # If no `num_controls` are given, then this is inferred from the shapes of the input B matrices
        self.num_controls = [self.B[f].shape[-1] for f in range(self.num_factors)]

        # Users have the option to make only certain factors controllable.
        # default behaviour is to make all hidden state factors controllable
        # (i.e. self.num_states == self.num_controls)
        # Users have the option to make only certain factors controllable.
        # default behaviour is to make all hidden state factors controllable, i.e. `self.num_factors == len(self.num_controls)`
        if control_fac_idx == None:
            self.control_fac_idx = [f for f in range(self.num_factors) if self.num_controls[f] > 1]
        else:
            assert max(control_fac_idx) <= (self.num_factors - 1), "Check control_fac_idx - must be consistent with `num_states` and `num_factors`..."
            self.control_fac_idx = control_fac_idx

            for factor_idx in self.control_fac_idx:
                assert self.num_controls[factor_idx] > 1, "Control factor (and B matrix) dimensions are not consistent with user-given control_fac_idx"

        if policies is not None:
            self.policies = policies
        else:
            self._construct_policies()
        
        # set E to uniform/uninformative prior over policies if not given
        if E is None:
            self.E = jnp.ones((self.batch_size, len(self.policies)))/ len(self.policies)
        else:
            self.E = E

    def _construct_policies(self):
        
        self.policies =  control.construct_policies(
            self.num_states, self.num_controls, self.policy_len, self.control_fac_idx
        )

    @vmap
    def _construct_I(self):
        return control.generate_I_matrix(self.H, self.B, self.inductive_threshold, self.inductive_depth)

    @property
    def unique_multiactions(self):
        size = pymath.prod(self.num_controls)
        return jnp.unique(self.policies[:, 0], axis=0, size=size, fill_value=-1)

    def infer_parameters(self, beliefs_A, outcomes, actions, beliefs_B=None, lr_pA=1., lr_pB=1., **kwargs):
        agent = self
        beliefs_B = beliefs_A if beliefs_B is None else beliefs_B
        if self.inference_algo == 'ovf':
            smoothed_marginals_and_joints = vmap(inference.smoothing_ovf)(beliefs_A, self.B, actions)
            marginal_beliefs = smoothed_marginals_and_joints[0]
            joint_beliefs = smoothed_marginals_and_joints[1]
        else:
            marginal_beliefs = beliefs_A
            if self.learn_B:
                nf = len(beliefs_B)
                joint_fn = lambda f: [beliefs_B[f][:, 1:]] + [beliefs_B[f_idx][:, :-1] for f_idx in self.B_dependencies[f]]
                joint_beliefs = jtu.tree_map(joint_fn, list(range(nf)))

        if self.learn_A:
            update_A = partial(
                learning.update_obs_likelihood_dirichlet,
                A_dependencies=self.A_dependencies,
                num_obs=self.num_obs,
                onehot_obs=self.onehot_obs,
            )
            
            lr = jnp.broadcast_to(lr_pA, (self.batch_size,))
            qA, E_qA = vmap(update_A)(
                self.pA,
                self.A,
                outcomes,
                marginal_beliefs,
                lr=lr,
            )
            
            agent = tree_at(lambda x: (x.A, x.pA), agent, (E_qA, qA))
            
        if self.learn_B:
            assert beliefs_B[0].shape[1] == actions.shape[1] + 1
            update_B = partial(
                learning.update_state_transition_dirichlet,
                num_controls=self.num_controls
            )

            lr = jnp.broadcast_to(lr_pB, (self.batch_size,))
            qB, E_qB = vmap(update_B)(
                self.pB,
                joint_beliefs,
                actions,
                lr=lr
            )
            
            # if you have updated your beliefs about transitions, you need to re-compute the I matrix used for inductive inferenece
            if self.use_inductive and self.H is not None:
                I_updated = vmap(control.generate_I_matrix)(self.H, E_qB, self.inductive_threshold, self.inductive_depth)
            else:
                I_updated = self.I

            agent = tree_at(lambda x: (x.B, x.pB, x.I), agent, (E_qB, qB, I_updated))

        return agent
    
    def infer_states(self, observations, empirical_prior, *, past_actions=None, qs_hist=None, mask=None):
        """
        Update approximate posterior over hidden states by solving variational inference problem, given an observation.

        Parameters
        ----------
        observations: ``list`` or ``tuple`` of ints
            The observation input. Each entry ``observation[m]`` stores one-hot vectors representing the observations for modality ``m``.
        past_actions: ``list`` or ``tuple`` of ints
            The action input. Each entry ``past_actions[f]`` stores indices (or one-hots?) representing the actions for control factor ``f``.
        empirical_prior: ``list`` or ``tuple`` of ``jax.numpy.ndarray`` of dtype object
            Empirical prior beliefs over hidden states. Depending on the inference algorithm chosen, the resulting ``empirical_prior`` variable may be a matrix (or list of matrices) 
            of additional dimensions to encode extra conditioning variables like timepoint and policy.
        Returns
        ---------
        qs: ``numpy.ndarray`` of dtype object
            Posterior beliefs over hidden states. Depending on the inference algorithm chosen, the resulting ``qs`` variable will have additional sub-structure to reflect whether
            beliefs are additionally conditioned on timepoint and policy.
            For example, in case the ``self.inference_algo == 'MMP' `` indexing structure is policy->timepoint-->factor, so that 
            ``qs[p_idx][t_idx][f_idx]`` refers to beliefs about marginal factor ``f_idx`` expected under policy ``p_idx`` 
            at timepoint ``t_idx``.
        """
        if not self.onehot_obs:
            o_vec = [nn.one_hot(o, self.num_obs[m]) for m, o in enumerate(observations)]
        else:
            o_vec = observations
        
        A = self.A
        if mask is not None:
            for i, m in enumerate(mask):
                o_vec[i] = m * o_vec[i] + (1 - m) * jnp.ones_like(o_vec[i]) / self.num_obs[i]
                A[i] = m * A[i] + (1 - m) * jnp.ones_like(A[i]) / self.num_obs[i]

        infer_states = partial(
            inference.update_posterior_states,
            A_dependencies=self.A_dependencies,
            B_dependencies=self.B_dependencies,
            num_iter=self.num_iter,
            method=self.inference_algo
        )
        
        output = vmap(infer_states)(
            A,
            self.B,
            o_vec,
            past_actions,
            prior=empirical_prior,
            qs_hist=qs_hist
        )

        return output

    def update_empirical_prior(self, action, qs):
        # return empirical_prior, and the history of posterior beliefs (filtering distributions) held about hidden states at times 1, 2 ... t

        # this computation of the predictive prior is correct only for fully factorised Bs.
        if self.inference_algo in ['mmp', 'vmp']:
            # in the case of the 'mmp' or 'vmp' we have to use D as prior parameter for infer states
            pred = self.D
        else:
            qs_last = jtu.tree_map( lambda x: x[:, -1], qs)
            propagate_beliefs = partial(control.compute_expected_state, B_dependencies=self.B_dependencies)
            pred = vmap(propagate_beliefs)(qs_last, self.B, action)
        
        return (pred, qs)

    def infer_policies(self, qs: List):
        """
        Perform policy inference by optimizing a posterior (categorical) distribution over policies.
        This distribution is computed as the softmax of ``G * gamma + lnE`` where ``G`` is the negative expected
        free energy of policies, ``gamma`` is a policy precision and ``lnE`` is the (log) prior probability of policies.
        This function returns the posterior over policies as well as the negative expected free energy of each policy.

        Returns
        ----------
        q_pi: 1D ``numpy.ndarray``
            Posterior beliefs over policies, i.e. a vector containing one posterior probability per policy.
        G: 1D ``numpy.ndarray``
            Negative expected free energies of each policy, i.e. a vector containing one negative expected free energy per policy.
        """

        latest_belief = jtu.tree_map(lambda x: x[:, -1], qs) # only get the posterior belief held at the current timepoint
        infer_policies = partial(
            control.update_posterior_policies_inductive,
            self.policies,
            A_dependencies=self.A_dependencies,
            B_dependencies=self.B_dependencies,
            use_utility=self.use_utility,
            use_states_info_gain=self.use_states_info_gain,
            use_param_info_gain=self.use_param_info_gain,
            use_inductive=self.use_inductive
        )

        q_pi, G = vmap(infer_policies)(
            latest_belief, 
            self.A,
            self.B,
            self.C,
            self.E,
            self.pA,
            self.pB,
            I = self.I,
            gamma=self.gamma,
            inductive_epsilon=self.inductive_epsilon
        )

        return q_pi, G
    
    def multiaction_probabilities(self, q_pi: Array):
        """
        Compute probabilities of unique multi-actions from the posterior over policies.

        Parameters
        ----------
        q_pi: 1D ``numpy.ndarray``
        Posterior beliefs over policies, i.e. a vector containing one posterior probability per policy.
        
        Returns
        ----------
        multi-action: 1D ``jax.numpy.ndarray``
            Vector containing probabilities of possible multi-actions for different factors
        """

        if self.sampling_mode == "marginal":
            get_marginals = partial(control.get_marginals, policies=self.policies, num_controls=self.num_controls)
            marginals = get_marginals(q_pi)
            outer = lambda a, b: jnp.outer(a, b).reshape(-1)
            marginals = jtu.tree_reduce(outer, marginals)

        elif self.sampling_mode == "full":
            locs = jnp.all(
                self.policies[:, 0] == jnp.expand_dims(self.unique_multiactions, -2),
                  -1
            )
            get_marginals = lambda x: jnp.where(locs, x, 0.).sum(-1)
            marginals = vmap(get_marginals)(q_pi)

        return marginals

    def sample_action(self, q_pi: Array, rng_key=None):
        """
        Sample or select a discrete action from the posterior over control states.
        
        Returns
        ----------
        action: 1D ``jax.numpy.ndarray``
            Vector containing the indices of the actions for each control factor
        action_probs: 2D ``jax.numpy.ndarray``
            Array of action probabilities
        """

        if (rng_key is None) and (self.action_selection == "stochastic"):
            raise ValueError("Please provide a random number generator key to sample actions stochastically")

        if self.sampling_mode == "marginal":
            sample_action = partial(control.sample_action, self.policies, self.num_controls, action_selection=self.action_selection)
            action = vmap(sample_action)(q_pi, alpha=self.alpha, rng_key=rng_key)
        elif self.sampling_mode == "full":
            sample_policy = partial(control.sample_policy, self.policies, action_selection=self.action_selection)
            action = vmap(sample_policy)(q_pi, alpha=self.alpha, rng_key=rng_key)

        return action
    
    def _get_default_params(self):
        method = self.inference_algo
        default_params = None
        if method == "VANILLA":
            default_params = {"num_iter": 8, "dF": 1.0, "dF_tol": 0.001}
        elif method == "MMP":
            raise NotImplementedError("MMP is not implemented")
        elif method == "VMP":
            raise NotImplementedError("VMP is not implemented")
        elif method == "BP":
            raise NotImplementedError("BP is not implemented")
        elif method == "EP":
            raise NotImplementedError("EP is not implemented")
        elif method == "CV":
            raise NotImplementedError("CV is not implemented")

        return default_params

def __init__(
        self,
        A,
        B,
        C,
        D,
        E,
        pA,
        pB,
        A_dependencies=None,
        B_dependencies=None,
        qs=None,
        q_pi=None,
        H=None,
        I=None,
        policy_len=1,
        control_fac_idx=None,
        policies=None,
        gamma=1.0,
        alpha=1.0,
        inductive_depth=1,
        inductive_threshold=0.1,
        inductive_epsilon=1e-3,
        use_utility=True,
        use_states_info_gain=True,
        use_param_info_gain=False,
        use_inductive=False,
        onehot_obs=False,
        action_selection="deterministic",
        sampling_mode="full",
        inference_algo="fpi",
        num_iter=16,
        learn_A=True,
        learn_B=True,
        learn_C=False,
        learn_D=True,
        learn_E=False
    ):
        ### PyTree leaves
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        # self.empirical_prior = D
        self.H = H
        self.pA = pA
        self.pB = pB
        self.qs = qs
        self.q_pi = q_pi

        self.onehot_obs = onehot_obs

        element_size = lambda x: x.shape[1]
        self.num_factors = len(self.B)
        self.num_states = jtu.tree_map(element_size, self.B) 

        self.num_modalities = len(self.A)
        self.num_obs = jtu.tree_map(element_size, self.A)

        # Ensure consistency of A_dependencies with num_states and num_factors
        if A_dependencies is not None:
            self.A_dependencies = A_dependencies
        else:
            # assume full dependence of A matrices and state factors
            self.A_dependencies = [list(range(self.num_factors)) for _ in range(self.num_modalities)]
        
        for m in range(self.num_modalities):
            factor_dims = tuple([self.num_states[f] for f in self.A_dependencies[m]])
            assert self.A[m].shape[2:] == factor_dims, f"Please input an `A_dependencies` whose {m}-th indices correspond to the hidden state factors that line up with lagging dimensions of A[{m}]..." 
            if self.pA != None:
                assert self.pA[m].shape[2:] == factor_dims if self.pA[m] is not None else True, f"Please input an `A_dependencies` whose {m}-th indices correspond to the hidden state factors that line up with lagging dimensions of pA[{m}]..." 
            assert max(self.A_dependencies[m]) <= (self.num_factors - 1), f"Check modality {m} of `A_dependencies` - must be consistent with `num_states` and `num_factors`..."
           
        # Ensure consistency of B_dependencies with num_states and num_factors
        if B_dependencies is not None:
            self.B_dependencies = B_dependencies
        else:
            self.B_dependencies = [[f] for f in range(self.num_factors)] # defaults to having all factors depend only on themselves

        for f in range(self.num_factors):
            factor_dims = tuple([self.num_states[f] for f in self.B_dependencies[f]])
            assert self.B[f].shape[2:-1] == factor_dims, f"Please input a `B_dependencies` whose {f}-th indices pick out the hidden state factors that line up with the all-but-final lagging dimensions of B[{f}]..." 
            if self.pB != None:
                assert self.pB[f].shape[2:-1] == factor_dims, f"Please input a `B_dependencies` whose {f}-th indices pick out the hidden state factors that line up with the all-but-final lagging dimensions of pB[{f}]..." 
            assert max(self.B_dependencies[f]) <= (self.num_factors - 1), f"Check factor {f} of `B_dependencies` - must be consistent with `num_states` and `num_factors`..."

        self.batch_size = self.A[0].shape[0]

        self.gamma = jnp.broadcast_to(gamma, (self.batch_size,))
        self.alpha = jnp.broadcast_to(alpha, (self.batch_size,))
        self.inductive_threshold = jnp.broadcast_to(inductive_threshold, (self.batch_size,))
        self.inductive_epsilon = jnp.broadcast_to(inductive_epsilon, (self.batch_size,))

        ### Static parameters ###
        self.num_iter = num_iter
        self.inference_algo = inference_algo
        self.inductive_depth = inductive_depth

        # policy parameters
        self.policy_len = policy_len
        self.action_selection = action_selection
        self.sampling_mode = sampling_mode
        self.use_utility = use_utility
        self.use_states_info_gain = use_states_info_gain
        self.use_param_info_gain = use_param_info_gain
        self.use_inductive = use_inductive

        if self.use_inductive and self.H is not None:
            # print("Using inductive inference...")
            self.I = self._construct_I()
        elif self.use_inductive and I is not None:
            self.I = I
        else:
            self.I = jtu.tree_map(lambda x: jnp.expand_dims(jnp.zeros_like(x), 1), self.D)

        # learning parameters
        self.learn_A = learn_A
        self.learn_B = learn_B
        self.learn_C = learn_C
        self.learn_D = learn_D
        self.learn_E = learn_E

        """ Determine number of observation modalities and their respective dimensions """
        self.num_obs = [self.A[m].shape[1] for m in range(len(self.A))]
        self.num_modalities = len(self.num_obs)

        # If no `num_controls` are given, then this is inferred from the shapes of the input B matrices
        self.num_controls = [self.B[f].shape[-1] for f in range(self.num_factors)]

        # Users have the option to make only certain factors controllable.
        # default behaviour is to make all hidden state factors controllable
        # (i.e. self.num_states == self.num_controls)
        # Users have the option to make only certain factors controllable.
        # default behaviour is to make all hidden state factors controllable, i.e. `self.num_factors == len(self.num_controls)`
        if control_fac_idx == None:
            self.control_fac_idx = [f for f in range(self.num_factors) if self.num_controls[f] > 1]
        else:
            assert max(control_fac_idx) <= (self.num_factors - 1), "Check control_fac_idx - must be consistent with `num_states` and `num_factors`..."
            self.control_fac_idx = control_fac_idx

            for factor_idx in self.control_fac_idx:
                assert self.num_controls[factor_idx] > 1, "Control factor (and B matrix) dimensions are not consistent with user-given control_fac_idx"

        if policies is not None:
            self.policies = policies
        else:
            self._construct_policies()
        
        # set E to uniform/uninformative prior over policies if not given
        if E is None:
            self.E = jnp.ones((self.batch_size, len(self.policies)))/ len(self.policies)
        else:
            self.E = E

def _construct_policies(self):
        
        self.policies =  control.construct_policies(
            self.num_states, self.num_controls, self.policy_len, self.control_fac_idx
        )

def _construct_I(self):
        return control.generate_I_matrix(self.H, self.B, self.inductive_threshold, self.inductive_depth)

def unique_multiactions(self):
        size = pymath.prod(self.num_controls)
        return jnp.unique(self.policies[:, 0], axis=0, size=size, fill_value=-1)

def infer_parameters(self, beliefs_A, outcomes, actions, beliefs_B=None, lr_pA=1., lr_pB=1., **kwargs):
        agent = self
        beliefs_B = beliefs_A if beliefs_B is None else beliefs_B
        if self.inference_algo == 'ovf':
            smoothed_marginals_and_joints = vmap(inference.smoothing_ovf)(beliefs_A, self.B, actions)
            marginal_beliefs = smoothed_marginals_and_joints[0]
            joint_beliefs = smoothed_marginals_and_joints[1]
        else:
            marginal_beliefs = beliefs_A
            if self.learn_B:
                nf = len(beliefs_B)
                joint_fn = lambda f: [beliefs_B[f][:, 1:]] + [beliefs_B[f_idx][:, :-1] for f_idx in self.B_dependencies[f]]
                joint_beliefs = jtu.tree_map(joint_fn, list(range(nf)))

        if self.learn_A:
            update_A = partial(
                learning.update_obs_likelihood_dirichlet,
                A_dependencies=self.A_dependencies,
                num_obs=self.num_obs,
                onehot_obs=self.onehot_obs,
            )
            
            lr = jnp.broadcast_to(lr_pA, (self.batch_size,))
            qA, E_qA = vmap(update_A)(
                self.pA,
                self.A,
                outcomes,
                marginal_beliefs,
                lr=lr,
            )
            
            agent = tree_at(lambda x: (x.A, x.pA), agent, (E_qA, qA))
            
        if self.learn_B:
            assert beliefs_B[0].shape[1] == actions.shape[1] + 1
            update_B = partial(
                learning.update_state_transition_dirichlet,
                num_controls=self.num_controls
            )

            lr = jnp.broadcast_to(lr_pB, (self.batch_size,))
            qB, E_qB = vmap(update_B)(
                self.pB,
                joint_beliefs,
                actions,
                lr=lr
            )
            
            # if you have updated your beliefs about transitions, you need to re-compute the I matrix used for inductive inferenece
            if self.use_inductive and self.H is not None:
                I_updated = vmap(control.generate_I_matrix)(self.H, E_qB, self.inductive_threshold, self.inductive_depth)
            else:
                I_updated = self.I

            agent = tree_at(lambda x: (x.B, x.pB, x.I), agent, (E_qB, qB, I_updated))

        return agent

def infer_states(self, observations, empirical_prior, *, past_actions=None, qs_hist=None, mask=None):
        """
        Update approximate posterior over hidden states by solving variational inference problem, given an observation.

        Parameters
        ----------
        observations: ``list`` or ``tuple`` of ints
            The observation input. Each entry ``observation[m]`` stores one-hot vectors representing the observations for modality ``m``.
        past_actions: ``list`` or ``tuple`` of ints
            The action input. Each entry ``past_actions[f]`` stores indices (or one-hots?) representing the actions for control factor ``f``.
        empirical_prior: ``list`` or ``tuple`` of ``jax.numpy.ndarray`` of dtype object
            Empirical prior beliefs over hidden states. Depending on the inference algorithm chosen, the resulting ``empirical_prior`` variable may be a matrix (or list of matrices) 
            of additional dimensions to encode extra conditioning variables like timepoint and policy.
        Returns
        ---------
        qs: ``numpy.ndarray`` of dtype object
            Posterior beliefs over hidden states. Depending on the inference algorithm chosen, the resulting ``qs`` variable will have additional sub-structure to reflect whether
            beliefs are additionally conditioned on timepoint and policy.
            For example, in case the ``self.inference_algo == 'MMP' `` indexing structure is policy->timepoint-->factor, so that 
            ``qs[p_idx][t_idx][f_idx]`` refers to beliefs about marginal factor ``f_idx`` expected under policy ``p_idx`` 
            at timepoint ``t_idx``.
        """
        if not self.onehot_obs:
            o_vec = [nn.one_hot(o, self.num_obs[m]) for m, o in enumerate(observations)]
        else:
            o_vec = observations
        
        A = self.A
        if mask is not None:
            for i, m in enumerate(mask):
                o_vec[i] = m * o_vec[i] + (1 - m) * jnp.ones_like(o_vec[i]) / self.num_obs[i]
                A[i] = m * A[i] + (1 - m) * jnp.ones_like(A[i]) / self.num_obs[i]

        infer_states = partial(
            inference.update_posterior_states,
            A_dependencies=self.A_dependencies,
            B_dependencies=self.B_dependencies,
            num_iter=self.num_iter,
            method=self.inference_algo
        )
        
        output = vmap(infer_states)(
            A,
            self.B,
            o_vec,
            past_actions,
            prior=empirical_prior,
            qs_hist=qs_hist
        )

        return output

def update_empirical_prior(self, action, qs):
        # return empirical_prior, and the history of posterior beliefs (filtering distributions) held about hidden states at times 1, 2 ... t

        # this computation of the predictive prior is correct only for fully factorised Bs.
        if self.inference_algo in ['mmp', 'vmp']:
            # in the case of the 'mmp' or 'vmp' we have to use D as prior parameter for infer states
            pred = self.D
        else:
            qs_last = jtu.tree_map( lambda x: x[:, -1], qs)
            propagate_beliefs = partial(control.compute_expected_state, B_dependencies=self.B_dependencies)
            pred = vmap(propagate_beliefs)(qs_last, self.B, action)
        
        return (pred, qs)

def infer_policies(self, qs: List):
        """
        Perform policy inference by optimizing a posterior (categorical) distribution over policies.
        This distribution is computed as the softmax of ``G * gamma + lnE`` where ``G`` is the negative expected
        free energy of policies, ``gamma`` is a policy precision and ``lnE`` is the (log) prior probability of policies.
        This function returns the posterior over policies as well as the negative expected free energy of each policy.

        Returns
        ----------
        q_pi: 1D ``numpy.ndarray``
            Posterior beliefs over policies, i.e. a vector containing one posterior probability per policy.
        G: 1D ``numpy.ndarray``
            Negative expected free energies of each policy, i.e. a vector containing one negative expected free energy per policy.
        """

        latest_belief = jtu.tree_map(lambda x: x[:, -1], qs) # only get the posterior belief held at the current timepoint
        infer_policies = partial(
            control.update_posterior_policies_inductive,
            self.policies,
            A_dependencies=self.A_dependencies,
            B_dependencies=self.B_dependencies,
            use_utility=self.use_utility,
            use_states_info_gain=self.use_states_info_gain,
            use_param_info_gain=self.use_param_info_gain,
            use_inductive=self.use_inductive
        )

        q_pi, G = vmap(infer_policies)(
            latest_belief, 
            self.A,
            self.B,
            self.C,
            self.E,
            self.pA,
            self.pB,
            I = self.I,
            gamma=self.gamma,
            inductive_epsilon=self.inductive_epsilon
        )

        return q_pi, G

def multiaction_probabilities(self, q_pi: Array):
        """
        Compute probabilities of unique multi-actions from the posterior over policies.

        Parameters
        ----------
        q_pi: 1D ``numpy.ndarray``
        Posterior beliefs over policies, i.e. a vector containing one posterior probability per policy.
        
        Returns
        ----------
        multi-action: 1D ``jax.numpy.ndarray``
            Vector containing probabilities of possible multi-actions for different factors
        """

        if self.sampling_mode == "marginal":
            get_marginals = partial(control.get_marginals, policies=self.policies, num_controls=self.num_controls)
            marginals = get_marginals(q_pi)
            outer = lambda a, b: jnp.outer(a, b).reshape(-1)
            marginals = jtu.tree_reduce(outer, marginals)

        elif self.sampling_mode == "full":
            locs = jnp.all(
                self.policies[:, 0] == jnp.expand_dims(self.unique_multiactions, -2),
                  -1
            )
            get_marginals = lambda x: jnp.where(locs, x, 0.).sum(-1)
            marginals = vmap(get_marginals)(q_pi)

        return marginals

def sample_action(self, q_pi: Array, rng_key=None):
        """
        Sample or select a discrete action from the posterior over control states.
        
        Returns
        ----------
        action: 1D ``jax.numpy.ndarray``
            Vector containing the indices of the actions for each control factor
        action_probs: 2D ``jax.numpy.ndarray``
            Array of action probabilities
        """

        if (rng_key is None) and (self.action_selection == "stochastic"):
            raise ValueError("Please provide a random number generator key to sample actions stochastically")

        if self.sampling_mode == "marginal":
            sample_action = partial(control.sample_action, self.policies, self.num_controls, action_selection=self.action_selection)
            action = vmap(sample_action)(q_pi, alpha=self.alpha, rng_key=rng_key)
        elif self.sampling_mode == "full":
            sample_policy = partial(control.sample_policy, self.policies, action_selection=self.action_selection)
            action = vmap(sample_policy)(q_pi, alpha=self.alpha, rng_key=rng_key)

        return action

def _get_default_params(self):
        method = self.inference_algo
        default_params = None
        if method == "VANILLA":
            default_params = {"num_iter": 8, "dF": 1.0, "dF_tol": 0.001}
        elif method == "MMP":
            raise NotImplementedError("MMP is not implemented")
        elif method == "VMP":
            raise NotImplementedError("VMP is not implemented")
        elif method == "BP":
            raise NotImplementedError("BP is not implemented")
        elif method == "EP":
            raise NotImplementedError("EP is not implemented")
        elif method == "CV":
            raise NotImplementedError("CV is not implemented")

        return default_params

def update_posterior_states(
        A, 
        B, 
        obs, 
        past_actions, 
        prior=None, 
        qs_hist=None, 
        A_dependencies=None, 
        B_dependencies=None, 
        num_iter=16, 
        method='fpi'
    ):

    if method == 'fpi' or method == "ovf":
        # format obs to select only last observation
        curr_obs = jtu.tree_map(lambda x: x[-1], obs)
        qs = run_factorized_fpi(A, curr_obs, prior, A_dependencies, num_iter=num_iter)
    else:
        # format B matrices using action sequences here
        # TODO: past_actions can be None
        if past_actions is not None:
            nf = len(B)
            actions_tree = [past_actions[:, i] for i in range(nf)]
            
            # move time steps to the leading axis (leftmost)
            # this assumes that a policy is always specified as the rightmost axis of Bs
            B = jtu.tree_map(lambda b, a_idx: jnp.moveaxis(b[..., a_idx], -1, 0), B, actions_tree)
        else:
            B = None

        # outputs of both VMP and MMP should be a list of hidden state factors, where each qs[f].shape = (T, batch_dim, num_states_f)
        if method == 'vmp':
            qs = run_vmp(A, B, obs, prior, A_dependencies, B_dependencies, num_iter=num_iter) 
        if method == 'mmp':
            qs = run_mmp(A, B, obs, prior, A_dependencies, B_dependencies, num_iter=num_iter)
    
    if qs_hist is not None:
        if method == 'fpi' or method == "ovf":
            qs_hist = jtu.tree_map(lambda x, y: jnp.concatenate([x, jnp.expand_dims(y, 0)], 0), qs_hist, qs)
        else:
            #TODO: return entire history of beliefs
            qs_hist = qs
    else:
        if method == 'fpi' or method == "ovf":
            qs_hist = jtu.tree_map(lambda x: jnp.expand_dims(x, 0), qs)
        else:
            qs_hist = qs
    
    return qs_hist

def joint_dist_factor(b: ArrayLike, filtered_qs: list[Array], actions: Array):
    qs_last = filtered_qs[-1]
    qs_filter = filtered_qs[:-1]

    def step_fn(qs_smooth, xs):
        qs_f, action = xs
        time_b = b[..., action]
        qs_j = time_b * qs_f
        norm = qs_j.sum(-1, keepdims=True)
        if isinstance(norm, JAXSparse):
            norm = sparse.todense(norm)
        norm = jnp.where(norm == 0, eps, norm)
        qs_backward_cond = qs_j / norm
        qs_joint = qs_backward_cond * jnp.expand_dims(qs_smooth, -1)
        qs_smooth = qs_joint.sum(-2)
        if isinstance(qs_smooth, JAXSparse):
            qs_smooth = sparse.todense(qs_smooth)
        
        # returns q(s_t), (q(s_t), q(s_t, s_t+1))
        return qs_smooth, (qs_smooth, qs_joint)

    # seq_qs will contain a sequence of smoothed marginals and joints
    _, seq_qs = lax.scan(
        step_fn,
        qs_last,
        (qs_filter, actions),
        reverse=True,
        unroll=2
    )

    # we add the last filtered belief to smoothed beliefs

    qs_smooth_all = jnp.concatenate([seq_qs[0], jnp.expand_dims(qs_last, 0)], 0)
    qs_joint_all = seq_qs[1]
    if isinstance(qs_joint_all, JAXSparse):
        qs_joint_all.shape = (len(actions),) + qs_joint_all.shape
    return qs_smooth_all, qs_joint_all

def smoothing_ovf(filtered_post, B, past_actions):
    assert len(filtered_post) == len(B)
    nf = len(B)  # number of factors

    joint = lambda b, qs, f: joint_dist_factor(b, qs, past_actions[..., f])

    marginals_and_joints = ([], [])
    for b, qs, f in zip(B, filtered_post, list(range(nf))):
        marginals, joints = joint(b, qs, f)
        marginals_and_joints[0].append(marginals)
        marginals_and_joints[1].append(joints)

    return marginals_and_joints

def step_fn(qs_smooth, xs):
        qs_f, action = xs
        time_b = b[..., action]
        qs_j = time_b * qs_f
        norm = qs_j.sum(-1, keepdims=True)
        if isinstance(norm, JAXSparse):
            norm = sparse.todense(norm)
        norm = jnp.where(norm == 0, eps, norm)
        qs_backward_cond = qs_j / norm
        qs_joint = qs_backward_cond * jnp.expand_dims(qs_smooth, -1)
        qs_smooth = qs_joint.sum(-2)
        if isinstance(qs_smooth, JAXSparse):
            qs_smooth = sparse.todense(qs_smooth)
        
        # returns q(s_t), (q(s_t), q(s_t, s_t+1))
        return qs_smooth, (qs_smooth, qs_joint)

def update_obs_likelihood_dirichlet_m(pA_m, obs_m, qs, dependencies_m, lr=1.0):
    """ JAX version of ``pymdp.learning.update_obs_likelihood_dirichlet_m`` """
    # pA_m - parameters of the dirichlet from the prior
    # pA_m.shape = (no_m x num_states[k] x num_states[j] x ... x num_states[n]) where (k, j, n) are indices of the hidden state factors that are parents of modality m

    # \alpha^{*} = \alpha_{0} + \kappa * \sum_{t=t_begin}^{t=T} o_{m,t} \otimes \mathbf{s}_{f \in parents(m), t}

    # \alpha^{*} is the VFE-minimizing solution for the parameters of q(A)
    # \alpha_{0} are the Dirichlet parameters of p(A)
    # o_{m,t} = observation (one-hot vector) of modality m at time t
    # \mathbf{s}_{f \in parents(m), t} = categorical parameters of marginal posteriors over hidden state factors that are parents of modality m, at time t
    # \otimes is a multidimensional outer product, not just a outer product of two vectors
    # \kappa is an optional learning rate

    relevant_factors = tree_map(lambda f_idx: qs[f_idx], dependencies_m)

    dfda = vmap(multidimensional_outer)([obs_m] + relevant_factors).sum(axis=0)

    new_pA_m = pA_m + lr * dfda
    A_m = dirichlet_expected_value(new_pA_m)

    return new_pA_m, A_m

def update_obs_likelihood_dirichlet(pA, A, obs, qs, *, A_dependencies, onehot_obs, num_obs, lr):
    """ JAX version of ``pymdp.learning.update_obs_likelihood_dirichlet`` """

    obs_m = lambda o, dim: nn.one_hot(o, dim) if not onehot_obs else o
    update_A_fn = lambda pA_m, o_m, dim, dependencies_m: update_obs_likelihood_dirichlet_m(
        pA_m, obs_m(o_m, dim), qs, dependencies_m, lr=lr
    )
    result = tree_map(update_A_fn, pA, obs, num_obs, A_dependencies)
    qA = []
    E_qA = []
    for i, r in enumerate(result):
        if r is None:
            qA.append(r)
            E_qA.append(A[i])
        else:
            qA.append(r[0])
            E_qA.append(r[1])

    return qA, E_qA

def update_state_transition_dirichlet_f(pB_f, actions_f, joint_qs_f, lr=1.0):
    """ JAX version of ``pymdp.learning.update_state_likelihood_dirichlet_f`` """
    # pB_f - parameters of the dirichlet from the prior
    # pB_f.shape = (num_states[f] x num_states[f] x num_actions[f]) where f is the index of the hidden state factor

    # \alpha^{*} = \alpha_{0} + \kappa * \sum_{t=t_begin}^{t=T} \mathbf{s}_{f, t} \otimes \mathbf{s}_{f, t-1} \otimes \mathbf{a}_{f, t-1}

    # \alpha^{*} is the VFE-minimizing solution for the parameters of q(B)
    # \alpha_{0} are the Dirichlet parameters of p(B)
    # \mathbf{s}_{f, t} = categorical parameters of marginal posteriors over hidden state factor f, at time t
    # \mathbf{a}_{f, t-1} = categorical parameters of marginal posteriors over control factor f, at time t-1
    # \otimes is a multidimensional outer product, not just a outer product of two vectors
    # \kappa is an optional learning rate

    joint_qs_f = [joint_qs_f] if isinstance(joint_qs_f, Array) else joint_qs_f
    dfdb = vmap(multidimensional_outer)(joint_qs_f + [actions_f]).sum(axis=0)
    qB_f = pB_f + lr * dfdb

    return qB_f, dirichlet_expected_value(qB_f)

def update_state_transition_dirichlet(pB, joint_beliefs, actions, *, num_controls, lr):

    nf = len(pB)
    actions_onehot_fn = lambda f, dim: nn.one_hot(actions[..., f], dim, axis=-1)
    update_B_f_fn = lambda pB_f, joint_qs_f, f, na: update_state_transition_dirichlet_f(
        pB_f, actions_onehot_fn(f, na), joint_qs_f, lr=lr
    )    
    result = tree_map(
        update_B_f_fn, pB, joint_beliefs, list(range(nf)), num_controls
    )

    qB = []
    E_qB = []
    for r in result:
        qB.append(r[0])
        E_qB.append(r[1])

    return qB, E_qB

class GridWorldEnv(Env):
    """ 2-dimensional grid-world implementation with 5 actions (the 4 cardinal directions and staying put)."""

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    STAY = 4

    CONTROL_NAMES = ["UP", "RIGHT", "DOWN", "LEFT", "STAY"]

    def __init__(self, shape=[2, 2], init_state=None):
        """
        Initialization function for 2-D grid world

        Parameters
        ----------
        shape: ``list`` of ``int``, where ``len(shape) == 2``
            The dimensions of the grid world, stored as a list of integers, storing the discrete dimensions of the Y (vertical) and X (horizontal) spatial dimensions, respectively.
        init_state: ``int`` or ``None``
            Initial state of the environment, i.e. the location of the agent in grid world. If not ``None``, must be a discrete index  in the range ``(0, (shape[0] * shape[1])-1)``. It is thus a "linear index" of the initial location of the agent in grid world.
            If ``None``, then an initial location will be randomly sampled from the grid.
        """
        
        self.shape = shape
        self.n_states = np.prod(shape)
        self.n_observations = self.n_states
        self.n_control = 5
        self.max_y = shape[0]
        self.max_x = shape[1]
        self._build()
        self.set_init_state(init_state)
        self.last_action = None

    def reset(self, init_state=None):
        """
        Reset the state of the 2-D grid world. In other words, resets the location of the agent, and wipes the current action.

        Parameters
        ----------
        init_state: ``int`` or ``None``
            Initial state of the environment, i.e. the location of the agent in grid world. If not ``None``, must be a discrete index  in the range ``(0, (shape[0] * shape[1])-1)``. It is thus a "linear index" of the initial location of the agent in grid world.
            If ``None``, then an initial location will be randomly sampled from the grid.

        Returns
        ----------
        self.state: ``int``
            The current state of the environment, i.e. the location of the agent in grid world. Will be a discrete index  in the range ``(0, (shape[0] * shape[1])-1)``. It is thus a "linear index" of the location of the agent in grid world.
        """
        self.set_init_state(init_state)
        self.last_action = None
        return self.state

    def set_state(self, state):
        """
        Sets the state of the 2-D grid world.

        Parameters
        ----------
        state: ``int`` or ``None``
            State of the environment, i.e. the location of the agent in grid world. If not ``None``, must be a discrete index  in the range ``(0, (shape[0] * shape[1])-1)``. It is thus a "linear index" of the location of the agent in grid world.
            If ``None``, then a location will be randomly sampled from the grid.

        Returns
        ----------
        self.state: ``int``
            The current state of the environment, i.e. the location of the agent in grid world. Will be a discrete index  in the range ``(0, (shape[0] * shape[1])-1)``. It is thus a "linear index" of the location of the agent in grid world.
        """
        self.state = state
        return state

    def step(self, action):
        """
        Updates the state of the environment, i.e. the location of the agent, using an action index that corresponds to one of the 5 possible moves.

        Parameters
        ----------
        action: ``int`` 
            Action index that refers to which of the 5 actions the agent will take. Actions are, in order: "UP", "RIGHT", "DOWN", "LEFT", "STAY".

        Returns
        ----------
        state: ``int``
            The new, updated state of the environment, i.e. the location of the agent in grid world after the action has been made. Will be discrete index in the range ``(0, (shape[0] * shape[1])-1)``. It is thus a "linear index" of the location of the agent in grid world.
        """
        state = self.P[self.state][action]
        self.state = state
        self.last_action = action
        return state

    def render(self, title=None):
        """
        Creates a heatmap showing the current position of the agent in the grid world.

        Parameters
        ----------
        title: ``str`` or ``None``
            Optional title for the heatmap.
        """
        values = np.zeros(self.shape)
        values[self.position] = 1.0
        _, ax = plt.subplots(figsize=(3, 3))
        if self.shape[0] == 1 or self.shape[1] == 1:
            ax.imshow(values, cmap="OrRd")
        else:
            _ = sns.heatmap(values, cmap="OrRd", linewidth=2.5, cbar=False, ax=ax)
        plt.xticks(range(self.shape[1]))
        plt.yticks(range(self.shape[0]))
        if title != None:
            plt.title(title)
        plt.show()

    def set_init_state(self, init_state=None):
        if init_state != None:
            if init_state > (self.n_states - 1) or init_state < 0:
                raise ValueError("`init_state` is greater than number of states")
            if not isinstance(init_state, (int, float)):
                raise ValueError("`init_state` must be [int/float]")
            self.init_state = int(init_state)
        else:
            self.init_state = np.random.randint(0, self.n_states)
        self.state = self.init_state

    def _build(self):
        P = {}
        grid = np.arange(self.n_states).reshape(self.shape)
        it = np.nditer(grid, flags=["multi_index"])

        while not it.finished:
            s = it.iterindex
            y, x = it.multi_index
            P[s] = {a: [] for a in range(self.n_control)}

            next_up = s if y == 0 else s - self.max_x
            next_right = s if x == (self.max_x - 1) else s + 1
            next_down = s if y == (self.max_y - 1) else s + self.max_x
            next_left = s if x == 0 else s - 1
            next_stay = s

            P[s][self.UP] = next_up
            P[s][self.RIGHT] = next_right
            P[s][self.DOWN] = next_down
            P[s][self.LEFT] = next_left
            P[s][self.STAY] = next_stay

            it.iternext()

        self.P = P

    def get_init_state_dist(self, init_state=None):
        init_state_dist = np.zeros(self.n_states)
        if init_state == None:
            init_state_dist[self.init_state] = 1.0
        else:
            init_state_dist[init_state] = 1.0

    def get_transition_dist(self):
        B = np.zeros([self.n_states, self.n_states, self.n_control])
        for s in range(self.n_states):
            for a in range(self.n_control):
                ns = int(self.P[s][a])
                B[ns, s, a] = 1
        return B

    def get_likelihood_dist(self):
        A = np.eye(self.n_observations, self.n_states)
        return A

    def sample_action(self):
        return np.random.randint(self.n_control)

    @property
    def position(self):
        """ @TODO might be wrong w.r.t (x & y) """
        return np.unravel_index(np.array(self.state), self.shape)

class DGridWorldEnv(object):
    """ 1-dimensional grid-world implementation with 3 possible movement actions ("LEFT", "STAY", "RIGHT")"""

    LEFT = 0
    STAY = 1
    RIGHT = 2

    CONTROL_NAMES = ["LEFT", "STAY", "RIGHT"]

    def __init__(self, shape=[2, 2], init_state=None):
        self.shape = shape
        self.n_states = np.prod(shape)
        self.n_observations = self.n_states
        self.n_control = 3
        self.max_y = shape[0]
        self.max_x = shape[1]
        self._build()
        self.set_init_state(init_state)
        self.last_action = None

    def reset(self, init_state=None):
        self.set_init_state(init_state)
        self.last_action = None
        return self.state

    def set_state(self, state):
        self.state = state
        return state

    def step(self, action):
        state = self.P[self.state][action]
        self.state = state
        self.last_action = action
        return state

    def render(self, title=None):
        values = np.zeros(self.shape)
        values[self.position] = 1.0
        _, ax = plt.subplots(figsize=(3, 3))
        if self.shape[0] == 1 or self.shape[1] == 1:
            ax.imshow(values, cmap="OrRd")
        else:
            _ = sns.heatmap(values, cmap="OrRd", linewidth=2.5, cbar=False, ax=ax)
        plt.xticks(range(self.shape[1]))
        plt.yticks(range(self.shape[0]))
        if title != None:
            plt.title(title)
        plt.show()

    def set_init_state(self, init_state=None):
        if init_state != None:
            if init_state > (self.n_states - 1) or init_state < 0:
                raise ValueError("`init_state` is greater than number of states")
            if not isinstance(init_state, (int, float)):
                raise ValueError("`init_state` must be [int/float]")
            self.init_state = int(init_state)
        else:
            self.init_state = np.random.randint(0, self.n_states)
        self.state = self.init_state

    def _build(self):
        P = {}
        grid = np.arange(self.n_states).reshape(self.shape)
        it = np.nditer(grid, flags=["multi_index"])

        while not it.finished:
            s = it.iterindex
            y, x = it.multi_index
            P[s] = {a: [] for a in range(self.n_control)}

            next_right = s if x == (self.max_x - 1) else s + 1
            next_left = s if x == 0 else s - 1
            next_stay = s

            P[s][self.LEFT] = next_left
            P[s][self.STAY] = next_stay
            P[s][self.RIGHT] = next_right

            it.iternext()

        self.P = P

    def get_init_state_dist(self, init_state=None):
        init_state_dist = np.zeros(self.n_states)
        if init_state == None:
            init_state_dist[self.init_state] = 1.0
        else:
            init_state_dist[init_state] = 1.0

    def get_transition_dist(self):
        B = np.zeros([self.n_states, self.n_states, self.n_control])
        for s in range(self.n_states):
            for a in range(self.n_control):
                ns = int(self.P[s][a])
                B[ns, s, a] = 1
        return B

    def get_likelihood_dist(self):
        A = np.eye(self.n_observations, self.n_states)
        return A

    def sample_action(self):
        return np.random.randint(self.n_control)

    @property
    def position(self):
        return self.state

def __init__(self, shape=[2, 2], init_state=None):
        """
        Initialization function for 2-D grid world

        Parameters
        ----------
        shape: ``list`` of ``int``, where ``len(shape) == 2``
            The dimensions of the grid world, stored as a list of integers, storing the discrete dimensions of the Y (vertical) and X (horizontal) spatial dimensions, respectively.
        init_state: ``int`` or ``None``
            Initial state of the environment, i.e. the location of the agent in grid world. If not ``None``, must be a discrete index  in the range ``(0, (shape[0] * shape[1])-1)``. It is thus a "linear index" of the initial location of the agent in grid world.
            If ``None``, then an initial location will be randomly sampled from the grid.
        """
        
        self.shape = shape
        self.n_states = np.prod(shape)
        self.n_observations = self.n_states
        self.n_control = 5
        self.max_y = shape[0]
        self.max_x = shape[1]
        self._build()
        self.set_init_state(init_state)
        self.last_action = None

def reset(self, init_state=None):
        """
        Reset the state of the 2-D grid world. In other words, resets the location of the agent, and wipes the current action.

        Parameters
        ----------
        init_state: ``int`` or ``None``
            Initial state of the environment, i.e. the location of the agent in grid world. If not ``None``, must be a discrete index  in the range ``(0, (shape[0] * shape[1])-1)``. It is thus a "linear index" of the initial location of the agent in grid world.
            If ``None``, then an initial location will be randomly sampled from the grid.

        Returns
        ----------
        self.state: ``int``
            The current state of the environment, i.e. the location of the agent in grid world. Will be a discrete index  in the range ``(0, (shape[0] * shape[1])-1)``. It is thus a "linear index" of the location of the agent in grid world.
        """
        self.set_init_state(init_state)
        self.last_action = None
        return self.state

def set_state(self, state):
        """
        Sets the state of the 2-D grid world.

        Parameters
        ----------
        state: ``int`` or ``None``
            State of the environment, i.e. the location of the agent in grid world. If not ``None``, must be a discrete index  in the range ``(0, (shape[0] * shape[1])-1)``. It is thus a "linear index" of the location of the agent in grid world.
            If ``None``, then a location will be randomly sampled from the grid.

        Returns
        ----------
        self.state: ``int``
            The current state of the environment, i.e. the location of the agent in grid world. Will be a discrete index  in the range ``(0, (shape[0] * shape[1])-1)``. It is thus a "linear index" of the location of the agent in grid world.
        """
        self.state = state
        return state

def step(self, action):
        """
        Updates the state of the environment, i.e. the location of the agent, using an action index that corresponds to one of the 5 possible moves.

        Parameters
        ----------
        action: ``int`` 
            Action index that refers to which of the 5 actions the agent will take. Actions are, in order: "UP", "RIGHT", "DOWN", "LEFT", "STAY".

        Returns
        ----------
        state: ``int``
            The new, updated state of the environment, i.e. the location of the agent in grid world after the action has been made. Will be discrete index in the range ``(0, (shape[0] * shape[1])-1)``. It is thus a "linear index" of the location of the agent in grid world.
        """
        state = self.P[self.state][action]
        self.state = state
        self.last_action = action
        return state

def render(self, title=None):
        """
        Creates a heatmap showing the current position of the agent in the grid world.

        Parameters
        ----------
        title: ``str`` or ``None``
            Optional title for the heatmap.
        """
        values = np.zeros(self.shape)
        values[self.position] = 1.0
        _, ax = plt.subplots(figsize=(3, 3))
        if self.shape[0] == 1 or self.shape[1] == 1:
            ax.imshow(values, cmap="OrRd")
        else:
            _ = sns.heatmap(values, cmap="OrRd", linewidth=2.5, cbar=False, ax=ax)
        plt.xticks(range(self.shape[1]))
        plt.yticks(range(self.shape[0]))
        if title != None:
            plt.title(title)
        plt.show()

def set_init_state(self, init_state=None):
        if init_state != None:
            if init_state > (self.n_states - 1) or init_state < 0:
                raise ValueError("`init_state` is greater than number of states")
            if not isinstance(init_state, (int, float)):
                raise ValueError("`init_state` must be [int/float]")
            self.init_state = int(init_state)
        else:
            self.init_state = np.random.randint(0, self.n_states)
        self.state = self.init_state

def _build(self):
        P = {}
        grid = np.arange(self.n_states).reshape(self.shape)
        it = np.nditer(grid, flags=["multi_index"])

        while not it.finished:
            s = it.iterindex
            y, x = it.multi_index
            P[s] = {a: [] for a in range(self.n_control)}

            next_up = s if y == 0 else s - self.max_x
            next_right = s if x == (self.max_x - 1) else s + 1
            next_down = s if y == (self.max_y - 1) else s + self.max_x
            next_left = s if x == 0 else s - 1
            next_stay = s

            P[s][self.UP] = next_up
            P[s][self.RIGHT] = next_right
            P[s][self.DOWN] = next_down
            P[s][self.LEFT] = next_left
            P[s][self.STAY] = next_stay

            it.iternext()

        self.P = P

def get_init_state_dist(self, init_state=None):
        init_state_dist = np.zeros(self.n_states)
        if init_state == None:
            init_state_dist[self.init_state] = 1.0
        else:
            init_state_dist[init_state] = 1.0

def get_transition_dist(self):
        B = np.zeros([self.n_states, self.n_states, self.n_control])
        for s in range(self.n_states):
            for a in range(self.n_control):
                ns = int(self.P[s][a])
                B[ns, s, a] = 1
        return B

def get_likelihood_dist(self):
        A = np.eye(self.n_observations, self.n_states)
        return A

def sample_action(self):
        return np.random.randint(self.n_control)

def position(self):
        """ @TODO might be wrong w.r.t (x & y) """
        return np.unravel_index(np.array(self.state), self.shape)

def __init__(self, shape=[2, 2], init_state=None):
        self.shape = shape
        self.n_states = np.prod(shape)
        self.n_observations = self.n_states
        self.n_control = 3
        self.max_y = shape[0]
        self.max_x = shape[1]
        self._build()
        self.set_init_state(init_state)
        self.last_action = None

def reset(self, init_state=None):
        self.set_init_state(init_state)
        self.last_action = None
        return self.state

def set_state(self, state):
        self.state = state
        return state

def step(self, action):
        state = self.P[self.state][action]
        self.state = state
        self.last_action = action
        return state

def render(self, title=None):
        values = np.zeros(self.shape)
        values[self.position] = 1.0
        _, ax = plt.subplots(figsize=(3, 3))
        if self.shape[0] == 1 or self.shape[1] == 1:
            ax.imshow(values, cmap="OrRd")
        else:
            _ = sns.heatmap(values, cmap="OrRd", linewidth=2.5, cbar=False, ax=ax)
        plt.xticks(range(self.shape[1]))
        plt.yticks(range(self.shape[0]))
        if title != None:
            plt.title(title)
        plt.show()

def set_init_state(self, init_state=None):
        if init_state != None:
            if init_state > (self.n_states - 1) or init_state < 0:
                raise ValueError("`init_state` is greater than number of states")
            if not isinstance(init_state, (int, float)):
                raise ValueError("`init_state` must be [int/float]")
            self.init_state = int(init_state)
        else:
            self.init_state = np.random.randint(0, self.n_states)
        self.state = self.init_state

def _build(self):
        P = {}
        grid = np.arange(self.n_states).reshape(self.shape)
        it = np.nditer(grid, flags=["multi_index"])

        while not it.finished:
            s = it.iterindex
            y, x = it.multi_index
            P[s] = {a: [] for a in range(self.n_control)}

            next_right = s if x == (self.max_x - 1) else s + 1
            next_left = s if x == 0 else s - 1
            next_stay = s

            P[s][self.LEFT] = next_left
            P[s][self.STAY] = next_stay
            P[s][self.RIGHT] = next_right

            it.iternext()

        self.P = P

def get_init_state_dist(self, init_state=None):
        init_state_dist = np.zeros(self.n_states)
        if init_state == None:
            init_state_dist[self.init_state] = 1.0
        else:
            init_state_dist[init_state] = 1.0

def get_transition_dist(self):
        B = np.zeros([self.n_states, self.n_states, self.n_control])
        for s in range(self.n_states):
            for a in range(self.n_control):
                ns = int(self.P[s][a])
                B[ns, s, a] = 1
        return B

def get_likelihood_dist(self):
        A = np.eye(self.n_observations, self.n_states)
        return A

def sample_action(self):
        return np.random.randint(self.n_control)

def position(self):
        return self.state

class TMazeEnv(Env):
    """ Implementation of the 3-arm T-Maze environment """
    def __init__(self, reward_probs=None):

        if reward_probs is None:
            a = 0.98
            b = 1.0 - a
            self.reward_probs = [a, b]
        else:
            if sum(reward_probs) != 1:
                raise ValueError("Reward probabilities must sum to 1!")
            elif len(reward_probs) != 2:
                raise ValueError("Only two reward conditions currently supported...")
            else:
                self.reward_probs = reward_probs

        self.num_states = [4, 2]
        self.num_locations = self.num_states[LOCATION_FACTOR_ID]
        self.num_controls = [self.num_locations, 1]
        self.num_reward_conditions = self.num_states[TRIAL_FACTOR_ID]
        self.num_cues = self.num_reward_conditions
        self.num_obs = [self.num_locations, self.num_reward_conditions + 1, self.num_cues]
        self.num_factors = len(self.num_states)
        self.num_modalities = len(self.num_obs)

        self._transition_dist = self._construct_transition_dist()
        self._likelihood_dist = self._construct_likelihood_dist()

        self._reward_condition = None
        self._state = None
    
    def reset(self, state=None):
        if state is None:
            loc_state = utils.onehot(0, self.num_locations)
            
            self._reward_condition = np.random.randint(self.num_reward_conditions) # randomly select a reward condition
            reward_condition = utils.onehot(self._reward_condition, self.num_reward_conditions)

            full_state = utils.obj_array(self.num_factors)
            full_state[LOCATION_FACTOR_ID] = loc_state
            full_state[TRIAL_FACTOR_ID] = reward_condition
            self._state = full_state
        else:
            self._state = state
        return self._get_observation()

    def step(self, actions):
        prob_states = utils.obj_array(self.num_factors)
        for factor, state in enumerate(self._state):
            prob_states[factor] = self._transition_dist[factor][:, :, int(actions[factor])].dot(state)
        state = [utils.sample(ps_i) for ps_i in prob_states]
        self._state = self._construct_state(state)
        return self._get_observation()

    def render(self):
        pass

    def sample_action(self):
        return [np.random.randint(self.num_controls[i]) for i in range(self.num_factors)]

    def get_likelihood_dist(self):
        return self._likelihood_dist

    def get_transition_dist(self):
        return self._transition_dist


    def get_rand_likelihood_dist(self):
        pass

    def get_rand_transition_dist(self):
        pass

    def _get_observation(self):

        prob_obs = [maths.spm_dot(A_m, self._state) for A_m in self._likelihood_dist]

        obs = [utils.sample(po_i) for po_i in prob_obs]
        return obs

    def _construct_transition_dist(self):
        B_locs = np.eye(self.num_locations)
        B_locs = B_locs.reshape(self.num_locations, self.num_locations, 1)
        B_locs = np.tile(B_locs, (1, 1, self.num_locations))
        B_locs = B_locs.transpose(1, 2, 0)

        B = utils.obj_array(self.num_factors)

        B[LOCATION_FACTOR_ID] = B_locs
        B[TRIAL_FACTOR_ID] = np.eye(self.num_reward_conditions).reshape(
            self.num_reward_conditions, self.num_reward_conditions, 1
        )
        return B

    def _construct_likelihood_dist(self):

        A = utils.obj_array_zeros([ [obs_dim] + self.num_states for obs_dim in self.num_obs] )

        for loc in range(self.num_states[LOCATION_FACTOR_ID]):
            for reward_condition in range(self.num_states[TRIAL_FACTOR_ID]):

                # The case when the agent is in the centre location
                if loc == 0:
                    # When in the centre location, reward observation is always 'no reward'
                    # or the outcome with index 0
                    A[REWARD_MODALITY_ID][0, loc, reward_condition] = 1.0

                    # When in the centre location, cue is totally ambiguous with respect to the reward condition
                    A[CUE_MODALITY_ID][:, loc, reward_condition] = 1.0 / self.num_obs[2]

                # The case when loc == 3, or the cue location ('bottom arm')
                elif loc == 3:

                    # When in the cue location, reward observation is always 'no reward'
                    # or the outcome with index 0
                    A[REWARD_MODALITY_ID][0, loc, reward_condition] = 1.0

                    # When in the cue location, the cue indicates the reward condition umambiguously
                    # signals where the reward is located
                    A[CUE_MODALITY_ID][reward_condition, loc, reward_condition] = 1.0

                # The case when the agent is in one of the (potentially-) rewarding armS
                else:

                    # When location is consistent with reward condition
                    if loc == (reward_condition + 1):
                        # Means highest probability is concentrated over reward outcome
                        high_prob_idx = REWARD_IDX
                        # Lower probability on loss outcome
                        low_prob_idx = LOSS_IDX
                    else:
                        # Means highest probability is concentrated over loss outcome
                        high_prob_idx = LOSS_IDX
                        # Lower probability on reward outcome
                        low_prob_idx = REWARD_IDX

                    reward_probs = self.reward_probs[0]
                    A[REWARD_MODALITY_ID][high_prob_idx, loc, reward_condition] = reward_probs

                    reward_probs = self.reward_probs[1]
                    A[REWARD_MODALITY_ID][low_prob_idx, loc, reward_condition] = reward_probs

                    # Cue is ambiguous when in the reward location
                    A[CUE_MODALITY_ID][:, loc, reward_condition] = 1.0 / self.num_obs[2]

                # The agent always observes its location, regardless of the reward condition
                A[LOCATION_MODALITY_ID][loc, loc, reward_condition] = 1.0

        return A

    def _construct_state(self, state_tuple):

        state = utils.obj_array(self.num_factors)
        for f, ns in enumerate(self.num_states):
            state[f] = utils.onehot(state_tuple[f], ns)

        return state

    @property
    def state(self):
        return self._state

    @property
    def reward_condition(self):
        return self._reward_condition

class TMazeEnvNullOutcome(Env):
    """ Implementation of the 3-arm T-Maze environment where there is an additional null outcome within the cue modality, so that the agent
    doesn't get a random cue observation, but a null one, when it visits non-cue locations"""

    def __init__(self, reward_probs=None):

        if reward_probs is None:
            a = 0.98
            b = 1.0 - a
            self.reward_probs = [a, b]
        else:
            if sum(reward_probs) != 1:
                raise ValueError("Reward probabilities must sum to 1!")
            elif len(reward_probs) != 2:
                raise ValueError("Only two reward conditions currently supported...")
            else:
                self.reward_probs = reward_probs

        self.num_states = [4, 2]
        self.num_locations = self.num_states[LOCATION_FACTOR_ID]
        self.num_controls = [self.num_locations, 1]
        self.num_reward_conditions = self.num_states[TRIAL_FACTOR_ID]
        self.num_cues = self.num_reward_conditions
        self.num_obs = [self.num_locations, self.num_reward_conditions + 1, self.num_cues + 1]
        self.num_factors = len(self.num_states)
        self.num_modalities = len(self.num_obs)

        self._transition_dist = self._construct_transition_dist()
        self._likelihood_dist = self._construct_likelihood_dist()

        self._reward_condition = None
        self._state = None

    def reset(self, state=None):
        if state is None:
            loc_state = utils.onehot(0, self.num_locations)
            
            self._reward_condition = np.random.randint(self.num_reward_conditions) # randomly select a reward condition
            reward_condition = utils.onehot(self._reward_condition, self.num_reward_conditions)

            full_state = utils.obj_array(self.num_factors)
            full_state[LOCATION_FACTOR_ID] = loc_state
            full_state[TRIAL_FACTOR_ID] = reward_condition
            self._state = full_state
        else:
            self._state = state
        return self._get_observation()

    def step(self, actions):
        prob_states = utils.obj_array(self.num_factors)
        for factor, state in enumerate(self._state):
            prob_states[factor] = self._transition_dist[factor][:, :, int(actions[factor])].dot(state)
        state = [utils.sample(ps_i) for ps_i in prob_states]
        self._state = self._construct_state(state)
        return self._get_observation()


    def sample_action(self):
        return [np.random.randint(self.num_controls[i]) for i in range(self.num_factors)]

    def get_likelihood_dist(self):
        return self._likelihood_dist.copy()

    def get_transition_dist(self):
        return self._transition_dist.copy()

    def _get_observation(self):

        prob_obs = [maths.spm_dot(A_m, self._state) for A_m in self._likelihood_dist]

        obs = [utils.sample(po_i) for po_i in prob_obs]
        return obs

    def _construct_transition_dist(self):
        B_locs = np.eye(self.num_locations)
        B_locs = B_locs.reshape(self.num_locations, self.num_locations, 1)
        B_locs = np.tile(B_locs, (1, 1, self.num_locations))
        B_locs = B_locs.transpose(1, 2, 0)

        B = utils.obj_array(self.num_factors)

        B[LOCATION_FACTOR_ID] = B_locs
        B[TRIAL_FACTOR_ID] = np.eye(self.num_reward_conditions).reshape(
            self.num_reward_conditions, self.num_reward_conditions, 1
        )
        return B

    def _construct_likelihood_dist(self):

        A = utils.obj_array_zeros([ [obs_dim] + self.num_states for _, obs_dim in enumerate(self.num_obs)] )
        
        for loc in range(self.num_states[LOCATION_FACTOR_ID]):
            for reward_condition in range(self.num_states[TRIAL_FACTOR_ID]):

                if loc == 0:  # the case when the agent is in the centre location
                    # When in the centre location, reward observation is always 'no reward', or the outcome with index 0
                    A[REWARD_MODALITY_ID][0, loc, reward_condition] = 1.0

                    # When in the center location, cue observation is always 'no cue', or the outcome with index 0
                    A[CUE_MODALITY_ID][0, loc, reward_condition] = 1.0

                # The case when loc == 3, or the cue location ('bottom arm')
                elif loc == 3:

                    # When in the cue location, reward observation is always 'no reward', or the outcome with index 0
                    A[REWARD_MODALITY_ID][0, loc, reward_condition] = 1.0

                    # When in the cue location, the cue indicates the reward condition umambiguously
                    # signals where the reward is located
                    A[CUE_MODALITY_ID][reward_condition + 1, loc, reward_condition] = 1.0

                # The case when the agent is in one of the (potentially-) rewarding arms
                else:

                    # When location is consistent with reward condition
                    if loc == (reward_condition + 1):
                        # Means highest probability is concentrated over reward outcome
                        high_prob_idx = REWARD_IDX
                        # Lower probability on loss outcome
                        low_prob_idx = LOSS_IDX  #
                    else:
                        # Means highest probability is concentrated over loss outcome
                        high_prob_idx = LOSS_IDX
                        # Lower probability on reward outcome
                        low_prob_idx = REWARD_IDX

                    reward_probs = self.reward_probs[0]
                    A[REWARD_MODALITY_ID][high_prob_idx, loc, reward_condition] = reward_probs
                    reward_probs = self.reward_probs[1]
                    A[REWARD_MODALITY_ID][low_prob_idx, loc, reward_condition] = reward_probs

                    # When in the one of the rewarding arms, cue observation is always 'no cue', or the outcome with index 0
                    A[CUE_MODALITY_ID][0, loc, reward_condition] = 1.0

                # The agent always observes its location, regardless of the reward condition
                A[LOCATION_MODALITY_ID][loc, loc, reward_condition] = 1.0

        return A

    def _construct_state(self, state_tuple):

        state = utils.obj_array(self.num_factors)

        for f, ns in enumerate(self.num_states):
            state[f] = utils.onehot(state_tuple[f], ns)
            
        return state

    @property
    def state(self):
        return self._state

    @property
    def reward_condition(self):
        return self._reward_condition

def __init__(self, reward_probs=None):

        if reward_probs is None:
            a = 0.98
            b = 1.0 - a
            self.reward_probs = [a, b]
        else:
            if sum(reward_probs) != 1:
                raise ValueError("Reward probabilities must sum to 1!")
            elif len(reward_probs) != 2:
                raise ValueError("Only two reward conditions currently supported...")
            else:
                self.reward_probs = reward_probs

        self.num_states = [4, 2]
        self.num_locations = self.num_states[LOCATION_FACTOR_ID]
        self.num_controls = [self.num_locations, 1]
        self.num_reward_conditions = self.num_states[TRIAL_FACTOR_ID]
        self.num_cues = self.num_reward_conditions
        self.num_obs = [self.num_locations, self.num_reward_conditions + 1, self.num_cues]
        self.num_factors = len(self.num_states)
        self.num_modalities = len(self.num_obs)

        self._transition_dist = self._construct_transition_dist()
        self._likelihood_dist = self._construct_likelihood_dist()

        self._reward_condition = None
        self._state = None

def reset(self, state=None):
        if state is None:
            loc_state = utils.onehot(0, self.num_locations)
            
            self._reward_condition = np.random.randint(self.num_reward_conditions) # randomly select a reward condition
            reward_condition = utils.onehot(self._reward_condition, self.num_reward_conditions)

            full_state = utils.obj_array(self.num_factors)
            full_state[LOCATION_FACTOR_ID] = loc_state
            full_state[TRIAL_FACTOR_ID] = reward_condition
            self._state = full_state
        else:
            self._state = state
        return self._get_observation()

def step(self, actions):
        prob_states = utils.obj_array(self.num_factors)
        for factor, state in enumerate(self._state):
            prob_states[factor] = self._transition_dist[factor][:, :, int(actions[factor])].dot(state)
        state = [utils.sample(ps_i) for ps_i in prob_states]
        self._state = self._construct_state(state)
        return self._get_observation()

def render(self):
        pass

def sample_action(self):
        return [np.random.randint(self.num_controls[i]) for i in range(self.num_factors)]

def get_likelihood_dist(self):
        return self._likelihood_dist

def get_transition_dist(self):
        return self._transition_dist

def get_rand_likelihood_dist(self):
        pass

def get_rand_transition_dist(self):
        pass

def _get_observation(self):

        prob_obs = [maths.spm_dot(A_m, self._state) for A_m in self._likelihood_dist]

        obs = [utils.sample(po_i) for po_i in prob_obs]
        return obs

def _construct_transition_dist(self):
        B_locs = np.eye(self.num_locations)
        B_locs = B_locs.reshape(self.num_locations, self.num_locations, 1)
        B_locs = np.tile(B_locs, (1, 1, self.num_locations))
        B_locs = B_locs.transpose(1, 2, 0)

        B = utils.obj_array(self.num_factors)

        B[LOCATION_FACTOR_ID] = B_locs
        B[TRIAL_FACTOR_ID] = np.eye(self.num_reward_conditions).reshape(
            self.num_reward_conditions, self.num_reward_conditions, 1
        )
        return B

def _construct_likelihood_dist(self):

        A = utils.obj_array_zeros([ [obs_dim] + self.num_states for obs_dim in self.num_obs] )

        for loc in range(self.num_states[LOCATION_FACTOR_ID]):
            for reward_condition in range(self.num_states[TRIAL_FACTOR_ID]):

                # The case when the agent is in the centre location
                if loc == 0:
                    # When in the centre location, reward observation is always 'no reward'
                    # or the outcome with index 0
                    A[REWARD_MODALITY_ID][0, loc, reward_condition] = 1.0

                    # When in the centre location, cue is totally ambiguous with respect to the reward condition
                    A[CUE_MODALITY_ID][:, loc, reward_condition] = 1.0 / self.num_obs[2]

                # The case when loc == 3, or the cue location ('bottom arm')
                elif loc == 3:

                    # When in the cue location, reward observation is always 'no reward'
                    # or the outcome with index 0
                    A[REWARD_MODALITY_ID][0, loc, reward_condition] = 1.0

                    # When in the cue location, the cue indicates the reward condition umambiguously
                    # signals where the reward is located
                    A[CUE_MODALITY_ID][reward_condition, loc, reward_condition] = 1.0

                # The case when the agent is in one of the (potentially-) rewarding armS
                else:

                    # When location is consistent with reward condition
                    if loc == (reward_condition + 1):
                        # Means highest probability is concentrated over reward outcome
                        high_prob_idx = REWARD_IDX
                        # Lower probability on loss outcome
                        low_prob_idx = LOSS_IDX
                    else:
                        # Means highest probability is concentrated over loss outcome
                        high_prob_idx = LOSS_IDX
                        # Lower probability on reward outcome
                        low_prob_idx = REWARD_IDX

                    reward_probs = self.reward_probs[0]
                    A[REWARD_MODALITY_ID][high_prob_idx, loc, reward_condition] = reward_probs

                    reward_probs = self.reward_probs[1]
                    A[REWARD_MODALITY_ID][low_prob_idx, loc, reward_condition] = reward_probs

                    # Cue is ambiguous when in the reward location
                    A[CUE_MODALITY_ID][:, loc, reward_condition] = 1.0 / self.num_obs[2]

                # The agent always observes its location, regardless of the reward condition
                A[LOCATION_MODALITY_ID][loc, loc, reward_condition] = 1.0

        return A

def _construct_state(self, state_tuple):

        state = utils.obj_array(self.num_factors)
        for f, ns in enumerate(self.num_states):
            state[f] = utils.onehot(state_tuple[f], ns)

        return state

def state(self):
        return self._state

def reward_condition(self):
        return self._reward_condition

def __init__(self, reward_probs=None):

        if reward_probs is None:
            a = 0.98
            b = 1.0 - a
            self.reward_probs = [a, b]
        else:
            if sum(reward_probs) != 1:
                raise ValueError("Reward probabilities must sum to 1!")
            elif len(reward_probs) != 2:
                raise ValueError("Only two reward conditions currently supported...")
            else:
                self.reward_probs = reward_probs

        self.num_states = [4, 2]
        self.num_locations = self.num_states[LOCATION_FACTOR_ID]
        self.num_controls = [self.num_locations, 1]
        self.num_reward_conditions = self.num_states[TRIAL_FACTOR_ID]
        self.num_cues = self.num_reward_conditions
        self.num_obs = [self.num_locations, self.num_reward_conditions + 1, self.num_cues + 1]
        self.num_factors = len(self.num_states)
        self.num_modalities = len(self.num_obs)

        self._transition_dist = self._construct_transition_dist()
        self._likelihood_dist = self._construct_likelihood_dist()

        self._reward_condition = None
        self._state = None

def reset(self, state=None):
        if state is None:
            loc_state = utils.onehot(0, self.num_locations)
            
            self._reward_condition = np.random.randint(self.num_reward_conditions) # randomly select a reward condition
            reward_condition = utils.onehot(self._reward_condition, self.num_reward_conditions)

            full_state = utils.obj_array(self.num_factors)
            full_state[LOCATION_FACTOR_ID] = loc_state
            full_state[TRIAL_FACTOR_ID] = reward_condition
            self._state = full_state
        else:
            self._state = state
        return self._get_observation()

def step(self, actions):
        prob_states = utils.obj_array(self.num_factors)
        for factor, state in enumerate(self._state):
            prob_states[factor] = self._transition_dist[factor][:, :, int(actions[factor])].dot(state)
        state = [utils.sample(ps_i) for ps_i in prob_states]
        self._state = self._construct_state(state)
        return self._get_observation()

def sample_action(self):
        return [np.random.randint(self.num_controls[i]) for i in range(self.num_factors)]

def get_likelihood_dist(self):
        return self._likelihood_dist.copy()

def get_transition_dist(self):
        return self._transition_dist.copy()

def _get_observation(self):

        prob_obs = [maths.spm_dot(A_m, self._state) for A_m in self._likelihood_dist]

        obs = [utils.sample(po_i) for po_i in prob_obs]
        return obs

def _construct_transition_dist(self):
        B_locs = np.eye(self.num_locations)
        B_locs = B_locs.reshape(self.num_locations, self.num_locations, 1)
        B_locs = np.tile(B_locs, (1, 1, self.num_locations))
        B_locs = B_locs.transpose(1, 2, 0)

        B = utils.obj_array(self.num_factors)

        B[LOCATION_FACTOR_ID] = B_locs
        B[TRIAL_FACTOR_ID] = np.eye(self.num_reward_conditions).reshape(
            self.num_reward_conditions, self.num_reward_conditions, 1
        )
        return B

def _construct_likelihood_dist(self):

        A = utils.obj_array_zeros([ [obs_dim] + self.num_states for _, obs_dim in enumerate(self.num_obs)] )
        
        for loc in range(self.num_states[LOCATION_FACTOR_ID]):
            for reward_condition in range(self.num_states[TRIAL_FACTOR_ID]):

                if loc == 0:  # the case when the agent is in the centre location
                    # When in the centre location, reward observation is always 'no reward', or the outcome with index 0
                    A[REWARD_MODALITY_ID][0, loc, reward_condition] = 1.0

                    # When in the center location, cue observation is always 'no cue', or the outcome with index 0
                    A[CUE_MODALITY_ID][0, loc, reward_condition] = 1.0

                # The case when loc == 3, or the cue location ('bottom arm')
                elif loc == 3:

                    # When in the cue location, reward observation is always 'no reward', or the outcome with index 0
                    A[REWARD_MODALITY_ID][0, loc, reward_condition] = 1.0

                    # When in the cue location, the cue indicates the reward condition umambiguously
                    # signals where the reward is located
                    A[CUE_MODALITY_ID][reward_condition + 1, loc, reward_condition] = 1.0

                # The case when the agent is in one of the (potentially-) rewarding arms
                else:

                    # When location is consistent with reward condition
                    if loc == (reward_condition + 1):
                        # Means highest probability is concentrated over reward outcome
                        high_prob_idx = REWARD_IDX
                        # Lower probability on loss outcome
                        low_prob_idx = LOSS_IDX  #
                    else:
                        # Means highest probability is concentrated over loss outcome
                        high_prob_idx = LOSS_IDX
                        # Lower probability on reward outcome
                        low_prob_idx = REWARD_IDX

                    reward_probs = self.reward_probs[0]
                    A[REWARD_MODALITY_ID][high_prob_idx, loc, reward_condition] = reward_probs
                    reward_probs = self.reward_probs[1]
                    A[REWARD_MODALITY_ID][low_prob_idx, loc, reward_condition] = reward_probs

                    # When in the one of the rewarding arms, cue observation is always 'no cue', or the outcome with index 0
                    A[CUE_MODALITY_ID][0, loc, reward_condition] = 1.0

                # The agent always observes its location, regardless of the reward condition
                A[LOCATION_MODALITY_ID][loc, loc, reward_condition] = 1.0

        return A

def _construct_state(self, state_tuple):

        state = utils.obj_array(self.num_factors)

        for f, ns in enumerate(self.num_states):
            state[f] = utils.onehot(state_tuple[f], ns)
            
        return state

def state(self):
        return self._state

def reward_condition(self):
        return self._reward_condition

class VisualForagingEnv(Env):
    """ Implementation of the visual foraging environment used for scene construction simulations """

    def __init__(self, scenes=None, n_features=2):
        if scenes is None:
            self.scenes = self._construct_default_scenes()
        else:
            self.scenes = scenes

        self.n_scenes = len(self.scenes)
        self.n_features = n_features + 1
        self.n_states = [np.prod(self.scenes[0].shape) + 1, self.scenes.shape[0]]
        self.n_locations = self.n_states[LOCATION_ID]
        self.n_control = [self.n_locations, 1]
        self.n_observations = [self.n_locations, self.n_features]
        self.n_factors = len(self.n_states)
        self.n_modalities = len(self.n_observations)

        self._transition_dist = self._construct_transition_dist()
        self._likelihood_dist = self._construct_likelihood_dist()
        self._true_scene = None
        self._state = None

    def reset(self, state=None):
        if state is None:
            loc_state = np.zeros(self.n_locations)
            loc_state[0] = 1.0
            scene_state = np.zeros(self.n_scenes)
            self._true_scene = np.random.randint(self.n_scenes)
            scene_state[self._true_scene] = 1.0
            full_state = np.empty(self.n_factors, dtype=object)
            full_state[LOCATION_ID] = loc_state
            full_state[SCENE_ID] = scene_state
            self._state = Categorical(values=full_state)
        else:
            self._state = Categorical(values=state)
        return self._get_observation()

    def step(self, actions):
        prob_states = np.empty(self.n_factors, dtype=object)
        for f in range(self.n_factors):
            prob_states[f] = (
                self._transition_dist[f][:, :, actions[f]]
                .dot(self._state[f], return_numpy=True)
                .flatten()
            )
        state = Categorical(values=prob_states).sample()
        self._state = self._construct_state(state)
        return self._get_observation()

    def render(self):
        pass

    def sample_action(self):
        return [np.random.randint(self.n_control[i]) for i in range(self.n_factors)]

    def get_likelihood_dist(self):
        return self._likelihood_dist.copy()

    def get_transition_dist(self):
        return self._transition_dist.copy()

    def get_uniform_posterior(self):
        values = np.array(
            [
                np.ones(self.n_states[f]) / self.n_states[f]
                for f in range(self.n_factors)
            ]
        )
        return Categorical(values=values)

    def get_rand_likelihood_dist(self):
        pass

    def get_rand_transition_dist(self):
        pass

    def _get_observation(self):
        prob_obs = self._likelihood_dist.dot(self._state)
        return prob_obs.sample()

    def _construct_transition_dist(self):
        B_locs = np.eye(self.n_locations)
        B_locs = B_locs.reshape(self.n_locations, self.n_locations, 1)
        B_locs = np.tile(B_locs, (1, 1, self.n_locations))
        B_locs = B_locs.transpose(1, 2, 0)

        B = np.empty(self.n_factors, dtype=object)
        B[LOCATION_ID] = B_locs
        B[SCENE_ID] = np.eye(self.n_scenes).reshape(self.n_scenes, self.n_scenes, 1)
        return Categorical(values=B)

    def _construct_likelihood_dist(self):
        A = np.empty(self.n_modalities, dtype=object)
        for g in range(self.n_modalities):
            A[g] = np.zeros([self.n_observations[g]] + self.n_states)

        for loc in range(self.n_states[LOCATION_ID]):
            for scene_id in range(self.n_states[SCENE_ID]):
                scene = self.scenes[scene_id]
                feat_loc_ids = np.ravel_multi_index(np.where(scene), scene.shape)
                if loc in feat_loc_ids + 1:
                    feat_ids = np.unravel_index(
                        feat_loc_ids[loc == (feat_loc_ids + 1)], scene.shape
                    )
                    feats = scene[feat_ids]
                    A[SCENE_ID][int(feats), loc, scene_id] = 1.0
                else:
                    A[SCENE_ID][0, loc, scene_id] = 1.0

                A[LOCATION_ID][loc, loc, scene_id] = 1.0
        return Categorical(values=A)

    def _construct_default_scenes(self):
        scene_one = [[2, 2], [2, 2]]
        scene_two = [[1, 1], [1, 1]]
        scenes = np.array([scene_one, scene_two])
        return scenes

    def _construct_state(self, state_tuple):
        state = np.empty(self.n_factors, dtype=object)
        for f in range(self.n_factors):
            state[f] = np.eye(self.n_states[f])[state_tuple[f]]
        return Categorical(values=state)

    @property
    def state(self):
        return self._state

    @property
    def true_scene(self):
        return self._true_scene

class SceneConstruction(Env):
    
    def __init__(self, starting_loc = 'start', scene_name = 'UP_RIGHT', config = "1_2"):

        pos1, pos2 = config.split("_")
        config_tuple = (int(pos1), int(pos2))

        assert scene_name in scene_names, f"{scene_name} is not a possible scene! please choose from {scene_names[0]}, {scene_names[1]}, {scene_names[2]}, or {scene_names[3]}\n"
        assert config_tuple in config_names, f"{config} is not a possible spatial configuration! Please choose an appropriate 2x2 spatial configuration\n"

        self.current_location = starting_loc
        self.scene_name = scene_name
        self.config = config
        self._create_visual_array()

        print(f'Starting location is {self.current_location}, Scene is {self.scene_name}, Configuration is {self.config}\n')

    def step(self,action_label):

        location = self.current_location

        if action_label == 'start': 
          
            new_location = 'start'
            what_obs = 'null'

        elif action_label in quadrant_names:

            what_obs = self.vis_array_flattened[int(action_label)-1]
            new_location = action_label

        elif action_label in choice_names:
            new_location = action_label

            chosen_scene_name = new_location.split('_')[1] + '_' + new_location.split('_')[2]

            if chosen_scene_name== self.scene_name:
                what_obs = 'correct!'
            else:
                what_obs = 'incorrect!'
        
        self.current_location = new_location # store the new grid location

        return what_obs, self.current_location

    def reset(self):
        self.current_location = "start"
        print(f'Re-initialized location to Start location')
        what_obs = 'null'

        return what_obs, self.current_location

    def _create_visual_array(self):
        """ Create scene array """

        vis_array_flattened = np.array(['null', 'null', 'null', 'null'],dtype="<U6")
        dot_dir1, dot_dir2 = self.scene_name.split("_")
        idx1, idx2 = tuple(map(lambda x: int(x) -1, self.config.split("_")))

        vis_array_flattened[idx1] = dot_dir1
        vis_array_flattened[idx2] = dot_dir2

        self.vis_array_flattened = vis_array_flattened
        self.vis_array = vis_array_flattened.reshape(2,2)

class RandomDotMotion(Env):
    """ 
    Implementation of the random-dot motion environment 
    """

    def __init__(self, precision = 1.0, dot_direction = None, sampling_state = None):
        """ Initialize the RDM task using a desired number of directions, the precision (aka coherence) of the motion, 
        a "true dot direction" that generates the observations, and a sampling_state corresponding to how the agent starts (by sampling or not sampling the dot motion)
        """

        if dot_direction is None:
            self._dot_dir = np.random.choice(motion_dir)
        else:
            assert dot_direction in motion_dir, f"{dot_direction} is not a valid motion direction\n"
            self._dot_dir = dot_direction
        
        if sampling_state is None:
            self._action = np.random.choice(sampling_states)
        else:
            self._set_sampling_state(sampling_state)

        self._p = precision
        self.direction_names = motion_dir
        self.sampling_names = sampling_states
        self.n_states = n_states
        self._generate_dot_dist()
        print(f'True motion direction is {self._dot_dir}, motion coherence is {100.0*self.coherence}\n')

    
    def reset(self, dot_direction = None, sampling_state = None):

        if dot_direction is not None:
            self._dot_dir = dot_direction
            self._generate_dot_dist()
        
        if sampling_state is not None:
            self._set_sampling_state(sampling_state)
        
        return self._get_observation()
    
    def step(self, action):
        
        self._set_sampling_state(action)

        return self._get_observation()

    def _generate_dot_dist(self):

        _stateidx = self.direction_names.index(self._dot_dir)
        if self._dot_dir == 'null':
            self.dot_dist = utils.onehot(_stateidx, self.n_states)
        else:
            dot_dist = np.zeros(self.n_states)
            dot_dist[1:] = maths.softmax(self._p * utils.onehot(_stateidx-1, len(self.direction_names)-1))
            self.dot_dist = dot_dist

        return self.dot_dist
    
    def _get_observation(self):

        is_sampling = self._action == 'sample'
        dot_obs = (self.direction_names[utils.sample(self.dot_dist)]) if is_sampling else 'null' # increment the sample by +1 to account for the fact that there's a "null" observation that occupies observation index 0
        action_obs = 'sampling' if is_sampling else 'breaking'

        return dot_obs, action_obs
    
    def _set_sampling_state(self, action):
        assert action in sampling_states, f"{action} is not a valid sampling state\n"
        self._action = action

    @property
    def dot_direction(self):
        return self._dot_dir

    @property
    def num_directions(self):
        return len(self.direction_names)

    @property
    def precision(self):
        return self._p
    
    @property
    def coherence(self):
        return 0. if self._dot_dir == 'null' else self.dot_dist.max()

def create_2x2_array(scene_name, config):
    """
    Helper function for generating array of visual outcomes from the type and configuration
    """

    flattened_scene_array = np.array(['null', 'null', 'null', 'null'],dtype="<U6")
    dot_dir1, dot_dir2 = scene_name.split("_")
    idx1, idx2 = tuple(map(lambda x: int(x) -1, config))

    flattened_scene_array[idx1] = dot_dir1
    flattened_scene_array[idx2] = dot_dir2

    return flattened_scene_array.reshape(2,2), flattened_scene_array

def initialize_scene_construction_GM(T = 6, reward = 2.0, punishment = -4.0, urgency = -4.0):

    loc_names = ['start'] + quadrant_names + choice_names
    what_obs_names = ['null','UP','RIGHT','DOWN','LEFT','correct!','incorrect!']
    where_obs_names = ['start'] + quadrant_names + choice_names
    action_names = ['start'] + quadrant_names + choice_names

    num_states   = [len(all_scenes_all_configs), len(loc_names)]
    num_obs      = [len(what_obs_names), len(where_obs_names)]            # 7 possible visual outcomes (what I'm looking at: "null", "UP", "RIGHT", "DOWN", "LEFT", "CORRECT", "INCORRECT"), 9 possible proprioceptive outcomes (where I'm looking)
    num_controls = [1, len(action_names), 1]

    A = utils.initialize_empty_A(num_obs, num_states)
    B = utils.initialize_empty_B(num_states, num_controls)
    C_shapes = [ [no, T] for no in num_obs]
    C = utils.obj_array_zeros(C_shapes)
    D = utils.obj_array_uniform(num_states)

    # # Create the A array (factorized representation)
    # for scene_id, scene_name in enumerate(scene_names):
    #     for loc_id, loc_name in enumerate(loc_names):
    #         for config_id, config_name in enumerate(config_names):
    #             _, flattened_scene_array = create_2x2_array(scene_name, config_name)
    #             if loc_name == 'start': # at fixation location
    #                 A[0][0, scene_id, loc_id, config_id] = 1.0
    #             elif loc_name in quadrant_names: # fixating one of the quadrants
    #                 A[0][0, scene_id, loc_id, config_id] = 'null' == flattened_scene_array[loc_id-1]
    #                 A[0][1, scene_id, loc_id, config_id] = 'UP' == flattened_scene_array[loc_id-1]
    #                 A[0][2, scene_id, loc_id, config_id] = 'RIGHT' == flattened_scene_array[loc_id-1]
    #                 A[0][3, scene_id, loc_id, config_id] = 'DOWN'  == flattened_scene_array[loc_id-1]
    #                 A[0][4, scene_id, loc_id, config_id] = 'LEFT'  == flattened_scene_array[loc_id-1]
    #             elif loc_name in choice_names: # making a choice

    #                 scene_choice = loc_name.split("_")[1] + "_" + loc_name.split("_")[2]
    #                 A[0][5,scene_id, loc_id, config_id] = scene_choice== scene_name # they get correct feedback if they choose the true scene at play
    #                 A[0][6,scene_id, loc_id, config_id] = scene_choice != scene_name # they get incorrect feedback if they choose anything other than the true scene at play
                
    #             A[1][loc_id, scene_id, loc_id, config_id] = 1.0

    # Create the A array (fully-enumerated parameterization)
    for state_id, scene_and_config_name in enumerate(all_scenes_all_configs):
        scene_name, config_name = scene_and_config_name
        for loc_id, loc_name in enumerate(loc_names):
            _, flattened_scene_array = create_2x2_array(scene_name, config_name)
            if loc_name == 'start': # at fixation location
                A[0][0, state_id, loc_id] = 1.0
            elif loc_name in quadrant_names: # fixating one of the quadrants
                A[0][0, state_id, loc_id] = 'null' == flattened_scene_array[loc_id-1]
                A[0][1, state_id, loc_id] = 'UP' == flattened_scene_array[loc_id-1]
                A[0][2, state_id, loc_id] = 'RIGHT' == flattened_scene_array[loc_id-1]
                A[0][3, state_id, loc_id] = 'DOWN'  == flattened_scene_array[loc_id-1]
                A[0][4, state_id, loc_id] = 'LEFT'  == flattened_scene_array[loc_id-1]
            elif loc_name in choice_names: # making a choice
                scene_choice = loc_name.split("_")[1] + "_" + loc_name.split("_")[2]
                A[0][5,state_id, loc_id] = scene_choice== scene_name # they get correct feedback if they choose the true scene at play
                A[0][6,state_id, loc_id] = scene_choice != scene_name # they get incorrect feedback if they choose anything other than the true scene at play
            
            A[1][loc_id, state_id, loc_id] = 1.0

    control_fac_idx = [1]
    for f, ns in enumerate(num_states):
        if f in control_fac_idx:
            B[f] = utils.construct_controllable_B( [ns], [num_controls[f]] )[0]
        else:
            B[f][:,:,0] = np.eye(ns)

    C[0][5,:] = reward # the agent expects to be right across timesteps
    C[0][6,:] = punishment # the agent expects to not be wrong across timesteps
    C[1][:5,4:] = urgency # make too much exploration costly

    D[1] = utils.onehot(0, num_states[1]) # give agent certain beliefs about starting location

    parameters = {'A': A,
                 'B': B,
                 'C': C,
                 'D': D
                }
    
    mapping = {'scene_names': scene_names,
                'what_obs_names': what_obs_names,
                'where_obs_names': where_obs_names,
                'action_names': action_names
                }

    dimensions = {'num_states': num_states,
                  'num_obs': num_obs,
                  'num_controls': num_controls,
                  }

    
    return parameters, mapping, dimensions

def initialize_RDM_GM(T=16, A_precis = 1.0, break_reward = 0.001):

    sampling_state_names = ['sampling','breaking']
    what_obs_names = ['null','UP','RIGHT','DOWN','LEFT']
    where_obs_names = ['sampling','breaking']
    action_names = ['sample','break']

    n_dir = len(what_obs_names)-1

    num_states = [len(motion_dir), len(sampling_state_names)]
    num_obs = [len(what_obs_names), len(where_obs_names)]
    num_controls = [1, len(action_names)]

    # Initialize A, B, C and D arrays
    A = utils.initialize_empty_A(num_obs=num_obs,num_states=num_states)
    B = utils.initialize_empty_B(num_states=num_states, num_controls=num_controls)
    C = utils.obj_array_zeros(num_obs)
    D = utils.obj_array_uniform(num_states)

    for idx, sampling_state in enumerate(sampling_state_names):
        if sampling_state == 'sampling':
            A[0][0,0,idx] = 1.0
            A[0][1:,1:,idx] = maths.softmax(A_precis * np.eye(n_dir))
            A[1][0,:,idx] = 1.0
        elif sampling_state == 'breaking':
            A[1][idx,:,idx] = 1.0
            A[0][0,:,idx] = 1.0
    
    B[0][:,:,0] = np.eye(num_states[0]) # agent assumes the hidden dot-direction state doesn't change over time
    B[1][0,0,0] = 1.0 # if agent chooses to continnue sampling while already sampling, they keep sampling.
    B[1][1,0,1] = 1.0 # you can move from sampling to breaking
    B[1][1,1,:] = 1.0 # Once you are in the break-state, you cannot "escape" it with either eaction (break-state is an absorbing state or sink in the transition model)

    C[1][1] = break_reward

    start_state_id = sampling_state_names.index('sampling')
    D[1] = utils.onehot(start_state_id, num_states[1]) # prior that agent starts in the sampling state

    parameters = {'A': A,
                 'B': B,
                 'C': C,
                 'D': D
                }
    
    mapping = { 'motion_dir': motion_dir,
                'sampling_state_names': sampling_state_names,
                'what_obs_names': what_obs_names,
                'where_obs_names': where_obs_names,
                'action_names': action_names
                }

    dimensions = {'num_states': num_states,
                  'num_obs': num_obs,
                  'num_controls': num_controls,
                  }

    return parameters, mapping, dimensions

def __init__(self, scenes=None, n_features=2):
        if scenes is None:
            self.scenes = self._construct_default_scenes()
        else:
            self.scenes = scenes

        self.n_scenes = len(self.scenes)
        self.n_features = n_features + 1
        self.n_states = [np.prod(self.scenes[0].shape) + 1, self.scenes.shape[0]]
        self.n_locations = self.n_states[LOCATION_ID]
        self.n_control = [self.n_locations, 1]
        self.n_observations = [self.n_locations, self.n_features]
        self.n_factors = len(self.n_states)
        self.n_modalities = len(self.n_observations)

        self._transition_dist = self._construct_transition_dist()
        self._likelihood_dist = self._construct_likelihood_dist()
        self._true_scene = None
        self._state = None

def reset(self, state=None):
        if state is None:
            loc_state = np.zeros(self.n_locations)
            loc_state[0] = 1.0
            scene_state = np.zeros(self.n_scenes)
            self._true_scene = np.random.randint(self.n_scenes)
            scene_state[self._true_scene] = 1.0
            full_state = np.empty(self.n_factors, dtype=object)
            full_state[LOCATION_ID] = loc_state
            full_state[SCENE_ID] = scene_state
            self._state = Categorical(values=full_state)
        else:
            self._state = Categorical(values=state)
        return self._get_observation()

def step(self, actions):
        prob_states = np.empty(self.n_factors, dtype=object)
        for f in range(self.n_factors):
            prob_states[f] = (
                self._transition_dist[f][:, :, actions[f]]
                .dot(self._state[f], return_numpy=True)
                .flatten()
            )
        state = Categorical(values=prob_states).sample()
        self._state = self._construct_state(state)
        return self._get_observation()

def render(self):
        pass

def sample_action(self):
        return [np.random.randint(self.n_control[i]) for i in range(self.n_factors)]

def get_likelihood_dist(self):
        return self._likelihood_dist.copy()

def get_transition_dist(self):
        return self._transition_dist.copy()

def get_uniform_posterior(self):
        values = np.array(
            [
                np.ones(self.n_states[f]) / self.n_states[f]
                for f in range(self.n_factors)
            ]
        )
        return Categorical(values=values)

def get_rand_likelihood_dist(self):
        pass

def get_rand_transition_dist(self):
        pass

def _get_observation(self):
        prob_obs = self._likelihood_dist.dot(self._state)
        return prob_obs.sample()

def _construct_transition_dist(self):
        B_locs = np.eye(self.n_locations)
        B_locs = B_locs.reshape(self.n_locations, self.n_locations, 1)
        B_locs = np.tile(B_locs, (1, 1, self.n_locations))
        B_locs = B_locs.transpose(1, 2, 0)

        B = np.empty(self.n_factors, dtype=object)
        B[LOCATION_ID] = B_locs
        B[SCENE_ID] = np.eye(self.n_scenes).reshape(self.n_scenes, self.n_scenes, 1)
        return Categorical(values=B)

def _construct_likelihood_dist(self):
        A = np.empty(self.n_modalities, dtype=object)
        for g in range(self.n_modalities):
            A[g] = np.zeros([self.n_observations[g]] + self.n_states)

        for loc in range(self.n_states[LOCATION_ID]):
            for scene_id in range(self.n_states[SCENE_ID]):
                scene = self.scenes[scene_id]
                feat_loc_ids = np.ravel_multi_index(np.where(scene), scene.shape)
                if loc in feat_loc_ids + 1:
                    feat_ids = np.unravel_index(
                        feat_loc_ids[loc == (feat_loc_ids + 1)], scene.shape
                    )
                    feats = scene[feat_ids]
                    A[SCENE_ID][int(feats), loc, scene_id] = 1.0
                else:
                    A[SCENE_ID][0, loc, scene_id] = 1.0

                A[LOCATION_ID][loc, loc, scene_id] = 1.0
        return Categorical(values=A)

def _construct_default_scenes(self):
        scene_one = [[2, 2], [2, 2]]
        scene_two = [[1, 1], [1, 1]]
        scenes = np.array([scene_one, scene_two])
        return scenes

def _construct_state(self, state_tuple):
        state = np.empty(self.n_factors, dtype=object)
        for f in range(self.n_factors):
            state[f] = np.eye(self.n_states[f])[state_tuple[f]]
        return Categorical(values=state)

def state(self):
        return self._state

def true_scene(self):
        return self._true_scene

def __init__(self, starting_loc = 'start', scene_name = 'UP_RIGHT', config = "1_2"):

        pos1, pos2 = config.split("_")
        config_tuple = (int(pos1), int(pos2))

        assert scene_name in scene_names, f"{scene_name} is not a possible scene! please choose from {scene_names[0]}, {scene_names[1]}, {scene_names[2]}, or {scene_names[3]}\n"
        assert config_tuple in config_names, f"{config} is not a possible spatial configuration! Please choose an appropriate 2x2 spatial configuration\n"

        self.current_location = starting_loc
        self.scene_name = scene_name
        self.config = config
        self._create_visual_array()

        print(f'Starting location is {self.current_location}, Scene is {self.scene_name}, Configuration is {self.config}\n')

def step(self,action_label):

        location = self.current_location

        if action_label == 'start': 
          
            new_location = 'start'
            what_obs = 'null'

        elif action_label in quadrant_names:

            what_obs = self.vis_array_flattened[int(action_label)-1]
            new_location = action_label

        elif action_label in choice_names:
            new_location = action_label

            chosen_scene_name = new_location.split('_')[1] + '_' + new_location.split('_')[2]

            if chosen_scene_name== self.scene_name:
                what_obs = 'correct!'
            else:
                what_obs = 'incorrect!'
        
        self.current_location = new_location # store the new grid location

        return what_obs, self.current_location

def reset(self):
        self.current_location = "start"
        print(f'Re-initialized location to Start location')
        what_obs = 'null'

        return what_obs, self.current_location

def _create_visual_array(self):
        """ Create scene array """

        vis_array_flattened = np.array(['null', 'null', 'null', 'null'],dtype="<U6")
        dot_dir1, dot_dir2 = self.scene_name.split("_")
        idx1, idx2 = tuple(map(lambda x: int(x) -1, self.config.split("_")))

        vis_array_flattened[idx1] = dot_dir1
        vis_array_flattened[idx2] = dot_dir2

        self.vis_array_flattened = vis_array_flattened
        self.vis_array = vis_array_flattened.reshape(2,2)

def __init__(self, precision = 1.0, dot_direction = None, sampling_state = None):
        """ Initialize the RDM task using a desired number of directions, the precision (aka coherence) of the motion, 
        a "true dot direction" that generates the observations, and a sampling_state corresponding to how the agent starts (by sampling or not sampling the dot motion)
        """

        if dot_direction is None:
            self._dot_dir = np.random.choice(motion_dir)
        else:
            assert dot_direction in motion_dir, f"{dot_direction} is not a valid motion direction\n"
            self._dot_dir = dot_direction
        
        if sampling_state is None:
            self._action = np.random.choice(sampling_states)
        else:
            self._set_sampling_state(sampling_state)

        self._p = precision
        self.direction_names = motion_dir
        self.sampling_names = sampling_states
        self.n_states = n_states
        self._generate_dot_dist()
        print(f'True motion direction is {self._dot_dir}, motion coherence is {100.0*self.coherence}\n')

def reset(self, dot_direction = None, sampling_state = None):

        if dot_direction is not None:
            self._dot_dir = dot_direction
            self._generate_dot_dist()
        
        if sampling_state is not None:
            self._set_sampling_state(sampling_state)
        
        return self._get_observation()

def step(self, action):
        
        self._set_sampling_state(action)

        return self._get_observation()

def _generate_dot_dist(self):

        _stateidx = self.direction_names.index(self._dot_dir)
        if self._dot_dir == 'null':
            self.dot_dist = utils.onehot(_stateidx, self.n_states)
        else:
            dot_dist = np.zeros(self.n_states)
            dot_dist[1:] = maths.softmax(self._p * utils.onehot(_stateidx-1, len(self.direction_names)-1))
            self.dot_dist = dot_dist

        return self.dot_dist

def _get_observation(self):

        is_sampling = self._action == 'sample'
        dot_obs = (self.direction_names[utils.sample(self.dot_dist)]) if is_sampling else 'null' # increment the sample by +1 to account for the fact that there's a "null" observation that occupies observation index 0
        action_obs = 'sampling' if is_sampling else 'breaking'

        return dot_obs, action_obs

def _set_sampling_state(self, action):
        assert action in sampling_states, f"{action} is not a valid sampling state\n"
        self._action = action

def dot_direction(self):
        return self._dot_dir

def num_directions(self):
        return len(self.direction_names)

def precision(self):
        return self._p

def coherence(self):
        return 0. if self._dot_dir == 'null' else self.dot_dist.max()

class Env(object):
    """ 
    The Env base class, loosely-inspired by the analogous ``env`` class of the OpenAIGym framework. 

    A typical workflow is as follows:

    >>> my_env = MyCustomEnv(<some_params>)
    >>> initial_observation = my_env.reset(initial_state)
    >>> my_agent.infer_states(initial_observation)
    >>> my_agent.infer_policies()
    >>> next_action = my_agent.sample_action()
    >>> next_observation = my_env.step(next_action)

    This would be the first step of an active inference process, where a sub-class of ``Env``, ``MyCustomEnv`` is initialized, 
    an initial observation is produced, and these observations are fed into an instance of ``Agent`` in order to produce an action,
    that can then be fed back into the the ``Env`` instance.

    """

    def reset(self, state=None):
        """
        Resets the initial state of the environment. Depending on case, it may be common to return an initial observation as well.
        """
        raise NotImplementedError

    def step(self, action):
        """
        Steps the environment forward using an action.

        Parameters
        ----------
        action
            The action, the type/format of which depends on the implementation.

        Returns
        ---------
        observation
            Sensory observations for an agent, the type/format of which depends on the implementation of ``step`` and the observation space of the agent.
        """
        raise NotImplementedError

    def render(self):
        """
        Rendering function, that typically creates a visual representation of the state of the environment at the current timestep.
        """
        pass

    def sample_action(self):
        pass

    def get_likelihood_dist(self):
        raise ValueError(
            "<{}> does not provide a model specification".format(type(self).__name__)
        )

    def get_transition_dist(self):
        raise ValueError(
            "<{}> does not provide a model specification".format(type(self).__name__)
        )

    def get_uniform_posterior(self):
        raise ValueError(
            "<{}> does not provide a model specification".format(type(self).__name__)
        )

    def get_rand_likelihood_dist(self):
        raise ValueError(
            "<{}> does not provide a model specification".format(type(self).__name__)
        )

    def get_rand_transition_dist(self):
        raise ValueError(
            "<{}> does not provide a model specification".format(type(self).__name__)
        )

    def __str__(self):
        return "<{} instance>".format(type(self).__name__)

def reset(self, state=None):
        """
        Resets the initial state of the environment. Depending on case, it may be common to return an initial observation as well.
        """
        raise NotImplementedError

def step(self, action):
        """
        Steps the environment forward using an action.

        Parameters
        ----------
        action
            The action, the type/format of which depends on the implementation.

        Returns
        ---------
        observation
            Sensory observations for an agent, the type/format of which depends on the implementation of ``step`` and the observation space of the agent.
        """
        raise NotImplementedError

def render(self):
        """
        Rendering function, that typically creates a visual representation of the state of the environment at the current timestep.
        """
        pass

def sample_action(self):
        pass

def get_likelihood_dist(self):
        raise ValueError(
            "<{}> does not provide a model specification".format(type(self).__name__)
        )

def get_transition_dist(self):
        raise ValueError(
            "<{}> does not provide a model specification".format(type(self).__name__)
        )

def get_uniform_posterior(self):
        raise ValueError(
            "<{}> does not provide a model specification".format(type(self).__name__)
        )

def get_rand_likelihood_dist(self):
        raise ValueError(
            "<{}> does not provide a model specification".format(type(self).__name__)
        )

def get_rand_transition_dist(self):
        raise ValueError(
            "<{}> does not provide a model specification".format(type(self).__name__)
        )

def __str__(self):
        return "<{} instance>".format(type(self).__name__)