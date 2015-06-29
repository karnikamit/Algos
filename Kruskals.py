__author__ = 'karnikamit'
from operator import itemgetter
graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
        'edges':[{'edge_w': ['A', 'B'], 'weight': 05,},
                 {'edge_w': ['A', 'C'], 'weight': 10},
                 {'edge_w': ['B', 'D'], 'weight': 45},
                 {'edge_w': ['B', 'E'], 'weight': 55},
                 {'edge_w': ['B', 'F'], 'weight': 20},
                 {'edge_w': ['C', 'F'], 'weight': 25},
                 {'edge_w': ['D', 'E'], 'weight': 35},
                 {'edge_w': ['D', 'F'], 'weight': 50},
                 {'edge_w': ['E', 'F'], 'weight': 45}
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
        # Firstly Edges arranged in increasing order of their weights
        new_graph = sorted(self.graph['edges'], key=itemgetter('weight'), reverse=False)
        visit = self.visited()
        total = set()
        for i in new_graph:
            edges = i['edge_w']
            for j in edges:
                if visit[j] == 'No':
                    visit[j] = 'Yes'
                    total.add(i['weight'])
        return sum(total), 'visited', visit

    def visited(self):
        vertices = self.graph['vertices']
        visit = dict()
        for i in vertices:      # initialize all vertices as unvisited
            visit[i] = 'No'
        return visit


k = Kruskals(graph)
print k.find_mst()
