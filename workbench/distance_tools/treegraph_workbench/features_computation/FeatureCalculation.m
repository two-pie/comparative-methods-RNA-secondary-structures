clc;
clear all;

AdjM = [0, 1; 1, 0]; % input adjacency matrix, example for tree graph 2_1
DegM = diag(sum(AdjM));
LapM = DegM - AdjM;
[V,D] = eig(LapM);
eigenvalues = diag(D);
[~,idx] = sort(eigenvalues);
column = 0;
for c = 1 : length(idx)
    if idx(c) == 2
        column = c;
    end
end
FV = V(:,column); % get Fiedler vector
FV = sort(FV); % sort
N = size(FV, 1); % vertex number
FV = FV*(N-1)/(FV(end)-FV(1)); % scale
p = polyfit([1:N]', FV, 1);  least squares linear regression
s = p(1)
e = sum((polyval(p,[1:N]')-FV).^2)

