# -*- coding: utf-8 -*-


def rearrange_with_lower_bound(matrix, lower_bound):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i, j] = max(matrix[i, j], lower_bound)
    return matrix


def safe_add(matrix, addend):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if addend > (255 - matrix[i, j]):
                matrix[i, j] = 255
            else:
                matrix[i, j] = matrix[i, j] + addend
    return matrix


def safe_subtract(matrix, subtractor):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if subtractor > matrix[i, j]:
                matrix[i, j] = 0
            else:
                matrix[i, j] = matrix[i, j] - subtractor
    return matrix


def safe_matrix_subtract(matrix, subtractor_matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if int(subtractor_matrix[i, j]) > int(matrix[i, j]):
                matrix[i, j] = 0
            else:
                matrix[i, j] = matrix[i, j] - subtractor_matrix[i, j]
    return matrix


def safe_matrix_divide(matrix, divisor_matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (int(matrix[i, j]) / divisor_matrix[i, j]) > 255:
                matrix[i, j] = 255
            else:
                matrix[i, j] = matrix[i, j] / divisor_matrix[i, j]
    return matrix