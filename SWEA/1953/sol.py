import sys
sys.stdin = open('input.txt', 'r')
#########################################
from collections import deque
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]
check_pipe = {
    (1, 0): [1, 2, 4, 7],
    (-1, 0): [1, 2, 5, 6],
    (0, 1): [1, 3, 6, 7],
    (0, -1): [1, 3, 4, 5]
}


def bfs(x, y):
    # deque 선언
    queue = deque([[x, y, 0]])
    visited = [[0] * M for _ in range(N)]   # 방문처리용 변수
    visited[x][y] = 1   # 첫 시작은 방문처리 필수!!!!
    count = 0   # 이동할 수 있는 터널의 개수를 확인
    while queue:
        x, y, t = queue.popleft()
        now_pipe = _map[x][y]
        # 종료조건
        if t >= L:
            break
        count += 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            # 범위 밖으로 벗어나면 안됨
            if not(0 <= nx < N and 0 <= ny < M):
                continue
            # 이미 방문한 터널이어도 안됨
            if visited[nx][ny]:
                continue
            # 터널이 없어도 안됨
            if _map[nx][ny] == 0:
                continue
            next_pipe = _map[nx][ny]
            # 현재 배관이 dx, dy 방향으로 구멍이 나있는 배관인지
            # 다음 배관이 dx, dy 방향으로 이동했을 때 이동 가능한 배관인지 검증
            if now_pipe in check_pipe[(-dx, -dy)] and next_pipe in check_pipe[(dx, dy)]:
                # 검증된 배관을 만나면 queue append + 방문처리
                queue.append([nx, ny, t+1])
                visited[nx][ny] = 1
    # while문이 끝나면 터널 개수를 반환한다.
    return count


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    # 세로크기 N, 가로크기 M, 세로위치 R, 가로위치 C, 소요시간 L
    N, M, R, C, L = map(int, input().split())
    _map = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}', bfs(R, C))
