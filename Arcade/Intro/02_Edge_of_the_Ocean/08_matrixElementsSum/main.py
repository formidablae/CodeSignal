def matrixElementsSum(matrix):
    totalSum = 0;
    dontConsid = [];
 
    for col in range(0, len(matrix[0])):
        for row in range(0, len(matrix)):
            if matrix[row][col] == 0:
                break;
            else:
                totalSum += matrix[row][col];
    return totalSum;
