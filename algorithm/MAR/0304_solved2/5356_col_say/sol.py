import sys
sys.stdin = open('input.txt', 'r')
#####################################

T = int(input()) # test case개수를 받아오는 코드
for tc in range(1, T+1):
    N = 5
    arr = [list(input()) for _ in range(N)]
    _len = 0
    ans = ''
    for _ in range(N):
        _len = max(_len, len(arr[_]))

    for i in range(_len):
        for j in range(N):
            if len(arr[j]) <= i:
                continue
            ans += arr[j][i]
    print(f'#{tc}', ans)
