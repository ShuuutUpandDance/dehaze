# -*- coding: utf-8 -*-
from dark_channel import get_gb_dark_channel, get_max_channel_for_channel
from util import rearrange_with_lower_bound, safe_subtract
import cv2
import numpy as np
from channel_average import channel_avg
from normalize import normalize_with_max_min

img_fake = np.array(
    [
        [[1,2,3],
         [1,2,3],
         [1,2,3]],
        [[2,3,1],
         [2,3,1],
         [2,3,1]],
        [[3,1,2],
         [3,1,2],
         [3,1,2]]
    ]
)

a = np.array([3,3,3])
b = np.array([2,2,2], dtype=np.uint8)
c = b - a
print(type(c[0]))
print(c)