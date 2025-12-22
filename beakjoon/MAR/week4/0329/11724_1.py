import sys
# sys.stdin = open("11724.txt")
from collections import deque


def point(vtx):
    queue = deque([vtx])
    visited[vtx] = True
    while queue:
        vtx = queue.popleft()
        for adj in graph[vtx]:
            if visited[adj]: continue
            queue.append(adj)
            visited[adj] = True


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
ans = 0
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


for i in range(1, N+1):
    if visited[i]:
        continue
    point(i)
    ans += 1
print(ans)
