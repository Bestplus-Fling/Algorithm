import sys
sys.stdin = open("1753.txt")
from collections import deque, defaultdict


def bfs(vtx):
    queue = deque([vtx])
    ans[vtx] = 0

    while queue:
        vtx = queue.popleft()
        wt = ans[vtx]
        visited[vtx] = 1
        for adj in graph[vtx]:
            # 시작정점에서 이동 가능한 경로의 정점으로 가는 비용을 저장
            # 시작정점을 방문처리, 다음 정점들로 이동한다
            # 다음 정점에서 이미 값이 수정된 경우라면,
            # 지금까지 이동해온 경로와 이미 저장된 값 중 최소값을 갱신한다.
            befo = ans[adj]
            check = wt + dic[(vtx, adj)]
            if befo == -1:
                ans[adj] = check
            else:
                # 지금까지 누적한 가중치 + 이동했을 때 추가되는 가중치
                if befo > check:
                    ans[adj] = check
            if visited[adj]:
                continue
        # 방문 노드를 설정하는 방법
        # 방문한 적 없는 노드 중에서 가장 작은 노드
        _min = float('inf')
        idx = -1
        for j in range(1, V+1):
            if ans[j] != -1 and not visited[j] and ans[j] < _min:
                _min = ans[j]
                idx = j
        if idx != -1:
            queue.append(idx)




V, E = map(int, input().split())
K = int(input())
graph = defaultdict(list)
dic = {}
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append(v)
    dic[(u, v)] = w
ans = [-1] * (V+1)
visited = [0] * (V+1)
bfs(K)
for i in range(1, V+1):
    p = ans[i]
    print(p if p != -1 else 'INF')
