import sys
sys.stdin = open('input.txt', 'r')
#########################################
from collections import deque

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 주차 위치별 요금
    parking_area = [[_ + 1, int(input()), 0] for _ in range(N)]
    # 차량 별 무게
    car_weight = [int(input()) for _ in range(M)]
    wait, is_parking = deque(), 0
    ans = 0
    locate = [None] * M
    for i in range(M*2):
        inout = int(input())
        # 입차
        if inout > 0:
            if is_parking == N:
                wait.append(inout)
                continue
            for j in range(N):
                if parking_area[j][2] == 0:
                    # 가장 앞에 있는 자리에 매칭해준다
                    parking_area[j][2] = inout
                    locate[inout-1] = j
                    is_parking += 1
                    break

        # 출차
        elif inout < 0:
            # 요금을 계산한다.
            inout = abs(inout)-1
            loc = locate[inout]
            parking_area[loc][2]
            is_parking -= 1
            parking_area[loc][2] = 0
            ans += parking_area[loc][1] * car_weight[inout]

            # 기다리던 차량이 있다면 우선 입차
            if wait:
                temp = wait.popleft()
                parking_area[loc][2] = temp
                locate[temp-1] = loc
                is_parking += 1
    print(f'#{tc}', ans)


"""
주차 공간 중 번호가 가장 작은 주차공간에 주차하도록 한다.
만약 주차를 기다리는 차량이 여러 대라면, 입구의 대기 장소에서 자기 차례를 기다려야 한다(선입선출)
=> 큐를 사용(deque)
주차 요금은 차량의 무게와 주차 공간마다 따로 책정된 단위 무게당 금액을 곱한 가격이다.

"""

"""
주차 자리마다 무게당 요금이 다름
우선순위 큐에서는 주차자리(인덱스, 무게당 요금)을 관리
우선순위 큐에 데이터가 없으면 나머지 차량은 입차 대기
PQ에 데이터가 생기면 대기중인 차 맨 앞에 있는
"""