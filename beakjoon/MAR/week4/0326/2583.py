import sys
sys.stdin = open("2583.txt")
from collections import deque
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def bfs(x, y):
    queue = deque([[x, y]])
    cnt = 0
    arr[x][y] = 1
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < M and 0 <= ny < N): continue
            if arr[nx][ny]: continue
            queue.append([nx, ny])
            arr[nx][ny] = 1
    return cnt


M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1
# print(*arr, sep='\n')
ans = []
for i in range(M):
    for j in range(N):
        if not arr[i][j]:
            ans.append(bfs(i, j))
print(len(ans))
print(*sorted(ans))
