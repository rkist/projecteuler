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
    if start == end:
        return 1
    if start[0] == end[0]:
        return FindNumberOfPaths((start[0],start[1]+1),end)
    if start[1] == end[1]:
        return FindNumberOfPaths((start[0]+1,start[1]),end)
    else:
        return FindNumberOfPaths((start[0],start[1]+1),end) + FindNumberOfPaths((start[0]+1,start[1]),end)

