import sys
sys.stdin = open('1260.txt', 'r')
#########################################


def dfs(vertax):
    visited[vertax] = True
    l_dfs.append(vertax)
    for adj in graph[vertax]:
        # 방문한 인접 정점은 pass
        if visited[adj]:
            continue
        dfs(adj)


from collections import deque


def bfs(vertax):
    queue = deque([vertax])
    visited[vertax] = True
    l_bfs.append(vertax)
    while queue:
        vertax = queue.popleft()
        for adj in graph[vertax]:
            if visited[adj]:
                continue
            queue.append(adj)
            visited[adj] = True
            l_bfs.append(adj)


# 정점의 개수, 간선의 개수, 시작 정점
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
# 간선의 개수를 입력받는다 (M개만큼)
for _ in range(M):
    # 시작 정점, 끝 정점(방향성이 없다) => 양방향 그래프
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
for i in range(1, N+1):
    graph[i].sort()
l_dfs, l_bfs = [], []
visited = [False] * (N+1)
dfs(V)
print(*l_dfs)
visited = [False] * (N+1)
bfs(V)
print(*l_bfs)
