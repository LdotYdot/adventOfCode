from common import read_file
crateInput = read_file("day5/day5inputcrate.txt")
moveInstructionInput = read_file("day5/day5inputmoveinstructions.txt")

crateList = crateInput.split("\n")
incompleteMoveInstructionList = moveInstructionInput.split("\n")
moveInstructionList = []

def fillInstructions():
    for instruction in incompleteMoveInstructionList:
        splittedInstruction = instruction.split(" ")

        
        moveInstructionList.append(splittedInstruction[0])
        moveInstructionList.append(splittedInstruction[1])
        moveInstructionList.append(splittedInstruction[2])
        

def takeLettersPart1(amount, string):
    i = 0 
    returnString = ""
    for letter in string:
        if amount == i:
            return returnString
        returnString = letter+returnString
        i += 1
    return returnString
     
fillInstructions()

def part1MainBody():
    for i in range(0, len(moveInstructionList), 3):
        moveQuantity = int(moveInstructionList[i])
        moveFromLocation = crateList[int(moveInstructionList[i+1])-1]
        moveToLocation = crateList[int(moveInstructionList[i+2])-1]
        x = str(takeLettersPart1(moveQuantity, moveFromLocation))+moveToLocation
        y = moveFromLocation[moveQuantity:]
        
        crateList[int(moveInstructionList[i+2])-1] = x
        crateList[int(moveInstructionList[i+1])-1] = y
        
    print(crateList)
    
# part2

def takeLettersPart2(amount, string):
    i = 0 
    returnString = ""
    for letter in string:
        if amount == i:
            return returnString
        returnString = returnString+letter
        i += 1
    return returnString

def part2MainBody():
    for i in range(0, len(moveInstructionList), 3):
        moveQuantity = int(moveInstructionList[i])
        moveFromLocation = crateList[int(moveInstructionList[i+1])-1]
        moveToLocation = crateList[int(moveInstructionList[i+2])-1]
        x = str(takeLettersPart2(moveQuantity, moveFromLocation))+moveToLocation
        y = moveFromLocation[moveQuantity:]
        
        crateList[int(moveInstructionList[i+2])-1] = x
        crateList[int(moveInstructionList[i+1])-1] = y
        
    print(crateList)
    
part2MainBody()


