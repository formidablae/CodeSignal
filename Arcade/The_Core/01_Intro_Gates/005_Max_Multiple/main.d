int maxMultiple(int divisor, int bound)
{
    int n = bound;
    while (n % divisor != 0) n--;
    return n;
}
