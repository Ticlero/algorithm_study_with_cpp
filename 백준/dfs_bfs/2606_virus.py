import sys
from collections import deque

n = int(sys.stdin.readline().rstrip()) #컴퓨터 수
m = int(sys.stdin.readline().rstrip()) #연결된 컴퓨터 수

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().rstrip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def bfs(g, v, visited):
    result = 0
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                result += 1
    print(result)

bfs(graph, 1, visited)