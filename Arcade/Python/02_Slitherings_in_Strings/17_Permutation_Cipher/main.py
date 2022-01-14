def solution(password, key):
    table = str.maketrans("abcdefghijklmnopqrstuvwxyz", key)
    return password.translate(table)
