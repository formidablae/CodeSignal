boolean checkPalindrome(String inputString) {
    int l = inputString.length();
    if (l < 2)
        return true;
    for (int i = 0; i <= (l / 2); i++) {
        if (!(inputString.substring(i, i + 1).equals(inputString.substring(l - 1 - i, l - i)))) {
            return false;
        }
    }
    return true;
}
