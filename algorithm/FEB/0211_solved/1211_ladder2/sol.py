import sys

sys.stdin = open('input.txt', 'r')
#########################################

dxy = [[1, 0], [0, -1], [0, 1]]


def search_ladder(x, y):
    count = 0
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    while x != N-1:
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            # print(f"{a}, {j}, 좌{visited[x][y-1]}, 우{visited[x][y+1]}, 아래{visited[x-1][y]}")
            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] and not visited[nx][ny]:
                visited[x][y] = 1
                x, y = nx, ny
                count += 1
        if count > cnt_short:
            return N*N
    return count


T = 10
for tc in range(1, T + 1):
    a = int(input())
    N = 100
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 가장 짧은 경로의 index를 저장
    cnt_short = N*N
    short_root = 0
    # 첫 열에서 시작지점 탐색
    for j in range(N):
        # 시작지점에 도달하면 함수 호출
        if matrix[0][j] == 1:
            result = search_ladder(0, j)
            # print(result)
            if cnt_short > result:
                short_root = j
                cnt_short = result
    print(f'#{a} {short_root}')