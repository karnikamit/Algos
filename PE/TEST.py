# -*- coding: utf-8 -*-
__author__ = "karnikamit"
import itertools

n = 10
for i in itertools.takewhile(lambda x: x < n, itertools.count(1)):
    print i


