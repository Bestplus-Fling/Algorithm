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
    ans_a = 0
    # 스택의 모든 데이터가 빠져나간 순간 => 완탐 끝
    while stack:
        # 방문처리
        visited[x][y] = True

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N) or maze[nx][ny] == 1 or visited[nx][ny]:
                continue
            if maze[nx][ny] == 3:
                ans_a = 1
                break
            # 재귀함수랑 달라지는 부분 => while로 재귀함수를 구현하기 위한 조건
            # - 스택 관리(재귀 함수 = 스택), 항상 다음 좌표로 넘어가기 전, 현재 좌표를 저장한다.
            stack.append((x, y))
            # 다음 좌표로 이동(갱신)
            x, y = nx, ny
            break
        else:
            x, y = stack.pop()
            # 더 이상의 델타탐색을 종료 => 갱신한 좌표에서의 탐색을 진행하게 된다.
        # 델타 탐색의 정상 종료: 모든 방향에서 해를 찾지 못했다.
            # 현재 좌표로 이동하기 전의 좌표로 돌아간다.
        if ans_a:
            break

        # 해를 찾은 경우 while문을 종료한다.
        # 해를 찾지 못한다면 while문은 stack의 모든 데이터가 사라질때까지 동작할 것이다.

    print(f'#{t}', ans_a)
