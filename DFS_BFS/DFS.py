#Depth First Search
#깊이 우선 탐색
#stack으로 구현 가능 - adjacency matrix 으로 구현
#그래프가 주어졌을 때, 탐색을 시작하고자 하는 vertex(node)를 주면 그 노드서 부터 시작 해 이어져 있는 모든 노드를 출력
#인접해 있는 노드 중 번호가  낮은 순서부터 시작

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] != True:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [6, 8],
    [1, 7]
]

visited = [False for _ in range(9)]

dfs(graph, 1, visited)