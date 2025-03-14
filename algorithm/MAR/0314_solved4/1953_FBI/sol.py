"""
터널끼리 연결이 되어 있는 경우 이동이 가능, 탈주범이 있을 수 있는 위치의 개수를 계산
탈주범은 시간당 1의 거리를 움직인다
지하터널의 종류는 7개
1: 상하좌우
2. 상하
3. 좌우
여기부터 엘보우
4. 상 -> 우
5. 하 -> 우
6. 하 -> 좌
7. 상 -> 좌

맨홀 뚜껑의 위치가 주어진다.
1시간 이내일 경우 맨홀 위치에
2시간이 지난 경우 맨홀을 기준으로 1칸 범위 내
4시간이 지나면 터널 종류에 따라 범위를 다르게 할 수 있다.
"""

import sys
sys.stdin = open('input.txt', 'r')
#####################################
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]
check = {
    (-1, 0): [1, 2, 5, 6],
    (1, 0): [1, 2, 4, 7],
    (0, -1): [1, 3, 4, 5],
    (0, 1): [1, 3, 6, 7],
}


def delta(x, y, time):
    visited[x][y] = time
    if time == L:
        return
    pipe = arr[x][y]
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not(0 <= nx < N and 0 <= ny < M) or arr[nx][ny] == 0:
            continue
        if visited[nx][ny]:
            continue
        nxt_pipe = arr[nx][ny]
        if pipe in check[(-dx, -dy)] and nxt_pipe in check[(dx, dy)]:
            delta(nx, ny, time + 1)


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    visited = [[0] * M for _ in range(N)]
    delta(R, C, 1)
    for i in range(N):
        ans += visited[i].count(0)
    print(f'#{tc}', (N*M) - ans)
