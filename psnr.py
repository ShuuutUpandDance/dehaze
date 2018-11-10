# -*- coding: utf-8 -*-
import numpy as np
import math


def psnr(src, dst):
    r_diff = src[:, :, 2] - dst[:, :, 2]
    g_diff = src[:, :, 1] - dst[:, :, 1]
    b_diff = src[:, :, 0] - dst[:, :, 0]

    mse_r = np.sqrt(np.mean(r_diff ** 2.))
    mse_g = np.sqrt(np.mean(g_diff ** 2.))
    mse_b = np.sqrt(np.mean(b_diff ** 2.))

    mse = (mse_r + mse_g + mse_b) / 3

    return 10 * math.log(255 ** 2. / mse, 10)
