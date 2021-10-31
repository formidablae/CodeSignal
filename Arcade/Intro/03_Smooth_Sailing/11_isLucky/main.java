boolean isLucky(int n)
{
    String numberString = String.valueOf(n);
    String firstHalf = numberString.substring(0, numberString.length() / 2);
    String secondHalf = numberString.substring(numberString.length() / 2, numberString.length());
    int sumFirstHalf = 0;
    int sumSecondHalf = 0;
    
    for (int i = 0; i < firstHalf.length(); i++)
    {
        sumFirstHalf = sumFirstHalf + Integer.parseInt(firstHalf.substring(i, i + 1));
        sumSecondHalf = sumSecondHalf + Integer.parseInt(secondHalf.substring(i, i + 1));
    }
    
    if (sumFirstHalf == sumSecondHalf) return true;
    else return false;
}
