# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
'''
The following rules have to be obeyed:
1. Only one disk may be moved at a time.
2. Only the most upper disk from one of the rods can be moved in a move
3. It can be put on another rod, if this rod is empty or if the most upper disk of this rod is larger than the one which is moved.

number of moves necessary to move a tower with n disks can be calculated as: 2^n - 1

'''

source_peg = [4, 3, 2, 1]
helper_peg = []
target_peg = []
steps = 0


def ihanoi(n, source, helper, target):
    if n > 1:
        ihanoi(n-1, source, target, helper)
        if source:
            target.append(source.pop())
        ihanoi(n-1, helper, source, target)
    return 'source: {0}, helper: {1}, target: {2}'.format(source, helper, target)

print ihanoi(len(source_peg), source_peg, helper_peg, target_peg)
