import sys
sys.stdin = open("input.txt", "r")
#########################################
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
check = {
    1: {0: 2, 1: 3, 2: 1, 3: 0},
    2: {0: 1, 1: 3, 2: 0, 3: 2},
    3: {0: 3, 1: 2, 2: 0, 3: 1},
    4: {0: 2, 1: 0, 2: 3, 3: 1},
}


def bfs(x, y):
    global ans
    queue = deque()
    visited = [[False] * N for _ in range(N)]
    for k in range(4):
        queue.append([x, y, k, 0])
    visited[x][y] = True
    while queue:
        # print(queue)
        x, y, d, cnt = queue.popleft()

        # 종료조건 : 게임 시작위치 or 블랙홀(-1)
        if cnt != 0 and ((i, j) == (x, y) or data[x][y] == -1):
            ans = max(ans, cnt)
            continue

        # 블럭(1~4)를 만났을 때, 진행방향을 확인하고 방향을 변경
        if 1 <= data[x][y] < 5:
            td = check[data[x][y]][d]
            if not(0 <= x + dx[td] < N and 0 <= y + dy[td] < N):
                pass
            else:
                queue.append([x + dx[td], y + dy[td], td, cnt+1])
                visited[x + dx[td]][y + dy[td]] = True
        # 웜홀을 만나면 같은 번호의 웜홀을 확인한다.(점수 포함 x)
        elif data[x][y] >= 6:
            fx, fy = hole[(x, y)]
            if not(0 <= fx + dx[d] < N and 0 <= fy + dy[d] < N):
                # 웜홀 넘어서 한칸 더가면 벽일 경우 벽 맞고 그대로 돌아온 경우로 산정
                # cnt += 1 / 좌표는 방향 바꾸고 한칸 건너서 queue 삽입
                fd = (d+2) % 4
                queue.append([x + dx[fd], y + dy[fd], d, cnt+1])
                visited[x + dx[d]][y + dy[d]] = True
            else:
                queue.append([fx + dx[d], fy + dy[d], d, cnt])
                visited[fx + dx[d]][fy + dy[d]] = True
        else:
            nx, ny = x + dx[d], y + dy[d]
            if not(0 <= nx < N and 0 <= ny < N) or data[x][y] == 5:
                td = (d+2) % 4
                queue.append([x+dx[td], y+dy[td], td, cnt+1])
                visited[x+dx[td]][y+dy[td]] = True
                continue
            queue.append([nx, ny, d, cnt])
            visited[nx][ny] = True
        # 벽 혹은 블럭5 인 경우 진행 방향과 반대로 이동
    print(*visited, sep='\n')
    print(ans, f'{i},{j}')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    location = []
    temp = [[] for _ in range(5)]
    hole = {}
    for i in range(N):
        for j in range(N):
            if data[i][j] == 0:
                location.append([i, j])
            elif data[i][j] >= 6:
                temp[(data[i][j] % 6)].append((i, j))
    for t in temp:
        if not t: continue
        axy, bxy = t
        hole[axy] = bxy
        hole[bxy] = axy
    for i, j in location:
        bfs(i, j)
    print(f'#{tc}', ans)
    break