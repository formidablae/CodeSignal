function almostIncreasingSequence(sequence: number[]): boolean {
    let sequence1: number[] = sequence.slice();
    let sequence2: number[] = sequence.slice();
    for (let i: number = 1; i < sequence.length; i++) {
        if (sequence[i-1] >= sequence[i]) {
            sequence1.splice(i-1, 1);
            sequence2.splice(i, 1);
            break;
        }
    }
    if (sequence.length === sequence2.length) return true;
    let seq1: boolean = false;
    let seq2: boolean = false;
    for (let i: number = 1; i < sequence1.length; i++) {
        if (sequence1[i-1] >= sequence1[i]) seq1 = true;
        if (sequence2[i-1] >= sequence2[i]) seq2 = true;
        if (seq1 && seq2) return false;
    }
    return true;
}
