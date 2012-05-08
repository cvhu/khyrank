%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Aron Yu, Ann Kilzer, C. Vic Hu
%%% CS 391D (Data Mining)
%%% Final Project: Finding Influencial Users on Twitter
%%%
%%% Calculate Influence Score
%%% -------------------------
%%% Construct the Influence Matrix and calculate the Influence Score of
%%% each user based on the algorithm. The Influence Score is calculated 
%%% using three different methods.
%%%
%%% This should be the first code to run after loading the data. Refer to
%%% sample_data for the format and the detailed explanation of the inputs.
%%%
%%% Inputs: A = adjacency matrix
%%%         R = retweet matrix
%%%         M = mention matrix
%%%         T = total # of Tweets
%%%     R_out = total # of Retweets (by user)
%%%     M_out = total # of @Mentions (by user)
%%%    UserID = mapping of actual user IDs
%%%
%%% Outputs: L2result = score based on only on immediate followers
%%%          L3result = score based on followers of followers
%%%       calc_result = L3result without follow-backs
%%%
%%% Usage: Load in required inputs for respective dataset first
%%%        (TwitterDataXXK where XX is the # of users in thousands)
%%%
%%%        Output columns represent sorted [UserIDs UserIndex NormScore]
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

format shortG;
% Make sure all the required files are loaded

% Construct Influence Matrix
% IF(I,J) = probability of User I influencing User J
tic;
IF = zeros(length(A));
for i = 1:length(A)
    for j = 1:length(A)
        if (A(j,i) == 1)  % if user j is a follower of user i
            IF(i,j) = prob_influence(i,j,R,M,R_out,M_out);
        end  
    end
    %disp(strcat(['Just finished(IF) User: ' num2str(i)]));
end
toc;
disp('Done: Influence Matrix computed!');

% Calculate influence of each user
% 1 Degree reach (dependent on immediate followers)
layer2_score = T.*sum(IF,2);
layer2_score_norm = layer2_score/max(layer2_score);
[s_L2score s_L2user] = sort(layer2_score_norm,'descend');
L2result = [UserID(s_L2user) s_L2user s_L2score];

% 2 Degree reach (dependent on followers of followers as well)
deg_factor = 0.5;   % weight of 2nd degree followers
layer3_score = T.*(IF*(deg_factor*layer2_score./(sum(ceil(IF),2)+1)));
layer3_score_norm = layer3_score/max(layer3_score);
[s_L3score s_L3user] = sort(layer3_score_norm,'descend');
L3result = [UserID(s_L3user) s_L3user s_L3score];

% Manual modified 2 Degree reach calculation
% Doesn't include the follow-back relationships
tic;
layer_score = zeros(length(A),1);
for i = 1:length(A)
    
    layer_score(i) = 0;
    followers = find(IF(i,:)>0);   % find followers
    
    % Followers of the followers
    for j = 1:length(followers)
        score = 0;   
        n_followers = find(IF(followers(j),:)>0);   % find followers
        n_followers(n_followers==i) = [];   % remove follow-back
        
        if (~isempty(n_followers))  % if not empty
           % Calculate score
            score = sum(IF(followers(j),n_followers))/length(n_followers);
            score = IF(i,followers(j))*T(followers(j))*score*deg_factor;
            layer_score(i) = layer_score(i) + score; 
        end
    end
    % Weigh score with total # of tweets
    layer_score(i) = layer_score(i)*T(i);
    %disp(strcat(['Just finished(score) User: ' num2str(i)]));
end
toc;

% Normalize
layer_score_norm = layer_score/max(layer_score);
[s_score s_user] = sort(layer_score_norm,'descend');
calc_result = [UserID(s_user) s_user s_score];

disp('Done: Ranking computed!');
