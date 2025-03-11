import sys
sys.stdin = open('input.txt', 'r')
#####################################
# 가장 높은 봉우리에서 시작
# 산으로 올라갈 수 있도록 높은 지형에서 낮은 지형으로
# 가로 또는 세로 방향으로 연결
# 긴 등산로를 만들기 위해 딱 한곳을 정해 K 깊이만큼 깎을 수 있음
# 지금 기준 나보다 작은값으로만 갈 수 있음
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def dfs(x, y, depth, z):
    global res
    # 방문처리
    visited[x][y] = True
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        # 범위 밖이거나
        if not(0 <= nx < N and 0 <= ny < N):
            continue
        # 방문처리된 적 있으면 skip
        if visited[nx][ny]:
            continue
        # 현재 위치보다 높은 봉우리를 만났을 때
        if matrix[nx][ny] >= matrix[x][y]:
            # 공사 기회를 쓴 적 있다면 skip
            if not z:
                continue
            # 깎아도 현재 위치보다 높아도 skip
            if matrix[nx][ny]-z >= matrix[x][y]:
                continue
            # 깎아내린 높이로 실행(최대 K만큼 깎을 수 있다 != 무조건 K만큼 깎는다)
            for k in range(1, z+1):
                if matrix[nx][ny] - k < matrix[x][y]:
                    matrix[nx][ny] -= k
                    dfs(nx, ny, depth+1, 0)
                    matrix[nx][ny] += k
        # 현재 좌표보다 낮은 봉우리로 이동
        if matrix[nx][ny] < matrix[x][y]:
            dfs(nx, ny, depth+1, z)
    # 가장 긴 등산로 길이를 갱신
    res = max(res, depth)
    visited[x][y] = False


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 길이 저장용
    res = 0
    # 가장 높은 봉우리의 좌표쌍을 저장할 변수
    top_level = []
    # 가장 높은 봉우리의 숫자 저장용 변수
    max_num = 0
    visited = [[False] * N for _ in range(N)]

    # 가장 높은 봉우리의 높이를 확인
    for i in range(N):
        mx = max(matrix[i])
        if max_num > mx:
            continue
        max_num = max(max(matrix[i]), max_num)

    # 가장 높은 봉우리의 좌표를 확인
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == max_num:
                top_level.append((i, j))
    # 좌표쌍으로 함수 호출
    for i, j in top_level:
        dfs(i, j, 1, K)
    print(f'#{tc}', res)

"""
등산로는 가장 높은 봉우리에서 시작해야 한다.
등산로는 산으로 올라갈 수 있도록 반드시 높은 지형에서 낮은 지형으로, 가로 또는 세로 방향으로 연결
- 높이가 같거나, 낮은 지형이거나, 대각선 방향의 연결은 불가능하다

긴 등산로를 만들기 위해 딱 한곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있다.
"""