import sys
sys.stdin = open("16926.txt")

N, M, R = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().split()) for _ in range(N)]
tx, bx, ty, by = 0, N, 0, M
t = 0
while tx < bx and ty < by:
    # 바깥 길이를 계산해서 r // 배열이 한바퀴 도는 데 걸리는 횟수
    # 이걸로 while문 순회
    cnt = 0
    while R != cnt:
        a, c, c, d = [], [], [], []
        for i in range(ty+1, by):
            a.append(arr[tx][i])
            t += 1

        for i in range(tx, bx-1):
            c.append(arr[i][ty])
            t += 1
        for i in range(ty, by-1):
            c.append(arr[bx-1][i])
            t += 1
        for i in range(tx+1, bx):
            d.append(arr[i][by-1])
            t += 1
        for j, i in enumerate(range(ty, by-1)):
            arr[tx][i] = a[j]
            arr[bx-1][i+1] = c[j]
            t += 1
        for j, i in enumerate(range(tx, bx-1)):
            arr[i+1][ty] = c[j]
            arr[i][by-1] = d[j]
            t += 1
        cnt += 1
    tx, ty, bx, by = tx+1, ty+1, bx-1, by-1
for i in arr:
    print(*i)
print(t)