import sys
sys.stdin = open("algo1_sample_in.txt")


def dfs(idx=0, cal_sum=0, cnt=0):
    global ans, min_cnt
    if cnt > min_cnt:
        return
    if idx == N:
        # min_cnt는 항상 최소를 만족, cal_sum은 M보다 크기만 하면 됨
        # 칼로리의 합이 최소칼로리(M) 이상이면서 현재까지 저장된 간식 수보다 작을 경우
        if min_cnt > cnt:
            if cal_sum >= M:
                ans = cal_sum
                min_cnt = cnt
        return
    dfs(idx+1, cal_sum+cals[idx], cnt+1)
    dfs(idx + 1, cal_sum, cnt)


# 무게를 최소로, M칼로리 이상, 가장 적게 간식을 선택한 경우의 합
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cals = list(map(int, input().split()))
    ans = float('inf')
    min_cnt = float('inf')
    dfs()
    if ans == float('inf'):
        ans = -1
    print(f'#{tc}', ans)
