% Active Inference Implementation in Prolog

% Generative model parameters
a_matrix(1, 1, 0.8).  % a_matrix(observation, state, probability)
a_matrix(1, 2, 0.1).
a_matrix(1, 3, 0.1).
a_matrix(2, 1, 0.1).
a_matrix(2, 2, 0.8).
a_matrix(2, 3, 0.1).
a_matrix(3, 1, 0.1).
a_matrix(3, 2, 0.1).
a_matrix(3, 3, 0.8).

b_matrix(1, 1, 1, 0.9).  % b_matrix(state, action, next_state, probability)
b_matrix(1, 1, 2, 0.1).
b_matrix(2, 1, 1, 0.1).
b_matrix(2, 1, 2, 0.9).

c_vector(1, 0.0).  % c_vector(observation, preference)
c_vector(2, 0.5).
c_vector(3, 0.0).

d_vector(1, 0.5).  % d_vector(state, prior)
d_vector(2, 0.5).

% Initial beliefs (uniform prior)
initial_belief(1, 0.25).
initial_belief(2, 0.25).
initial_belief(3, 0.25).
initial_belief(4, 0.25).

% Update beliefs using Bayesian inference
update_beliefs(Observation, OldBeliefs, NewBeliefs) :-
    findall(P, (
        between(1, 4, State),
        member(belief(State, OldB), OldBeliefs),
        a_matrix(Observation, State, Likelihood),
        P is Likelihood * OldB
    ), Posterior),
    
    sum_list(Posterior, Total),
    (Total > 0 -> 
        findall(belief(S, NB), (
            nth1(S, Posterior, P),
            NB is P / Total
        ), NewBeliefs)
    ; NewBeliefs = OldBeliefs).

% Calculate expected free energy (simplified)
expected_free_energy(Beliefs, Action, EFE) :-
    findall(Entropy, (
        member(belief(_, B), Beliefs),
        (B > 0 -> Entropy is -B * log(B); Entropy = 0)
    ), Entropies),
    sum_list(Entropies, EFE).

% Select action with minimum expected free energy
select_action(Beliefs, Action) :-
    findall(EFE-Act, (
        between(1, 2, Act),
        expected_free_energy(Beliefs, Act, EFE)
    ), EFEs),
    keysort(EFEs, [MinEFE-Action|_]).

% Complete perception-action cycle
step(Observation, OldBeliefs, Action, NewBeliefs) :-
    update_beliefs(Observation, OldBeliefs, NewBeliefs),
    select_action(NewBeliefs, Action).

% Demo predicate
demo(Cycle) :- demo(Cycle, [
    belief(1, 0.25), belief(2, 0.25), 
    belief(3, 0.25), belief(4, 0.25)
]).

demo(0, _) :- 
    write('Prolog Active Inference Demo'), nl,
    write('Initial beliefs: [0.25, 0.25, 0.25, 0.25]'), nl.

demo(Cycle, Beliefs) :-
    Cycle > 0,
    Cycle =< 5,
    Observation is (Cycle - 1) mod 3 + 1,
    step(Observation, Beliefs, Action, NewBeliefs),
    
    write('Cycle '), write(Cycle), 
    write(': Observation='), write(Observation),
    write(', Action='), write(Action),
    write(', Beliefs=['),
    
    findall(B, member(belief(_, B), NewBeliefs), BeliefValues),
    write_beliefs(BeliefValues),
    write(']'), nl,
    
    NextCycle is Cycle + 1,
    demo(NextCycle, NewBeliefs).

write_beliefs([B]) :- format('~3f', [B]).
write_beliefs([B|Rest]) :- 
    format('~3f', [B]), write(', '),
    write_beliefs(Rest).

% Run demo
:- demo(0).
