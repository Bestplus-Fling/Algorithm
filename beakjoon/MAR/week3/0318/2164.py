import sys
sys.stdin = open('2164.txt', 'r')
#########################################
from collections import deque

N = int(sys.stdin.readline())
queue = deque([i for i in range(1, N+1)])
a, Flag = 0, False
while queue:
    temp = queue.popleft()
    if len(queue) <= 1:
        if len(queue) == 1:
            Flag = True
        break
    insert = queue.popleft()
    queue.append(insert)
print(queue[0] if Flag else temp)
