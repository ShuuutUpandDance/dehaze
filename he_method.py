# -*- coding: utf-8 -*-
from dark_channel import get_dark_channel, get_gb_dark_channel
from util import rearrange_with_lower_bound, safe_check, safe_add, safe_matrix_subtract, safe_matrix_divide, safe_subtract
import cv2
import numpy as np
from bg_light import get_bg_light_hemethod
import math
from queue import PriorityQueue
from point import Point

# img = cv2.imread('uw_pic/uw7.jpg')
# img = cv2.imread('fish_uw_pic/fish_uw5.jpg')
img = cv2.imread('fish/fish9.jpg')

filename = 'fish9_' + 'he_enhanced.jpg'

height = img.shape[0]
width = img.shape[1]

brightest_points_in_dc = get_bg_light_hemethod(img, radius=7, isUW=True)
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
x = brightest_point_in_img.x
y = brightest_point_in_img.y
print('pos: (' + str(x) + ", " + str(y) + ')')
# cv2.circle(img, (brightest_point_in_img.y, brightest_point_in_img.x), 10, (0, 0, 255), 7)

bg_light_vector = (int(img[x, y, 0]) + int(img[x, y, 1]) + int(img[x, y, 2])) / 3
print('bg_light_vector:', bg_light_vector)

img_b = img[:, :, 0]
img_g = img[:, :, 1]
img_r = img[:, :, 2]

norm_img = np.divide(img.astype(np.int32), bg_light_vector)
dc = get_gb_dark_channel(norm_img, 7)

t = 1 - dc
t = cv2.bilateralFilter(t.astype(np.float32), 5, 75, 75)
lower_bound_for_trans = 0.1
t = rearrange_with_lower_bound(t, lower_bound_for_trans)
# print(t)
# print('=================')

j_r = safe_check((img_r - bg_light_vector) / t + bg_light_vector)
j_g = safe_check((img_g - bg_light_vector) / t + bg_light_vector)
j_b = safe_check((img_b - bg_light_vector) / t + bg_light_vector)
# j_r = safe_matrix_divide(safe_matrix_subtract(img_r, bg_light_vector * dc), t)
# # j_g = safe_matrix_divide(safe_matrix_subtract(img_g, bg_light_vector * dc), t)
# # j_b = safe_matrix_divide(safe_matrix_subtract(img_b, bg_light_vector * dc), t)
# j_g = safe_add(safe_matrix_divide(img_g - bg_light_vector, t), bg_light_vector)
# j_b = safe_add(safe_matrix_divide(img_b - bg_light_vector, t), bg_light_vector)
# print(j_b)
# print('=================')

j_r = j_r.astype(np.uint8)
j_g = j_g.astype(np.uint8)
j_b = j_b.astype(np.uint8)

# print(j_r)
# print(j_g)
cv2.imshow('jr', j_r)
cv2.imshow('jg', j_g)
cv2.imshow('jb', j_b)
img_refine = cv2.merge([j_b, j_g, j_r])
cv2.imshow('refine', img_refine)
cv2.imwrite(filename, img_refine)
cv2.waitKey(0)
cv2.destroyAllWindows()

