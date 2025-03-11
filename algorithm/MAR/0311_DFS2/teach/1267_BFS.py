import sys
from collections import defaultdict
from collections import deque
sys.stdin = open('1267.txt', 'r')
#####################################

T = 10
for tc in range(1, T+1):
    v_cnt, e_cnt = map(int, input().split())
    edges = list(map(int, input().split()))

    graph = defaultdict(list)

    for i in range(e_cnt):
        graph[edges[2*i]].append(edges[2*i+1])

    # 모든 노드들의 진입차수를 확인
    in_degree = [0] * (v_cnt+1)

    # 진입 차수를 계산
    for node in graph:
        for n in graph[node]:
            in_degree[n] += 1
    queue = deque()
    for i in range(1, v_cnt+1):
        if not in_degree[i]:
            queue.append(i)
    res = []
    while queue:
        node = queue.popleft()
        res.append(node)

        for adj in graph[node]:
            in_degree[adj] -= 1

            if in_degree[adj] == 0:
                queue.append(adj)


    print(f'#{tc}', *res)