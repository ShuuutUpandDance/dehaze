# -*- coding: utf-8 -*-
import numpy as np


def normalize_with_max_min(img):
    norm_img = np.zeros(img.shape)
    for i in range(3):
        img_channel = img[:, :, i]
        maxValue = np.max(img_channel)
        minValue = np.min(img_channel)
        norm_img[:, :, i] = np.divide(np.subtract(img_channel, minValue), (maxValue - minValue) * 1.0)

    return norm_img


def normalize_with_max_min_channel(channel):
    max_val = np.max(channel)
    min_val = np.min(channel)
    norm_channel = np.divide(np.subtract(channel, min_val), (max_val - min_val) * 1.0)

    return norm_channel