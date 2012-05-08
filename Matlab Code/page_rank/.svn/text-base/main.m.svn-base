load sub10000.mat

clc; close all
A = sorted_users_new_sub10000(2:end, :);
% A = [0 0 0 0 1 ; 1 0 0 0 0 ; 1 0 0 0 0 ; 0 1 1 0 0 ; 0 0 1 1 0];
d = .8;

N = length(A);
R = zeros(numel(d), N);
for i = 1:numel(d)
    R(i,:) = page_rank(A, d(i), 0.001);
end
plot(R')

pr = [sorted_users_new_sub10000(1,:); R];
save pr10000.mat pr;

t = 2*pi/N*(0:N-1);
xy = 10*[cos(t);sin(t)]';
figure
subplot(121), spy(A)
subplot(122), gplot(A, xy);

