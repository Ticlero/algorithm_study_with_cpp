import sys
n, m, k = map(int,sys.stdin.readline().rstrip().split(' '))

number_list = list(map(int, sys.stdin.readline().rstrip().split()))

number_list.sort(reverse=True)

if len(number_list) > n:
    exit()

number_list.sort(reverse=True)
#print(number_list)
first_big_num = number_list[0]
second_big_num = number_list[1]

count = int(m/(k+1)) * k
count += m%(k+1)

result = 0
result += count * first_big_num
result += (m-count)*second_big_num

print(result)
