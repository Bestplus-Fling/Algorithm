N, M = map(int, input().split())
J = int(input())
arr = [[0, M], [0, N]]
for _ in range(J):
    rc, index = map(int, input().split())
    arr[rc].append(index)
arr[0].sort()
arr[1].sort()
max_range = 0
for i in range(len(arr[0])-1):
    col = arr[0][i+1] - arr[0][i]
    for j in range(len(arr[1])-1):
        row = arr[1][j + 1] - arr[1][j]
        max_range = max(max_range, row*col)
print(max_range)