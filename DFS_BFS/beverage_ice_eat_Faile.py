import sys
from collections import deque

n,m = map(int, sys.stdin.readline().rstrip().split())

ice_list = [[0]*m for _ in range(n)]
ice_check = [[0]*m for _ in range(n)]
for i in range(n):
    line = sys.stdin.readline().rstrip()
    for j in range(m):
        ice_check[i][j] = False
        ice_list[i][j] = int(list(line)[j])

print(ice_check)
print(ice_list)

stack = []
def dfs(list, i, j, checked):
    if (i < 0 and i >= n) or (j < 0 and j >= m):
        return False

    if list[i][j] == 0 and ice_check[i][j] == False:
        ice_check[i][j] = True
        dfs(list, i - 1, j, checked) #상
        dfs(list, i + 1, j, checked) #하
        dfs(list, i, j - 1, checked) #좌
        dfs(list, i, j + 1, checked) #우
        return True
    return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(ice_list, i, j, ice_check) == True:
            result += 1

print(result)