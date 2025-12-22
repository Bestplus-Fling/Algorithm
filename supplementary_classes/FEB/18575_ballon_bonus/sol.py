import sys
sys.stdin = open('input.txt', 'r')
#########################################


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_value, min_value = 0, 1e10
    for i in range(N):
        for j in range(N):
            temp = sum(matrix[i][:N:]) + sum(list(zip(*matrix))[j][::]) - matrix[i][j]
            max_value = max(temp, max_value)
            min_value = min(temp, min_value)
    print(f'#{tc} {max_value - min_value}')
