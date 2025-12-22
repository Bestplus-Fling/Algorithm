import sys
sys.stdin = open("input.txt", "r")


def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    px, py = find_set(x), find_set(y)

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
    parent = [i for i in range(N+1)]
    rank = [0] * (N+1)
    for i in range(M):
        a, b = map(int, input().split())
        union(a, b)
    for i in range(1, N+1):
        find_set(i)
    ans = len(set(parent[1::]))
    print(f'#{tc}', ans)
