<<<<<<< HEAD
# 理解傅里叶

## Some definition of $\sin$ and $\cos$
- 正弦波是一个圆周运动在一条直线上的投影。所以频域的基本单元也可以理解为一个始终在旋转的圆。
![image3](../Note/images/Fourier_image_3.png "image3")

## 1. 频域
- 任何周期函数，都可以看作是不同振幅，不同相位正弦波的叠加。
- 贯穿时域与频域的方法，就是傅里叶分析。
  
## 2. Fourier Series 的频谱
![image1](../Note/images/Fourier_image_1.png "image1")
-  左上中有一个正弦波 $\cos (x)$
-  右上中由两个正弦波叠加 $\cos (x) + a. \cos (3x)$
-  左下由四个正弦波叠加
-  右下由10个正弦波叠加
- 随着正弦波数量逐渐的增长，他们最终会叠加成一个标准的矩形，随着叠加的递增，所有正弦波中上升的部分逐渐让原本缓慢增加的曲线不断变陡，而所有正弦波中下降的部分又抵消了上升到最高处时继续上升的部分使其变为水平线。一个矩形就这么叠加而成了。

![image2](../Note/images/Fourier_image_2.png "image2")
- 在这几幅图中，最前面黑色的线就是所有正弦波叠加而成的总和，也就是越来越接近矩形波的那个图形。而后面依不同颜色排列而成的正弦波就是组合为矩形波的各个分量。这些正弦波按照频率从低到高从前向后排列开来，而每一个波的振幅都是不同的。一定有细心的读者发现了，每两个正弦波之间都还有一条直线，那并不是分割线，而是振幅为0的正弦波！也就是说，为了组成特殊的曲线，有些正弦波成分是不需要的。这里，不同频率的正弦波我们成为频率分量。

![image4](../Note/images/Fourier_image_4.png "image4")
- 上图就是上面的无数频率叠加图从侧面看过去的样子。 也就是一个矩形波在频域的样子。

![image5](../Note/images/Fourier_image_5.png "image5")




# The Discrete Fourier Tansform (DFT)
=======
# Fourier 
>>>>>>> 6e844cb153c56a9ab7aea8b2f5f6e7748c49b2ca

## Part 1 三角函数的正交性

 - 三角函数系： 集合
    - $$ \{0(sin0x), 1(cos0x), sinx, cosx, sin2x, cos2x,..., sin(nx), cos(nx)...\}, n = 0, 1, 2, 3...$$
  - Orthogonality:
    $$
    \int_{-\pi}^{\pi} \sin nx \cos mx dx = 0, n \neq m
    $$
    $$
    \int_{-\pi}^{\pi} \cos nx \cos mx dx = 0, n \neq m
    $$
    如果两个向量正交，则
   - 如果
