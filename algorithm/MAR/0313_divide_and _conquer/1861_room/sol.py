import sys
sys.stdin = open('input.txt', 'r')
#####################################
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def delta(x, y, st):
    global number, depth
    stack = []
    stack.append((x, y, 1))
    Flag = False
    t = 1
    while stack:
        # 이미 지나온 경로가 없으면 델타탐색으로 이동할 좌표를 저장
        if not Flag:
            x, y, dp = stack[-1]
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if not(0 <= nx < N and 0 <= ny < N):
                    continue
                if arr[nx][ny] != arr[x][y] + 1:
                    continue
                if visited[nx][ny] > 0:
                    dp += visited[nx][ny]
                    t = dp
                    continue
                stack.append((nx, ny, dp+1))
                break
            else:
                # 가장 긴 거리를 가지는 방 중 번호가 가장 작은 방을 저장
                if depth < dp:
                    number = st
                    depth = dp
                elif depth == dp:
                    if st < number:
                        number = st
                # 델타탐색 정상 종료시 이동 가능한 방이 없다는 의미
                Flag = True
        # 스택 POP 하면서 왔던 경로의 길이를 저장
        else:
            vx, vy, temp = stack.pop()
            visited[vx][vy] = t
            t += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    number, depth = 1001, 0
    visited = [[0] * N for _ in range(N)]
    # 탐색한 적 없는 방만 찾아서 시작
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                delta(i, j, arr[i][j])

    print(f'#{tc}', number, depth)
