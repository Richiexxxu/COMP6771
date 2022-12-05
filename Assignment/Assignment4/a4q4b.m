I = imread('lena.tif');

% question b
[c, s] = wavedec2(I, 3, 'db4');
% level 1
[H1, V1, D1] = detcoef2('all', c, s, 1);
A1 = appcoef2(c, s, 'db4', 1);
V1img = wcodemat(V1, 255, 'mat', 1);
H1img = wcodemat(H1, 255, 'mat', 1);
D1img = wcodemat(D1, 255, 'mat', 1);
A1img = wcodemat(A1, 255, 'mat', 1);
figure
subplot(2, 2, 1);imagesc(A1img);colormap pink(255);title("(DB4)Approximation coef. of Level 1")
subplot(2, 2, 2);imagesc(H1img);title("(DB4) Horizontal detail coef. of level 1")
subplot(2, 2, 3);imagesc(V1img);title("(DB4) Vertical detail coef. of Level 1")
subplot(2, 2, 4);imagesc(D1img);title("(DB4) Diagonal detail coef. of Level 1")

% level 2
[H2, V2, D2] = detcoef2('all', c, s, 2);
A2 = appcoef2(c, s, 'db4', 2);
V2img = wcodemat(V2, 255, 'mat', 1);
H2img = wcodemat(H2, 255, 'mat', 1);
D2img = wcodemat(D2, 255, 'mat', 1);
A2img = wcodemat(A2, 255, 'mat', 1);
figure
subplot(2, 2, 1); imagesc(A2img); colormap pink(255); title("(DB4) Approximation coef. of level 2")
subplot(2, 2, 2); imagesc(H2img); title("(DB4) Horizontal detail coef. of level 2")
subplot(2, 2, 3); imagesc(V2img); title("(DB4) Vertical detail coef. of level 2")
subplot(2, 2, 4); imagesc(D2img); title("(DB4) Diagonal detail coef. of level 2")

% level 3
[H3, V3, D3] = detcoef2('all', c, s, 3);
A3 = appcoef2(c, s, 'db4', 3);
V3img = wcodemat(V3, 255, 'mat', 1);
H3img = wcodemat(H3, 255, 'mat', 1);
D3img = wcodemat(D3, 255, 'mat', 1);
A3img = wcodemat(A3, 255, 'mat', 1);
figure
subplot(2, 2, 1); imagesc(A3img); colormap pink(255); title("(DB4) Approximation coef. of level 3")
subplot(2, 2, 2); imagesc(H3img); title("(DB4) Horizontal detail coef. of level 3")
subplot(2, 2, 3); imagesc(V3img); title("(DB4) Vertical detail coef. of level 3")
subplot(2, 2, 4); imagesc(D3img); title("(DB4) Diagonal detail coef. of level 3")