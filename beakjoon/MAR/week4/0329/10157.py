import sys
sys.stdin = open("10157.txt")

C, R = map(int, input().split())
K = int(input())
x, y, t, i = R-1, 0, 1, 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
grid = [[0] * C for _ in range(R)]
width = R * C
F = False
while t <= width:
    if t == K:
        F = True
        break
    grid[x][y] = t

    t += 1
    nx, ny = x + dx[i], y + dy[i]
    if not(0 <= nx < R and 0 <= ny < C) or grid[nx][ny]:
        i += 1
    if i >= 4:
        i = 0
    x, y = x + dx[i], y + dy[i]

if F:
    print(y+1, R-x)
else:
    print(0)
