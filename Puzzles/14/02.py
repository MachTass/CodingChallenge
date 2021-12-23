import collections

first_digit = None
last_digit = None
polymer_pairs = {}
polymer_mappings = {}

with open("polymer.txt") as file:
    polymer = list(file.readline().rstrip())
    first_digit = polymer[0]
    last_digit = polymer[len(polymer) - 1]
    file.readline()

    for line in file:
        pair_insertion = line.split(" -> ")
        polymer_mappings[pair_insertion[0]] = pair_insertion[1].rstrip()

for i in range(len(polymer)-1):
    polymer_pair = str(polymer[i] + polymer[i+1])
    if not polymer_pair in polymer_pairs:
        polymer_pairs[polymer_pair] = 1
    else:
        polymer_pairs[polymer_pair] += 1

for _ in range(40):
    new_polymer_pairs = {}
    for pair in polymer_pairs:
        if pair in polymer_mappings:
            pair_list = list(pair)
            amount = polymer_pairs[pair]
            first_pair = str(pair[0] + polymer_mappings[pair])
            second_pair = str(polymer_mappings[pair] + pair[1])
            if not first_pair in new_polymer_pairs:
                new_polymer_pairs[first_pair] = amount
            else:
                new_polymer_pairs[first_pair] += amount

            if not second_pair in new_polymer_pairs:
                new_polymer_pairs[second_pair] = amount
            else:
                new_polymer_pairs[second_pair] += amount
    polymer_pairs = new_polymer_pairs.copy()

print(polymer_pairs)

element_count = {}
for pair in polymer_pairs:
    for element in list(pair):
        if not element in element_count:
            element_count[element] = polymer_pairs[pair]
        else:
            element_count[element] += polymer_pairs[pair]

element_count[first_digit] += 1
element_count[last_digit] += 1

print((max(element_count.values()) - min(element_count.values()))/2)