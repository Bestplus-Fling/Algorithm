import sys
sys.stdin = open('2667.txt', 'r')

from collections import deque

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(x, y):
    global le
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    le.append(cnt)


n = int(input())
arr = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
le = []
for i in range(n):
    for j in range(n):
        if arr[i][j] and not visited[i][j]:
            bfs(i, j)
le.sort()
print(len(le))
print(*le, sep='\n')