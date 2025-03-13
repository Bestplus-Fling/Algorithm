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
        if not Flag:
            x, y, dp = stack[-1]
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if not(0 <= nx < N and 0 <= ny < N):
                    continue
                if arr[nx][ny] == arr[x][y] + 1:
                    # if visited[nx][ny] > 0:
                    #     dp += visited[nx][ny]
                    #     continue
                    stack.append((nx, ny, dp+1))
                    break
            else:
                if depth < dp:
                    number = st
                    depth = dp
                elif depth == dp:
                    if st < number:
                        number = st
                Flag = True

        else:
            vx, vy, temp = stack.pop()
            visited[vx][vy] = t
            t += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(N)
    arr = [list(map(int, input().split())) for _ in range(N)]
    number, depth = 1001, 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                delta(i, j, arr[i][j])
    # if tc == 17 or tc == 23:
    #     for i in range(N):
    #         print(arr[i])
    #     print()
    #     for i in range(N):
    #         print(visited[i])
    print(f'#{tc}', number, depth)