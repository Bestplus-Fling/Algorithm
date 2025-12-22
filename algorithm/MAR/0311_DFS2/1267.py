import sys
sys.stdin = open('teach/1267.txt', 'r')
#####################################


def dfs(now_v):
    for adj_v in edge[now_v]:
        if edge[adj_v] and not visited[adj_v]:
            dfs(adj_v)
    visited[now_v] = True
    res.append(now_v)


T = 10
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    edge = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    for i in range(0, E*2, 2):
        edge[arr[i]].append(arr[i+1])
    print(edge)
    res = []
    for i in range(1, V+1):
        if not edge[i]:
            dfs(i)
    print(*res)
    break