#can do a +1 -1 interation over each value
elements = [0 for i in range(12)]

with open('diagnostic_input.txt') as f:
    for line in f:
        position = 0
        for c in list(line.rstrip("\n")):
            if (c == '0'):
                elements[position] -= 1
            elif (c == '1'):
                elements[position] += 1
            else :
                print(f"Input was incorrectly parsed: {c}")
            position += 1

print (f"Gamma rate is equal to : {elements}")

gamma = ""
epsilon = ""
for e in elements:
    if (e > 0):
        gamma += "1"
        epsilon += "0"
    else :
        gamma += "0"
        epsilon += "1"

print (f"final gamma is equal to : {gamma}")
print (f"final epsilon is equal to : {epsilon}")

print (f"final result is {int(gamma, 2) * int(epsilon, 2)}")