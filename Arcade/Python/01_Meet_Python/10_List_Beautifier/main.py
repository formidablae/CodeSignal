def solution(a):
    res = a[:]
    while res and res[0] != res[-1]:
        first, *res, last = res
    return res
