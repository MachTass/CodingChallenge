result = 0

def bracketToInt(character):
    if character in ['(',')']:
        return 3
    elif character in ['[',']']:
        return 57
    elif character in ['{','}']:
        return 1197
    elif character in ['<','>']:
        return 25137

with open("corrupted-lines.txt") as file:
    for line in file:
        stack = []
        brackets = list(line.rstrip())
        for c in brackets:
            if c in ['[','{','(','<']:
                stack.append(bracketToInt(c))
            else:
                removedBracket = stack.pop()
                comparisonBracket = bracketToInt(c)
                if removedBracket != comparisonBracket:
                    result += comparisonBracket
                    break

print(result)
