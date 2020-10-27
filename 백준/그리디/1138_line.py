import sys

#키가 가장 작은 사람인 1부터 넣는다.
#키가 작은 순으로 넣기 때문에 이후에 넣는 값들은 for문을 돌며 
#자신이 들어갈 위치까지 값이 0인 자리에 대해서만 count를 올려 count가 자신의 위치와 같을 때 그 위치에 값을 넣는다.

N = int(input())
people = list(map(int,sys.stdin.readline().rstrip().split()))
result = [0] * N
#숫자를 순서대로 넣기위해 즉, 0번이 아니라 1번부터 시작 되게
for i in range(1, N+1):
    count = 0
    k = people[i-1] #왼쪽 사람의 수 즉, 자신 다 키가 큰 사람의 수
    for j in range(0, N):
        if count == k and result[j] == 0:
            result[j] = i
            break
        elif result[j] == 0:
            count += 1

print(*result)