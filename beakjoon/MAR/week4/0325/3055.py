import sys
sys.stdin = open("3055.txt")
from collections import deque
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]
water = []


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
                temp.append([nx, ny])
                arr[nx][ny] = '*'
    water = temp


def bfs(x, y):
    queue = deque([[x, y, 0]])
    visited = [[False] * C for _ in range(R)]
    visited[x][y] = True
    change()
    check = 0
    while queue:
        x, y, cnt = queue.popleft()
        if cnt != check:
            check += 1
            change()
        cnt += 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < R and 0 <= ny < C):
                continue
            if arr[nx][ny] == '*' or arr[nx][ny] == 'X' or visited[nx][ny]: continue
            if arr[nx][ny] == 'D':
                return cnt
            queue.append([nx, ny, cnt])
            visited[nx][ny] = True
    return 'KAKTUS'


R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'S':
            sx, sy = i, j
        elif arr[i][j] == '*':
            water.append([i, j])

print(bfs(sx, sy))
