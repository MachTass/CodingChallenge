result = 0
digitValues = None
fiveSegments = []
sixSegments = []

with open("numbers.txt") as file:
    for line in file:
        digitValues = ["" for i in range(10)]
        input = line.split("|")
        signal_patterns = input[0].strip().split(" ")
        for unsorted_pattern in signal_patterns:
            sp = "".join(sorted(unsorted_pattern))
            length = len(sp)
            if length == 2:
                digitValues[1] = sp
            elif length == 3:
                digitValues[7] = sp
            elif length == 4:
                digitValues[4] = sp
            elif length == 7:
                digitValues[8] = sp
            elif length == 5:
                fiveSegments.append(sp)
            elif length == 6:
                sixSegments.append(sp)

        #loop through 6 segment list
        for s in sixSegments:
            #check if string contains all of 4
            if (all(e in list(s) for e in list(digitValues[4]))):
                digitValues[9] = s
            #check if string contains all of 1
            elif (sum(e in list(digitValues[1]) for e in list(s)) == 1):
                digitValues[6] = s
            #if neither, must be 0
            else :
                digitValues[0] = s

        #loop through 5 segment list
        for s in fiveSegments:
            if (all(e in list(s) for e in list(digitValues[1]))):
                digitValues[3] = s
            elif (sum(e in list(digitValues[9]) for e in list(s)) == 5):
                digitValues[5] = s
            else :
                digitValues[2] = s

        output_values = input[1].strip().split(" ")
        output_value = ""
        for v in output_values:
            output_value += str(digitValues.index("".join(sorted(v))))

        print(output_value)
        result += int(output_value)
print(f"final amount: {result}")