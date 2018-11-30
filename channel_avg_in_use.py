# -*- coding: utf-8 -*-
from channel_average import channel_avg
import cv2

# img = cv2.imread('no_haze_pic/no_haze1.jpg')
# img = cv2.imread('ld/ld1.jpg')
img = cv2.imread('fish/fish7.jpg')

avgR, avgG, avgB = channel_avg(img)

print('R', avgR)
print('G', avgG)
print('B', avgB)