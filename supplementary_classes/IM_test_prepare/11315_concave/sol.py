import sys
sys.stdin = open("input.txt")

"""
돌이 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지
판정하는 프로그램

돌이 5개 이상 연속한 부분이 있으면 YES, 아니면 NO

5개만 되면 되니까 대각선으로 오목이 되는 경우가 여러군데서 생긴다??
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [input() for _ in range(N)]
    # 오목의 참 거짓을 판별
    ans = False

    for i in range(N):
        # 행, 열의 연속된 돌의 개수를 확인
        row, col = 0, 0
        # 대각선의 연속된 돌의 개수를 확인
        dag1, dag2, dag3, dag4 = 0, 0, 0, 0
        for j in range(N):
            # 행, 열을 탐색
            row += 1 if matrix[i][j] == 'o' else (-row)
            col += 1 if matrix[j][i] == 'o' else (-col)
            # 모든 대각선을 탐색
            # 이때 대각선 탐색의 시작 위치를 선택해야 하는데,
            # 행의 증가, 열의 증가 위치에서 시작하는 대각선 탐색을 설정
            if i+j < N:
                dag1 += 1 if matrix[j][i+j] == 'o' else -dag1
                dag3 += 1 if matrix[i+j][j] == 'o' else -dag3
            if N-1-i-j >= 0:
                dag2 += 1 if matrix[j][N-1-i-j] == 'o' else -dag2
                dag4 += 1 if matrix[i+j][N-1-j] == 'o' else -dag4
            # 중간에 연속된 돌의 개수가 5를 초과하면 바로 for문 탈출
            if row >= 5 or col >= 5 or dag1 >= 5 or dag2 >= 5 or dag3 >= 5 or dag4 >= 5:
                ans = True
                break
        if ans:
            break

    print(f'#{tc}', 'YES' if ans else 'NO')
