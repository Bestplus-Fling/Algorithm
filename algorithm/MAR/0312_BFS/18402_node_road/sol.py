import sys
sys.stdin = open('input.txt', 'r')
#####################################
from collections import deque


def bfs():
    queue = deque()
    queue.append((S, 0))

    while queue:
        v, cnt = queue.popleft()
        visited[v] = True

        for adj in graph[v]:
            if visited[adj]:
                continue
            queue.append((adj, cnt+1))
            if adj == G:
                return cnt+1
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    for i in range(E):
        s, t = map(int, input().split())
        graph[s].append(t)
        graph[t].append(s)
    S, G = map(int, input().split())
    print(f'#{tc}', bfs())
