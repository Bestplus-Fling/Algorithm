import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    max_val = 0
    for i in range(N):
        for j in range(M):
            temp = 0
            for dx, dy in dxy:
                ni = i + dx
                nj = j + dy
                if 0 <= ni < N and 0 <= nj < M:
                    temp += arr[ni][nj]
            temp += arr[i][j]
            if max_val < temp:
                max_val = temp
    print(f'#{tc} {max_val}')
