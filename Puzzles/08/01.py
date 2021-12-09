import numpy as np

digitAmounts = 0

with open("numbers.txt") as file:
    for line in file:
        input = line.split("|")
        signal_patterns = input[0].strip().split(" ")
        output_values = input[1].strip().split(" ")
        for v in output_values:
            if len(v) in [2,3,4,7]:
                digitAmounts += 1

print (digitAmounts)