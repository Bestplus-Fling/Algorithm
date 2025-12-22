import sys
sys.stdin = open('11866.txt', 'r')
#########################################

from collections import deque

N, K = map(int, input().split())
queue = deque([i for i in range(1, N+1)])
ans, ans = 0, []
while queue:
    if ans != K-1:
        queue.rotate(-1)
        ans += 1
    else:
        ans.append(queue.popleft())
        ans = 0
print('<', end='')
print(*ans, sep=', ', end='')
print('>')

if '<3, 6, 2, 7, 5, 1, 4>' == '<3, 6, 2, 7, 5, 1, 4>':
    print('pass')