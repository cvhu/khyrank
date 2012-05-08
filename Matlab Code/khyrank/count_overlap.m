%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Aron Yu, Ann Kilzer, C. Vic Hu
%%% CS 391D (Data Mining)
%%% Final Project: Finding Influencial Users on Twitter
%%%
%%% Match Results
%%% -------------------------
%%% Find overlap users among the collected results. Compare the result of
%%% the 3 methods against the test result and displays the number and the
%%% percentage of overlap.
%%%
%%% Inputs: L2result = score based on only on immediate followers
%%%         L3result = score based on followers of followers
%%%      calc_result = L3result without follow-backs
%%%      test_result = score from simulation
%%%
%%% Outputs: L2match = match between L2result & test_result
%%%          L3match = match between L3result & test_result
%%%          calc_match = match between calc_result & test_result
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Top K influential users to match
K = [5 10 50 100 500 1000];

for k = 1:length(K)
    L2(k) = length(intersect(L2result(1:K(k),1),test_result(1:K(k),1)));
    L3(k) = length(intersect(L3result(1:K(k),1),test_result(1:K(k),1)));
    calc(k) = length(intersect(calc_result(1:K(k),1),test_result(1:K(k),1)));
end

L2match = [L2;L2./K]
L3match = [L3;L3./K]
calc_match = [calc;calc./K]
