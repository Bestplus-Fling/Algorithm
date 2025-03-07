import sys
sys.stdin = open('input.txt', 'r')
#####################################

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 정방행렬에 대한 탐색
    """
    단차가 발생했을 때 발생한 시점에서 x칸 이내 변경점이 있다면 활주로 x
    범위 밖을 벗어나면 그때도 불가
    """
    for i in range(N):
        row_FLAG, col_FLAG = True, True
        for j in range(N):
            # 이전 숫자와 차이가 0일 경우 pass
            # 이전 숫자랑 차이가 음수일 때, 뒤에 있는 숫자가 더 크다
            # 이전 숫자랑 차이가 양수일 때, 현재 있는 숫자가 더 크다
            if not (0 <= j-1 < N and 0 <= j+X < N):
                continue
            if matrix[i][j-1] == matrix[i][j]:
                continue
            # 이전 숫자와 차이가 발생할 경우 탐색 시작
            """
            
            """
            # print(matrix[i][j:j+X])
            for ii in range(j, j+X+1):
                if matrix[i][j] != matrix[i][ii] or ii >= N:
                    row_FLAG = False
                    break
        print(matrix[i] if row_FLAG else 0)
    break


