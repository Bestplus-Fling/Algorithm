import sys
sys.stdin = open('input.txt', 'r')
#####################################

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prev_switches = list(map(int, input().split()))
    next_switches = list(map(int, input().split()))

    result = 0

    # 주어진 현재 스위치를 순회하면서, 목표 스위치와 같은 상태인지 비교한다
    for i in range(N):
        # 같은 상태라면 skip
        if prev_switches[i] == next_switches[i]:
            continue
        # 다른 경우, 누르는 logic 작성
        result += 1
        for j in range(i, N):
            prev_switches[j] = 1 - prev_switches[j]


    print(f"#{tc} {result}")