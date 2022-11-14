x = imread("house.tif");
y = imread("jet.tiff");


xf = fft2(double(x));
yf = fft2(double(y));

xf1 = abs(xf);
xf2 = angle(xf);

yf1 = abs(yf);
yf2 = angle(yf);



xfr=xf1.*cos(yf2)+xf1.*sin(yf2).*1i;
yfr=yf1.*cos(xf2)+yf1.*sin(xf2).*1i;



xr=abs(ifft2(xfr));
yr=abs(ifft2(yfr));

xr=uint8(xr);
yr=uint8(yr);
size(xr);

xr = xr(:, :, 1:1);
yr = yr(:, :, 1:1);


imshow(xr);
imshow(yr)
