__author__ = 'karnikamit'

"""
    Assume that G is connected, undirected and weighted graph.
    Input: The cost adjacency matrix c and number of vertices n.
    output: Minimum weight spanning tree T
"""
n = 5
visited = dict()
for i in range(1, n+1):
    visited[i] = 0      # Initialize all vertices as unvisited
