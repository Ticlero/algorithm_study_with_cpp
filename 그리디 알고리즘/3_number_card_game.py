import sys

n, m = list(map(int, sys.stdin.readline().rstrip().split()))

if (n < 1 and n > 100) or (m < 1 and m > 100):
    exit()

card_list = [[0]*m for _ in range(n)]

#card_list[0] = [1,2,3,4]
min_num_list = []
for i in range(n):
    card_list[i] = list(map(int, sys.stdin.readline().split()))
    card_list[i].sort()
    min_num_list.append(card_list[i][0])

min_num_list.sort(reverse=True)

print(min_num_list[0])
