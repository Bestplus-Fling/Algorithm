import sys
sys.stdin = open("input.txt", "r")


def subset(start, num_sum, check):
    global result
    if start == N:
        return
    if num_sum == K:
        result += 1
        return
    for i in range(start, N):
        if check[i]: continue
        check[i] = True
        subset(start+1, num_sum+data[i], check)
        check[i] = False


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    temp = [False] * N
    result = 0
    subset(0, 0, temp)
    print(f'#{tc}', result)
