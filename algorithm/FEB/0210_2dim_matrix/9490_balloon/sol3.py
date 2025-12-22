import sys
sys.stdin = open('input.txt', 'r')
#########################################
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def delta(x, y):
    temp = arr[x][y]
    for k in range(1, arr[x][y]+1):
        for dx, dy in dxy:
            nx, ny = x + dx*k, y + dy*k
            if not(0 <= nx < N and 0 <= ny < M):
                continue
            temp += arr[nx][ny]
    return temp


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans_a = 0
    for i in range(N):
        for j in range(M):
            ans_a = max(delta(i, j), ans_a)
    print(f'#{tc}', ans_a)
