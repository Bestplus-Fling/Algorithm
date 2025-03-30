import sys
sys.stdin = open('input.txt', 'r')
#########################################
from collections import deque
dxy = [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]


def bfs(x, y):
    queue = deque([[x, y]])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        cnt = 0
        temp = []
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N): continue
            if grid[nx][ny] == "*":
                cnt += 1
                visited[nx][ny] = True
                continue
            if visited[nx][ny]: continue
            if grid[nx][ny] != '.': continue
            temp.append([nx, ny])
        grid[x][y] = cnt
        if not cnt:
            queue.extend(temp)
            for r, c in temp:
                visited[r][c] = True

# check = []
T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    grid = [list(input().strip()) for _ in range(N)]

    visited = [[False] * N for _ in range(N)]
    zero, ans = [], 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '*': continue
            if visited[i][j]: continue
            # 0인 점에 한해서 8방향을 모두 탐색한다.
            for di, dj in dxy:
                ni, nj = i + di, j + dj
                if not(0 <= ni < N and 0 <= nj < N): continue
                if grid[ni][nj] == '*': break
            else:
                zero.append([i, j])
    for i, j in zero:
        if visited[i][j]:
            continue
        bfs(i, j)
        ans += 1

    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.':
                ans += 1
    # print(*grid, sep='\n', end='\n\n')
    # print(*visited, sep='\n', end='\n\n')
    print(f'#{tc}', ans)
    # check.append(f'#{tc} {ans}')

# re = [
#     '#1 1990',
#     '#2 1574',
#     '#3 1252',
#     '#4 1080',
#     '#5 7645',
#     '#6 6378',
#     '#7 5073',
#     '#8 4093',
#     '#9 17111',
#     '#10 14683',
#     '#11 11693',
#     '#12 9135',
#     '#13 30616',
#     '#14 26184',
#     '#15 20124',
#     '#16 15225',
#     '#17 48378',
#     '#18 39769',
#     '#19 31522',
#     '#20 24196',
# ]
#
# for k in range(1, T+1):
#     if re[k-1] == check[k-1]:
#         print(f'{k}번 정답')
#     else:
#         print(f'{k}번 오답')