x = [1, 0; 0, 1; 0, -1; -1, 0; 0, 2; 0, -2; -2, 0];
y = [-1; -1; -1; 1; 1; 1; 1];
H = ones(7,7);
f = ones(7,1);
f = -f;
K = x * x';
for i = 1:7
	for j = 1:7
		K(i, j) = (K(i, j) + 1)^2;
	end
end
for i = 1:7
	for j = 1:7
		H(i, j) = y(i) * y(j) * K(i, j);
	end
end
lb = zeros(7,1);
Aeq = y';
beq = 0;
alpha = quadprog(H, f, [], [], Aeq, beq, lb,[])
