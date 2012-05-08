%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Aron Yu, Ann Kilzer, C. Vic Hu
%%% CS 391D (Data Mining)
%%% Final Project: Finding Influencial Users on Twitter
%%%
%%% Information Progression Test
%%% ----------------------------
%%% Using the Influence Matrix, quantitatively simulate the actual
%%% influence of each user in the network. When given a piece of 
%%% information at the seed user, it counts the number of people who have 
%%% knowledge of the information by the end of L layers of information 
%%% passage. Test for single seed user.
%%%
%%% Inputs: seed = user under test
%%%         iter = # of iterations
%%%            L = max # of propagation layers
%%%            A = adjacency matrix
%%%           IF = influence matrix
%%%
%%% Outputs: num_I = average # of users influenced
%%%         perc_I = average percent of users influenced
%%%
%%% Usage: Designate a seed user and the information propagation will be
%%%        simulated for the desired number of iterations. 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [num_I perc_I] = measure_influence(seed,iter,L,A,IF)

% Initialization
info = zeros(length(A),1);
info(seed) = 1;    % only seed user knows about the infomation initially
seed_info = info;  % reset vector
layer = 0;         % layer counter
num_I = 0;         % total influence counter

% Influence followers
for i = 1:iter
    [info layer] = influence_follower(seed,A,IF,info,L,layer);
    num_I = num_I + sum(info);
    %disp(strcat(['Final State is: ' num2str(info')]));
    info = seed_info;   % reset the info vector
end

num_I = num_I/iter;         % average # of users influenced
perc_I = num_I/length(A);   % average percent of users influenced

end
