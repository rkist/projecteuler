def FindNumberOfPaths(start, end):
    if start == end:
        return 1
    if start[0] == end[0]:
        return FindNumberOfPaths((start[0],start[1]+1),end)
    if start[1] == end[1]:
        return FindNumberOfPaths((start[0]+1,start[1]),end)
    else:
        return FindNumberOfPaths((start[0],start[1]+1),end) + FindNumberOfPaths((start[0]+1,start[1]),end)

def FindNumberOfPathsDynamic(start, end):
    pathmatrix = [[-1 for x in xrange(start[0], end[0]+1)] for x in xrange(start[1], end[1]+1)]
    #print len(pathmatrix), len(pathmatrix[0])
    return __FindNumberOfPathsDynamicRecursion__(start, end, pathmatrix)



def __FindNumberOfPathsDynamicRecursion__(start, end, pathmatrix):
    if start == end:
        return 1
    if pathmatrix[start[0]][start[1]] != -1:
        return pathmatrix[start[0]][start[1]]

    if start[0] == end[0]:
        pathmatrix[start[0]][start[1]] = __FindNumberOfPathsDynamicRecursion__((start[0],start[1]+1), end, pathmatrix)
    elif start[1] == end[1]:
        pathmatrix[start[0]][start[1]] = __FindNumberOfPathsDynamicRecursion__((start[0]+1,start[1]), end, pathmatrix)
    else:
        pathmatrix[start[0]][start[1]] = __FindNumberOfPathsDynamicRecursion__((start[0],start[1]+1), end, pathmatrix) + __FindNumberOfPathsDynamicRecursion__((start[0]+1,start[1]), end, pathmatrix)
    return pathmatrix[start[0]][start[1]]
