import sys
sys.stdin = open('input.txt', 'r')
#####################################
from collections import deque
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def bfs():
    queue = deque()
    queue.append((1, 1))

    while queue:
        x, y = queue.popleft()
        arr[x][y] = '1'

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if not(0 <= nx < N and 0 <= ny < N) or arr[nx][ny] == '1':
                continue

            queue.append((nx, ny))
            if arr[nx][ny] == '3':
                return 1
    return 0


T = 10
N = 100
for tc in range(1, T+1):
    t = int(input())
    arr = [list(input().strip()) for _ in range(N)]
    print(f'#{t}', bfs())
