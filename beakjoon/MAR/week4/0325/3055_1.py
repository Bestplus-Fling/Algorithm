import sys
sys.stdin = open("3055.txt")
from collections import deque
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def change():
    global water
    temp = []
    while water:
        x, y = water.pop()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < R and 0 <= ny < C):
                continue
            if arr[nx][ny] == '.':
                arr[nx][ny] = '*'
                temp.append([nx, ny])
    water = temp
    # print(*arr, sep='\n', end='\n\n')


def bfs(x, y):
    queue = deque([[x, y, 0]])
    visited = [[0] * C for _ in range(R)]
    visited[x][y] = 1
    check = 0
    change()
    while queue:
        x, y, cnt = queue.popleft()
        if cnt != check:
            change()
            check += 1
        cnt += 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < R and 0 <= ny < C):
                continue
            if arr[nx][ny] == 'D':
                return cnt
            if arr[nx][ny] == '.':
                queue.append([nx, ny, cnt])
                visited[nx][ny] = 1
    return 'KAKTUS'


R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
water = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            water.append([i, j])
        if arr[i][j] == 'S':
            sx, sy = i, j
print(bfs(sx, sy))




# def change():
#     v = [[0] * C for _ in range(R)]
#     for i in range(R):
#         for j in range(C):
#             if arr[i][j] == '*' and v[i][j] == 0:
#                 v[i][j] = 1
#                 for dx, dy in dxy:
#                     nx, ny = i + dx, j + dy
#                     if not(0 <= nx < R and 0 <= ny < C):
#                         continue
#                     if arr[nx][ny] == '.':
#                         arr[nx][ny] = '*'
#                         v[nx][ny] = 1
#     print(*arr, sep='\n', end='\n\n')
