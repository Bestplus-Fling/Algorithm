import sys
sys.stdin = open("1260.txt", "r")
from collections import deque


def dfs(vtx):
    d_list.append(vtx)
    visited[vtx] = True
    for adj_v in edge[vtx]:
        if visited[adj_v]:
            continue
        dfs(adj_v)


def bfs(vtx):
    queue = deque([vtx])
    visited[vtx] = True
    while queue:
        vtx = queue.popleft()
        b_list.append(vtx)
        for adj_v in edge[vtx]:
            if visited[adj_v]:
                continue
            queue.append(adj_v)
            visited[adj_v] = True


N, M, V = map(int, input().split())
edge = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    edge[s].append(e)
    edge[e].append(s)

for i in range(1, N+1):
    edge[i].sort()
d_list, b_list = [], []
visited = [False] * (N+1)
dfs(V)
visited = [False] * (N+1)
bfs(V)
print(*d_list)
print(*b_list)