import networkx as nx
import matplotlib.pyplot as plt

from graph import DAG

class GraphPlotter:
    def __init__(self):
        self.G = nx.DiGraph()

    def __createGraph(self, nodes, edges):
        self.G = nx.DiGraph()
        for node in nodes:
            self.G.add_node(node)
        for edge in edges:
            self.G.add_edge(edge[0], edge[1])

    def __drawGraph(self):
        pos = nx.spring_layout(self.G)
        nx.draw_networkx(self.G, pos, with_labels=True, arrows=True)
        plt.show()

    def drawDAG(self, dag: DAG):
        nodes = dag.get_nodes()
        edges = []
        for node in nodes:
            for child in dag.get_children(node):
                edges.append((node, child))
        self.__createGraph(nodes, edges)
        self.__drawGraph()

