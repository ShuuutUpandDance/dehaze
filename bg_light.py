# -*- coding: utf-8 -*-
import numpy as np
from dark_channel import get_dark_channel_for_channel, get_gb_dark_channel, get_dark_channel
from point import Point
from queue import PriorityQueue
import math


def get_bg_light_hemethod(img, radius, p=0.001, isUW=False):
    if isUW:
        dc = get_gb_dark_channel(img, radius)
    else:
        dc = get_dark_channel(img, radius)

    rows = dc.shape[0]
    cols = dc.shape[1]

    pq = PriorityQueue()
    for i in range(rows):
        for j in range(cols):
            point = Point(x=i, y=j, val=dc[i, j])
            pq.put(point)

    n = math.floor(rows * cols * p)
    brightest_points = []
    for i in range(n):
        brightest_points.append(pq.get())

    return brightest_points


def get_bg_light_by_diff(img, radius):
    dc_r = get_dark_channel_for_channel(img[:, :, 2], radius=radius).astype(np.int32)
    dc_b = get_dark_channel_for_channel(img[:, :, 0], radius=radius).astype(np.int32)
    dc_g = get_dark_channel_for_channel(img[:, :, 1], radius=radius).astype(np.int32)

    diff = np.zeros((img.shape[0], img.shape[1]), dtype=np.int32)

    for i in range(diff.shape[0]):
        for j in range(diff.shape[1]):
            diff[i, j] = dc_r[i, j] - max(dc_b[i, j], dc_g[i, j])

    # print(diff)
    return np.argmin(diff)
