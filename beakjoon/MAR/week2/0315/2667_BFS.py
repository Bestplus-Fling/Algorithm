import sys
sys.stdin = open('2667.txt', 'r')
#########################################
from collections import deque
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def dfs(x, y):
    cnt = 0
    queue = deque([[x, y]])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < N) or arr[nx][ny] == '0':
                continue
            if visited[nx][ny]:
                continue
            queue.append([nx, ny])
            visited[nx][ny] = True
    return cnt


N = int(input())
arr = [list(input().strip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
ans = []
for i in range(N):
    for j in range(N):
        if visited[i][j] or arr[i][j] == '0':
            continue
        ans.append(dfs(i, j))
print(len(ans), *ans, sep='\n')


