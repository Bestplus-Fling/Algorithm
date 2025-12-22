import sys
sys.stdin = open("input.txt")

dxy = [1, 0], [0, 1], [-1, 0], [0, -1]


def razer(x, y):
    for dx, dy in dxy:
        for k in range(N):
            # 상하 좌우로 레이저가 나가는데 벽(1)을 만나면 탐색 종료
            nx, ny = x + dx*k, y + dy*k
            if not(0 <= nx < N and 0 <= ny < N):
                break
            if matrix[nx][ny] == 1:
                break
            matrix[nx][ny] = 2


# 우주괴물의 위치를 확인해서 레이저의 범위를 측정한다
def search_alien():
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                razer(i, j)
                return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 레이저 범위를 확인
    search_alien()
    ans_a = 0
    # 안전지대(0)의 개수를 확인, 출력
    for _ in range(N):
        ans_a += matrix[_].count(0)
    print(f'#{tc}', ans_a)
