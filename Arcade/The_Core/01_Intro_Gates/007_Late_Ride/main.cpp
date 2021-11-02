int lateRide(int n)
{
    std::string hours = std::to_string(n / 60);
    std::string minutes = std::to_string(n % 60);
    
    int sum = 0;
    
    if (hours.length() == 1) sum = sum + std::stoi(hours.substr(0, 1));
    else
    {
        sum = sum + std::stoi(hours.substr(0, 1));
        sum = sum + std::stoi(hours.substr(1, 1));
    }
    
    if (minutes.length() == 1) sum = sum + std::stoi(minutes.substr(0, 1));
    else
    {
        sum = sum + std::stoi(minutes.substr(0, 1));
        sum = sum + std::stoi(minutes.substr(1, 1));
    }
    
    return sum;
}
