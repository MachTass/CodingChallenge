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
        #don't worry about diagonal lines


        print(grid)
#find the amount of times values are greater than 1
print((grid > 1).sum())