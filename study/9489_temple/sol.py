import sys
sys.stdin = open('input.txt', 'r')
#########################################


def check(width, height, matrix):
    global result
    count = 0
    for i in range(height):
        for j in range(width):
            if matrix[i][j]:
                count += 1
            if not matrix[i][j] or j == width-1:
                result = max(result, count)
                count = 0
    return count


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    photo_data = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    check(M, N, photo_data)
    photo_data_reverse = list(zip(*photo_data[::-1]))
    check(N, M, photo_data_reverse)
    print(f"#{tc}", result)

