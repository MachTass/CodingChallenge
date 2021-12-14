import numpy as np
from timeit import default_timer


dots = []
folds = []

start_time = default_timer()

with open("dots-folds.txt") as file:
    for line in file:
        if line == "\n":
            continue
        elif (line.startswith("fold")):
            split_fold = line.split()
            fold_instructions = split_fold[2].split("=")
            print(fold_instructions)

            fold_line = int(fold_instructions[1])

            if (fold_instructions[0] == 'x'):
                for dot in dots:
                    if dot[0] > fold_line:
                        dot[0] -= (dot[0] - fold_line) *2
            elif (fold_instructions[0] == 'y'):
                for dot in dots:
                    if dot[1] > fold_line:
                        dot[1] -= (dot[1] - fold_line) *2
        else:
            dot = list(map(int, line.rstrip().split(",")))
            dots.append(dot)

maxx = 0
maxy = 0
for dot in dots:
    maxx = max(maxx, dot[0])
    maxy = max(maxy, dot[1])

dot_matrix = np.zeros((maxy+1, maxx+1))

for dot in dots:
    x = dot[0]
    y = dot[1]
    dot_matrix[y][x] = 1

final_matrix = np.where(dot_matrix == 1, '#', dot_matrix)
true_final_matrix = np.where(dot_matrix == 0, '.', final_matrix)
print(true_final_matrix)

duration = default_timer() - start_time

print(duration)