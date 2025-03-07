import sys
sys.stdin = open('input.txt', 'r')
#####################################

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    default = list(map(int, input().split()))
    ans = list(map(int, input().split()))
    switch = default[0]
    count = 0
    for idx in range(N):
        if ans[idx] == default[idx]:
            continue
        for next in range(idx, N):
            default[next] = 1 - default[next]
        count += 1
    print(f'#{tc}', count)


