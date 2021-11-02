int addTwoDigits(int n)
{
    string myNumb = n.ToString();
    string firstDigit = myNumb.Substring(0, 1);
    string secondDigit = myNumb.Substring(1, 1);
    int fd = Int32.Parse(firstDigit);
    int sd = Int32.Parse(secondDigit);
    return fd + sd;
}
