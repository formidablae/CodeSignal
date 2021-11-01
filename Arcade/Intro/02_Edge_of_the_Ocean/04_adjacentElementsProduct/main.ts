function adjacentElementsProduct(inputArray: number[]): number {
    let result: number = -1000;
    for (let i: number = 0; i < inputArray.length - 1; i++) {
        if (inputArray[i] * inputArray[i + 1] > result) {
            result = inputArray[i] * inputArray[i + 1];
        }
    }
    return result;
}
