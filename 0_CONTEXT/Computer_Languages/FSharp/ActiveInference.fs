// Active Inference Implementation in F#

open System

type ActiveInferenceAgent(beliefs: float array,
                          aMatrix: float[,],
                          bMatrix: float[,,],
                          cVector: float array,
                          dVector: float array) =

    let numStates = beliefs.Length
    let numObservations = aMatrix.GetLength(0)
    let numActions = bMatrix.GetLength(1)

    member this.Beliefs = beliefs

    member this.UpdateBeliefs(observation: int) =
        let likelihood = aMatrix.[observation-1, *]
        let posterior = Array.map2 (*) likelihood beliefs
        let total = Array.sum posterior
        if total > 0.0 then
            Array.map (fun p -> p / total) posterior
        else
            beliefs

    member this.CalculateExpectedFreeEnergy(action: int) =
        // Simplified EFE calculation
        beliefs
        |> Array.mapi (fun i belief ->
            if belief > 0.0 then -belief * Math.Log(belief) else 0.0)
        |> Array.sum

    member this.SelectAction() =
        [1..numActions]
        |> List.minBy (fun action -> this.CalculateExpectedFreeEnergy(action))

    member this.Step(observation: int) =
        let newBeliefs = this.UpdateBeliefs(observation)
        let action = this.SelectAction()
        (newBeliefs, action)

// Demo
let agent = ActiveInferenceAgent(
    beliefs = [|0.25; 0.25; 0.25; 0.25|],
    aMatrix = array2D [[0.8; 0.1; 0.1];
                       [0.1; 0.8; 0.1];
                       [0.1; 0.1; 0.8]],
    bMatrix = Array3D.zeroCreate 4 2 4,
    cVector = [|0.0; 0.5; 0.0|],
    dVector = [|0.5; 0.5|]
)

printfn "F# Active Inference Demo"
printfn "Initial beliefs: %A" agent.Beliefs

[1..5] |> List.iter (fun cycle ->
    let observation = (cycle % 3) + 1
    let (beliefs, action) = agent.Step(observation)
    printfn "Cycle %d: Observation=%d, Action=%d, Beliefs=%A"
             cycle observation action beliefs)
