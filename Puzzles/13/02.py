import numpy as np
from timeit import default_timer

dots = []
folds = []

maxx = 0
maxy = 0

start_time = default_timer()

with open("dots-folds.txt") as file:
    for line in file:
        if line == "\n":
            continue
        elif (line.startswith("fold")):
            folds.append(line)
        else:
            dot = list(map(int, line.rstrip().split(",")))
            maxx = max(dot[0], maxx)
            maxy = max(dot[1], maxy)
            dots.append(dot)

dot_matrix = np.zeros((maxy + 1, maxx + 1))

for dot in dots:
    x = dot[0]
    y = dot[1]
    dot_matrix[y][x] = 1

print(dot_matrix)

# Do the folding
for fold in folds:
    split_fold = fold.split()
    fold_instructions = split_fold[2].split("=")
    print(fold_instructions)

    if (fold_instructions[0] == 'x'):
        fold_line = int(fold_instructions[1])
        iteration = 1
        highest_value = len(dot_matrix[0])
        while (fold_line + iteration < highest_value and fold_line - iteration >= 0):
            for j in range(len(dot_matrix)):
                dot_matrix[j][fold_line - iteration] = max(dot_matrix[j][fold_line - iteration],
                                                           dot_matrix[j][fold_line + iteration])
            iteration += 1
        dot_matrix = dot_matrix[:, :fold_line]
    elif (fold_instructions[0] == 'y'):
        fold_line = int(fold_instructions[1])
        iteration = 1
        highest_value = len(dot_matrix)
        while (fold_line + iteration < highest_value and fold_line - iteration >= 0):
            for j in range(len(dot_matrix[0])):
                dot_matrix[fold_line - iteration][j] = max(dot_matrix[fold_line - iteration][j],
                                                           dot_matrix[fold_line + iteration][j])
            iteration += 1
        dot_matrix = dot_matrix[:fold_line, :]

final_matrix = np.where(dot_matrix == 1, '#', dot_matrix)
true_final_matrix = np.where(dot_matrix == 0, '.', final_matrix)
print(true_final_matrix)

duration = default_timer() - start_time

print(duration)
