%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Aron Yu, Ann Kilzer, C. Vic Hu
%%% CS 391D (Data Mining)
%%% Final Project: Finding Influencial Users on Twitter
%%%
%%% Sample Dataset
%%% --------------
%%% Manually created dataset containing 6 users.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Adjacency Matrix (input)
% User I is following User J if A(I,J)=1
A = [0 1 1 1 0 0;
     1 0 0 1 0 1;
     0 0 0 0 1 0;
     0 1 0 0 1 0;
     1 1 1 0 0 1;
     0 0 0 1 1 0];

% Retweet Matrix (input)
% User I retweeted about User J R(I,J) times
R = [0 2 4 0 0 0;
     2 0 0 0 0 1;
     0 0 0 0 10 0;
     0 0 0 0 3 0;
     0 2 2 0 0 1;
     0 0 0 5 5 0];

% Mention Matrix (input)
% User I mentioned about User J M(I,J) times
M = [0 1 1 0 0 0;
     2 0 0 1 0 0;
     0 0 0 0 2 0;
     0 2 0 0 1 0;
     1 0 0 0 0 2;
     0 0 0 0 2 0];

% Tweets Vector (input)
% Total number of tweets by each User
T = [100 50 120 30 60 50]';

% Total number of retweets by each User
R_out = sum(R,2);

% Total number of mentions by each User
M_out = sum(M,2);
