import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0
    for y in range(0, N):
        for x in range(0, M):
            rng = (arr[y][x])
            temp = 0 - rng
            for i in range(x-rng, rng+x+1):
                if 0 <= i < M:
                    temp += arr[y][i]
            for i in range(y-rng, rng+y+1):
                if 0 <= i < N:
                    temp += arr[i][x]
            if max_num < temp:
                max_num = temp
    print(f'#{tc} {max_num}')
