import sys
sys.stdin = open('2606.txt', 'r')
#########################################

"""
1번 컴퓨터에서 출발, 연결된 모든 정점을 방문, 횟수를 센다
"""

# # 깊이 우선 탐색
# def dfs(vertax):
#     global ans
#     visited[vertax] = True
#     for adj_v in graph[vertax]:
#         if visited[adj_v]:
#             continue
#         ans += 1
#         dfs(adj_v)


from collections import deque


def bfs(vertax):
    global ans
    queue = deque()
    # 초기 시작 위치를 queue에 저장한다.
    queue.append(vertax)
    # 저장될때마다 방문처리를 한다.
    visited[vertax] = True
    # queue에 모든 데이터가 사라질때까지 동작
    while queue:
        vertax = queue.popleft()
        # 인접한 정점을 조회
        for adj in graph[vertax]:
            # 만약 방문한 정점은 pass
            if visited[adj]:
                continue
            # 여기까지 프로그램이 왔다면, 방문한 적 없는 정점이다.
            queue.append(adj)
            visited[adj] = True
            ans += 1    # 인접한 정점에 들어갈때마다 체크


V = int(input())    # 정점의 개수
E = int(input())    # 간선의 개수
graph = [[] for _ in range(V+1)]
for _ in range(E):
    start, end = map(int, input().split())
    # 양방향을 보장하는 간선을 저장
    graph[start].append(end)
    graph[end].append(start)
visited = [False] * (V+1)
ans = 0
# dfs(1)
bfs(1)
print(ans)

