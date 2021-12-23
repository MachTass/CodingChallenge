import threading
from dataclasses import dataclass, field
from timeit import default_timer
from queue import PriorityQueue
import sys

from concurrent.futures import ThreadPoolExecutor, Future

NUM_WORKER_THREADS = 7

grid = []
routes = PriorityQueue()
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
        self.route_risk = self.prev_risk + grid[self.y_position][self.x_position]
        self.size = self.route_risk + 2 * ((maxy - self.y_position) + (maxx - self.x_position))

    def __lt__(self, other):
        return self.size < other.size

def insert_sorted(route):
    routes.put(route)

with open("risk-test.txt") as file:
    for line in file:
        grid.append(list(map(int, list(line.rstrip()))))

maxx = len(grid[0]) - 1
maxy = len(grid) - 1
start = route()
routes.put(start)

start_time = default_timer()

def route_calculation():
    while(True):
        if not routes.empty():
            current_route = routes.get()
            current_risk = current_route.route_risk
            if (current_route.y_position == maxy and current_route.x_position == maxx):
                print(f"Final risk = {current_risk - grid[0][0]}")
                sys.exit()

            path_history = current_route.path.copy()
            path_history.add(tuple([current_route.x_position, current_route.y_position]))
            if current_route.x_position < maxx and (
                    tuple([current_route.x_position + 1, current_route.y_position]) not in current_route.path):
                insert_sorted(route(current_route.x_position + 1, current_route.y_position, current_risk, path_history))
            if current_route.x_position > 0 and (
                    tuple([current_route.x_position - 1, current_route.y_position]) not in current_route.path):
                insert_sorted(route(current_route.x_position - 1, current_route.y_position, current_risk, path_history))
            if current_route.y_position < maxy and (
                    tuple([current_route.x_position, current_route.y_position + 1]) not in current_route.path):
                insert_sorted(route(current_route.x_position, current_route.y_position + 1, current_risk, path_history))
            if current_route.y_position > 0 and (
                    tuple([current_route.x_position, current_route.y_position - 1]) not in current_route.path):
                insert_sorted(route(current_route.x_position, current_route.y_position - 1, current_risk, path_history))

upload_workers = ThreadPoolExecutor(max_workers=NUM_WORKER_THREADS)

def initialise_calculation():
    future = upload_workers.submit(route_calculation)

for _ in range(NUM_WORKER_THREADS):
    initialise_calculation()

print(default_timer() - start_time)