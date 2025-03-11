import sys
sys.stdin = open('input.txt', 'r')
#####################################

dxy = [1, 0], [0, -1], [-1, 0], [0, 1]
# 배열의 크기 100 고정
N = 100
T = 10
for tc in range(1, T+1):
    t = int(input())
    # 미로 입력
    maze = [list(map(int, input().strip())) for _ in range(N)]
    # 방문처리용
    visited = [[False] * N for _ in range(N)]
    # 시작 지점은 항상 2,2
    x, y = 2, 2
    stack = [(2, 2)]
    ans = 0
    # 스택의 모든 데이터가 빠져나간 순간 => 완탐 끝
    while stack:
        # 방문처리
        visited[x][y] = True
        x, y = stack.pop()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N) or maze[nx][ny] == 1 or visited[nx][ny]:
                continue
            if maze[nx][ny] == 3:
                ans = 1
                break
            stack.append((nx, ny))
        if ans:
            break
        # 해를 찾지 못한다면 while문은 stack의 모든 데이터가 사라질때까지 동작할 것이다.

    print(f'#{t}', ans)