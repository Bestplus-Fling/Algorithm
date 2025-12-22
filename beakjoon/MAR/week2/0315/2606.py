import sys
sys.stdin = open('2606.txt', 'r')
#########################################

"""
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 바이러스를 전파받는 컴퓨터의 수
"""
from collections import deque


def bfs(st=1):
    global ans_a
    queue = deque([st])
    visited_a[st] = 1
    while queue:
        vtx = queue.popleft()
        for adj in graph[vtx]:
            if visited_a[adj]:
                continue
            visited_a[adj] = 1
            queue.append(adj)
            ans_a += 1


def dfs(vtx=1):
    global ans_b
    visited_b[vtx] = 1
    for adj in graph[vtx]:
        if visited_b[adj]:
            continue
        ans_b += 1
        dfs(adj)


N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(int(input())):
    a, c = map(int, input().split())
    graph[a].append(c)
    graph[c].append(a)
visited_a = [0] * (N + 1)
visited_b = [0] * (N + 1)
ans_a, ans_b = 0, 0
bfs()
dfs()
print(ans_a)
print(ans_b)