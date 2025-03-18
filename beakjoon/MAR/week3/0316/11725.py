import sys
sys.stdin = open('input/11725_2.txt', 'r')
#########################################
from collections import deque


def m_tree(parent):
    queue = deque([parent])
    while queue:
        parent = queue.popleft()
        for child in temp[parent]:
            if parents[child]:
                continue
            queue.append(child)
            parents[child] = parent


N = int(input())
temp = [[] for _ in range(N + 1)]
parents = [0] * (N+1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    temp[a].append(b)
    temp[b].append(a)
m_tree(1)
for p in range(2, N+1):
    print(parents[p])
