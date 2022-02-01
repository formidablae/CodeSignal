def solution(answers, p):
    questionPoints = lambda i, ans : ans + i if ans == True else ans - p
    
    res = 0
    for i, ans in enumerate(answers):
        res += questionPoints(i, ans)
    return res
