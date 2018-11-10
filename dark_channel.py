# -*- coding: utf-8 -*-
import cv2
import numpy as np
from normalize import normalize_with_max_min


def get_dark_channel(img, radius):
    height = img.shape[0]
    width = img.shape[1]

    dc = np.zeros((img.shape[0], img.shape[1]))

    for i in range(height):
        for j in range(width):
            left = max(j - radius, 0)
            right = min(j + radius, width - 1)
            up = max(i - radius, 0)
            down = min(i + radius, height - 1)

            min_in_channels = np.min(img[up: down + 1, left: right + 1, 0])
            for c in range(3):
                min_in_patch = np.min(img[up: down + 1, left: right + 1, c])
                min_in_channels = min_in_channels if min_in_channels < min_in_patch else min_in_patch

            dc[i, j] = min_in_channels

    return dc.astype(np.uint8)


def get_dark_channel_for_channel(channel, radius):
    height = channel.shape[0]
    width = channel.shape[1]

    dc = np.zeros((channel.shape[0], channel.shape[1]))

    for i in range(height):
        for j in range(width):
            left = max(j - radius, 0)
            right = min(j + radius, width - 1)
            up = max(i - radius, 0)
            down = min(i + radius, height - 1)

            min_in_channels = np.min(channel[up: down + 1, left: right + 1])
            dc[i, j] = min_in_channels

    return dc


def get_max_channel_for_channel(channel, radius):
    height = channel.shape[0]
    width = channel.shape[1]

    dc = np.zeros((channel.shape[0], channel.shape[1]))

    for i in range(height):
        for j in range(width):
            left = max(j - radius, 0)
            right = min(j + radius, width - 1)
            up = max(i - radius, 0)
            down = min(i + radius, height - 1)

            max_in_channels = np.max(channel[up: down + 1, left: right + 1])
            dc[i, j] = max_in_channels

    return dc


# opencv 读出来的通道顺序是BGR！！！
def get_gb_dark_channel(img, radius):
    height = img.shape[0]
    width = img.shape[1]

    dc = np.zeros((img.shape[0], img.shape[1]))

    for i in range(height):
        for j in range(width):
            left = max(j - radius, 0)
            right = min(j + radius, width - 1)
            up = max(i - radius, 0)
            down = min(i + radius, height - 1)

            # print(img[up: down + 1, left: right + 1, 1])
            min_in_channels = np.min(img[up: down + 1, left: right + 1, 0])
            for c in [0, 1]:
                min_in_patch = np.min(img[up: down + 1, left: right + 1, c])
                # print('min_in_patch: ', min_in_patch)
                min_in_channels = min_in_channels if min_in_channels < min_in_patch else min_in_patch

            dc[i, j] = min_in_channels

    return dc


# opencv 读出来的通道顺序是BGR！！！
def get_red_channel(img, radius):
    norm_img = normalize_with_max_min(img)

    height = norm_img.shape[0]
    width = norm_img.shape[1]

    dc = np.zeros((norm_img.shape[0], norm_img.shape[1]))

    for i in range(height):
        for j in range(width):
            left = max(j - radius, 0)
            right = min(j + radius, width - 1)
            up = max(i - radius, 0)
            down = min(i + radius, height - 1)

            min_in_channels = np.min(1 - norm_img[up: down + 1, left: right + 1, 2])
            for c in [0, 1]:
                min_in_patch = np.min(norm_img[up: down + 1, left: right + 1, c])
                # print('min_in_patch: ', min_in_patch)
                min_in_channels = min_in_channels if min_in_channels < min_in_patch else min_in_patch

            dc[i, j] = min_in_channels

    return dc