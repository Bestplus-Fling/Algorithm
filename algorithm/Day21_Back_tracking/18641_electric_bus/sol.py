import sys
sys.stdin = open("input.txt", "r")


def f(i, battery, cnt):
    global result
    # 최소값 초과시 백트래킹
    if cnt > result:
        return
    if N-1 <= i:    # 종료조건 => 최소값 갱신
        result = min(result, cnt)
        return

    # 지금 교환해서 끝까지 갈 수 있으면
    if charge[i] >= N-i-1:
        f(i + charge[i], charge[i], cnt + 1)
    # 1. 배터리가 있으니까 그냥 간다.
    if battery:
        f(i+1, battery-1, cnt)
    # 2. 배터리가 있어도 교환한다.
    f(i+1, charge[i]-1, cnt+1)


T = int(input())
for tc in range(1, T+1):
    N, *charge = map(int, input().split())
    result = float('inf')
    # 첫번째 정류장에서 배터리 교환은 카운트하지 않는다
    # -> 그냥 두번째부터 확인
    f(1, charge[0]-1, 0)
    print(f'#{tc}', result)
