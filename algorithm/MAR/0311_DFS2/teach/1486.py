import sys
sys.stdin = open('1486.txt', 'r')
#####################################

"""
부분집합을 구하는 문제
부분집합  => DFS => 안쪽으로 파고 들어서 경우의 수를 찾는다
"""


def dfs(idx, h_sum):
    global res
    if h_sum > res:
        return
    if idx == N:  # 모든 직원을 탐색했을 때
        if h_sum >= B:   # 직원들의 키의 합이 B를 넘을 때
            # 그 중에서 최소값
            res = min(res, h_sum)
            pass
        return
    dfs(idx+1, h_sum+arr[idx])
    dfs(idx+1, h_sum)
    pass



T = int(input())
for tc in range(1, T+1):
    # N: 사람 수, B: 목표 값
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    # 원하는 결과 => B를 넘으면서 최소값
    # 초기값으로는 매우 큰 값은 놔야 한다.
    res = float('inf')

    # 부분집합
    # 1. 재귀함수를 종료학 위한 파라미터
    # - 선택하고 있는 점원의 인덱스(N에 도달하면 재귀를 중단)
    # 2. 누적해서 가져가고 싶은 값
    # - 선택한 점원들의 키의 합
    dfs(0, 0)
    print(f'#{tc} {res - B}')
