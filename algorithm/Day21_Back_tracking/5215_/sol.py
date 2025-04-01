import sys
sys.stdin = open("input.txt", "r")


def select(i, cal, taste):
    global result
    # 제한 칼로리 초과시 백트래킹
    if L < cal:
        return

    if i == N:  # 종료조건 => 최대값 갱신
        result = max(result, taste)
        return
    # 재료를 선택했을때와, 선택하지 않았을 때를 구분
    select(i+1, cal + case[i][1], taste + case[i][0])
    select(i + 1, cal, taste)


T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    case = [tuple(map(int, input().split())) for _ in range(N)]
    result = 0
    select(0, 0, 0)
    print(f'#{tc}', result)
