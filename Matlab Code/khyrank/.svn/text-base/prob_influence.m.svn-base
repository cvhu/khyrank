%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Aron Yu, Ann Kilzer, C. Vic Hu
%%% CS 391D (Data Mining)
%%% Final Project: Finding Influencial Users on Twitter
%%%
%%% Influence Probability
%%% ---------------------
%%% Calcuate the probability that a user can successfully influence its
%%% followers. The factors considered here are the # of retweets and
%%% @mentions that the followers tweets about the particular user. The
%%% retweets and @mentions are weighted such that the more a follower
%%% retweets, the more weight its retweets carry. (same for @mentions)
%%%
%%% Inputs: A = user influencing
%%%         B = user being influenced
%%%         R = retweet matrix
%%%         M = mention matrix
%%%     R_out = total # of Retweets (by user)
%%%     M_out = total # of @Mentions (by user)
%%%
%%% Outputs: Pr_influence = probability of user A influencing user B
%%%
%%% Usage: Call this function from calc_influence to construct the 
%%%        influence matrix (IF)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function Pr_influence = prob_influence(A,B,R,M,R_out,M_out)
% Probability of User B retweeting about User A
Pr_retweet = 0;
% Probability of User B mentioning about User A
Pr_mention = 0;

if (R_out(B) > 0)
    Pr_retweet = R(B,A)/R_out(B);
end
if (M_out(B) > 0)
    Pr_mention = M(B,A)/M_out(B);
end

% Weighing factors
% NOTE: The more a User retweets, the more weight retweets should carry
if ((R_out(B) == 0) && (M_out(B) == 0))
    w_rt = 0;
    w_mn = 0;
else
    w_rt = R_out(B)/(R_out(B)+M_out(B));
    w_mn = M_out(B)/(R_out(B)+M_out(B));
end

% Probability of User A influencing User B
% Note: User B must be a follower of User A
Pr_influence = w_rt*Pr_retweet + w_mn*Pr_mention;
end
