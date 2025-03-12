import sys
sys.stdin = open('input.txt', 'r')
#####################################
from collections import deque
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def bfs(r, o, h):
    global ans
    queue = deque()
    queue.append((r, o, h))

    while queue:
        x, y, cnt = queue.popleft()
        arr[x][y] = '1'
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < N) or arr[nx][ny] == '1':
                continue
            queue.append((nx, ny, cnt+1))

            if arr[nx][ny] == '3':
                ans = cnt
                return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                bfs(i, j, 0)
    print(f'#{tc}', ans)
