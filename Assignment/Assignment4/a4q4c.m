I = imread('lena.tif');

[c, s] = wavedec2(I, 3, 'haar');
[cdb, sdb] = wavedec2(I, 3, 'db4');



A3db = appcoef2(cdb, sdb, 'db4', 3);
A3dbimg = wcodemat(A3db, 255, 'mat', 1);


[H, V, D] = detcoef2('all', c, s, 3);
A3 = appcoef2(c, s, 'haar', 3);
A3img = wcodemat(A3, 255, 'mat', 1);




figure
subplot(1, 2, 1); imagesc(A3dbimg); colormap pink(255); title("approximation coef. of level 3 DB4")
subplot(1, 2, 2); imagesc(A3img); colormap pink(255); title("approximation coef. of level 3 Haar")


