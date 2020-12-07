def validLine(line):
    countRange, letter, password = line.split(" ")
    min, max = countRange.split("-")
    min = int(min)
    max = int(max)
    letter = letter[0]
    letterCount = len(list(filter(lambda x: x == letter, password)))
    return letterCount >= min and letterCount <= max

with open("input.txt") as input:
    lines = input.read().splitlines()
    print(sum(1 if validLine(line) else 0 for line in lines))
    
