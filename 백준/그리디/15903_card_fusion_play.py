import sys
# n은 카드의 개 수.
# m은 합체 횟수.
n, m = map(int, sys.stdin.readline().rstrip().split())

card_list = list(map(int, sys.stdin.readline().rstrip().split()))

def fusion(x, y):
    tmp = card_list[x] + card_list[y]
    card_list[x] = tmp
    card_list[y] = tmp

for i in range(0, m):
    card_list.sort()
    fusion(0,1)

print(sum(card_list))