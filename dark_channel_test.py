# -*- coding: utf-8 -*-
from dark_channel import get_dark_channel, get_gb_dark_channel, get_dark_channel_for_channel
import numpy as np

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

print(img_fake[:, :, 1])
print(img_fake[:,:, 1].shape)
print(np.argmin(img_fake[:, :, 1]))
print("########################")
# dc = get_dark_channel(img_fake, radius=2).astype(np.uint8)
# dc = get_gb_dark_channel(img_fake, radius=1).astype(np.uint8)
# dc = get_dark_channel_for_channel(img_fake[:, :, 1], radius=1)


