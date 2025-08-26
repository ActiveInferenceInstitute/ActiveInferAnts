(* Active Inference Implementation in OCaml *)

type active_inference_agent = {
  num_states : int;
  num_observations : int;
  num_actions : int;
  mutable beliefs : float array;
  a_matrix : float array array;
  b_matrix : float array array;
  c_vector : float array;
  d_vector : float array;
}

let create_agent () = {
  num_states = 4;
  num_observations = 3;
  num_actions = 2;
  beliefs = [|0.25; 0.25; 0.25; 0.25|];
  a_matrix = [|
    [|0.8; 0.1; 0.1|];
    [|0.1; 0.8; 0.1|];
    [|0.1; 0.1; 0.8|]
  |];
  b_matrix = [|
    [|0.9; 0.1|];
    [|0.1; 0.9|]
  |];
  c_vector = [|0.0; 0.5; 0.0|];
  d_vector = [|0.5; 0.5|];
}

let normalize_array arr =
  let total = Array.fold_left (+.) 0.0 arr in
  if total > 0.0 then
    Array.map (fun x -> x /. total) arr
  else
    arr

let update_beliefs agent observation =
  let likelihood = agent.a_matrix.(observation - 1) in
  let posterior = Array.map2 ( *. ) likelihood agent.beliefs in
  agent.beliefs <- normalize_array posterior

let calculate_expected_free_energy agent action =
  Array.fold_left (fun acc belief ->
    acc +. if belief > 0.0 then -. belief *. log(belief) else 0.0
  ) 0.0 agent.beliefs

let select_action agent =
  let rec find_min_action current best_efe best_action =
    if current > agent.num_actions then best_action
    else
      let efe = calculate_expected_free_energy agent current in
      if efe < best_efe then
        find_min_action (current + 1) efe current
      else
        find_min_action (current + 1) best_efe best_action
  in
  find_min_action 1 infinity 1

let step agent observation =
  update_beliefs agent observation;
  select_action agent

let print_beliefs agent =
  print_string "Beliefs: ";
  Array.iteri (fun i belief ->
    Printf.printf "%.3f" belief;
    if i < Array.length agent.beliefs - 1 then print_string ", "
  ) agent.beliefs;
  print_newline ()

(* Demo *)
let () =
  print_endline "OCaml Active Inference Demo";
  let agent = create_agent () in
  print_string "Initial ";
  print_beliefs agent;
  
  for cycle = 1 to 5 do
    let observation = (cycle - 1) mod 3 + 1 in
    let action = step agent observation in
    Printf.printf "Cycle %d: Observation=%d, Action=%d, " cycle observation action;
    print_beliefs agent
  done
