import sys
sys.stdin = open("im.txt", "r")

# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
dxy = [1, 0], [0, 1], [-1, 0], [0, -1]


def delta():
    count = 0
    x, y = i, j
    while True:
        a = []
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if not(0 <= nx < N and 0 <= ny < N) or not(arr[x][y] > arr[nx][ny]):
                continue
            a.append((arr[nx][ny], nx, ny))
        if a:
            a.sort()
            temp, x, y = a[0]
            count += 1
            continue
        else:
            break
    return count+1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            max_cnt = max(max_cnt, delta())

    print(f'#{tc} {max_cnt}')
