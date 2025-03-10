import sys
sys.stdin = open('input.txt', 'r')
#####################################
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


# 델타 탐색
def search(x, y):
    visited[x][y] = True    # 방문 처리
    for dx, dy in dxy:      # 델타 탐색
        nx, ny = x + dx, y + dy
        # 탐색하면 안되는 조건
        """
        1. 범위 밖을 벗어나거나(out of range)
        2. 벽을 만나거나(maze[nx][ny] == 1)
        3. 이미 방문한 이력이 있으면(visited[nx][ny] == True)
        continue
        """
        if not(0 <= nx < N and 0 <= ny < N) or maze[nx][ny] == 1 or visited[nx][ny]:
            continue
        # 종료 지점 확인 시 return 1
        if maze[nx][ny] == 3:
            return 1
        # 이곳까지 연산하러 온 경우는 nx, ny에 value가 0일 때만
        if search(nx, ny):
            # 이때 3을 찾은 경로를 만나면 1을 반환받으므로 if문은 참이다.
            # 따라서 이 경로는 1을 계속 반환한다.
            return 1
    # 모든 경우를 확인해도 1을 반환받은 적이 없다(3을 찾지 못했다.)면 0을 반환
    return 0


T = 10
N = 16
for tc in range(1, T+1):
    u = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    print(f'#{u}', search(1, 1))