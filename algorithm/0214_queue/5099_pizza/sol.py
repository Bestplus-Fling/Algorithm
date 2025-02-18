import sys
sys.stdin = open('input.txt', 'r')
#########################################
from collections import deque

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    oven = deque()
    i = 0
    # 모든 피자치즈가 0이 아니거나 오븐에 데이터가 있을 때
    while pizza.count(0) != M or oven:
        # oven에 피자가 가득 차있을 때
        if len(oven) >= N or pizza.count(0) == M:
            # 가장 먼저 들어간 피자를 꺼내면서 //2 연산
            output, idx = oven.popleft()
            output = output // 2
            # 치즈가 0이 아니면 오븐에 다시 넣는다.
            if output != 0:
                oven.append((output, idx))
            # 치즈가 0이 되면 버림(아무것도 안함)
            continue

        # 피자위 치즈가 0이 아니면
        if pizza[i] != 0 and len(oven) < N:
            oven.append((pizza[i], i))
            pizza[i] = 0
        i += 1
        if i == M:
            i = 0

    print(f'#{tc} {idx + 1}')

