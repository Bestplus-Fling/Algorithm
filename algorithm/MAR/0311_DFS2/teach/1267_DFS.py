import sys
from collections import defaultdict
sys.stdin = open('1267.txt', 'r')
#####################################


def dfs(v):
    # 현재 방문하는 노드를 방문처리
    visited[v] = True

    # v와 인접한 노드들을 방문
    for adj in graph[v]:
        if not visited[adj]:
            dfs(adj)
    res.append(v)


T = 10
for tc in range(1, T+1):
    v_cnt, e_cnt = map(int, input().split())
    edges = list(map(int, input().split()))

    graph = defaultdict(list)

    for i in range(e_cnt):
        graph[edges[2*i]].append(edges[2*i+1])

    # 모든 노드들의 진입차수를 확인
    # 1. 방문처리
    # 2. 모든 정점에서 시작
    visited = [False] * (v_cnt+1)
    res = []

    for v in range(1, v_cnt+1):
        if not visited[v]:
            dfs(v)

    print(f'#{tc}', *reversed(res))