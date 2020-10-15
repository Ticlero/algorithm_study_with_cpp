import sys

count = 0
coin = [500, 100, 50, 10]


change = int(sys.stdin.readline().rstrip())
i = change%10
if i != 0:
    sys.exit()

for c in coin:
    count += change//c
    change %= c

print(count)
