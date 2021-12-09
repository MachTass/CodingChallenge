import numpy as np

grid = np.zeros((1000, 1000))

with open ("ventlines.txt") as f:
    for line in f:
        #iteratively adjust the grid
        temp = line.rstrip().split("->")
        start = list(map(int, temp[0].split(",")))
        end = list(map(int, temp[1].split(",")))
        if int(start[0]) == int(end[0]):
            #loop over [1]
            for i in range(np.min([start[1], end[1]]),np.max([start[1],end[1]]) +1):
                grid[i,start[0]] +=1
        elif int(start[1]) == int(end[1]):
            #loop over [0]
            for i in range(np.min([start[0], end[0]]),np.max([start[0],end[0]]) +1):
                grid[start[1],i] += 1
        #worry about diagonal lines
        #exactly 45 degrees means that y2-y1 == x2-x1
        else:
            minx = np.min([start[0], end[0]])
            maxx = np.max([start[0], end[0]])
            miny = np.min([start[1], end[1]])
            maxy = np.max([start[1], end[1]])
            size = maxx - minx
            #check if diagonal going top left to bottom right
            if((minx == start[0] and miny == start[1]) or (minx == end[0] and miny == end[1])):
                for i in range(size+1):
                    grid[miny+i][minx+i] += 1
            #must be a diagonal going top right to bottom left
            #must add to one and subtract from the other
            elif(minx == start[0]):
                for i in range(size+1):
                    grid[maxy-i][minx+i] += 1
            else:
                for i in range(size+1):
                    grid[miny+i][maxx-i] += 1

#find the amount of times values are greater than 1
print((grid > 1).sum())