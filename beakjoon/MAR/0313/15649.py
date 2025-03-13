def f(idx, nums, c):
    if idx == N and c != M:
        return
    if c == M:
        print(*nums)
        return
    if arr[idx] not in nums:
        nums.append(arr[idx])
        f(idx+1, nums, c+1)
        nums.pop()
    f(idx+1, nums, c)


N, M = map(int, input().split())
arr = [_ for _ in range(1, N+1)]

for i in range(N):
    f(0, [arr[i]], 1)
