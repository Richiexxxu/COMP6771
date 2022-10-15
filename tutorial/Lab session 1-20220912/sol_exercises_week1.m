%% Question 1
% number of elements
n = 10

% a
x = [2:2:2 * n]

% b
x = [10:-2:-8]

% c
x = 1 ./ [1:1:n]

% d
x = [0:1:n - 1] ./ [1:1:n]

%% Question 2
x = [2 5 1 6]

% a 
x + 16

% b
x(1:2:end) = x(1:2:end) + 3

% c
sqrt(x)

%% Question 3
M = 3
N = 2
A = rand(M, N)
A(A < 0.2) = 0
A(A >= 0.2) = 1

%% Question 4
function B = ChangeMatrix(M, N)

    A = rand(M, N);
    
    for i = 1:M
        for j = 1:N
            if(A(i, j) < 0.2)
                A(i, j) = 0;
            else
                A(i, j) = 1;
            end
        end
    end
end

%% Question 5
x = [3 15 9 12 -1 0 -12 9 6 1]
% a
x(x > 0) = 0

% b
index = find(x(mod(x, 2) == 0))
x(index) = x(index) * 5

% c
y = x(x > 10)


%% Question 6
t = [1790:1:2020]
pt  = 197273000 ./ (1 + exp(-0.0313 * (t - 1913.25)))

plot(t, pt);
x = pt(find(t == 2020));

