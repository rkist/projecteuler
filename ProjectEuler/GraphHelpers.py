def CreateGraph(nodes, vertices):
    graph = dict()
    for node in nodes:
        graph[node] = []

    for n, m in vertices:
        graph[n].append(m)
        graph[m].append(n)

    return graph






def DetectClique(graph, size):
    cliqueCandidate = []
    _DetectCliqueRecursion(cliqueCandidate, graph, size)       
    return cliqueCandidate


def _DetectCliqueRecursion(cliqueCandidate, graph, size):
    if (_CheckSubsetCompleteness(cliqueCandidate, graph)):
        if (len(cliqueCandidate) == size):
            print cliqueCandidate
            return True
        else:
            for k, v in graph.iteritems():              
                if (k not in cliqueCandidate):
                    newCliqueCandidate = cliqueCandidate[:]
                    newCliqueCandidate.append(k)
                    if (_DetectCliqueRecursion(newCliqueCandidate, graph, size)):
                        return True
    else:
        return False


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