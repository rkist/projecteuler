
class Graph:
    def __init__(self, nodes: set):
        self.nodes = nodes

    def get_nodes(self) -> set:
        return self.nodes
    
    def add_node(self, node):
        self.nodes.add(node)

class DAG (Graph):
    def __init__(self, nodes: set):
        super().__init__(nodes)
        self.edges = {node: [] for node in nodes}

    def add_node(self, node):
        super().add_node(node)
        self.edges[node] = []

    def add_edge(self, start, end):
        self.edges[start].append(end)

    def remove_edge(self, start, end):
        self.edges[start].remove(end)

    def remove_node(self, node):
        self.nodes.remove(node)
        parents = self.get_parents(node)
        for parent in parents:
            self.remove_edge(parent, node)
        children = self.get_children(node)
        for child in children:
            self.remove_edge(node, child)
    
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
    
