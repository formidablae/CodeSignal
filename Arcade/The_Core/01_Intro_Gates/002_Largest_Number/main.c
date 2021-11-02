int largestNumber(int n)
{
    int num = 10;
    for (int i = 1; i < n; i++)
    {
        num = num * 10;
    }
    
    return num - 1;
}
