def solution(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        found = upperBound

    return found
