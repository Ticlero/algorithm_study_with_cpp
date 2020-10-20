import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

if n < 5 or n > 25:
    exit()

graph = []
check = [[False] * n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

last = 0
house_list = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x, y):
    if graph[x][y] == 0 or check[x][y] == True:
        return False
    house = 1
    queue = deque()
    queue.append([x,y])
    check[x][y] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1 and check[nx][ny] == False:
                queue.append([nx, ny])
                check[nx][ny] = True
                house += 1
    house_list.append(house)
    return True

for i in range(n):
    for j in range(n):
        if bfs(i,j) == True:
            last += 1


print(last)
house_list.sort()
for i in range(len(house_list)):
    print(house_list[i])