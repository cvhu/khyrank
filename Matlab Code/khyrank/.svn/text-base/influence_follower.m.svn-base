%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Aron Yu, Ann Kilzer, C. Vic Hu
%%% CS 391D (Data Mining)
%%% Final Project: Finding Influencial Users on Twitter
%%%
%%% Influence Follower
%%% ------------------
%%% Given a user, find its followers using the Adjacency Matrix and attempt
%%% to influence them. The attempt is given only if the follower has yet to
%%% have knowledge of the information. The code calls itself recursively to
%%% progress down the connection network until the maximum number of layers
%%% is reached.
%%%
%%% Inputs: user = influncer
%%%            A = adjacency matrix
%%%           IF = influence matrix
%%%         info = information vector
%%%            L = max # of propagation layers
%%%       layers = current layer
%%%
%%% Outputs: info = updated information vector
%%%         layer = updated layer count
%%%
%%% Usage: Call this function from measure_influence to simulate influence
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [info layer] = influence_follower(user,A,IF,info,L,layer)

followers = find(A(:,user)==1);   % followers of the input user
layer = layer + 1;                % increase layer count
%disp(strcat(['Layer ' num2str(layer) ': User ' num2str(user) ' has followers ' num2str(followers')]));

% Return if user doesn't have any followers
if (isempty(followers))
    layer = layer - 1;   % reduce layer count
    return;
end

% Influence one follower at a time
for u = 1:length(followers)
    % Check that follower is still uninfluenced (OFF)
    if (~info(followers(u)))
        
        % Attempt to influence follower
        if (rand <= IF(user,followers(u)))
            info(followers(u)) = 1;   % turn follower ON if successful
            % Check for layer limitation
            if (layer < L)
                % Recursive call with current follower as new user
                [info layer] = influence_follower(followers(u),A,IF,info,L,layer);
            end
        end
        
    end
end
layer = layer - 1;   % reduce layer count
end
