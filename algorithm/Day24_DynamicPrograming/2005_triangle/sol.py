import sys
sys.stdin = open("input.txt", "r")


def f(n):
    global ans
    for i in range(N):
        temp = []
        ni = i - 1
        for j in range(i+1):
            nj = j - 1
            if not(0 <= ni and 0 <= nj and j < i):
                temp.append(1)
                continue
            temp.append(ans[ni][nj] + ans[ni][j])
        ans.append(temp)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = []
    f(N)
    print(f'#{tc}')
    for i in ans:
        print(*i)
