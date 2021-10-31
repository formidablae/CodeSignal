std::vector<int> alternatingSums(std::vector<int> a)
{
    int sumOne = 0, sumTwo = 0;
    for (int i = 0; i < a.size(); i++)
    {
        if (i % 2 == 0) sumOne = sumOne + a[i];
        else sumTwo = sumTwo + a[i];
    }
    vector<int> vect{sumOne, sumTwo};
    return vect;
}
