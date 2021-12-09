previousValue = 134;
increment = 0

with open('seabed-values.txt') as f:
    for line in f:
        print(line)
        if int(line) > previousValue:
            increment += 1
        previousValue = int(line)
print(f"The final increment decrease is {increment}")