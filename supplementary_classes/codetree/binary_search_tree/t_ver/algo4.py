from sortedcontainers import SortedSet

N, M = map(int, input().split())

coordinates = [
    tuple(map(int, input().split()))
    for _ in range(N)
]

coordinates = SortedSet(coordinates)
check = [False] * (N+5)

for _ in range(M):
    target_x = int(input())

    target = (target_x, 0)

    idx = coordinates.bisect_right(target)

    if idx == len(coordinates):
        print(-1, -1)
    else:
        print(coordinates[idx][0], coordinates[idx][1])
        coordinates.remove(idx)