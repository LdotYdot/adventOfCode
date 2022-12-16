from common import read_file

input =  read_file("day1/input.txt")
splittedList = input.split("\n")

def part1():
    temp = 0
    output = []
    for line in splittedList:
        try:
           temp += int(line)
        except:
            output.append(temp)
            temp = 0
    output.sort()
    biggestEaterElfsCalories = output[len(output)-1]
    return biggestEaterElfsCalories

def part2():
    temp = 0
    output = []
    for line in splittedList:
        try:
           temp += int(line)
        except:
            output.append(temp)
            temp = 0
    output.sort()
    biggest3EaterElfsCalories = output[len(output)-1] + output[len(output)-2] + output[len(output)-3]
    return biggest3EaterElfsCalories

print(part2())


