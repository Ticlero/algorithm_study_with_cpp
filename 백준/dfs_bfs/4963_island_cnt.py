import sys
from collections import deque
sys.setrecursionlimit(100000)
dx = [1,-1, 0, 0, 1, 1, -1,-1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

result = []

def bfs(graph, x, y, rows, cols, visited):
    if visited[x][y] == True or graph[x][y] == 0:
        return False
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                continue
            if graph[nx][ny] == 0 or visited[nx][ny] == True:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                queue.append((nx, ny))
                visited[nx][ny] = True
    return True

def island_print(cols, rows):
    graph = [[] for _ in range(rows)]
    visited = [[False]*cols for _ in range(rows)]
    if cols >= 1 or cols <= 50 or rows <= cols:
        for i in range(rows):
            graph[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    r = 0
    for i in range(rows):
        for j in range(cols):
            if bfs(graph, i, j, rows,cols, visited) == True:
                r += 1
    result.append(r)


while True:
    cols, rows = map(int, sys.stdin.readline().rstrip().split())
    if cols != 0 and rows != 0:
        island_print(cols, rows)
    else:
        for i in result:
            print(i)
        exit()