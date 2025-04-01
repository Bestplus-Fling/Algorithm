import sys
sys.stdin = open("input.txt", "r")


def select(i, factory, cost):
    global result
    # 이미 저장한 최소값보다 큰 경우 백트래킹
    if result < cost:
        return
    if i == N:  # 종료조건 => 최소값 갱신
        result = min(cost, result)
        return

    for j in range(N):  # 공장을 선택
        # 이미 선택한 공장을 제외하고 탐색
        if factory[j]: continue

        factory[j] = True
        select(i+1, factory, cost+data[i][j])
        factory[j] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # 최소값 저장
    result = float('inf')
    temp = [False] * N
    select(0, temp, 0)
    print(f'#{tc}', result)

