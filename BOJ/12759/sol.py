import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: BOJ/12759
# 작성 코드 시작
def check(r, c, p):
    # 가로 세로는 필수로 검사
    if all(board[r][i] == p for i in range(3)):
        return True
    if all(board[i][c] == p for i in range(3)):
        return True
    if r == c:
        if all(board[i][i] == p for i in range(3)):
            return True
    if r + c == 2:
        if all(board[i][2 - i] == p for i in range(3)):
            return True
    return False


def game():
    global player
    for _ in range(9):
        r, c = map(int, input().split())
        board[r - 1][c - 1] = player
        if check(r - 1, c - 1, player):
            return player
        player = 3 - player
    return 0

player = int(input())
board = [[0] * 3 for _ in range(3)]
print(game())