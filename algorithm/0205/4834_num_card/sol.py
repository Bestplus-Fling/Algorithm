import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    temp = str(input())
    _dict = {}
    for _ in range(N):
        x = temp[_]
        if x in _dict:
            _dict[x] += 1
        else:
            _dict[x] = 1

    print(max(_dict))
