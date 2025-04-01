import sys
sys.stdin = open("input.txt", "r")


def f(now, battery, area, cnt=0):
    global result
    # 최소값보다 커지는 경우 백트래킹
    if result < battery:
        return
    # 마지막 선택일 때 1로 보낸다.
    if cnt == N-1:
        f(0, battery + e[now][0], area, cnt+1)
        return

    if cnt == N:    # 종료조건 => 최소값 갱신
        result = min(result, battery)
        return
    for i in range(N):
        # 이미 지나간 곳 제외, 현재 위치도 제외
        if area[i]: continue
        if i == now: continue

        area[now] = True
        f(i, battery + e[now][i], area, cnt + 1)
        area[now] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]
    temp = [False] * N
    result = float('inf')
    f(0, 0, temp)
    print(f'#{tc}', result)
