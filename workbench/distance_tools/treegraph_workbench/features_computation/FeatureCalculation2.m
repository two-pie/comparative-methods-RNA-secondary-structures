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
p = polyfit([1:N]', FV, 1); % least squares linear regression
s = p(1)
e = sum((polyval(p,[1:N]')-FV).^2)


AdjM1 = [0, 1; 1, 0]; % input adjacency matrix, example for tree graph 2_1
DegM1 = diag(sum(AdjM1));
LapM1 = DegM1 - AdjM1;
[V1,D1] = eig(LapM1);
eigenvalues1 = diag(D1);
[~,idx1] = sort(eigenvalues1);
column1 = 0;
for c1 = 1 : length(idx1)
    if idx1(c1) == 2
        column1 = c1;
    end
end
FV1 = V1(:,column1); % get Fiedler vector
FV1 = sort(FV1); % sort
N1 = size(FV1, 1); % vertex number
FV1 = FV1*(N1-1)/(FV1(end)-FV1(1)); % scale
p1 = polyfit([1:N1]', FV1, 1); % least squares linear regression
s1 = p1(1)
e1 = sum((polyval(p1,[1:N1]')-FV1).^2)

x = [s, e];
y = [s1, e1];

D = pdist2(x,y)


