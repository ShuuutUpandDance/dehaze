# -*- coding: utf-8 -*-
import numpy as np
from bg_light import get_bg_light_by_diff
from dark_channel import get_dark_channel

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

# pos = get_bg_light_by_diff(img_fake, radius=1)
# print('pos', pos)
dc = get_dark_channel(img_fake, radius=1)
print(dc)