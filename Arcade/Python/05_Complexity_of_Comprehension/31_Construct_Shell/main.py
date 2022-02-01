def solution(n):
    return [[0] * x for x in list(range(1, n + 1)) + list(range(n - 1, 0, -1))]
