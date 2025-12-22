import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    # N자리 16진수(_hex)를 입력
    N, _hex = input().split()
    # 정수형으로 변환
    N = int(N)
    # hex -> decimal로 변환
    _dec = int(_hex, 16)
    # decimal -> binary 로 변환한 형태를 저장
    bin_list = []
    # decimal 을 2로 나누면서 binary 를 생성
    while _dec >= 1:
        bin_list.append(str(_dec % 2))
        _dec //= 2
    # 4자리씩 끊어져야 하므로 공란에 0을 채운다.
    while len(bin_list) % 4 != 0:
        bin_list.append(str(0))
    # 현재 bin_list에는 거꾸로 추가된 2진 형태이기 때문에 출력 전 reversed 를 통해 출력값을 맞춘다.
    print(f'#{tc}', ''.join(list(reversed(bin_list))))


