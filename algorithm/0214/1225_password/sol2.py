import sys
sys.stdin = open('input.txt', 'r')
#########################################

from collections import deque

T = 10  # int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    password = deque(map(int, input().split()))
    i = 1
    while password[-1] != 0:
        temp = password.popleft()
        temp -= i
        if temp <= 0:
            password.append(0)
            continue
        password.append(temp)
        i += 1
        if i == 6:
            i = 1

    print(f'#{N}', *password)
