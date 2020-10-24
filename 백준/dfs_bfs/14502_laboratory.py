import sys, copy
from itertools import combinations #벽을 세우는 경우를 모두 계산하기 위해. combination을 이용하기 위해 필요한 라이브러리
from collections import deque #bfs로 문제를 풀기위해 필요한 라이브러리

rows, cols = map(int, sys.stdin.readline().rstrip().split())

graph = [] #연구소의 지도
visited = [[False]*cols for _ in range(rows)] #바이러스가 방문한 곳
virus_pos = [] #바이러스의 최초 위치들 저장
blank_pos = [] #벽을 세우기 위해 빈 공간의 위치들를 저장

dx = [1,-1,0,0] # 바이러스의 좌,우 이동
dy = [0,0,1,-1] # 바이러스의 상,하 이동

for _ in range(rows):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(line)

for i in range(rows):
    for j in range(cols):
        if graph[i][j] == 0:
            blank_pos.append((i,j))
        elif graph[i][j] == 2:
            virus_pos.append((i,j))

wall_building_list = list(combinations(blank_pos,3)) #벽이 그려질 수 있는 모든 경우의 수

result = 0

def visited_init():
    for i in range(rows):
        for j in range(cols):
            visited[i][j] = False

def graph_init(walls):
    for i in range(rows):
        for j in range(cols):
            if graph[i][j] == 1:
                for pos in walls:
                    x,y = pos
                    if i == x and j == y:
                        graph[i][j] = 0
            elif graph[i][j] == 2:
                for pos in virus_pos:
                    x,y = pos
                    if i != x or j != y:
                        graph[i][j] = 0
    
#bfs를 이용해 바이서르 퍼뜨리기
def bfs(g, vis):
    queue = deque()
    for i in range(len(virus_pos)):
        queue.append(virus_pos[i])

    while queue:
        x, y = queue.popleft()
        vis[x][y] = True
        g[x][y] = 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                continue
            if g[nx][ny] == 1 or vis[nx][ny] == True:
                continue
            if g[nx][ny] == 0 and vis[nx][ny] == False:
                queue.append([nx, ny])
#바이러스가 퍼뜨려진 후 0의 개수 세기
def count_fun(g):
    count = 0
    for i in range(rows):
        for j in range(cols):
            if g[i][j] == 0:
                count += 1
    return count



for i in range(len(wall_building_list)):
    # c_graph = copy.deepcopy(graph)
    # c_visited = copy.deepcopy(visited)
    for pos in wall_building_list[i]:
        x,y = pos
        graph[x][y] = 1
    bfs(graph, visited)
    result = max(result, count_fun(graph))
    visited_init()
    graph_init(wall_building_list[i])

print(result)