import sys
sys.stdin = open('input.txt', 'r')
#########################################

from collections import deque


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int ,input().split())
    _list = deque(map(int, input().split()))
    rot_case = M % N
    for _ in range(rot_case):
        temp = _list.popleft()
        _list.append(temp)

    print(f'#{tc} {_list[-N]}')
