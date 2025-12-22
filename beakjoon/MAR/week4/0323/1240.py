import sys
sys.stdin = open('1240.txt', 'r')
#########################################
from collections import defaultdict, deque


def search(vtx, evtx):
    queue = deque([[vtx, 0]])
    visited = [0] * (N+1)
    visited[vtx] = 1
    while queue:
        vtx, ws = queue.popleft()
        if vtx == evtx:
            return ws
        for adj in graph[vtx]:
            if visited[adj]:
                continue
            queue.append([adj, ws+weight[(vtx, adj)]])
            visited[adj] = 1


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
weight = defaultdict(int)
for i in range(N-1):
    s, e, w = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    weight[(s, e)] = w
    weight[(e, s)] = w

for i in range(M):
    s, e = map(int, input().split())
    print(search(s, e))
