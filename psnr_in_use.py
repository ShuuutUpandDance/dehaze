# -*- coding: utf-8 -*-
from psnr import psnr
import cv2
from skimage.measure import compare_psnr, compare_ssim

# src_he = cv2.imread('uw_pic/refined/uw7_he_enhanced.jpg')
# src = cv2.imread('uw_pic/refined/uw7_enhanced.jpg')
# dst = cv2.imread('uw_pic/uw7.jpg')

# src_he = cv2.imread('fish_uw_pic/refined/fish_uw5_he_enhanced.jpg')
# src = cv2.imread('fish_uw_pic/refined/fish_uw5_enhanced.jpg')
# dst = cv2.imread('fish_uw_pic/fish_uw5.jpg')

src_he = cv2.imread('fish/fish9_he_enhanced.jpg')
src = cv2.imread('fish/fish9_enhanced.jpg')
dst = cv2.imread('fish/fish9.jpg')

print('he:', psnr(src_he, dst))
print('my:', psnr(src, dst))

print('=======================')

print('he:', compare_ssim(src_he, dst, win_size=15, multichannel=True))
print('my:', compare_ssim(src, dst, win_size=15, multichannel=True))