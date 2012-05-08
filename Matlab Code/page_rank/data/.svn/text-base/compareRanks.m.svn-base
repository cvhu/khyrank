function ranks = compareRanks(master, slave1, slave2)

N = 15;
ranks = zeros(N,3);

for i = 1:N
    id = master(i);
    rank2 = find(slave1 == id);
    rank3 = find(slave2 == id);
    ranks(i,:) = [id, rank2, rank3];
end
