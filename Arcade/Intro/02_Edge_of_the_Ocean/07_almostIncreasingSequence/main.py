def almostIncreasingSequence(sequence):
    s_1 = list(sequence)
    s_2 = list(sequence)
    for i in range(0, len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            s_1.pop(i)
            s_2.pop(i+1)
            break
    if s_1 == sorted(set(s_1)) and s_1 == sorted(s_1):
        return True
    elif s_2 == sorted(set(s_2)) and s_2 == sorted(s_2):
        return True
    else:
        return False
