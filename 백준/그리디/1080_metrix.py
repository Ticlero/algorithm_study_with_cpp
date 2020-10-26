#https://mizzo-dev.tistory.com/entry/baekjoon1080 풀이 해설
import sys

n,m = map(int, sys.stdin.readline().rstrip().split())

A = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
B = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
result = 0

def flip(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]

for i in range(0,n-2):
    for j in range(0,m-2):
        if A[i][j] != B[i][j]:
            flip(i,j)
            result+=1
        
for i in range(n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            print(-1)
            exit()

print(result)

# print(A)
# print(B)
# print(check)

# N, M =map(int,input().split())

# A = [list(map(int,list(input()))) for _ in range(N)]
# B = [list(map(int,list(input()))) for _ in range(N)]

# def flip(x,y):
#     for i in range(x,x+3):
#         for j in range(y,y+3):
#             A[i][j] = 1 - A[i][j]

# def checkEquality():
#     for i in range(N):
#         for j in range(M):
#             if A[i][j] !=B[i][j]:
#                 return 0
#     return 1

# cnt = 0
# for i in range(0,N-2):
#     for j in range(0,M-2):
#         if A[i][j] != B[i][j]:
#             flip(i,j)
#             cnt+=1

# if checkEquality():
#     print(cnt)
# else:
#     print(-1)