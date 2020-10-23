import sys

n,m = map(int, sys.stdin.readline().rstrip().split())

if n > 1000 or n < 1 or m < 0 or m > (n*(n-1)/2):
    exit()

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().rstrip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(graph, v, visited):
    if visited[v] != False:
        return False
    visited[v] = True
    for i in graph[v]:
        dfs(graph, i, visited)
    return True

result = 0
if m != 0:
    for i in range(n):
        if dfs(graph, i+1, visited) == True:
            result += 1

print(result)