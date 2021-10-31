def shapeArea(n):
    result = 1
    for i in range (1, n + 1):
        result = result + 4 * i - 4
    return result
