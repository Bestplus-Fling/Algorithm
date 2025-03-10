import sys
sys.stdin = open('input.txt', 'r')
#####################################
dxy = [-1, 0], [1, 0], [0, -1], [0, 1]


# 시작 위치 확인
def set_start():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return (i, j)


# 종료 위치(3) 확인
def search(now):
    x, y = now

    # 방문 처리
    visited[x][y] = True
    # 델타 탐색
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        # 찾으면 안되는 조건
        # 1. 범위 밖을 탐색
        # 2. 벽을 만났을 때(= 1)
        # 3. 이미 방문한 위치일 때 (= visited[nx][ny] == True)
        if not(0 <= nx < N and 0 <= ny < N) or maze[nx][ny] == 1 or visited[nx][ny]:
            continue
        # 도착지를 찾는 순간 return 1
        if maze[nx][ny] == 3:
            return 1

        # 위의 조건을 모두 통과했다면, [nx][ny]의 값은 0이다.
        # 통로를 따라 3을 만났다면 if문은 참이므로 왔던 길을 되돌아갈 때 1을 계속 반환한다.
        if search((nx, ny)):
            return 1
    # 모든 조건을 확인했으나 3을 찾지 못했다면 0을 반환한다.
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 1: 벽, 2: 시작, 3: 종료
    maze = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    print(f'#{tc}', search(set_start()))
