def makeArrayConsecutive2(statues):
    statArray = statues;
    statArray.sort();
    return statArray[-1] - statArray[0] - len(statArray) + 1;
