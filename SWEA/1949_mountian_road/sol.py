import sys
sys.stdin = open('input.txt', 'r')
#########################################
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def dfs(x, y, depth, z):
    global ans
    visited[x][y] = True
    for dx, dy in dxy:
        nx, ny = x+dx, y+dy
        if not(0 <= nx < N and 0 <= ny < N): continue
        if visited[nx][ny]: continue
        temp1, temp2 = grid[nx][ny], grid[x][y]
        if temp1 >= temp2 and z:
            if temp1 - temp2 + 1 <= z:
                grid[nx][ny] = temp2 - 1
                dfs(nx, ny, depth+1, 0)
                grid[nx][ny] = temp1
            pass
        if temp1 < temp2:
            dfs(nx, ny, depth+1, z)
    ans = max(ans, depth)
    visited[x][y] = False


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    max_height, ans = 0, 0
    for i in range(N):
        max_height = max(max_height, max(grid[i]))

    peaks = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] != max_height:
                continue
            peaks.append([i, j])

    for i, j in peaks:
        visited = [[False] * N for _ in range(N)]
        dfs(i, j, 1, K)

    print(f'#{tc}', ans)
