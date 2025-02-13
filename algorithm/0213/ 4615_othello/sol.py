import sys
sys.stdin = open('input.txt', 'r')
#########################################


# 초기 보드 세팅
def default_set():
    for k in range(center-1, center+1):
        for o in range(center-1, center+1):
            if k - o == 0:
                game_board[k][o] = 2
            else:
                game_board[k][o] = 1


# 델타 탐색 - 대각선 방향
def delta_search():
    dxy = [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]
    stack = []
    # 델타탐색 하면서 색이 다른 스택을 저장, 끝날때까지 같은 색을 못만나면
    for dx, dy in dxy:
        for k in range(1, N+1):
            nx = x + (dx * k)
            ny = y + (dy * k)
            while 0 <= nx < N and 0 <= ny < N:
                if game_board[nx][ny] != bw:
                    stack.append([nx, ny])
                    break
            ux, uy = stack[-1]
            if game_board[ux][uy] != bw:
                stack.clear()
                break

            while stack:
                mx, my = stack.pop()
                game_board[mx][my] = bw



"""
흑과 백의 좌표를 담는 stack(black_stack, white_stack) 생성
만약 현재 돌이 백일 경우 흑돌 stack을 확인
반대로 현재 돌이 흑일 경우 백돌 stack을 확인
확인해서 
"""
for i in range(3, 0):
    print(i)
T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    game_board = [[0] * N for _ in range(N)]
    center = N // 2
    default_set()
    black_stack, white_stack = [], []
    for i in range(M):
        x, y, bw = map(int, input().split())
        x, y = x-1, y-1
        game_board[x][y] = bw
        delta_search()

    for _ in game_board:
        print(_)

    break
