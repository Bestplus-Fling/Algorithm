import sys
sys.stdin = open('2667.txt', 'r')
#########################################
dxy = [1, 0], [0, -1], [-1, 0], [0, 1]


def dfs(x, y, depth=1):
    # 방문처리
    visited[x][y] = True
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not(0 <= nx < N and 0 <= ny < N) or arr[nx][ny] == '0':
            continue
        if visited[nx][ny]:
            continue
        # 가장 긴 길이를 반환
        # 왜? 만약 지금까지 갔던 길의 값을 리턴받으면서 갱신하고, 다음 좌표를 이동할 때도
        # 갱신된 값을 +1해서 보내기 때문이다.
        depth = dfs(nx, ny, depth+1)
    return depth


# 배열의 크기 N * B
N = int(input())
# 단지들의 위치를 입력
arr = [list(input().strip()) for _ in range(N)]
# 방문처리용
visited = [[False] * N for _ in range(N)]

ans = []    # 답을 저장할 리스트
for i in range(N):
    for j in range(N):
        # 방문한 적 있거나 0은 skip
        if visited[i][j] or arr[i][j] == '0':
            continue
        # 아파트 개수를 return받아서 저장
        ans.append(dfs(i, j))
# 아파트 단지의 개수와 그 크기를 출력(오름차순으로)
print(len(ans), *ans, sep='\n')
