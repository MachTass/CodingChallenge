hPosition = 0
depth = 0
aim = 0

with open('movement-commands.txt') as f:
    for line in f:
        #split line into command and amount
        splitline = line.split()
        print(splitline)
        #case statement on command
        if splitline[0] == "forward":
            hPosition += int(splitline[1])
            depth += aim * int(splitline[1])
        if splitline[0] == "up":
            aim -= int(splitline[1])
        if splitline[0] == "down":
            aim += int(splitline[1])
        #print the current position
        print(f"horizontal position: {hPosition}, aim: {aim}, depth: {depth}")
#print final result
print(f"The final result is {hPosition * depth}")