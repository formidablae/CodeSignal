def solution(t, width, precision):
    return ('{:^{w}.{p}f}').format(t, w=width, p=precision)
