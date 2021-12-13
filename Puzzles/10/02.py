import numpy as np

line_result = []
corrupted_lines = []

def bracketToInt(character):
    if character in ['(', ')']:
        return 3
    elif character in ['[', ']']:
        return 57
    elif character in ['{', '}']:
        return 1197
    elif character in ['<', '>']:
        return 25137

def closingBracketValue(character):
    if character in ['(', ')']:
        return 1
    elif character in ['[', ']']:
        return 2
    elif character in ['{', '}']:
        return 3
    elif character in ['<', '>']:
        return 4


with open("corrupted-lines.txt") as file:
    for line in file:
        corrupted_lines.append(list(line.rstrip()))

for line in corrupted_lines[:]:
    stack = []
    for c in line:
        if c in ['[', '{', '(', '<']:
            stack.append(bracketToInt(c))
        else:
            removedBracket = stack.pop()
            comparisonBracket = bracketToInt(c)
            if removedBracket != comparisonBracket:
                corrupted_lines.remove(line)
                break

for line in corrupted_lines[:]:
    result = 0
    stack = []
    for c in line:
        if c in ['[', '{', '(', '<']:
            stack.append(c)
        else:
            stack.pop()
    for i in range(len(stack)):
        result *= 5
        result += closingBracketValue(stack.pop())
    line_result.append(result)

median = np.median(line_result)

print(median)