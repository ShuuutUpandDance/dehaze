# -*- coding: utf-8 -*-
from bg_light import get_bg_light_hemethod
import cv2
import numpy as np
from queue import PriorityQueue
from point import Point

# img = cv2.imread('haze_pic/haze1.jpg')
# img = cv2.imread('uw_pic/uw6.jpg')
# img = cv2.imread('fish_uw_pic/fish_uw2.jpg')
img = cv2.imread('fish/fish7.jpg')
filename = 'fish7_he_bglight_exact' + ".jpg"

brightest_points_in_dc = get_bg_light_hemethod(img, radius=7, isUW=True)

# paint the area
# for i in range(len(brightest_points_in_dc)):
#     point_in_dc = brightest_points_in_dc[i]
#     y = point_in_dc.y
#     x = point_in_dc.x
#     cv2.circle(img, (y, x), 5, (0, 0, 255), 8)

pq = PriorityQueue()
for i in range(len(brightest_points_in_dc)):
    point_in_dc = brightest_points_in_dc[i]
    y = point_in_dc.y
    x = point_in_dc.x
    temp_sum = 0
    for c in range(3):
        temp_sum = temp_sum + img[x, y, c]
    mean = temp_sum / 3
    point_in_img = Point(x=x, y=y, val=mean)
    pq.put(point_in_img)

brightest_point_in_img = pq.get()
cv2.circle(img, (brightest_point_in_img.y, brightest_point_in_img.x), 15, (0, 0, 255), 7)

cv2.imshow('a', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite(filename, img)