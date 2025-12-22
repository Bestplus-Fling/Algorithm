import sys
sys.stdin = open('input.txt', 'r')
#####################################


def dfs(nv, depth, vst):
    global depths
    # 방문한 정점들을 저장
    vst.append(nv)
    # 간선을 확인
    for adj_v in graph[nv]:
        # 방문한 적 없는 정점만을 찾는다.
        if adj_v in vst:
            continue
        dfs(adj_v, depth+1, vst)
    # 모든 탐색이 끝나면 현재 정점의 방문처리 취소
    vst.pop()
    # 최대 깊이 갱신
    depths = max(depth, depths)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    # 깊이의 최대값 저장용 변수
    depths = -float('inf')
    for i in range(M):
        v, n = map(int, input().split())
        graph[v].append(n)
        graph[n].append(v)
    # 방문처리용
    visited = [False] * (N + 1)
    for i in range(1, N+1):
        # 방문한 적 있는 정점은 pass
        if visited[i]:
            continue
        # 방문처리 하고 탐색 시작
        visited[i] = True
        dfs(i, 1, [])

    print(f'#{tc}', depths)
