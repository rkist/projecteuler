import networkx as nx
import matplotlib.pyplot as plt

class GraphPlotter:
    def __init__(self):
        self.G = nx.DiGraph()

    def createGraph(self, nodes, edges):
        self.G = nx.DiGraph()
        for node in nodes:
            self.G.add_node(node)
        for edge in edges:
            self.G.add_edge(edge[0], edge[1])


    def drawGraph(self):
        pos = nx.spring_layout(self.G)
        nx.draw_networkx(self.G, pos, with_labels=True, arrows=True)
        plt.show()

class Graph:
    def __init__(self, nodes: set):
        self.plotter = GraphPlotter()

    def plot(self, nodes, edges):
        self.plotter.createGraph(nodes, edges)
        self.plotter.drawGraph()

class DAG (Graph):
    def __init__(self, nodes: set):
        self.nodes = nodes
        self.edges = {node: [] for node in nodes}

    def add_edge(self, start, end):
        self.edges[start].append(end)

    def get_nodes(self) -> set:
        return self.nodes
    
    def get_edges(self) -> dict:
        return self.edges
    
    def get_children(self, node) -> list:
        return self.edges[node]
    
    def get_parents(self, node) -> list:
        parents = []
        for parent in self.nodes:
            if node in self.edges[parent]:
                parents.append(parent)
        return parents
    
    def get_roots(self) -> list:
        roots = []
        for node in self.nodes:
            if not self.get_parents(node):
                roots.append(node)
        return roots
    
    def get_leaves(self) -> list:
        leaves = []
        for node in self.nodes:
            if not self.get_children(node):
                leaves.append(node)
        return leaves
    
