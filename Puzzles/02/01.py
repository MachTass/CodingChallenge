hPosition = 0
vPosition = 0

with open('movement-commands.txt') as f:
    for line in f:
        #split line into command and amount
        splitline = line.split()
        print(splitline)
        #case statement on command
        if splitline[0] == "forward":
            hPosition += int(splitline[1])
        if splitline[0] == "up":
            vPosition -= int(splitline[1])
        if splitline[0] == "down":
            vPosition += int(splitline[1])
        #print the current position
        print(f"horizontal position: {hPosition}, vertical position: {vPosition}")
#print final result
print(f"The final result is {hPosition * vPosition}")