import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # 가로 줄 먼저 카운팅(연속된 1을 카운팅)
    for row in range(N):
        count = 0
        for col in range(N):
            if matrix[row][col] == 1:
                count += 1
            else:   # 1이 아니라면 (막힌 칸을 만난 경우)
                if count == K:
                    result += 1
                count = 0   # 새롭게 1을 세기 위해(뚫린 연속된 칸을 세기 위함)
        if count == K:
            result += 1


    for col in range(N):
        count = 0
        for row in range(N):
            if matrix[row][col] == 1:
                count += 1
            else:
                if count == K:
                    result += 1
                count = 0
        if count == K:
            result += 1

    print(f'#{tc} {result}')

    """
    다른 방식
    전치행렬로 회전하고 함수로 탐색하는 방법
    """