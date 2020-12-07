def validLine(line):
    countRange, letter, password = line.split(" ")
    min, max = countRange.split("-")
    min = int(min)
    max = int(max)
    letter = letter[0]
    # 1-indexed
    return (password[min - 1] == letter) ^ (password[max - 1] == letter)

with open("input.txt") as input:
    lines = input.read().splitlines()
    print(sum(1 if validLine(line) else 0 for line in lines))

