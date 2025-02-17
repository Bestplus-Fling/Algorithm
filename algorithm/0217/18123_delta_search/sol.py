import sys
sys.stdin = open('input.txt', 'r')
#########################################


dxy = [0, 1], [1, 0], [-1, 0], [0, -1]

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            temp = 0
            for dx, dy in dxy:
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < N:
                    temp += abs(matrix[nx][ny] - matrix[i][j])
            result += temp
    print(f'#{tc} {result}')
