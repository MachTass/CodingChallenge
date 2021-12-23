import math
from dataclasses import dataclass, field
from timeit import default_timer
from queue import PriorityQueue

from copy import deepcopy
import numpy as np

grid = []
routes = PriorityQueue()
marked_nodes = set()
maxx = 0
maxy = 0

@dataclass
class route:
    x_position: int = 0;
    y_position: int = 0;
    prev_risk: int = 0;
    path: set = field(default_factory=set);
    route_risk: int = 0;
    size: int = 0;

    def __post_init__(self):
        self.route_risk = self.prev_risk + large_grid[self.y_position][self.x_position]
        self.size = self.route_risk

    def __lt__(self, other):
        return self.size < other.size

def insert_sorted(route):
    routes.put(route)

with open("risk.txt") as file:
    for line in file:
        grid.append(list(map(int, list(line.rstrip()))))

#recalculate the grid
grids = []
grids.append(grid)
for i in range(1, 9):
    grid_copy = [row[:] for row in grids[i-1]]
    for i in range(len(grid_copy)):
        for j in range(len(grid_copy[0])):
            if(grid_copy[i][j] == 9):
                grid_copy[i][j] = 1
            else:
                grid_copy[i][j] += 1
    grids.append(grid_copy)

large_grid = None
for i in range(5):
    temp_grid = [row[:] for row in grids[i]]
    for j in range(1,5):
        temp_grid = np.append(temp_grid, grids[i+j], axis=1)

    if large_grid is not None:
        large_grid = np.append(large_grid, temp_grid, axis=0)
    else:
        large_grid = temp_grid

maxx = len(large_grid[0]) - 1
maxy = len(large_grid) - 1
start = route()
routes.put(start)
marked_nodes.add(tuple([0, 0]))

while(True):
    current_route = routes.get()
    current_risk = current_route.route_risk
    if (current_route.y_position == maxy and current_route.x_position == maxx):
        print(current_risk - large_grid[0][0])
        break

    up_position = tuple([current_route.x_position, current_route.y_position - 1])
    down_position = tuple([current_route.x_position, current_route.y_position + 1])
    left_position = tuple([current_route.x_position - 1, current_route.y_position])
    right_position = tuple([current_route.x_position + 1, current_route.y_position])

    if current_route.x_position < maxx and right_position not in marked_nodes:
        insert_sorted(route(current_route.x_position + 1, current_route.y_position, current_risk))
        marked_nodes.add(right_position)
    if current_route.x_position > 0 and left_position not in marked_nodes:
        insert_sorted(route(current_route.x_position - 1, current_route.y_position, current_risk))
        marked_nodes.add(left_position)
    if current_route.y_position < maxy and down_position not in marked_nodes:
        insert_sorted(route(current_route.x_position, current_route.y_position + 1, current_risk))
        marked_nodes.add(down_position)
    if current_route.y_position > 0 and up_position not in marked_nodes:
        insert_sorted(route(current_route.x_position, current_route.y_position - 1, current_risk))
        marked_nodes.add(up_position)
