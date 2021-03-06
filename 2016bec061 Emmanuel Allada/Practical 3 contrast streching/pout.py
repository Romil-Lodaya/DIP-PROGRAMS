# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:25:50 2019

@author: Admin
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'D:\Btech practicals\DIP\pout.jfif')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(gray)
cv2.imshow("Gray_original",gray)
for i in range(247):
    for j in range(204):
        k=gray[i][j]
        if k<101:
            gray[i][j] *= 0.5
        elif k>100 and k<201:
            gray[i][j]=gray[i][j]*1.5-100
cv2.imwrite('pout_image.jpg',gray)
cv2.imshow("pout_histogram",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()