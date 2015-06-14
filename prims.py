__author__ = 'karnikamit'
import numpy as np

"""
    Assume that G is connected, undirected and weighted graph.
    Input: The cost adjacency matrix c and number of vertices n.
    output: Minimum weight spanning tree T
"""

# preparing adjacency matrix

matrix_values = np.array([[None, 5, 15, 20, None],
                 [5, None, 25, None, None],
                 [15, 25, None, 30, 37],
                 [10, None, 30, None, 35],
                 [None, None, 37, 35, None]])

matrix_values = matrix_values.transpose()
n = len(matrix_values)
s = set()
visited = dict()
for v in range(1, n+1):
    visited[v] = 0      # Initialize all vertices as unvisited


visited[1] = 'yes'    # assuming the starting node as 1
i = 1
cost = set()
for t in matrix_values:
    m = min([t[item] for item in range(len(t)) if t[item] is not None])  # determining minimum edge
    cost.add(m)
    visited[i] = 'yes'
    i += 1
print 'visited', visited
print 'total_cost ', sum(cost)
