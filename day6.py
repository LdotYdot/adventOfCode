from common import read_file
input = read_file("day6/day6input.txt")

abcDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

listOfLetters = []

def splitIntoList():
    for letters in input:
        listOfLetters.append(abcDict[letters])
    
splitIntoList()

def part1():
    i = 0
    for numbers in listOfLetters:
        firstLetter = listOfLetters[i]
        secondLetter = listOfLetters[i + 1]
        thirdLetter = listOfLetters[i + 2]
        fourthLetter = listOfLetters[i + 3]
        print(firstLetter)
        if firstLetter is not secondLetter and firstLetter is not thirdLetter and firstLetter is not fourthLetter:
            if secondLetter is not thirdLetter and secondLetter is not fourthLetter:
                if thirdLetter is not fourthLetter:
                    print("result")
                    print(i+4)
                    
                    return
        i = i + 1
 
def AreElementsDifferent(list):
    emptyList = []
    i = 0
    for letter in list:
        if letter not in emptyList:
            emptyList.append(letter)
        i = i + 1
    if len(emptyList) < len(list):
        return False
    return True
               
        
def part2():
    i = 0
    for numbers in listOfLetters:
        fourteenLetters = [listOfLetters[i], listOfLetters[i+1], listOfLetters[i+2], listOfLetters[i+3],listOfLetters[i+4],listOfLetters[i+5],listOfLetters[i+6],listOfLetters[i+7],listOfLetters[i+8],listOfLetters[i+9],listOfLetters[i+10],listOfLetters[i+11],listOfLetters[i+12],listOfLetters[i+13]]
        if AreElementsDifferent(fourteenLetters):
            print(i + 14)
            return
        i = i + 1

part2()

