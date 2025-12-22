import sys
sys.stdin = open('input.txt', 'r')
#########################################
from collections import deque

N = int(input())
queue = deque()
for i in range(N):
    work = list(sys.stdin.readline().split())
    if work[0] == 'push_back':
        queue.append(work[1])
    elif work[0] == 'push_front':
        queue.appendleft(work[1])
    elif work[0] == 'front':
        if not queue:
            print(-1)
            continue
        print(queue[0])
    elif work[0] == 'back':
        if not queue:
            print(-1)
            continue
        print(queue[-1])
    elif work[0] == 'pop_front':
        if not queue:
            print(-1)
            continue
        print(queue.popleft())
    elif work[0] == 'pop_back':
        if not queue:
            print(-1)
            continue
        print(queue.pop())
    elif work[0] == 'size':
        print(len(queue))
    elif work[0] == 'empty':
        print(0 if queue else 1)
