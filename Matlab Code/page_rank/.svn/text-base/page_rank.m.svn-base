% Parameter M adjacency matrix where Mi,j represents the link from 'j' to 'i', such that for all 'j' sum(i, Mi,j) = 1
% Parameter d damping factor
% Parameter v_quadratic_error quadratic error for v
% Return v vector rank such as vi is the i-th rank from [0, 1]
function [v] = page_rank(A, d, v_quadratic_error)
K = diag(sum(A,1));
M = A*pinv(K);
N = size(M, 2);
v = rand(N, 1);
v = v ./ norm(v, 2);
last_v = ones(N, 1) * inf;
M_prime = (d .* M) + (((1 - d) / N) .* ones(N, N));
while(norm(v - last_v, 2) > v_quadratic_error)
        last_v = v;
        v = M_prime * v;
        v = v ./ norm(v, 2);
end

% function h_k = page_rank(A)
% n = length(A);
% % h_0 = ones(n,1);
% % k = 10;
% % h_k = (A*A')^k*h_0;
% % hist(h_k)
% 
% D = diag(sum(A,2));
% 
% P = D\A;