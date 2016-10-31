def CreateUndirectedGraph(nodes, vertices):
    graph = dict()
    for node in nodes:
        graph[node] = []

    for n, m in vertices:
        graph[n].append(m)
        graph[m].append(n)

    return graph

def CreateDirectedGraph(nodes, vertices):
    graph = dict()
    for node in nodes:
        graph[node] = []

    for n, m in vertices:
        graph[n].append(m)

    return graph







def DetectCicles(graph):
    cicles = []
    for k, v in graph.iteritems():
        _DetectCicleRecursion([k], cicles, graph)
    return cicles

def _DetectCicleRecursion(cicleCandidate, cicles, graph):
    rootNode = cicleCandidate[-1]  
    if (len(cicleCandidate) > 1 and rootNode == cicleCandidate[0]): 
        cicles.append(cicleCandidate)
        return
    if (rootNode in cicleCandidate[1:]): 
        return
    adjNodes = graph[rootNode]
    for node in adjNodes:
        newCicleCandidate = cicleCandidate[:]
        newCicleCandidate.append(node)
        _DetectCicleRecursion(newCicleCandidate, cicles, graph)









def DetectKClique(graph, size):
    cleanGraph = dict()
    for k, v in graph.iteritems():
        if (len(v) >= size-1):
            cleanGraph[k] = v

    cliqueCandidate = []
    return _DetectCliqueRecursion(cliqueCandidate, cleanGraph, size)       

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