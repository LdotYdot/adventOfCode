from common import read_file
input = read_file("day4/day4input.txt")

splittedList = input.split("\n")


def part1MainBody():
    temp = 0
    for line in splittedList:
        splitLine = line.split(",")
        range1start = int(splitLine[0].split("-")[0])
        range1end = int(splitLine[0].split("-")[1])
        range2start = int(splitLine[1].split("-")[0])
        range2end = int(splitLine[1].split("-")[1])
        
        if range1start >= range2start and range2end >= range1end or range2start >= range1start and range1end >= range2end:
            temp += 1
        
    return print(temp)
part1MainBody()


    