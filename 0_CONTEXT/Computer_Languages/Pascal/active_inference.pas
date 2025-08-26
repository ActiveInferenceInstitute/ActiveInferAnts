{ Active Inference Implementation in Pascal }

program ActiveInferenceDemo;

const
  NumStates = 4;
  NumObservations = 3;
  NumActions = 2;

type
  TBeliefsArray = array[1..NumStates] of Real;
  TAMatrix = array[1..NumObservations, 1..NumStates] of Real;
  TBMatrix = array[1..NumStates, 1..NumActions] of Real;
  TCVector = array[1..NumObservations] of Real;
  TDVector = array[1..NumStates] of Real;

var
  beliefs: TBeliefsArray;
  aMatrix: TAMatrix;
  bMatrix: TBMatrix;
  cVector: TCVector;
  dVector: TDVector;

procedure InitializeModel;
var
  i, j: Integer;
begin
  { Initialize beliefs (uniform) }
  for i := 1 to NumStates do
    beliefs[i] := 1.0 / NumStates;
  
  { Initialize A matrix (observation likelihood) }
  aMatrix[1,1] := 0.8; aMatrix[1,2] := 0.1; aMatrix[1,3] := 0.1;
  aMatrix[2,1] := 0.1; aMatrix[2,2] := 0.8; aMatrix[2,3] := 0.1;
  aMatrix[3,1] := 0.1; aMatrix[3,2] := 0.1; aMatrix[3,3] := 0.8;
  
  { Initialize B matrix (transition likelihood) }
  bMatrix[1,1] := 0.9; bMatrix[1,2] := 0.1;
  bMatrix[2,1] := 0.1; bMatrix[2,2] := 0.9;
  
  { Initialize C and D vectors }
  cVector[1] := 0.0; cVector[2] := 0.5; cVector[3] := 0.0;
  dVector[1] := 0.5; dVector[2] := 0.5;
end;

procedure UpdateBeliefs(observation: Integer);
var
  posterior: TBeliefsArray;
  total: Real;
  i: Integer;
begin
  total := 0.0;
  
  { Calculate posterior P(s|o) ∝ P(o|s) * P(s) }
  for i := 1 to NumStates do begin
    posterior[i] := aMatrix[observation, i] * beliefs[i];
    total := total + posterior[i];
  end;
  
  { Normalize }
  if total > 0.0 then
    for i := 1 to NumStates do
      beliefs[i] := posterior[i] / total;
end;

function SelectAction: Integer;
begin
  { Simplified action selection }
  SelectAction := 1;  { Default action }
end;

procedure PrintBeliefs;
var
  i: Integer;
begin
  Write('Beliefs: ');
  for i := 1 to NumStates do begin
    Write(beliefs[i]:4:3);
    if i < NumStates then Write(', ');
  end;
  Writeln;
end;

var
  cycle, observation, action: Integer;

begin
  Writeln('Pascal Active Inference Demo');
  
  InitializeModel;
  Write('Initial '); PrintBeliefs;
  
  for cycle := 1 to 5 do begin
    observation := (cycle - 1) mod 3 + 1;
    UpdateBeliefs(observation);
    action := SelectAction;
    Write('Cycle ', cycle, ': Observation=', observation, ', Action=', action, ', ');
    PrintBeliefs;
  end;
end.
