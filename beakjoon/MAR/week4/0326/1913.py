import sys
sys.stdin = open("1913.txt")

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())
num = int(input())
arr = [[0]*N for _ in range(N)]

x, y, i = -1, 0, 0
k = N*N

while k != 0:
    if i >= 4:
        i = 0

    x, y = x + dx[i], y + dy[i]
    arr[x][y] = k

    if k == num:
        R, C = x, y
    k -= 1
    nx, ny = x+dx[i], y+dy[i]

    if not(0 <= nx < N and 0 <= ny < N):
        i += 1
        # print(*arr, sep='\n', end='\n\n')
        continue
    if arr[nx][ny]:
        i += 1

        continue
for i in arr:
    print(*i)
print(R+1, C+1)
