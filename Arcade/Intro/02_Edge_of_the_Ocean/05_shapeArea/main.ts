function shapeArea(n: number): number {
    let result: number = 1;
    for (let i: number = 1; i < n + 1; i++) {
        result = result + 4 * i - 4;
    }
    return result;
}
