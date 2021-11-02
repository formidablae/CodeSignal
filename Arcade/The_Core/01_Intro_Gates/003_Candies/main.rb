def candies(n, m)
    num = 0
    newNum = 0
    i = 0
    while newNum < m do
        num = newNum
        newNum = n * i
        i += 1
    end
    if newNum == m
        return newNum
    else
        return num
    end
end
