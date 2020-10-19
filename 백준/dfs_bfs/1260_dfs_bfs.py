import sys
from collections import deque

n,m,v = map(int, sys.stdin.readline().rstrip().split())
graph = []
dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)
graph = [[0] for _ in range(n+1)] # 0으로 초기화 된 고정 크기의 리스트 선언
for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().rstrip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    graph[v1].sort()
    graph[v2].sort()

def dfs(graph, v, dfs_visited):
    if v != 0:
        print(v, end=' ')
    dfs_visited[v] = True
    for i in graph[v]:
        if i != 0:
            if dfs_visited[i] != True:
                dfs(graph, i, dfs_visited)

def bfs(graph, v, bfs_visited):
    q = deque()
    q.append(v)
    bfs_visited[v] = True
    while q:
        p = q.popleft()
        if p !=0:
            print(p, end=' ')
        for i in graph[p]:
            if bfs_visited[i] != True:
                q.append(i)
                bfs_visited[i] = True


dfs(graph, v, dfs_visited)
print()
bfs(graph, v, bfs_visited)