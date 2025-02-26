N, M, L = map(int, input().split())
arr = [0] * N
idx = 0
while True:
    if arr[idx] % 2 == 0:
        arr[idx] += 1
        idx += L
    else:
        arr[idx] += 1
        idx -= L
    if arr.count(M):
        break

    if idx < 0:
        idx = N + idx
    elif idx >= N:
        idx = idx - N

print(sum(arr) - 1)