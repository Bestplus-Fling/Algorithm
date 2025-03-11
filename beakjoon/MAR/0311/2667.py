import sys
sys.stdin = open('2667.txt', 'r')
#########################################

dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def dfs(x, y):
    global count
    count += 1
    visited[x][y] = True

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not(0 <= nx < N and 0 <= ny < N):
            continue
        if not matrix[nx][ny] or visited[nx][ny]:
            continue
        dfs(nx, ny)


N = int(input())
matrix = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
ans = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and matrix[i][j]:
            count = 0
            dfs(i, j)
            ans.append(count)
print(len(ans))
for k in sorted(ans):
    print(k)
