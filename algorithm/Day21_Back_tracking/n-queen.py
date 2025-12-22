def is_valid(board, row, col):
    """
    1. 내 위쪽 열에 체스 말이 있는지 확인
        board[row][col] => 현재 내 위치
    """
    for i in range(row):
        if board[i][col] == 1:
            return False
    # 2. 내 왼쪽 위 대각선에 체스 말이 있는지 확인
    for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[r][c] == 1:
            return False
    # 3. 내 오른쪽 위 대각선에 체스 말이 있는지 확인
    for r, c in zip(range(row, -1, -1), range(col, n)):
        if board[r][c] == 1:
            return False

    return True


def n_queens(row, board):
    """
    :param row: 시작 행
    :param board: 체스말을 둘 위치
    :return: -> n_queens 함수가 최종적으로 할 일
    """
    # 함수가 최종적으로 할 일
    if row == n:    # 모든 행에 퀸을 다 삽입하는데 성공했다면
        solutions.append([r[:] for r in board])
        return  # 조사 종료
    # 아직 조사 중이라면
    for col in range(n):
        if is_valid(board, row, col):  # 검증
            board[row][col] = 1

            n_queens(row + 1, board)    # 다음 행으로 조사
            board[row][col] = 0


n = 4
board = [[0] * n for _ in range(n)]
solutions = []

n_queens(0, board)

for solution in solutions:
    # print(*solution)
    print(*solution, sep='\n', end='\n\n')