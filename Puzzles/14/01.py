import collections

polymer = None
polymer_mappings = {}

with open("polymer.txt") as file:
    polymer = list(file.readline().rstrip())
    file.readline()

    for line in file:
        pair_insertion = line.split(" -> ")
        polymer_mappings[pair_insertion[0]] = pair_insertion[1].rstrip()

for _ in range(10):
    for i in range(len(polymer)-1,0,-1):
        pair = polymer[i-1] + polymer[i]
        if pair in polymer_mappings.keys():
            polymer.insert(i, polymer_mappings[pair])

most_common_list = collections.Counter(polymer).most_common()
print(most_common_list[0][1]-most_common_list[-1][1])