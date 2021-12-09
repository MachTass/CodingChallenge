elements = list()

with open('diagnostic_input.txt') as f:
    for line in f:
        elements.append(line.rstrip("\n"))\

mostCommonBits = list(elements)
comparison = ""
while len(mostCommonBits) > 1:
    #find the first most common element
    value = 0
    for e in mostCommonBits:
        temp = comparison + "1"
        if e.startswith(comparison + "1"):
            value += 1
        else :
            value -= 1

    #1 is most common
    if value >= 0:
        comparison += "1"
    else:
        comparison += "0"

    # remove all that aren't starting with comparison
    mostCommonBits[:] = [e for e in mostCommonBits if e.startswith(comparison)]

leastCommonBits = list(elements)
comparison = ""
while len(leastCommonBits) > 1:
    #find the first most common element
    value = 0
    for e in leastCommonBits:
        if e.startswith(comparison + "1"):
            value += 1
        else :
            value -= 1

    #1 is most common
    if value >= 0:
        comparison += "0"
    else:
        comparison += "1"

    # remove all that aren't starting with comparison
    leastCommonBits[:] = [e for e in leastCommonBits if e.startswith(comparison)]

print (f"final oxygen is equal to : {mostCommonBits}")
print (f"final co2 is equal to : {leastCommonBits}")
print (f"final result is {int(mostCommonBits[0], 2) * int(leastCommonBits[0], 2)}")