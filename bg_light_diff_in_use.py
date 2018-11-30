# -*- coding: utf-8 -*-
from bg_light import get_bg_light_by_diff
from dark_channel import get_gb_dark_channel
import numpy as np
import cv2
import math

img = cv2.imread('fish/fish7.jpg')
filename = 'fish7'+'_bglight_diff.jpg'
# img = cv2.imread('uw_pic/uw1.jpg')
height = img.shape[0]
width = img.shape[1]
print(img.shape)

pos = get_bg_light_by_diff(img, radius=7)
print(pos)

x = math.floor(pos / width)
y = max(pos - math.floor(pos / width) * width - 1, 0)
print('pos: (' + str(x) + ", " + str(y) + ')')

temp = img.astype(np.int32)
bg_light_val = (temp[x, y, 0] + temp[x, y, 1] + temp[x, y, 2]) / 3
print('bg_light_val:', bg_light_val)

cv2.circle(img, (y, x), 15, (0, 0, 255), 7)  # 注意，这里要把x,y反过来


cv2.imshow('a', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite(filename, img)

# dc = get_gb_dark_channel(img, radius=15)
# pos2 = get_bg_light(dc)
# print(pos2)