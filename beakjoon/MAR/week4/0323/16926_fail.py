import sys
sys.stdin = open("16926.txt")

N, M, R = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dxy = [0, 1], [1, 0], [0, -1], [-1, 0]
cnt = 0
while R != cnt:
    tx, bx, ty, by = 0, N, 0, M
    x, y = 0, 0
    sx, sy = 0, 0
    while tx < bx and ty < by:
        Flag = False
        for dx, dy in dxy:
            while True:
                if x+dx == sx and y+dy == sy:
                    Flag = True
                    break
                nx, ny = x + dx, y + dy
                if not(tx <= nx < bx and ty <= ny < by):
                    break
                arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
                x, y = nx, ny
            if Flag:
                break
        tx, ty, bx, by = tx+1, ty+1, bx-1, by-1
        sx, sy = sx+1, sy+1
        x, y = sx, sy
    cnt += 1
for i in arr:
    print(*i)




