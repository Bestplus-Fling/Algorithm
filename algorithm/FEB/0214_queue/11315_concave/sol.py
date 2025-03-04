import sys
sys.stdin = open('input.txt', 'r')
#########################################

dxy = [0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, 1], [1, -1]


def search_concave(x, y):
    for dx, dy in dxy:
        cnt = 0
        for k in range(N):
            nx = x + dx*k
            ny = y + dy*k
            if not(0 <= nx < N and 0 <= ny < N) or _list[nx][ny] == '.':
                break
            cnt += 1
        if cnt >= 5:
            return True
    return False


def search_o():
    for i in range(N):
        for j in range(N):
            if _list[i][j] == 'o':
                if search_concave(i, j):
                    return True
    return False



T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    _list = [list(input()) for _ in range(N)]
    ending = search_o()

    if ending:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')

