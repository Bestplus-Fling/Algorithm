import sys
sys.stdin = open("2178.txt")
from collections import deque
dxy = [1, 0], [0, 1], [-1, 0], [0, -1]


def bfs(ex, ey):
    global result
    queue = deque([[0, 0, 1]])
    visited[0][0] = 1
    while queue:
        x, y, dist = queue.popleft()
        if x == ex and y == ey:
            result = min(result, dist)
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < M) or visited[nx][ny]:
                continue
            if maze[nx][ny] == '0':
                continue
            queue.append([nx, ny, dist+1])
            visited[nx][ny] = 1


N, M = map(int, input().split())
maze = [list(input().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
result = float('inf')
bfs(N-1, M-1)
print(result)
