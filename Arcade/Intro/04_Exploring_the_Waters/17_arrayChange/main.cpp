int arrayChange(std::vector<int> inputArray)
{
    int count = 0;
    for (int i = 1; i < inputArray.size(); i++)
    {
        if (inputArray[i - 1] >= inputArray[i])
        {
            inputArray[i]++;
            count++;
            i--;
        }
    }
    return count;
}
