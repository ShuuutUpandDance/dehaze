# -*- coding: utf-8 -*-
import cv2

# img = cv2.imread('fish_uw_pic/fish_uw5.jpg')
img = cv2.imread('uw_pic/uw7.jpg')
origin_file_name = 'uw7' + '_edge.jpg'

# enhanced = cv2.imread('fish_uw_pic/refined/fish_uw5_enhanced.jpg')
enhanced = cv2.imread('uw_pic/refined/uw7_enhanced.jpg')
enhanced_file_name = 'uw7_enhanced' + '_edge.jpg'

img_edge = cv2.Canny(img, 100, 200)
enhanced_edge = cv2.Canny(enhanced, 100, 200)

cv2.imwrite(origin_file_name, img_edge)
cv2.imwrite(enhanced_file_name, enhanced_edge)
cv2.imshow('a', img_edge)
cv2.imshow('b', enhanced_edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
