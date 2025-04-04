import sys
sys.stdin = open("input.txt", "r")


def f(n, a, b):
    trianlge = []
    for i in range(N+1):
        ni = i - 1
        temp = []
        for j in range(i+1):
            nj = j - 1
            if ni < 0 or nj < 0 or j > ni:
                temp.append(1)
                continue
            temp.append(trianlge[ni][nj] + trianlge[ni][j])
        trianlge.append(temp)
    # print(*trianlge, sep='\n')
    if a == b:
        return trianlge[n][n//2]
    elif n == a or n == b:
        return trianlge[n][0]
    else:
        return trianlge[n][a]


T = int(input())
for tc in range(1, T+1):
    N, A, B = map(int, input().split())
    ans = f(N, A, B)
    print(f'#{tc}', ans)
