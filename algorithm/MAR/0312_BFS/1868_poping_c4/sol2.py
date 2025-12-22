import sys
sys.stdin = open('input.txt', 'r')
#########################################
from collections import deque
dxy = [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]


# 1. 지뢰의 개수를 확인, 갱신한다.
def change_num(x, y):
    # 델타 탐색을 한다.
    count = 0
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not(0 <= nx < N and 0 <= ny < N):
            continue
        # 폭탄의 개수를 샌다.
        if arr[nx][ny] == '*':
            count += 1
            vit[nx][ny] = True

    # 폭탄의 개수를 문자열로 수정한다
    arr[x][y] = str(count)


# 0을 누를 때 주변을 활성화(vit = True)
def bfs(cx, cy):
    # 0의 좌표를 받아온다.
    queue = deque()
    queue.append((cx, cy))
    # '0'만 탐색
    while queue:
        x, y = queue.popleft()
        if vit[x][y]:
            continue
        vit[x][y] = True
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N) or vit[nx][ny] or arr[nx][ny] == '*':
                continue
            if arr[nx][ny] == '0':
                queue.append((nx, ny))
                continue
            vit[nx][ny] = True


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(N)]
    vit = [[False] * N for _ in range(N)]
    ans_a = 0
    z_queue = deque()
    for i in range(N):
        for j in range(N):
            # .을 만난다 => 폭탄이 없다 -> 숫자로 변환
            if arr[i][j] == '.':
                change_num(i, j)
            if arr[i][j] == '0':
                z_queue.append((i, j))

    while z_queue:
        lx, ly = z_queue.popleft()
        if vit[lx][ly]:
            continue
        bfs(lx, ly)
        ans_a += 1

    for i in range(N):
        for j in range(N):
            if arr[i][j] != '*' and not vit[i][j]:
                ans_a += 1
    print(f'#{tc}', ans_a)