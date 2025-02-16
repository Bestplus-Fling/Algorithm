import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    # A의 길이 N과 B의 길이 M을 입력
    N, M = map(int, input().split())
    if N >= M:
        iter_range = N - M+1
    else:
        iter_range = M - N+1
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    for i in range(iter_range):

        pass
    pass