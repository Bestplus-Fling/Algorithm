import sys
sys.stdin = open("algo2_sample_in.txt")
from collections import deque
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def bfs(x, y):
    queue = deque([[x, y]])
    cnt = 1
    arr[x][y] = 1
    # visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < M): continue
            # if visited[nx][ny]: continue
            if arr[nx][ny] == 1: continue
            queue.append([nx, ny])
            cnt += 1
            arr[nx][ny] = 1
            # visited[nx][ny] = True
    return cnt


T = int(input())
for tc in range(1, T+1):
    N, M, A = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # visited = [[False] * M for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(M):
            # if visited[i][j]:
            #     continue
            if arr[i][j] == 1:
                continue
            if bfs(i, j) >= A:
                ans += 1
    print(f'#{tc}', ans)