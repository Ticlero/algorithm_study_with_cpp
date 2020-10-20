import sys
from collections import deque

n,m = map(int, sys.stdin.readline().rstrip().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

q = deque()
q.append([0,0])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x,y = q.popleft()

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 0:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            q.append([nx, ny])

print(graph[n-1][m-1])