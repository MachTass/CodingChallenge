import numpy as np

tube_levels = []
risk = 0

with open ("tube-levels.txt") as f:
    for line in f:
        tube_levels.append(list(map(int, list(line.strip()))))

width = len(tube_levels[0])
height = len(tube_levels)
for i in range (height):
    for j in range (width):
        left = tube_levels[i][j-1] if j > 0 else np.inf
        right  = tube_levels[i][j+1] if j < width - 1 else np.inf
        if tube_levels[i][j] < left and tube_levels[i][j] < right:
            top = tube_levels[i-1][j] if i > 0 else np.inf
            bottom = tube_levels[i+1][j] if i < height - 1 else np.inf
            if tube_levels[i][j] < top and tube_levels[i][j] < bottom:
                risk += tube_levels[i][j] + 1

print (risk)