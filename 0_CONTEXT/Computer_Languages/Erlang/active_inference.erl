-module(active_inference).
-export([start/0, initialize/1, update_beliefs/2, select_action/1, step/2]).

-record(state, {
    beliefs = [0.25, 0.25, 0.25, 0.25],
    a_matrix = [[0.8, 0.1, 0.1],
                [0.1, 0.8, 0.1],
                [0.1, 0.1, 0.8]],
    b_matrix = [[0.9, 0.1], [0.1, 0.9]],
    c_vector = [0.0, 0.5, 0.0],
    d_vector = [0.5, 0.5]
}).

start() ->
    spawn(fun() -> loop(#state{}) end).

initialize(Pid) ->
    Pid ! initialize.

update_beliefs(Pid, Observation) ->
    Pid ! {update_beliefs, Observation, self()},
    receive
        Beliefs -> Beliefs
    end.

select_action(Pid) ->
    Pid ! {select_action, self()},
    receive
        Action -> Action
    end.

step(Pid, Observation) ->
    Pid ! {step, Observation, self()},
    receive
        {Beliefs, Action} -> {Beliefs, Action}
    end.

loop(State) ->
    receive
        initialize ->
            NewState = #state{},
            loop(NewState);

        {update_beliefs, Observation, From} ->
            Likelihood = lists:nth(Observation, State#state.a_matrix),
            Posterior = lists:zipwith(fun(L, B) -> L * B end,
                                    Likelihood, State#state.beliefs),
            Total = lists:sum(Posterior),
            NewBeliefs = if Total > 0 ->
                [P / Total || P <- Posterior];
                          true ->
                State#state.beliefs
                          end,
            From ! NewBeliefs,
            loop(State#state{beliefs = NewBeliefs});

        {select_action, From} ->
            % Simplified action selection
            Action = 1,  % Default action
            From ! Action,
            loop(State);

        {step, Observation, From} ->
            % Update beliefs
            Likelihood = lists:nth(Observation, State#state.a_matrix),
            Posterior = lists:zipwith(fun(L, B) -> L * B end,
                                    Likelihood, State#state.beliefs),
            Total = lists:sum(Posterior),
            NewBeliefs = if Total > 0 ->
                [P / Total || P <- Posterior];
                          true ->
                State#state.beliefs
                          end,

            % Select action (simplified)
            Action = 1,

            From ! {NewBeliefs, Action},
            loop(State#state{beliefs = NewBeliefs});

        stop ->
            ok
    end.

% Demo function
demo() ->
    io:format("Erlang Active Inference Demo~n"),
    Pid = start(),
    initialize(Pid),

    lists:foreach(fun(Cycle) ->
        Observation = (Cycle rem 3) + 1,
        {Beliefs, Action} = step(Pid, Observation),
        io:format("Cycle ~p: Observation=~p, Action=~p, Beliefs=~p~n",
                 [Cycle, Observation, Action, Beliefs])
    end, lists:seq(1, 5)),

    Pid ! stop.
