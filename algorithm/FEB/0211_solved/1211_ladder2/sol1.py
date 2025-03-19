import sys
sys.stdin = open('input.txt', 'r')
#########################################

dxy = [1, 0], [0, -1], [0, 1]


def ladder_search(x, y=0):
    count_ladder = 0
    visited = [[0] * M for _ in range(M)]
    visited[y][x] = 1
    while y != M - 1:
        for dy, dx in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < M and 0 <= ny < M and ladder[ny][nx] and not visited[ny][nx]:
                visited[y][x] = 1
                count_ladder += 1
                x, y = nx, ny
        if min_way < count_ladder:
            return 1e9
    return count_ladder



T = 10  # int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    M = 100
    ladder = [list(map(int, input().split())) for _ in range(M)]
    idx, min_way = -1, 1e9

    for _ in range(M):
        if ladder[0][_] == 0:
            continue
        ans = ladder_search(_)
        if min_way > ans:
            min_way = ans
            idx = _
    print(f'#{N} {idx}')

