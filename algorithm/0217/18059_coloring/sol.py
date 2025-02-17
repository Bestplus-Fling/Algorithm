import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    # 칠할 영역의 개수 N을 입력
    N = int(input())
    # 격자의 크기 10을 변수에 저장
    grid = 10
    # 빈 격자를 생성
    matrix = [[0] * grid for _ in range(grid)]
    # 색칠할 좌표와 색을 입력
    for index in range(N):
        r1, c1, r2, c2, clr = map(int, input().split())
        # 좌표의 시작을 0부터 해야 하므로 r1-1, c1-1
        # r2, c2는 미포함이니까 그냥 둔다.
        for x in range(r1-1, r2):
            for y in range(c1-1, c2):
                # 아무 것도 칠해지지 않았다면 칠하기
                if matrix[x][y] == 0:
                    matrix[x][y] = clr
                # 만약 현재위치가 다른 색으로 칠해져 있고, 이미 보라색이 아니면
                elif matrix[x][y] != clr and matrix[x][y] != 3:
                    # 보라색으로 만든다.
                    matrix[x][y] += clr
    # 보라색으로 칠해진 영역을 확인
    count_purple = 0
    for _ in range(grid):
        count_purple += matrix[_].count(3)
    # 보라색으로 칠해진 영역의 범위를 출력
    print(f'#{tc} {count_purple}')


