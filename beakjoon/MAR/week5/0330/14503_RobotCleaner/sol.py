import sys
sys.stdin = open('input.txt', 'r')
#########################################
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


# 조건용 함수
def check(x, y):
    global d
    cnt = 0
    for dx, dy in dxy:
        nx, ny = x+dx, y+dy
        if grid[nx][ny]: continue
        cnt += 1

    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if cnt == 0:
        gx, gy = dxy[d]
        nx, ny = x+gx, y+gy
        # 2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        if grid[nx][ny] == 1:
            return [x, y]
        # 1. 바라보는 방향을 유지한 채로 한칸 후진, 1번으로 돌아간다.
        return [nx, ny]

    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    else:
        for _ in range(4):
            # 1. 반시계 방향으로 회전
            d = (d-1 if d != 0 else 3)
            gx, gy = dxy[d]
            nx, ny = x-gx, y-gy
            # 2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸이 경우 한칸 전진.
            if grid[nx][ny]: continue
            # 3. 1번으로 이동
            return [nx, ny]


def clean(x, y):
    cnt = 0
    while True:
        if grid[x][y] == 0:
            grid[x][y] = 2
            cnt += 1
        cx, cy = check(x, y)
        if cx == x and cy == y:
            break
        x, y = cx, cy
    return cnt


N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(clean(r, c))
