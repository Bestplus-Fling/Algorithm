import sys
sys.stdin = open('input.txt', 'r')
####################################

from collections import deque


T = 10
# stack 에 값을 추가하고 +가 나오면 앞에 두개를 pop, 더해서 다시 추가
for tc in range(1, T+1):
    t = int(input())
    queue = deque(map(int, input().split()))
    # queue = list(map(int,input().split()))
    ans = 1
    while queue[-1] != 0: # queue 마지막 값이 0이 될 때까지 반복
        queue[0] - ans
        if ans < 6: # cnt의 값이 6미만이라면 +1
            ans += 1
        else: # 5초과라면 1로 초기화
            ans = 1
        queue.rotate(-1) # queue[0]의 값에서 cnt를 뺀 값을 맨 뒤로 보냄
    print(queue)