def CreateUndirectedGraph(nodes, vertices):
    graph = dict()
    for node in nodes:
        graph[node] = []

    for n, m in vertices:
        graph[n].append(m)
        graph[m].append(n)

    return graph






def DetectKClique(undirectedGraph, size):
    cliqueCandidate = []
    return _DetectCliqueRecursion(cliqueCandidate, undirectedGraph, size)       

def _DetectCliqueRecursion(cliqueCandidate, graph, size):
    if (_CheckSubsetCompleteness(cliqueCandidate, graph)):
        if (len(cliqueCandidate) == size):
            print cliqueCandidate
            return cliqueCandidate
        else:
            for k, v in graph.iteritems():              
                if (k not in cliqueCandidate):
                    newCliqueCandidate = cliqueCandidate[:]
                    newCliqueCandidate.append(k)
                    c = _DetectCliqueRecursion(newCliqueCandidate, graph, size)
                    if (c is not None):
                        return c
    else:
        return None


def _CheckSubsetCompleteness(cliqueCandidate, graph):
    for node in cliqueCandidate:
        for secNode in cliqueCandidate:
            if (node == secNode):
                continue
            elif (secNode in graph[node]):
                continue
            else:
                return False
    return True