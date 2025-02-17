import sys
sys.stdin = open('input.txt', 'r')
#########################################

# 델타 탐색 범위 설정
dxy = [0, 1], [1, 0], [-1, 0], [0, -1]

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    # 행렬의 길이
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 이웃한 값과 차의 절대값들의 합을 저장
    result = 0
    for i in range(N):
        for j in range(N):
            # 임시로 이웃한 값들과의 차를 저장
            temp = 0
            # 델타 탐색으로 이웃한 값들을 탐색
            for dx, dy in dxy:
                nx, ny = i + dx, j + dy
                # 행렬의 범위 안에 있는 요소만 순회
                if 0 <= nx < N and 0 <= ny < N:
                    # |이웃한 위치의 값 - 현재 위치의 값|을 저장
                    temp += abs(matrix[nx][ny] - matrix[i][j])
            # [i][j]에 이웃한 값과의 차의 합을 저장
            result += temp
    # 총합을 출력
    print(f'#{tc} {result}')
