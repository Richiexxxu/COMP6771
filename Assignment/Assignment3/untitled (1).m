%read image
img_house = imread("house.tif");
img_jet = imread("jet.tiff");
img_house = img_house(:, :, 1);
img_jet = img_jet(:, :, 1);


% Fourier Transformer
img_house_f = fft2(double(img_house));
img_jet_f = fft2(double(img_jet));

%calculate the magnitude and phase of house
img_house_m = abs(img_house_f);
img_house_ph = angle(img_house_f);

%calculate the magnitude and phase of jet
img_jet_m = abs(img_jet_f);
img_jet_ph = angle(img_jet_f); 

%reconstruct images
image_a=img_house_m.*cos(img_jet_ph)+img_house_m.*sin(img_jet_ph).*1i;
image_b=img_jet_m.*cos(img_house_ph)+img_jet_m.*sin(img_house_ph).*1i;
image_a=abs(ifft2(image_a));
image_b=abs(ifft2(image_b));
image_a=uint8(image_a);
image_b=uint8(image_b);


% plot images
subplot(2,2,1);imshow(img_house);title('House');
subplot(2,2,2);imshow(img_jet);title('Jet');
subplot(2,2,3);imshow(image_a);title('Magenitude of house with phase of Jet');
subplot(2,2,4);imshow(image_b);title('Magnitude of Jet with phase of House');