import sys
sys.stdin = open("2567.txt")
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = 100
grid = [[0] * N for _ in range(N)]
K = int(input())
for _ in range(K):
    r1, c1 = map(int, input().split())
    r1, c1 = r1-1, c1-1
    i, cnt, n = 0, 0, 0

    if grid[c1][r1] == 0:
        Flag = False
        grid[c1][r1] = 1
        cnt += 1
    else:
        Flag = True

    r2, c2 = r1 + 11, c1 + 11
    x, y = c1+1, r1

    while cnt < 40:
        if not Flag:
            grid[x][y] = 1
            cnt += 1
        if x == c1 and y == r1:
            break

        if (x+dx[i] >= c2 or y+dy[i] >= r2) or (x+dx[i] < c1 or y+dy[i] < r1):
            i += 1
        if i >= 4:
            i = 0
        nx, ny = x + dx[i], y + dy[i]

        if Flag and grid[nx][ny] and grid[x][y] == 0:
            Flag = False
        if grid[nx][ny]:
            Flag = True


        x, y = nx, ny
    print(cnt)

print(*grid, sep='\n')


