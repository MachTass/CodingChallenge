import numpy as np

class tubepoint:

    def __init__(self, value):
        self.value = int(value)
        self.marked = False
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None

    def check_lowest(self):
        return all(self.value < e.value for e in list(filter(None, [self.top, self.bottom, self.left, self.right])))

    def recursive_basin_check(self):
        if self.marked:
            return 0
        self.marked = True
        points_to_check = list(filter(lambda point: point != None
                                                    and not point.marked
                                                    and point.value > self.value
                                                    and point.value != 9,
                                      [self.top, self.bottom, self.left, self.right]))
        size = 0
        for point in points_to_check:
            size += point.recursive_basin_check()
        return size + 1

tube_levels = []
risk = 0
low_points = []

with open ("tube-levels.txt") as f:
    for line in f:
        tube_levels.append(list(map(tubepoint, list(line.strip()))))

width = len(tube_levels[0])
height = len(tube_levels)
for i in range (height):
    for j in range (width):
        if j > 0:
            tube_levels[i][j].left = tube_levels[i][j-1]
        if j < width - 1:
            tube_levels[i][j].right  = tube_levels[i][j+1]
        if i > 0 :
            tube_levels[i][j].top = tube_levels[i-1][j]
        if i < height - 1 :
            tube_levels[i][j].bottom = tube_levels[i+1][j]

        if tube_levels[i][j].check_lowest():
            low_points.append([i,j])

largest_basins = [0] * 3

for point in low_points:
    size = tube_levels[point[0]][point[1]].recursive_basin_check()
    smallest_basin = np.min(largest_basins)
    if size > smallest_basin:
        largest_basins.remove(smallest_basin)
        largest_basins.append(size)

print(np.prod(largest_basins))