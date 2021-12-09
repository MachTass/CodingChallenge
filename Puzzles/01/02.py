previousValue = 142
prepreviousValue = 138
preprepreviousValue = 134
increment = 0

with open('seabed-values.txt') as f:
    for line in f:
        if (int(line) + previousValue + prepreviousValue) > (previousValue + prepreviousValue + preprepreviousValue):
            increment += 1
        preprepreviousValue = prepreviousValue
        prepreviousValue = previousValue
        previousValue = int(line)
print(f"The final increment decrease is {increment}")