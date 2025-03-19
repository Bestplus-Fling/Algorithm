import sys
sys.stdin = open('input.txt', 'r')
#########################################
from collections import deque
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]
check = {
    (0, -1): ['1', '3', '4', '5'],
    (0, 1): ['1', '3', '6', '7'],
    (-1, 0): ['1', '2', '5', '6'],
    (1, 0): ['1', '2', '4', '7'],
}


def bfs(x, y):
    queue = deque([[x, y, 0]])
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1
    count = 0
    while queue:
        x, y, t = queue.popleft()
        if t >= L:
            continue
        count += 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < M): continue   # 범위를 벗어날 때
            if arr[nx][ny] == '0': continue     # 터널 구조물이 아닐 때
            if visited[nx][ny]: continue        # 이미 방문한 적 있을 때
            now_pipetype = arr[x][y]
            next_pipetype = arr[nx][ny]
            if now_pipetype in check[(-dx, -dy)] and next_pipetype in check[(dx, dy)]:
                queue.append([nx, ny, t+1])
                visited[nx][ny] = 1
    return count


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    #가로 M, 세로 N, 시작 좌표 R,C 시간 L
    N, M, R, C, L = map(int, input().split())
    arr = [list(input().split()) for _ in range(N)]
    ans = bfs(R, C)
    print(f'#{tc}', ans)
