int circleOfNumbers(int n, int firstNumber)
{
    if (n % 2 != 0) return ((n - 1) / 2 + firstNumber) % n;
    else return (n / 2 + firstNumber) % n;
}
