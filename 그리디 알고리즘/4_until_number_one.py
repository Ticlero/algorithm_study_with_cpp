import sys

value, div_val = list(map(int, sys.stdin.readline().rstrip().split()))

if (value < 2 and value > 100000) or (div_val < 2 and div_val > 100000):
    exit()

count = 0
while value != 1:
    if value%div_val == 0:
        value = value//div_val
        count += 1
    else:
        value -= 1
        count += 1

print(count)
