# 내 접근법
# 나열되어있는 주식 가격들 중 고점이 되는 지점의 위치를 다 찾아서 변수에 담는다. ex) 1 2 3 4 5 1 4 3 2 10  여기서는(0부터 시작) 4번째와 9번째

import sys
test_case = int(input())

result = []

def find_pick_pos(p_list):
    max_val = p_list[0]
    pick_list = []
    for i in range(1, len(p_list)):
        if(max_val < p_list[i])
            max_val = p_list[i]



def max_profit():
    days = int(input())
    price = list(map(int, sys.stdin.readline().rstrip().split()))
    print(days, price)

for _ in range(0, test_case):
    max_profit()