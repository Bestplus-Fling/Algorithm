import sys
sys.stdin = open('input.txt', 'r')
#####################################
from collections import deque
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]

check = {
    (0, -1): [1, 3, 4, 5],
    (0, 1): [1, 3, 6, 7],
    (-1, 0): [1, 2, 5, 6],
    (1, 0): [1, 2, 4, 7],
}


def bfs(x, y):
    queue = deque([[x, y, 1]])

    while queue:
        x, y, t = queue.popleft()
        visited[x][y] = t
        if t == L:
            continue
        p = arr[x][y]
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < M) or visited[nx][ny]:
                continue
            if arr[nx][ny] == 0:
                continue
            np = arr[nx][ny]
            if p in check[(-dx, -dy)] and np in check[(dx, dy)]:
                queue.append([nx, ny, t+1])


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    ans = 0
    bfs(R, C)
    for i in range(N):
        ans += visited[i].count(0)
    print(f'#{tc}', (N*M) - ans)