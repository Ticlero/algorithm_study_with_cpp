import sys

buttons = [300, 60, 10]
push_cnt = [0,0,0]
time = int(input())

if time % 10 != 0:
    print(-1)
    exit()

input_t = 0

while time != 0:
    if time >= buttons[0]:
        push_cnt[0] += 1
        time -= buttons[0]
    elif time >= 60:
        push_cnt[1] += 1
        time -= buttons[1]
    elif time >= 10:
        push_cnt[2] += 1
        time -= buttons[2]

for i in push_cnt:
    print(i, end=" ")