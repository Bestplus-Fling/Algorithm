import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    # N: 마지막 비트를 확인하려는 길이 M: 10진수
    N, M = map(int, input().split())
    # DEC -> BIN 변환 후 저장할 리스트
    bin_list = []
    while M > 1:
        # 2로 나눈 나머지를 저장
        bin_list.append(M % 2)
        # 2로 나누고 반복하면서 1 혹은 0일때까지 진행
        M //= 2
    # while문 종료 후 M에 1이 남았을 때 추가하기
    bin_list.append(1 if M == 1 else 0)
    # 마지막 비트가 모두 켜져있을 때를 확인
    count = 0
    for i in range(N):
        # 2진수로 변환한 길이가 탐색범위 N을 넘을 때만 자리를 확인
        count += 1 if len(bin_list) >= N and bin_list[i] else 0
    print(f'#{tc}', 'ON' if count == N else 'OFF')
