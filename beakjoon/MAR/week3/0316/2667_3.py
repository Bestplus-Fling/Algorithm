import sys
sys.stdin = open('input/2667.txt', 'r')

dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def dfs(x, y, depth=0):
    stack = [[x, y]]
    cnt = 1
    while stack:
        x, y = stack[-1]
        visited[x][y] = 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < N):
                continue
            if visited[nx][ny]:
                continue
            if complex_apartment[nx][ny] == 0:
                continue
            stack.append([nx, ny])
            cnt += 1
            break
        else:
            stack.pop()
    return cnt
    # global count
    # count += 1
    # visited[x][y] = 1
    # for dx, dy in dxy:
    #     nx, ny = x + dx, y + dy
    #     if not(0 <= nx < N and 0 <= ny < N):
    #         continue
    #     if visited[nx][ny]:
    #         continue
    #     if complex_apartment[nx][ny] == 0:
    #         continue
    #     # depth = dfs(nx, ny, depth+1)
    #     dfs(nx, ny)
    # # return depth


N = int(input())
complex_apartment = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
count = 0
result = []
for i in range(N):
    for j in range(N):
        if visited[i][j] or complex_apartment[i][j] == 0:
            continue
        result.append(dfs(i, j))
        # dfs(i, j)
        # result.append(count)
        # count = 0
result.sort()
print(len(result), *result, sep='\n')