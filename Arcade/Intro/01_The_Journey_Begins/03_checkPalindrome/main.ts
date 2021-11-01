function checkPalindrome(inputString: string): boolean {
    let l: number = inputString.length;
    if (l < 2) return true;
    for (let i: number = 0; i <= (l / 2); i++) {
        if (!(inputString.substring(i, i + 1) === inputString.substring(l - 1 - i, l - i)))return false;
    }
    return true;
}
