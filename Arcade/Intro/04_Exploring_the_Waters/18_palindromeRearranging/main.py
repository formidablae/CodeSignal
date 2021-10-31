def palindromeRearranging(inputString):
    count = 0
    evenOddChars = []
    iterated = []
    for i in range (0, len(inputString)):
        if inputString[i] not in iterated:
            evenOddChars.append(inputString.count(inputString[i]))
            iterated.append(inputString[i])
                      
    for j in range (0, len(evenOddChars)):
        if evenOddChars[j] % 2 != 0:
            count += 1
    
    if count < 2:
        return True
    else:
        return False
