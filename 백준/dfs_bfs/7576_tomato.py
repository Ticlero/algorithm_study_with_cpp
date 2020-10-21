import sys
from collections import deque

#m = colums, n = rows

# 내 접근 방식
# bfs로 풀되 1의 개 수가 x 일 때, queue에서 x만큼 뽑아낸 후 하루를 지나게 해야 한다. <- x 만큼 뽑은 후 하루를 지나게 하는 것을 생각하는게 어려웠음
# bfs가 끝난 후, dfs로 비어있거나 익지 않은 토마토가 존재할 시 0 또는 -1 
#  boolean 타입의 글로벌 변수로
m, n = map(int, sys.stdin.readline().rstrip().split())

if n < 2 or n > 1000 or m < 2 or m > 1000:
    exit()

graph = [[] for _ in range(n)]
ripe_pos = []
sRipeCnt = 0
enable_block = 0
result = 1
# -1 비어있는 토마토 칸, 0은 아직 익지 않은 토마토, 1은 익은 토마토
for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().rstrip().split()))

#queue에 1의 위치를 모두 저장
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ripe_pos.append([i,j])
            sRipeCnt += 1
            enable_block += 1
        elif graph[i][j] == 0:
            enable_block += 1

if sRipeCnt == enable_block:
    print(0)
    exit()

#print(graph)

queue = deque()
#queue에 위치 list 추가
for i in range(sRipeCnt):
    queue.append(ripe_pos[i])

dx = [0,0,-1,1]
dy = [-1,1,0,0]
endX = 0
endY = 0
while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue
        if graph[nx][ny] == -1:
            continue
        if graph[nx][ny] == 0:
            queue.append((nx, ny))
            if(sRipeCnt != 0):
                graph[nx][ny] = 1
            elif(sRipeCnt == 0):
                graph[nx][ny] = graph[x][y] + 1
    if(sRipeCnt != 0):
        sRipeCnt -= 1
    if queue == False:
        endX = x
        endY = y

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit()
        else:
            result = max(result, graph[i][j])
        
print(result)
