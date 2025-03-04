import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    min_num = max_num = sum(arr[0:M])

    for i in range(N-M+1):
        temp = sum(arr[i:M+i])
        if temp > max_num: max_num = temp
        if temp < min_num: min_num = temp

    print(f'#{tc} {max_num - min_num}')


