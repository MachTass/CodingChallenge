from dataclasses import dataclass, field

start = None
caves = []
probes = []

number_of_paths = 0

@dataclass
class cave:
    name: str
    isSmall: bool = False
    connectedCaves: list = field(default_factory=list)

    def __post_init__(self):
        if self.name.islower():
            self.isSmall = True

@dataclass
class probe:
    currentCave: cave
    visitedCaves: list = field(default_factory=list)
    traversed_path: list = field(default_factory=list)
    has_revisited_small_cave: bool = False

    def probeCaves(self):
        self.traversed_path.append(self.currentCave.name)
        if (self.currentCave.name == "end"):
            print(self.traversed_path)
            return True
        if self.currentCave.isSmall:
            self.visitedCaves.append(self.currentCave.name)
        for cave in self.currentCave.connectedCaves:
            if (cave.name == 'start'):
                continue;
            if (cave.name not in self.visitedCaves):
                newprobe = probe(cave, self.visitedCaves[:], self.traversed_path[:], self.has_revisited_small_cave)
                probes.append(newprobe)
            elif (not self.has_revisited_small_cave and cave.name in self.visitedCaves):
                newprobe = probe(cave, self.visitedCaves[:], self.traversed_path[:], True)
                probes.append(newprobe)


with open("cave-paths.txt") as file:
    for line in file:
        path = line.rstrip().split("-")
        for caveName in path:
            if not any(cave.name == caveName for cave in caves[:]):
                newCave = cave(caveName)
                caves.append(newCave)
                if (caveName == "start"):
                    start = newCave

        caves_on_path = [cave for cave in caves if cave.name in path[:]]
        caves_on_path[0].connectedCaves.append(caves_on_path[1])
        caves_on_path[1].connectedCaves.append(caves_on_path[0])

probes.append(probe(start))

while len(probes) > 0 :
    currentProbe = probes.pop()
    if (currentProbe.probeCaves()):
        number_of_paths += 1

print (number_of_paths)