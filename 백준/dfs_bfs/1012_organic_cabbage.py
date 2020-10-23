import sys
sys.setrecursionlimit(50000)
case = int(sys.stdin.readline().rstrip()) #반복 횟수
rows = 0 # 행의 개수
cols = 0 # 열의 개수
result_box = [] # 결과 값 저장 list
dx = [1, -1, 0, 0] # 4방향 이동하기 위한 변수
dy = [0, 0, 1, -1]

def dfs(farm, x,y):
    #범위를 넘어가지 않게
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return False
    if farm[x][y] == 1: #배추가 있는 곳을 재귀적으로 돌아서 연결된 부분 모두 0으로 만듦
        farm[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(farm, nx,ny)
        return True #배추가 1개 이상 있으면 지렁이가 필요하니 True 반환
    return False

for _ in range(case):
    rows, cols, cabbages = map(int, sys.stdin.readline().rstrip().split())
    if rows < 1 or rows > 50 or cols < 1 or cols > 50 or cabbages < 1 or cabbages > 2500:
        exit()

    farm = [[0]*cols for _ in range(rows)]
    for _ in range(cabbages):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        farm[x][y] = 1

    result = 0
    for i in range(rows):
        for j in range(cols):
            if dfs(farm,i,j) == True:
                result += 1

    result_box.append(result)
    
for i in result_box:
    print(i)