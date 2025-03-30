import sys
sys.stdin = open("7576.txt")
from collections import deque
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def bfs(n):
    queue = deque(n)
    while queue:
        x, y, cnt = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < M): continue
            if arr[nx][ny] != 0: continue
            queue.append([nx, ny, cnt+1])
            arr[nx][ny] = -1
    for k in range(N):
        for l in range(M):
            if arr[k][l] == 0:
                return -1
    return cnt


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

stack = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            stack.append([i, j, 0])
            arr[i][j] = -1
print(bfs(stack))
