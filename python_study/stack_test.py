stack = [] #리스트 자체가 스택임

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
# print(stack.pop())
print(stack)
# print(stack.pop())
# stack.append(1)
# stack.append(2)
# print(stack)

def test(stack):
    s = stack
    s.append(6)
    s.append(7)
    print(s)

print(test(stack))
print(stack)