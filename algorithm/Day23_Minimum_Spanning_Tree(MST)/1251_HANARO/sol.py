import sys
sys.stdin = open("output.txt", "r")
output = [input for _ in range(20)]
result = []
count = 0
sys.stdin = open("input.txt", "r")
from math import sqrt
import heapq


def prim(vertices, edges):
    mst = []

    adj_list = {v: [] for v in vertices}
    for start_v, end_v, w in edges:
        adj_list[start_v].append((end_v, w))
        adj_list[end_v].append((start_v, w))

    visited = set()
    init_vertex = vertices[0]
    min_heap = [[w, init_vertex, e] for e, w in adj_list[init_vertex]]
    heapq.heapify(min_heap)
    visited.add(init_vertex)

    while min_heap:
        weight, start_v, end_v = heapq.heappop(min_heap)
        if end_v in visited: continue

        visited.add(end_v)
        mst.append((start_v, end_v, weight))

        for adj_v, adj_w in adj_list[end_v]:
            if adj_v in visited: continue
            heapq.heappush(min_heap, [adj_w, end_v, adj_v])

    return mst


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dx = list(map(int, input().split()))
    dy = list(map(int, input().split()))
    E = float(input())

    vtx = list(range(N))
    visited_arr = [[False] * N for _ in range(N)]
    edg = []
    for i in range(N-1):
        st_x, st_y = dx[i], dy[i]
        for j in range(N):
            if j == i or visited_arr[i][j]: continue
            ed_x, ed_y = dx[j], dy[j]
            a, b = abs(st_x - ed_x), abs(st_y - ed_y)
            c = sqrt((a ** 2) + (b ** 2))
            edg.append([i, j, c])
            visited_arr[i][j], visited_arr[j][i] = True, True
    temp = prim(vtx, edg)
    ans = 0
    for k in temp:
        ans += (k[2] ** 2) * E

    print(f'#{tc} {ans:.0f}')

    result.append(f'#{tc} {ans:.0f}')


# for p, z in zip(result, output):
#     print(p, str(z))
#     if p == z:
#         count += 1
# print(count)
