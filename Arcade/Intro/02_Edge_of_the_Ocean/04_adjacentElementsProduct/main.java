int adjacentElementsProduct(int[] inputArray) {
    int result = -1000;
    for (int i = 0; i < inputArray.length - 1; i++) {
        if (inputArray[i] * inputArray[i + 1] > result)
            result = inputArray[i] * inputArray[i + 1];
    }
    return result;
}
