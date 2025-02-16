import sys
sys.stdin = open('input.txt', 'r')
#########################################

from collections import deque


def arrive_customer():
    i = 0
    bread = 0
    while dequeue:
        # M초마다 K개만큼 제작
        if i != 0 and i % M == 0:
            bread += K
        # 손님이 방문할 시간이 되면 손님 보내기
        while dequeue and dequeue[0] == i:
            # 손님이 왔는데 빵이 없으면 break
            dequeue.popleft()
            bread -= 1
            if bread < 0:
                return False
        i += 1
    if not dequeue:
        return True


def sorting_array():
    for k in range(N):
        for j in range(N-k-1):
            if customer_arrive[j+1] < customer_arrive[j]:
                customer_arrive[j], customer_arrive[j+1] = customer_arrive[j+1], customer_arrive[j]


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customer_arrive = list(map(int, input().split()))
    sorting_array()
    dequeue = deque(customer_arrive)
    result = arrive_customer()
    print(f'#{tc}', end=' ')

    if result:
         print("Possible")
    else:
        print("Impossible")
