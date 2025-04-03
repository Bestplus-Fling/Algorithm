import sys
sys.stdin = open("input.txt", "r")


def dfs(num, depth, join_num):
    global ans, time, check

    if depth == time:
        ans = max(join_num, ans)
        return

    for i in range(N):
        for j in range(i+1, N):
            num[i], num[j] = num[j], num[i]
            temp = int("".join(num))
            if (temp, depth) not in check:
                dfs(num, depth+1, temp)
                check.add((temp, depth))
            num[i], num[j] = num[j], num[i]


T = int(input())
for tc in range(1, T+1):
    nums, time = input().split()
    nums = list(nums)
    N = len(nums)
    time = int(time)
    ans = 0
    check = set()
    dfs(nums, 0, ans)
    print(f'#{tc}', ans)
