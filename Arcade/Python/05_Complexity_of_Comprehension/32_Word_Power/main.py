def solution(word):
    num = {c: ord(c) - ord('a') + 1 for c in word}
    return sum([num[ch] for ch in word])
