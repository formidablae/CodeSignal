std::vector<int> sortByHeight(std::vector<int> a)
{
    std::vector<int> inputVector = a;
    std::vector<int> orderedVectorNoTrees;
    
    for (int i = 0; i < inputVector.size(); i++)
    {
        if (inputVector[i] == -1) continue;
        else orderedVectorNoTrees.push_back(inputVector[i]);
    }
    
    std::sort (orderedVectorNoTrees.begin(), orderedVectorNoTrees.end());
    
    for (int i = 0; i < inputVector.size(); i++)
    {
        if (inputVector[i] == -1) continue;
        else inputVector[i] = orderedVectorNoTrees[0];
        orderedVectorNoTrees.erase(orderedVectorNoTrees.begin());
    }
    
    return inputVector;
}
