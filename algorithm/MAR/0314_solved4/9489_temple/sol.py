import sys
sys.stdin = open('input.txt', 'r')
#####################################
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def delta(i, j):
    for di, dj in dxy:
        ni, nj = i + di, j + dj
        if not (0 <= ni < N and 0 <= nj < M) or arr[ni][nj] == '0':
            continue
        dist(i, j, di, dj)


def dist(x, y, dx, dy):
    global result
    cnt = 0
    while True:
        if not(0 <= x < N and 0 <= y < M) or arr[x][y] == '0':
            break
        cnt += 1
        x, y = x + dx, y + dy
    result = max(result, cnt)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().split() for _ in range(M)]

    print(arr)
    result = 0
    # 1을 찾은 위치에서 나아갈 방향을 정한 후에 진행
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '1':
                delta(i, j)
    print(f"#{tc}", result)
