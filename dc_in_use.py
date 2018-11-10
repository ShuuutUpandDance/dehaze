# -*- coding: utf-8 -*-
import cv2
import numpy as np
from dark_channel import get_dark_channel, get_gb_dark_channel, get_red_channel, get_dark_channel_for_channel

# img = cv2.imread('haze_pic/haze1.jpg')
img = cv2.imread('uw_pic/uw7.jpg')
# img = cv2.imread('no_haze_pic/no_haze1.jpg')
# img = cv2.imread('fish_uw_pic/fish_uw3.jpg')

print(img.shape)

# dc = get_dark_channel(img, radius=20)
# dc_gb = get_gb_dark_channel(img, radius=20)
# dc_red = get_red_channel(img, radius=10)
min_channel_red = get_dark_channel_for_channel(img[:,:,2], 10).astype(np.uint8)

file_name = 'uw7_min_channel_red' + '.jpg'
# cv2.imshow('gb', dc_gb)
# cv2.imshow('red', dc_red)
cv2.imshow('dc', min_channel_red)
cv2.waitKey(0)
cv2.destroyAllWindows()
# dc_red = (dc_red * 255).astype(np.uint8)
cv2.imwrite(file_name, min_channel_red)
