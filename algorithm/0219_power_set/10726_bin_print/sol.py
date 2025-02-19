import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    bin_list = []
    while M > 1:
        bin_list.append(M % 2)
        M //= 2
    bin_list.append(1 if M == 1 else 0)
    count = 0
    for i in range(N):
        count += 1 if len(bin_list) >= N and bin_list[i] else 0
    print(f'#{tc}', 'ON' if count == N else 'OFF')
