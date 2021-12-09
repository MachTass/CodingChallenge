import numpy as np

lanternfish = np.zeros(9)

with open('lanternfish.txt') as f:
    currentfish = f.readline().rstrip().split(",")
    for fish in currentfish:
        lanternfish[int(fish)] += 1

print (lanternfish)
for i in range(80):
    #logic goes in here
    #store the 0 value
    givingbirth = lanternfish[0]
    #move all other values over one
    for i in range (1, len(lanternfish)):
        lanternfish[i-1] = lanternfish[i]
    #add the 0 value to 6 and 8
    lanternfish[6] += givingbirth
    lanternfish[8] = givingbirth
    print (lanternfish)

print(sum(lanternfish))