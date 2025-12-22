import sys
sys.stdin = open('1012.txt', 'r')
#####################################
from collections import deque
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def bfs(x, y):
    queue = deque([[x, y]])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < M) or visited[nx][ny] or not grid[nx][ny]:
                continue
            queue.append([nx, ny])
            visited[nx][ny] = True


T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    grid = [[0] * M for _ in range(N)]
    for u in range(K):
        cx, cy = map(int, input().split())
        grid[cy][cx] = 1
    ans = 0
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j] or not grid[i][j]:
                continue
            bfs(i, j)
            ans += 1
    print(ans)
