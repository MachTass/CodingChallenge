targetxmax = 0
targetxmin = 0
targetymax = 0
targetymin = 0

def calculate_y_validity(value):
    valid_steps = []
    steps = 0
    position = 0
    while(position > targetymax):
        position += value
        value -= 1
        steps += 1
    while(position >= targetymin):
        valid_steps.append(steps)
        position += value
        value -= 1
        steps += 1
    return valid_steps

def calculate_x_validity(value, max_steps):
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
            for i in range(steps, max_steps+1):
                valid_steps.append(i)
            break
    return valid_steps

with open("target-area.txt") as file:
    for line in file:
        dimensions = line.rstrip().split(" ")
        targetxmin = int(dimensions[0])
        targetxmax = int(dimensions[1])
        targetymin = int(dimensions[2])
        targetymax = int(dimensions[3])

valid_y_steps_dict = {}
for y in range(abs(targetymin), targetymin-1, -1):
    steps = calculate_y_validity(y)
    if steps:
        for step in steps:
            valid_y_steps_dict.setdefault(step, set()).add(y)

valid_x_steps_dict = {}
max_steps = max(valid_y_steps_dict.keys())
for x in range(targetxmax+1):
    steps = calculate_x_validity(x, max_steps)
    if steps:
        for step in steps:
            valid_x_steps_dict.setdefault(step, set()).add(x)

valid_pairs = set()
for x in valid_x_steps_dict.keys():
    if x in valid_y_steps_dict.keys():
        for x_item in valid_x_steps_dict[x]:
            for y_item in valid_y_steps_dict[x]:
                valid_pairs.add(f"{x_item},{y_item}")
print(len(valid_pairs))