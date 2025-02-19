import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, _hex = input().split()
    N = int(N)
    _dec = int(_hex, 16)
    # print(_dec)
    bin_list = []
    while _dec >= 1:
        bin_list.append(str(_dec % 2))
        _dec //= 2
    while len(bin_list) % 4 != 0:
        bin_list.append(str(0))
    print(f'#{tc}', ''.join(list(reversed(bin_list))))


