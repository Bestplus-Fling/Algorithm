import sys
sys.stdin = open('input.txt', 'r')
#########################################
from collections import deque


def bfs(s):
    queue = deque()
    queue.append((s, 0))

    while queue:
        vertax, depth = queue.popleft()
        if visited[vertax] >= 0:
            continue
        visited[vertax] = depth
        count = 0
        for adj_v in graph[vertax]:
            if visited[adj_v] != -1:
                continue
            queue.append((adj_v, depth+1))
            count += 1
        if count == 0:
            res.append(vertax)


T = 10
for tc in range(1, T+1):
    V, S = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    visited = [-1] * 101
    for i in range(0, V, 2):
        graph[arr[i]].append(arr[i+1])
    # print(graph)
    res = []
    bfs(S)
    res = sorted(res, reverse=True)
    # print(res)
    ans = 0
    dp = 0
    # for i in range(100, 0, -1):
    #     if visited != -1 and dp < visited[i]:
    #         ans = i
    #         dp = visited[i]
    for vtx in res:
        if dp < visited[vtx]:
            ans = vtx
            dp = visited[vtx]
    print(f"#{tc}", ans)