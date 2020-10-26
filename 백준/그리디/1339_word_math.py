import sys
import math

# 풀이 아이디어
# 10진법의 숫 자의 특징을 이용해야한다.
# ABCDEF 와 FDA라는 문자가 있을 때, 두 수의 합이 최대가 되도록 하려는 문제이다.
# A는 10^5 자리에있고 첫 번째는  A*10^0 번째 자리에 있다. 
# 즉, 100000의 자리와 1의 자리가 있다 이 둘을 더하면 100001이고 A가 9라면 900009이다.
# 두 수를 100001 * 9 꼴이다 이를 이용해야 한다.

# GCF와 ACDEB가 있다면
# 1.  GCF =  100*G + 10*C + 1*F
# 2. ACDEB = 10000*A + 1000*C + 100*D + 10*E + 1*B
# 이므로 각 알파벳 별로 곱해지게 될 숫자는
# A : 10000
# B : 1
# C : 1010
# D : 100
# E : 10
# F : 1

lines = int(input())

words = []
sets = {}
for _ in range(lines):
    words.append(sys.stdin.readline().rstrip())

words.sort(key=lambda x : len(x), reverse=True)

for i in range(len(words)):
    word = list(words[i])
    for j in range(len(word)):
        if sets.get(word[j]) != None:
            sets[word[j]] += int(math.pow(10, (len(word) - (j+1))))
        else:
            sets[word[j]] = int(math.pow(10, (len(word) - (j+1))))

sum_list = []
result = 0
start_num = 9
for i in sets:
    sum_list.append(sets[i])

sum_list.sort(reverse=True)

for val in sum_list:
    result += (start_num * val)
    start_num -=1

print(result)