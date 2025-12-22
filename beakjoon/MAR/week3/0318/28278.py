import sys
sys.stdin = open('28278.txt', 'r')
#########################################

N = int(input())
inputs = [list(sys.stdin.readline().split()) for _ in range(N)]
stack = []
for i in inputs:
    if i[0] == '1':
        stack.append(int(i[1]))
    elif i[0] == '2':
        print(stack.pop() if stack else -1)

    elif i[0] == '3':
        print(len(stack))

    elif i[0] == '4':
        print(0 if stack else 1)

    elif i[0] == '5':
        print(stack[-1] if stack else -1)



