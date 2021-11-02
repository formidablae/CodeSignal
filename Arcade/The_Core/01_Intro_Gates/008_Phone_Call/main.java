int phoneCall(int min1, int min2_10, int min11, int s)
{
    int minutes = 0;
    if (s < min1)
    {
        return 0;
    }
    else
    {
        minutes++;
        s = s - min1;
    }
    
    if (s < min2_10)
    {
        return minutes;
    }
    else if (s >= min2_10 && s <= min2_10 * 9)
    {
        minutes = minutes + s / min2_10;
        s = s - (s / min2_10) * min2_10;
    }
    else
    {
        minutes = minutes + 9;
        s = s - 9 * min2_10;
        
        minutes = minutes + s / min11;
        s = s - (s / min11) * min11;
    }
    return minutes;
}
