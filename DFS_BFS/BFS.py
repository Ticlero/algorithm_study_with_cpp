from collections import deque

def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        i = queue.popleft()
        print(i, end=' ')
        for j in graph[i]:
            if not visited[j]:
                queue.append(j)
                visited[j] = True

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

visited = [False] * 9
bfs(graph, 1, visited)
queue = deque()
queue.append(1)
print(queue)