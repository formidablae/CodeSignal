function matrixElementsSum(matrix: number[][]): number {
    let total: number = 0;
    for (let i: number = 0; i < matrix[0].length; i++) {
        for (let j: number = 0; j < matrix.length; j++) {
            if (matrix[j][i] === 0) {
                j = matrix.length;
            } else {
                total += matrix[j][i];
            }
        }
    }
    return total;
}
