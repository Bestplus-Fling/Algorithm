import sys
sys.stdin = open('input.txt', 'r')
#########################################

from collections import deque
# 진기야 장사 접자 ㅇㅈ
T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customer_arrive = deque(map(int, input().split()))
    i = 0
    # print(*customer_arrive)
    bread = 0
    impos_or_pos = False
    while customer_arrive:
        # 진기는 붕어빵을 M초마다 K개만큼 만든다
        if i != 0 and i % (M) == 0:
            bread += K
        # 손님이 도착할 시간(customer_arrive[0]) == i라면 손님이 도착한 것
        if customer_arrive[0] == i:
            # 근데 빵이 없으면 불가능
            if bread == 0:
                break
            # 빵이 있다면 빵 개수 차감하고 고객 가장 처음 값 삭제
            else:
                bread -= 1
                customer_arrive.popleft()
        i += 1

        # 그런데 bread가 0이라면 손님에게 붕어빵을 줄 수 없으므로 break후 impos_or_pos에 True False를 할당
        # 그러면 i가 deque[0]값이랑 일치할 때 진기가 붕어빵을 만들었는지 확인
        # 만들었다면 붕어빵 개수에서 -1 차감
    if len(customer_arrive) == 0:
        impos_or_pos = True

    print(f'#{tc}', end=' ')

    if impos_or_pos == True:
         print("Possible")
    else:
        print("Imossible")

    break
    pass
