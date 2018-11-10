# -*- coding: utf-8 -*-
class Point:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val

    def __cmp__(self, other):
        if self.val < other.val:
            return -1
        elif self.val == other.val:
            return 0
        else:
            return 1

    def __lt__(self, other):  # 优先级队列以 lt 来比较，为了构建大顶堆，这里就要反直觉
        if self.val > other.val:
            return True
        else:
            return False

    def __str__(self):
        return "Point's value is " + str(self.val) + " position is (" + str(self.x) + ", " + str(self.y) + ")"

