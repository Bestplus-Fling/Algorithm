import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    grid = 10
    matrix = [[0] * grid for _ in range(grid)]
    for index in range(N):
        r1, c1, r2, c2, clr = map(int, input().split())
        for x in range(r1-1, r2):
            for y in range(c1-1, c2):
                if matrix[x][y] == 0:
                    matrix[x][y] = clr
                elif matrix[x][y] != clr and matrix[x][y] != 3:
                    matrix[x][y] += clr
    count_purple = 0
    for _ in range(grid):
        count_purple += matrix[_].count(3)
    print(f'#{tc} {count_purple}')


