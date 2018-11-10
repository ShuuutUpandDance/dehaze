# -*- coding: utf-8 -*-
from dark_channel import get_gb_dark_channel, get_max_channel_for_channel
from util import rearrange_with_lower_bound
import cv2
import numpy as np
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
b = img_fake ** 2.
print(b)
