# -*- coding: utf-8 -*-
__author__ = "karnikamit"


def displayPathToPrincess(n, grid):
    """
    Find princess in the grid in min moves
    """
    for i, row in enumerate(grid):
        if 'p' in row:
            princess = [i, row.index('p')]
        if 'm' in row:
            me = [i, row.index('m')]

    r, c = find_path(princess, me)
    path = [r]
    path.append(c)
    return '\n'.join(path)


def find_path(p_pos, me_pos):
    cd = p_pos[0] - me_pos[0]
    rd = p_pos[1] - me_pos[1]
    if cd > 0:
        r_path = 'DOWN'
    else:
        r_path = 'UP'

    if p_pos[1] - me_pos[1] > 0:
        c_path = 'RIGHT'
    else:
        c_path = 'LEFT'
    return r_path * abs(cd), c_path * abs(rd)


if __name__ == '__main__':
    N = int(raw_input())
    grid = []
    for _ in xrange(N):
        grid.append(raw_input().strip())

    print displayPathToPrincess(N, grid)