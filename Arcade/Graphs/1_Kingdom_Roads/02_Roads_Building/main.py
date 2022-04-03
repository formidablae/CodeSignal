def solution(cities, roads):
    graph = {}
    new_roads = []
    for city in range(cities):
        graph[city] = []
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])
    for city1 in range(cities):
        for city2 in range(city1 + 1, cities):
            if city1 not in graph[city2] and city2 not in graph[city1]:
                new_roads.append([city1, city2])
    return new_roads

# cities = 4
# roads = [[0,1], [1,2], [2,0]]
# print(solution(cities, roads))
