import numpy as np

targetxmax = 0
targetxmin = 0
targetymax = 0
targetymin = 0

def calculate_y_validity(value):
    valid_steps = []
    steps = 0
    position = 0
    while(position >= targetymax):
        position += value
        value -= 1
        steps += 1
    while(position >= targetymin):
        valid_steps.append(steps)
        position += value
        value -= 1
        steps += 1
    return valid_steps

def calculate_x_validity(value):
    valid_steps = []
    steps = 0
    position = 0
    while(position < targetxmin and value > 0):
        position += value
        steps += 1
        value -= 1
    while position <= targetxmax and position >= targetxmin:
        valid_steps.append(steps)
        position += value
        steps += 1
        if value > 0:
            value -= 1
        elif value == 0:
            valid_steps.append(np.inf)
            break
    return valid_steps

with open("target-area.txt") as file:
    for line in file:
        dimensions = line.rstrip().split(" ")
        targetxmin = int(dimensions[0])
        targetxmax = int(dimensions[1])
        targetymin = int(dimensions[2])
        targetymax = int(dimensions[3])

valid_x_steps_dict = {}
for x in range(targetxmax):
    steps = calculate_x_validity(x)
    if steps:
        for step in steps:
            valid_x_steps_dict.setdefault(x, set()).add(step)

valid_y_steps_dict = {}
for y in range(abs(targetymin), targetymin, -1):
    steps = calculate_y_validity(y)
    if steps:
        for step in steps:
            valid_y_steps_dict.setdefault(y, set()).add(step)

for y in valid_y_steps_dict.keys():
    for x in valid_x_steps_dict.values():
        if (any(item in x for item in valid_y_steps_dict[y]) or np.inf in x):
            print(f"{(y*(y+1))/2}")
            exit()