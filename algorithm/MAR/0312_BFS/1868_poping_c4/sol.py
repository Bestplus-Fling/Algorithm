import sys
sys.stdin = open('input2.txt', 'r')
#####################################
# from pprint import pprint
from collections import deque
dxy = [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]


def check_bomb(x, y):
    count = 0
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not(0 <= nx < N and 0 <= ny < N) or arr[nx][ny] == '.':
            continue
        if arr[nx][ny] == '*':
            visited[nx][ny] = True
            count += 1
    return str(count)


def bfs(cx, cy):
    queue1 = deque()
    queue1.append((cx, cy))
    while queue1:
        x, y = queue1.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny]:
                continue
            if arr[nx][ny] != '*' and arr[nx][ny] != '0':
                visited[nx][ny] = True
                continue
            queue1.append((nx, ny))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    ans = 0
    # print(arr)
    queue = deque()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.':
                arr[i][j] = check_bomb(i, j)
                if arr[i][j] == '0':
                    queue.append((i, j))
    while queue:
        lx, ly = queue.popleft()
        if visited[lx][ly]:
            continue
        ans += 1
        bfs(lx, ly)
    for n in range(N):
        ans += visited[n].count(False)
    # for n in range(N):
    #     print(visited[n])
    # for n in range(N):
    #     print(arr[n])
    print(f'#{tc}', ans)
