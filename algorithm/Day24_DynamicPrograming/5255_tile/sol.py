import sys
sys.stdin = open("input.txt", "r")


def f(n):
    dp = [1, 3, 6]
    if n <= 3:
        return dp[n]
    for i in range(3, n):
        dp.append(dp[i-1] + (dp[i-2] * 2) + dp[i-3])
    return dp[n-1]


for tc in range(1, int(input())+1):
    print(f'#{tc}', f(int(input())))
