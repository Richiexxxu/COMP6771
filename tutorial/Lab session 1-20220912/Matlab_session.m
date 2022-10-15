% Matlab tutorial

% =======================================================
% Section 1: Matlab Tutorial: Basic operations

%% elementary operations
% math operations
5+6
3-2
5*8
1/2
2^6
% logical operations
1 == 2  % false   % <----- this is the comment
1 ~= 2  % true.  note, not "!="
1 && 0  % and operation
1 || 0  % or operation
xor(1,0)


%% variable assignment
a = 3; % semicolon suppresses output
b = 'hi';
c = 3>=1;

% Displaying them:
a = pi
disp(sprintf('2 decimals: %0.2f', a))
disp(sprintf('6 decimals: %0.6f', a))
format long
a
format short
a


%%  vectors and matrices
v = [1 2 3]
v = [1; 2; 3]
v = [1:0.1:2]  % from 1 to 2, with stepsize of 0.1. Useful for plot axes
v = 1:6        % from 1 to 6, assumes stepsize of 1

w = ones(1,3)    % 1x3 vector of ones
w = zeros(1,3)
w = rand(1,3)  % drawn from a uniform distribution 
w = randn(1,3) % drawn from a normal distribution (mean=0, var=1)
w = -6 + sqrt(10)*(randn(1,10000))  % (mean = 1, var = 2)
hist(w)

A = [1 2; 3 4; 5 6]

C = 2*ones(2,3)  % same as C = [2 2 2; 2 2 2]
I = eye(4)    % 4x4 identity matrix

% help function
help eye
help rand

% useful commands
who		% list the name of all variables
whos	% list all information about every variables
clc		% clear command window
clear	% or clear all (for all variables)
clear x % x is a specific variable
close	% close all opening windows/figures

% =======================================================
% Section 2: Matlab Tutorial: Moving data around 


%% dimensions
sz = size(A) % size of a matrix
size(A,1)  % number of rows
size(A,2)  % number of cols
length(v)  % size of longest dimension

%% indexing
A(3,2)  % indexing is (row,col)
A(2,:)  % get the 2nd row. 
        % ":" means every element along that dimension
A(:,2)  % get the 2nd col
A([1 3],:)  % get the 1st and 3rd rows

A(:,2) = [10; 11; 12]     % change second column
A = [A, [100; 101; 102]]; % append column vec
A(:) % Select all elements as a column vector.

% Putting data together 
A = [1 2; 3 4; 5 6]
B = [11 12; 13 14; 15 16] % same dims as A
C = [A B]       % or [A, B] the same
C = [A; B] 


% =======================================================
% Section 3: Matlab Tutorial: Computing on data 

%% vector operations
v = [1; 2; 3]
1./v
log(v)  % functions like this operate element-wise on vecs or matrices 
exp(v)  % e^v
abs(v) % abs([-1; 2; -3])

-v  % -1*v

v + ones(length(v), 1)
% v + 1  % same


%% matrix operations
A = [1 2; 3 4; 5 6]
B = [11 12; 13 14; 15 16] % same dims as A
C = [1 1; 2 2]
A * C  % matrix multiplication
A .* B % element-wise multiplcation
% A .* C  or A * B gives error - wrong dimensions
A .^ 2

A'  % matrix transpose A prime


%% misc useful functions
% functions on vector

% max  (or min)
a = [1 15 2 0.5]
val = max(a)
[val,ind] = max(a)

% sum, prod
a = [1 15 2 0.5]
sum(a)
prod(a)
floor(a) % or ceil(a)   % round up or round down

% find
a < 3       % element-wise comparison
find(a < 3)     % which elements are less than 3

% functions on matrix
A = magic(9)

sum(A,1)
sum(A,2)
sum(sum( A .* eye(9) ))
sum(sum( A .* flipud(eye(9)) ))

A = magic(3)    % help magic -> math property that its has sum of each row, columns, diagonal as the same number
[r,c] = find(A>=7)

max(A,[],1)     % per column maximum
max(A,[],2)     % per row maximum
max(max(A))     % or max(A(:))

% Matrix inverse (pseudo-inverse)
pinv(A)        % inv(A'*A)*A'


% =======================================================
% Section 4: Matlab Tutorial: Plotting 


%% plotting
t = [0:0.01:0.98];
y1 = sin(2*pi*4*t); 
plot(t,y1);
y2 = cos(2*pi*4*t);
hold on;  % "hold off" to turn off
plot(t,y2,'r');
xlabel('time');
ylabel('value');
legend('sin','cos');
title('my plot');
print -dpng 'myPlot.png'
close;           % or,  "close all" to close all figs

% =======================================================
% Section 5: Matlab Tutorial: For, while, if statements, and functions.

v = zeros(10,1);
for i=1:10, 
    v(i) = 2^i;
end
% another way
indecies = 1:10
for i = indecies
    v(i) = 2^i;
end
% Can also use "break" and "continue" inside for and while loops to control execution.

i = 1;
while i <= 5,
  v(i) = 100; 
  i = i+1;
end

i = 1;
while true, 
  v(i) = 999; 
  i = i+1;
  if i == 6,
    break;
  end;
end

if v(1)==1,
  disp('The value is one!');
elseif v(1)==2,
  disp('The value is two!');
else
  disp('The value is not one or two!');
end

% Functions

% Create a file called squareThisNumber.m with the following contents (without the %):
% function r = squareThisNumber(x)
%   r = x * x;
% end

squareThisNumber(5);  
% If function is undefine, use "pwd" to check current directory (path), 
% and "cd" to change directories
pwd
cd 'C:\Users\ang\Desktop';
squareThisNumber(5);  

% multiple output values
[a,b] = squareAndCubeThisNumber(5);
                     
% Matlab search path (advanced/optional) 
addpath('C:\Users\ang\Desktop');
cd 'C:\'
squareThisNumber(5);

%% last thing
exit  % or quit




