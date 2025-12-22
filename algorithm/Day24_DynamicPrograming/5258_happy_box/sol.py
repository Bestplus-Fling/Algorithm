import sys
sys.stdin = open("input.txt", "r")


def f():
    K = [[0] * (N+1) for _ in range(M+1)]
    for i in range(1, M+1):
        for w in range(1, N+1):
            if wt[i-1] <= w:
                K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    print(*K, sep='\n')
    return K[M][N]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    wt, val = [0], [0]
    for k in range(M):
        w, v = map(int, input().split())
        wt.append(w)
        val.append(v)
    print(f'#{tc}', f())