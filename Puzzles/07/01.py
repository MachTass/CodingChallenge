import numpy as np
from timeit import default_timer

with open("crabs.txt") as f:
    crabs = list(map(int, f.readline().split(",")))

minfuelcost = np.inf
minposition = None

start_time = default_timer()

for i in range(max(crabs)):
    fuelcost = 0
    for crab in crabs:
        movement = abs(crab - i)
        fuelcost += movement
        if fuelcost > minfuelcost:
            break;
    if fuelcost > minfuelcost:
        continue;
    minfuelcost = fuelcost
    minposition = i


end_time = default_timer()

print(minfuelcost)
print(minposition)
print(f"duration = {end_time - start_time}")
