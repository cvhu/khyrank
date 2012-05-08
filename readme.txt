***********************
** MATLAB Code Usage **
***********************

-----------------------------
>> Data Formatting Example <<
-----------------------------

A = importdata('sorted_users_new_sub10000.csv');
A = A(2:end,:);
A = A';
R = importdata('retweetArray10K.txt');
R = R(:,2:end);
R_out = sum(R,2);
M = importdata('mentionsArray10K.txt');
M = M(:,2:end);
M_out = sum(M,2);
Tweets = importdata('training_tweet_retweet_counts10Kaa.txt');
T = Tweets(:,2);
UserID = Tweets(:,1);
save TwitterData15K.mat;

---------------------------------
>> Propagation Based Algorithm <<
---------------------------------

1.Load the desired dataset. Run sample_data.m for a small sample dataset.
2.Run calc_influence.m. Outputs 3 calculated influence score matrices.
3.Run measure_driver.m with appropriate inputs. Outputs 1 simulated influence score matrix.
4.Run count_overlap.m. Displays the number of overlap and the percent of overlap in the top K users between the calculated scores and the simulated score.

Note: The score matrices are sorted in descending order with the most influential user at the top. The first column of each matrix represents the sorted user IDs.

----------------
>> Sample Run <<
----------------

load TwitterData10k;
calc_influence;
test_result = measure_driver(100,5,A,IF,UserID);
count_overlap;

