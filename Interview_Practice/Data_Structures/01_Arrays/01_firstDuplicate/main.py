def firstDuplicate(a):
    aSet = set()
    for i in a:
        if i in aSet:
            return i
        aSet.add(i)
    return -1
