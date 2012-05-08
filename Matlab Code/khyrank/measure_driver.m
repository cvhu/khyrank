%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Aron Yu, Ann Kilzer, C. Vic Hu
%%% CS 391D (Data Mining)
%%% Final Project: Finding Influencial Users on Twitter
%%%
%%% Information Progression Test Driver
%%% -----------------------------------
%%% Calls measure_influence multiple times to simulate the information
%%% propagation seeding from each user.
%%%
%%% This should be the second code to run after constructing the Influence
%%% Matrix and calculating the Influence Score.
%%%
%%% Inputs: iter = # of iterations
%%%            L = max # of propagation layers
%%%            A = adjacency matrix
%%%           IF = influence matrix
%%%       UserID = list of actual user IDs
%%%
%%% Outputs: test_result = ranked influence results
%%%
%%% Usage: test_result = measure_driver(100,5,A,IF,UserID)
%%%
%%%        Output columns represent sorted 
%%%                 [UserIDs UserIndex PercentInfluenced NumberInfluenced]
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function test_result = measure_driver(iter,L,A,IF,UserID)

%close all; clc;
disp(strcat(['Testing ' num2str(L) ' Layers for ' num2str(iter) ' iterations']));

num_I = zeros(length(A),1);
perc_I = zeros(length(A),1);

tic
% Call measure_influence seeding from all users
for i = 1:length(A)
    [num perc] = measure_influence(i,iter,L,A,IF);
    num_I(i) = num;
    perc_I(i) = perc;
    %disp(strcat(['Just finished Seed User: ' num2str(i)]));
end
toc

% Sort results
[num_I s_user] = sort(num_I,'descend');
perc_I = sort(perc_I,'descend');
test_result = [UserID(s_user) s_user perc_I num_I];

disp('Done: Tested Ranking computed!');
end

