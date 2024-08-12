
from graph import DAG

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


def SolveProblem():
    print(__name__)

    with open("problem79/codes.txt") as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]

    # print(lines)
    # print(len(lines))

    nodes = get_nodes(lines)
    # print(nodes)

    dag = DAG(nodes)
    # print(dag.get_nodes())

    edges = get_edges(lines)
    # print(edges)

    for edge in edges:
        dag.add_edge(edge[0], edge[1])

    # print(dag.get_edges())

    return 0