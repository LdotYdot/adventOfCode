from common import read_file
input = read_file("day3/day3input.txt")
splittedList = input.split("\n")

# part 1

abcList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
abcDict = {}



def abcDictFiller():
    i = 0
    for letters in abcList:
        i = i + 1
        abcDict[letters] = i
# end
    
def duplicateSifter(array):
    newArray = []
    for numbers in array:
        if numbers not in newArray:
            newArray.append(numbers)     
    return newArray
        
        
def sumOfArray(array):
    sum = 0
    for numbers in array:
        sum = sum + numbers    
    return sum 
        
def part1MainBody():
    abcDictFiller()
    temp = 0
    for rucksacks in splittedList:
        currentWordSplitted = [abcDict[c] for c in rucksacks]
        L = currentWordSplitted[:int(len(currentWordSplitted)/2)]
        R = currentWordSplitted[int(len(currentWordSplitted)/2):]
        L = duplicateSifter(L)
        R = duplicateSifter(R)
        extended = L
        extended.extend(R)
        comparedWord = duplicateSifter(extended)
        print(extended)
        print(comparedWord)
        result = sumOfArray(extended) - sumOfArray(comparedWord)
        temp += result
    return print(temp)



#part 2





def part2MainBody():
    abcDictFiller()
    temp = 0
    for i in range(0,len(splittedList),3):
        duplicateList = []
        rucksack1 = [abcDict[c] for c in splittedList[i]]
        rucksack2 = [abcDict[c] for c in splittedList[i + 1]]
        rucksack3 = [abcDict[c] for c in splittedList[i + 2]]
        for item in rucksack1:
            if item in rucksack2:
                duplicateList.append(item)
        for item in duplicateList:
            if item in rucksack3:
                temp += item
                break
                
    return print(temp)

part2MainBody()






