def solution(a, b):
    uniqueSums = {(i + j): i * j for i in a for j in b if (i * j) % (i + j) == 0}
    return len(uniqueSums)
