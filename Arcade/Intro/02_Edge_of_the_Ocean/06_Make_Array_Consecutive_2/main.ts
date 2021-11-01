function makeArrayConsecutive2(statues: number[]): number {
    return Math.max(...statues) - Math.min(...statues) - statues.length + 1;
}
