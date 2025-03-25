import sys
sys.stdin = open("1926.txt")
# queue 사용
from collections import deque
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def bfs(x, y):
    queue = deque([[x, y]])
    c = 0
    arr[x][y] = '0'
    while queue:
        x, y = queue.popleft()
        c += 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < M): continue
            if arr[nx][ny] == '0': continue
            queue.append([nx, ny])
            arr[nx][ny] = '0'
    return c


N, M = map(int, input().split())
arr = [list(input().split()) for _ in range(N)]
ans, cnt = 0, 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == '1':
            cnt += 1
            ans = max(ans, bfs(i, j))
print(cnt, ans, sep='\n')
