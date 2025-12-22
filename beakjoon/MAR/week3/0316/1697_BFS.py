import sys
sys.stdin = open('input/1697.txt', 'r')
#########################################
from collections import deque


def dfs(n):
    global ans
    queue = deque([[n, 0]])
    visited = [0] * 10000000
    while queue:
        now, time = queue.popleft()
        if ans < time:
            continue
        if now == K:
            ans = min(ans, time)
        if visited[now]:
            continue
        time += 1
        queue.append([now + 1, time])
        if now < K:
            queue.append([now * 2, time])
        queue.append([now - 1, time])
        visited[now] = 1


N, K = map(int, input().split())
ans = float('inf')
dfs(N)
print(ans)
