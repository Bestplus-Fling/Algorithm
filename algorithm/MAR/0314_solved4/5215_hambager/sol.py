import sys
sys.stdin = open('input.txt', 'r')
#####################################


def dfs(idx=0, ts=0, ks=0):
    global result
    if ks > K:
        return
    if idx == N:
        result = max(result, ts)
        return
    dfs(idx+1, ts+t_list[idx][0], ks+t_list[idx][1])
    dfs(idx+1, ts, ks)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    t_list = [tuple(map(int, input().split())) for _ in range(N)]
    result = 0
    dfs()

    print(f'#{tc}', result)
