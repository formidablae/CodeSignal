def reverseInParentheses(inputString):
    result = ""
    other = ""
    mod= 0
    for i in list(inputString):
        if i =="(":
            if mod != 0:
                other+=")"
            mod +=1
        elif i ==")":
            mod -=1
            if mod != 0:
                other+="("
        else:
            if mod == 0:
                result += i
            else:
                other += i
        if mod == 0 and other != "":
            result += reverseInParentheses(other[::-1])
            other =""
    return result
