#백준 1697번 숨바꼭질 문제
# bfs의 핵심은 visited 된 공간이용이다.

# 생각 못했던 것... queue에 담는 데이터를 [방문 한 점, sec]로 두는 것을 생각하는 것과 visited 배열을 생각 못함
# '-' 될 때 음수로 나가는 것을 생각 못함, + 될 때 제한된 숫자인 100,000을 넘기는 걸 생각 못했음
# 이렇게 할 경우 각 큐에서 나오는 값들이 자기 자신만의 고유의 시간 값(초)을 가질 수 있음
import sys
from collections import deque
n,k = map(int, sys.stdin.readline().rstrip().split())
check_list = [0] * 100001
sec = 0

q = deque()
q.append([n, sec])

def bfs(v):
    count = 0
    q = deque()
    q.append([v, count])

    while q:
        v, count = q.popleft()
        if check_list[v] != 1:
            check_list[v] = 1
            if v == k: # 0초에 바로 찾는 경우
                break
            count += 1
            if (v + 1 <= 100000):
                q.append([v+1, count])
            if (v - 1 >= 0):
                q.append([v-1, count])
            if v * 2 <= 100000:
                q.append([v * 2, count])
    print(count)

bfs(n)