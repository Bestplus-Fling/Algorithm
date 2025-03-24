import sys
sys.stdin = open('3055.txt')
from collections import deque

dxy = [1, 0], [0, -1], [-1, 0], [0, 1]
# 물을 미리 채운다


def change():
    stack = []
    for i in range(R):
        for ii in range(C):
            if arr[i][ii] == '*':
                for dx, dy in dxy:
                    nx, ny = i + dx, ii + dy
                    if not(0 <= nx < R and 0 <= ny < C):
                        continue
                    if arr[nx][ny] != '.': continue
                    stack.append([nx, ny])
    while stack:
        bx, by = stack.pop()
        arr[bx][by] = '*'
    # if tc == 1:
    #     print(*arr, sep='\n', end='\n \n')


# 그 다음 델타 탐색을 한다.
def bfs(x, y):
    queue = deque([[x, y, 0]])
    visited = [[False] * C for _ in range(R)]
    visited[x][y] = True
    check = 0
    change()
    while queue:
        x, y, cnt = queue.popleft()
        if check != cnt:
            change()
            check += 1
        cnt += 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < R and 0 <= ny < C): continue
            if visited[nx][ny]: continue
            if arr[nx][ny] == '*': continue
            if arr[nx][ny] == 'X': continue
            if (nx, ny) == end:
                return cnt
            queue.append([nx, ny, cnt])
            visited[nx][ny] = True
    return 'KAKTUS'


for _ in range(5):
    R, C = map(int, input().split())
    arr = [list(input().strip()) for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '.':
                continue
            if arr[i][j] == 'D':
                end = (i, j)
            elif arr[i][j] == 'S':
                start = (i, j)
    sx, sy = start
    print(bfs(sx, sy))
