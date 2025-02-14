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
    # 델타탐색 하면서 돌 위치를 저장
    for dx, dy in dxy:
        stack = []
        for k in range(1, N+1):
            # 델타 좌표 지정
            nx = x + (dx * k)
            ny = y + (dy * k)
            # out of range 방지용 + 돌을 두지 않았다면 추가하지 않음(퀵리턴)
            if not (0 <= nx < N and 0 <= ny < N) or game_board[nx][ny] == 0:
                break
            # 다른 색 돌을 만나면 저장
            if game_board[nx][ny] != bw:
                stack.append([nx, ny])
            # 같은 색의 돌을 만나면 스택에 쌓인 돌 뒤집기
            else:
                while stack:
                    mx, my = stack.pop()
                    game_board[mx][my] = bw
                break


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    game_board = [[0] * N for _ in range(N)]
    center = N // 2
    default_set()
    # P개 만큼의 착수를 입력 받는다.
    for i in range(M):
        x, y, bw = map(int, input().split())
        # 인덱스의 시작은 0이므로 입력받은 좌표에서 -1씩 한다
        x, y = x-1, y-1
        game_board[x][y] = bw
        # 함수를 호출해서 착수에 의해 뒤집힐 돌을 판별한다.
        delta_search()

    black, white = 0, 0
    # 흑돌과 백돌의 개수를 확인
    for _ in game_board:
        black += _.count(1)
        white += _.count(2)

    print(f'#{tc} {black} {white}')
