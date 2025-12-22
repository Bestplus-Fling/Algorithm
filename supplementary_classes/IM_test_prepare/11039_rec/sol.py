import sys
sys.stdin = open("input.txt")


# 사각형의 범위를 확인(W, H는 각각 사각형의 너비와 높이를 저장)
def check_rec(x, y):
    W, H = 0, 0
    w, h = y, x
    while matrix[x][w]:
        W += 1
        w += 1
        if w >= N:
            break
    while matrix[h][y]:
        H += 1
        h += 1
        if h >= N:
            break
    # 사각형의 넓이를 반환
    return W * H


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # print(matrix)
    max_range = 0
    # 사각형의 시작 위치를 확인, 함수를 호출
    for i in range(N):
        for j in range(N):
            if matrix[i][j]:
                temp = check_rec(i, j)
                # 최대값 저장
                max_range = max(temp, max_range)
    print(f'#{tc}', max_range)
