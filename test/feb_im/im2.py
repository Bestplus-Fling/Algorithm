import sys
sys.stdin = open("im.txt", "r")

# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
dxy = [1, 0], [0, 1], [-1, 0], [0, -1]


def delta(x, y):
    none_move = 4
    a = []
    for dx, dy in dxy:
        # count = 0
        nx = x + dx
        ny = y + dy
        if not(0 <= nx < N and 0 <= ny < N) or not(arr[x][y] > arr[nx][ny]):
            none_move -= 1
            if none_move == 0:
                break
            continue
        none_move = 4
        a.append((delta(nx, ny)))
    if not a:
        return 1
    else:
        return max(a)+1



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            max_cnt = max(max_cnt, delta(i, j)-1)
            # for ux, uy in dxy:
            #     ni = i + ux
            #     nj = j + uy
            #     if not (0 <= ni < N and 0 <= nj < N) or not(arr[i][j] < arr[ni][nj]):
            #         continue

    print(f'#{tc} {max_cnt}')