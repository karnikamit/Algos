# -*- coding: utf-8 -*-
__author__ = 'karnikamit'


def get_hight_diff(heights_array):
    heights_array.sort()
    heights = {}
    [heights.setdefault(i, []).append(i) for i in heights_array]
    sorted_heights = sorted(heights, key=lambda x: len(heights[x]))
    h1 = len(heights[sorted_heights[-1]])
    h2 = len(heights[sorted_heights[0]])
    max_diff = h1 - h2
    if not max_diff:
        return -1
    return max_diff

cases = int(raw_input())
for _ in xrange(cases):
    N = int(raw_input())
    heights = map(int, raw_input().split(' '))
    assert N == len(heights)
    print get_hight_diff(heights)
