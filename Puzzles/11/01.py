from dataclasses import dataclass, field
from typing import List

octopi = []
flashes_count = 0

@dataclass
class octopus:
    value: int
    hasflashed: bool = False
    surroundingOctopi: list = field(default_factory=list)

    def __str__(self):
        return str(self.value)

    def __repr(selfself):
        return str(self.value)

    def increaseValue(self):
        self.value += 1
        if self.value > 9:
            self.flash()


    def flash(self):
        if self.hasflashed:
            return

        self.hasflashed = True
        for octopus in self.surroundingOctopi:
            octopus.increaseValue()

    def reset(self):
        if self.hasflashed:
            self.hasflashed = False
            self.value = 0
            return True

with open("octopi.txt") as file:
    for line in file:
        octopus_line = []
        for value in list(map(int, list(line.rstrip()))):
            octopus_line.append(octopus(value))
        octopi.append(octopus_line)

for x in range(len(octopi)):
    for y in range(len(octopi[0])):
        minx = max(x-1, 0)
        miny = max(y-1, 0)
        maxx = min(x+1, len(octopi)-1)
        maxy = min(y+1, len(octopi[0])-1)
        for i in range(minx, maxx + 1):
            for j in range(miny, maxy + 1):
                if i != x or j != y:
                    octopi[x][y].surroundingOctopi.append(octopi[i][j])

for i in range(100):
    for octoline in octopi:
        for octopus in octoline:
            octopus.increaseValue()

    for octoline in octopi:
        for octopus in octoline:
            if (octopus.reset()):
                flashes_count += 1
    print(flashes_count)

print(flashes_count)