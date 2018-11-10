# -*- coding: utf-8 -*-
import numpy as np


def channel_avg(img):
    avgB = np.average(img[:, :, 0])
    avgG = np.average(img[:, :, 1])
    avgR = np.average(img[:, :, 2])
    return avgR, avgG, avgB