def areSimilar(a, b):
    i = 0
    newArray = []

    while i < len(a):
        if a[i] != b[i]:
            newArray.append(i)
        i += 1

    if not newArray:
        return True

    if len(newArray) != 2:
        return False

    return a[newArray[0]] == b[newArray[1]] and a[newArray[1]] == b[newArray[0]]
