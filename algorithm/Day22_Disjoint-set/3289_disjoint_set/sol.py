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
    parent = [i for i in range(N+1)]    # make_set
    rank = [0] * (N+1)
    ans = ''
    # 확인 연산은 1, union 은 0으로 확인
    for i in range(M):
        func, a, b = map(int, input().split())
        if func == 1:   # a와 b의 집합이 같은 지 확인
            ans += '1' if find_set(a) == find_set(b) else '0'

        else:   # 합집합 실행
            union(a, b)
    print(f'#{tc}', ans)

