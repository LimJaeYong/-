def multiple(myList):
    newList = []

    for i in range(len(myList)):
        mul = 1
        for j in range(len(myList)):
            if i == j:
                continue
            else:
                mul *= myList[j]
        newList.append(mul)

    return newList


def plus(myList):
    newList = []
    sum = 0
    
    for i in range(len(myList)):
        for j in range(len(myList)):
            if i == j:
                continue
            else:
                sum += myList[j]
        newList.append(sum)
        
    return newList

inputList =[]

while len(inputList) < 4:
    inputList.append(int(input("숫자 입력 >> ")))
    
print(multiple(inputList))
print(plus(inputList))
    
        
