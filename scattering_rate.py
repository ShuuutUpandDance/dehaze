# -*- coding: utf-8 -*-
from dark_channel import get_gb_dark_channel, get_max_channel_for_channel
from util import rearrange_with_lower_bound, safe_add, safe_matrix_subtract, safe_matrix_divide
import cv2
import numpy as np
from normalize import normalize_with_max_min_channel
from bg_light import get_bg_light_by_diff
import math
import time

img = cv2.imread('uw_pic/uw6.jpg')
# img = cv2.imread('fish_uw_pic/fish_uw5.jpg')

filename = 'fish_uw5_' + 'enhanced.jpg'

start_time = time.time()

height = img.shape[0]
width = img.shape[1]
pos = get_bg_light_by_diff(img, radius=10)
x = math.floor(pos / width)
y = max(pos - math.floor(pos / width) * width - 1, 0)
print('pos: (' + str(x) + ", " + str(y) + ')')

# bg_light_vector = [img[0, 350, 0], img[0, 350, 1], img[0, 350, 2]]
bg_light_vector = (int(img[x, y, 0]) + int(img[x, y, 1]) + int(img[x, y, 2])) / 3
bg_light_r_channel = img[x, y, 2]
print('bg_light_r_channel:', bg_light_r_channel)

img_b = img[:, :, 0]
img_g = img[:, :, 1]
img_r = img[:, :, 2]
print('bg_light_vector:', bg_light_vector)

norm_img = np.divide(img.astype(np.int32), bg_light_vector)

dc = get_gb_dark_channel(norm_img, 10)
scattering_rate = dc.copy()

# print("=================")
t_b = 1 - dc
t_g = 1 - dc
t_b = cv2.bilateralFilter(t_b.astype(np.float32), 5, 75, 75)
t_g = cv2.bilateralFilter(t_g.astype(np.float32), 5, 75, 75)
# cv2.imshow('tb', t_b)
# cv2.imshow('tg', t_g)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

### red trans ###
max_r_channel = get_max_channel_for_channel(img_r, 10)
# cv2.imshow('mr', max_r_channel.astype(np.uint8))
tal = np.mean(t_b) / np.mean(max_r_channel)
t_r = np.multiply(max_r_channel, tal)
t_r = cv2.bilateralFilter(t_r.astype(np.float32), 5, 75, 75)
# print(t_r)
# cv2.imshow('tr', t_r)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # print("=================")
### rec ###
lower_bound_for_trans = 0.45
t_r = rearrange_with_lower_bound(t_r, 0.4)
t_g = rearrange_with_lower_bound(t_g, lower_bound_for_trans)
t_b = rearrange_with_lower_bound(t_b, lower_bound_for_trans)

# j_r = (img_r - bg_light_vector[2] * scattering_rate) / t_r
# j_g = (img_g - bg_light_vector[1] * scattering_rate) / t_g
# j_b = (img_b - bg_light_vector[0] * scattering_rate) / t_b

j_g = safe_add(safe_matrix_divide(img_g - bg_light_vector, t_g), bg_light_vector)
j_b = safe_add(safe_matrix_divide(img_b - bg_light_vector, t_b), bg_light_vector)
# j_g = safe_matrix_divide(safe_matrix_subtract(img_g, bg_light_vector * scattering_rate), t_g)
# j_b = safe_matrix_divide(safe_matrix_subtract(img_b, bg_light_vector * scattering_rate), t_b)
j_r = safe_matrix_divide(safe_matrix_subtract(img_r, bg_light_r_channel * scattering_rate), t_r)

j_r = j_r.astype(np.uint8)
j_g = j_g.astype(np.uint8)
j_b = j_b.astype(np.uint8)

end_time = time.time()
print('Duration:', end_time - start_time)
# norm_j_b = normalize_with_max_min_channel(j_b)
# norm_j_g = normalize_with_max_min_channel(j_g)
# norm_img_r = normalize_with_max_min_channel(img_r)
# avg_b_rec = np.mean(norm_j_b)
# avg_g_rec = np.mean(norm_j_g)
# avg_r_rec = 1.5 - avg_b_rec - avg_g_rec
# delta = avg_r_rec / np.mean(norm_img_r)
# print('delta', delta)
# norm_j_r = norm_img_r * delta * 0.2

# print(norm_j_r)

cv2.imshow('a', j_r)
cv2.imshow('b', j_b)
cv2.imshow('c', j_g)
img_refine = cv2.merge([j_b, j_g, j_r])
cv2.imshow('d', img_refine)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite(filename, img_refine)
