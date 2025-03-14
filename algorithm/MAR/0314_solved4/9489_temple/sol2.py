import sys
sys.stdin = open('input.txt', 'r')
#####################################

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    result = 0
    for i in range(N):
        arr.append(input().split())
        cnt = 0
        for j in range(M):
            if arr[i][j] == '1':
                cnt += 1
            if (arr[i][j] == '0' or j == M-1) and cnt:
                result = max(cnt, result)
                cnt = 0

    for j in range(M):
        cnt = 0
        for i in range(N):
            if arr[i][j] == '1':
                cnt += 1
            if (arr[i][j] == '0' or i == N-1) and cnt:
                result = max(cnt, result)
                cnt = 0
    print(f'#{tc}', result)