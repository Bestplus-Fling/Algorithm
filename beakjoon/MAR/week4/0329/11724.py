import sys
sys.stdin = open("11724.txt")
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def point(vtx):
    start_v = vtx
    q = deque([vtx])
    F = False
    while q:
        vtx = q.popleft()
        if F and vtx == start_v:
            return True
        F = True
        for adj in graph[vtx]:
            if visited[adj]: continue
            q.append(adj)
            visited[adj] = True

    return False


ans = 0
for i in range(1, N+1):
    if visited[i]: continue
    if point(i):
        ans += 1
print(ans)
