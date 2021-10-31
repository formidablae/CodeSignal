std::vector<std::string> allLongestStrings(std::vector<std::string> inputArray)
{
    std::vector<std::string> result;
    result.push_back("");
    
    std::vector<std::string> theInputArray = inputArray;
    
    for (int i = 0; i < theInputArray.size(); i++)
    {
        if (theInputArray[i].length() > result[result.size() - 1].length())
        {
            result.clear();
            result.push_back(theInputArray[i]);
        }
        else if (theInputArray[i].length() == result[result.size() - 1].length())
        {
            result.push_back(theInputArray[i]);
        } // else do nothing
    }
                             
    return result;
}
