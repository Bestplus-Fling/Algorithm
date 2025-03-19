import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    _list = []
    for i in range(N):
        ans = 0
        for j in range(i+1, N):
            if arr[i] <= arr[j]:
                ans += 1
        _list.append(N - ans - i - 1)
    print(f'#{tc} {max(_list)}')
