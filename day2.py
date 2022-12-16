from common import read_file
input = read_file("day2/day2input.txt")
splittedList = input.split("\n")
rpsMap = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
rpsMapPart2 = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}


def part1():
    temp = 0
    for case in splittedList:
        temp += rpsMap[case]
    return temp

def part2():
    temp = 0
    for case in splittedList:
        temp += rpsMapPart2[case]
    return temp

print(part2())
