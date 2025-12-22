import sys
sys.stdin = open("input.txt", "r")


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px != py:
        if rank[px] > rank[py]:
            parent[py] = px
        elif rank[px] < rank[py]:
            parent[px] = py
        else:
            parent[py] = px
            rank[px] += 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = 0
    parent = [i for i in range(N+1)]
    rank = [0] * (N+1)
    who = list(map(int, input().split()))
    for i in range(0, M*2, 2):
        union(who[i], who[i+1])
    for i in range(1, N+1):
        find_set(i)
    ans = len(set(parent[1::]))
    print(f"#{tc}", ans)
