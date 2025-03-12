import sys
from typing import List, Any

sys.stdin = open('input.txt', 'r')
#####################################
"""
시작 당번 S가 주어질 때, 연락을 가장 마지막에 받는 번호 중 큰 값을 출력
번호와, 받은 순서를 튜플에 계속 집어 넣는다.

마지막에 동시에 연락받은 사람 중, 가장 숫자가 큰 사람
"""


from collections import deque


def bfs():
    queue = deque()
    queue.append((S, 0))

    while queue:
        now, count = queue.popleft()
        if visited[now]:
            continue
        visited[now] = True
        call_stack = 0
        for adj in graph[now]:
            if visited[adj]:
                continue
            queue.append((adj, count + 1))
            call_stack += 1

        if call_stack == 0:
            result.append((now, count))


T = 10
for tc in range(1, T+1):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    visited = [False for _ in range(101)]
    result = []
    for i in range(0, N, 2):
        f, t = arr[i], arr[i + 1]
        graph[f].append(t)
    bfs()
    ans = sorted(result, key=lambda x: (-x[1], -x[0]))
    print(f'#{tc}', ans[0][0])
