
from graph import DAG
from plotter import GraphPlotter

def get_nodes(lines):
    nodes = set()
    for line in lines:
        for char in line:
            nodes.add(char)
    return nodes

def get_edges(lines):
    edges = []
    for line in lines:
        edges.append((line[0], line[1]))
        edges.append((line[1], line[2]))
    return edges

def kahn(dag: DAG):
    L = []
    S = dag.get_roots()
    while S:
        n = S.pop()
        L.append(n)
        dag.remove_node(n)
        m = dag.get_roots()
        if m:
            S.extend(m)
    return L


def SolveProblem():
    print(__name__)

    with open("ProjectEuler/problem79/codes.txt") as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]

    nodes = set(get_nodes(lines))
    dag = DAG(nodes)

    edges = get_edges(lines)
    for edge in edges:
        dag.add_edge(edge[0], edge[1])

    plotter = GraphPlotter()
    plotter.drawDAG(dag)

    L = kahn(dag)
    passcode = "".join(L)

    # 73162890
    return passcode