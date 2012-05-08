function plotRanks(r1, r2, r3, N)
close all
rank1 = normalizeRank(r1(1:N,2));
rank2 = normalizeRank(r2(1:N,2));
rank3 = normalizeRank(r3(1:N,2));

figure 
R = [rank1 rank2 rank3];
h = area(log(100000*R+1));
C = [1 0 0];
a = .1;
b = .5;
c = .9;
% set(get(h(1),'BaseLine'),'LineWidth',5,'LineStyle',':')
set(h(1),'facecolor',a*C,'EdgeColor',a*C) % use color name
% set(get(h(2),'BaseLine'),'LineWidth',5,'LineStyle',':')
set(h(2),'facecolor',b*C,'EdgeColor',b*C) % or use RGB triple
% set(get(h(3),'BaseLine'),'LineWidth',5,'LineStyle',':')
set(h(3),'facecolor',c*C,'EdgeColor',c*C) % or use a color defined in the help for PLOT
% colormap hsv
legend('','','')

function r = normalizeRank(r)
r = 1/sum(r)*r;
display(sum(r))