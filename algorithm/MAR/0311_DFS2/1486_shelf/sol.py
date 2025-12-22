import sys
sys.stdin = open('input.txt', 'r')
#####################################


def dfs(idx, h):
    global res
    # 백트레킹 -> 현재 탐색중인 해가 최소값보다 커진 순간 -> 더 볼 필요 없음
    if h > res:
        return
    # 모든 선택이 완료됐을 때
    if idx == N:
        # 최소차를 갱신한다.
        if h >= B:
            res = min(res, h)
        return
    # 사람을 선택했을 때의 경우
    dfs(idx+1, h+arr[idx])
    # 선택하지 않았을 때의 경우
    dfs(idx+1, h)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    res = float('inf')
    dfs(0, 0)
    print(f'#{tc}', res-B)
