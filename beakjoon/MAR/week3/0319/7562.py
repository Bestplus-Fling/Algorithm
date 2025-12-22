import sys
sys.stdin = open('7562.txt', 'r')
#########################################
from collections import deque
knight = [-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]


def bfs(x, y):
    visited = [[0] * N for _ in range(N)]
    queue = deque([[x, y, 0]])
    visited[x][y] = 1
    while queue:
        x, y, c = queue.popleft()
        if x == mx and y == my:
            return c
        c += 1
        for dx, dy in knight:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < N) or visited[nx][ny]:
                continue
            queue.append([nx, ny, c])
            visited[nx][ny] = 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    i, j = map(int, input().split())
    mx, my = map(int, input().split())
    ans = bfs(i, j)
    print(ans)
