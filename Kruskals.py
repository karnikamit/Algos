__author__ = 'karnikamit'
from operator import itemgetter

graph = {
        'vertices': ['1', '2', '3', '4', '5', '6'],
        'edges':[{'edge_w': '1, 2', 'weight': 05,},
                 {'edge_w': '1, 3', 'weight': 10},
                 {'edge_w': '2, 4', 'weight': 45},
                 {'edge_w': '2, 5', 'weight': 55},
                 {'edge_w': '2, 6', 'weight': 20},
                 {'edge_w': '3, 6', 'weight': 25},
                 {'edge_w': '4, 5', 'weight': 35},
                 {'edge_w': '4, 6', 'weight': 50},
                 {'edge_w': '5, 6', 'weight': 45}
                 ]
        }


class Kruskals:
    """
        This Algorithm begins by sorting grahph's edges in
        increasing order of their weights.
        scans through the sorted list, starting with empty sub graph
        and it adds next edge on the list to the current sub graph
        if this inclusion dooes not create a cycle, if else
        that edge is skipped
        :param: graph
        :return: minimum spanning tree
    """

    def __init__(self, graph):
        self.graph = graph

    def find_mst(self):
        pass

    def graph_sort(self):
        return sorted(self.graph['edges'], key=itemgetter('weight'), reverse=False)

