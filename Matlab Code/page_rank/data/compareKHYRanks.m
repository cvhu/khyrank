function R = compareKHYRanks(KHYResult, other_ranks)

[n, m] = size(KHYResult);
[p, q] = size(other_ranks);
rank1 = normalizeRank(KHYResult(:,3));
R = zeros(n, q+1);
R(:,1) = rank1;
for j = 1:q
    rank2 = zeros(n,1);
    another_rank = other_ranks(:,j);
    for i = 1:n
        rank2(i) = another_rank(KHYResult(i,2),:);
    end
    rank2 = normalizeRank(rank2);
    R(:, j+1) = rank2;
end



function nrank = normalizeRank(rank)
nrank = 1/sum(rank)*rank;
display(sum(nrank));


% R3 = compareKHYRanks(L2result, [pr(2,:)' dcMat(:,2)]);
% close all;b = bar(R3(1:100,:));l = legend('KHYRank', 'PageRank', 'Degree Counts');xl = xlabel('KHYRank position');yl = ylabel('normalized rank');axis tight;set(l, 'FontSize', 24);set(gca, 'FontSize', 24);set(xl, 'FontSize', 24);set(yl, 'FontSize', 24);set(b(1),'facecolor',0.3*C);set(b(2),'facecolor',0.5*C);set(b(3),'facecolor',0.7*C);set(b(1),'edgecolor',0.3*C);set(b(2),'edgecolor',0.5*C);set(b(3),'edgecolor',0.7*C)