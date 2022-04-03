def colorGraph(n, G, color, pos, c):
    if color[pos] != -1 and color[pos] != c:
        return False

    # color this pos as c and all its neighbours and 1-c
    color[pos] = c
    ans = True
    for i in range(0, n):
        if i in G[pos]:
            if color[i] == -1:
                ans &= colorGraph(n, G, color, i, 1-c)

            if color[i] != -1 and color[i] != 1-c:
                return False

        if not ans:
            return False

    return True


def isBipartite(n, G):
    color = [-1] * n

    #start is vertex 0
    pos = 0
    # two colors 1 and 0
    return colorGraph(n, G, color, pos, 1)


def solution(n, wmap):
    wmap_new_form = { i: set() for i in range(n) }
    for arc in wmap:
        wmap_new_form[arc[0]].add(arc[1])
        wmap_new_form[arc[1]].add(arc[0])
    return isBipartite(n, wmap_new_form)
    

n = 5
G = [[1, 2], [1, 3], [1, 4], [0, 2], [4, 0]]
print(solution(n, G))  # True

n = 5
G = [[1, 2], [1, 3], [1, 4], [0, 2], [4, 0], [1, 0]]
print(solution(n, G))  # False
