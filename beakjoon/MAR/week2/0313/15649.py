def f(nums, c, depth):
    if depth == N and c != M:
        return
    if c == M:
        print(nums)
        return
    for num in arr:
        if vistied[num]:
            continue
        vistied[num] = True
        f(nums+' '+str(num), c+1, depth+1)
        vistied[num] = False


N, M = map(int, input().split())
arr = [_ for _ in range(1, N+1)]
vistied = [False] * (N+1)
for n in arr:
    vistied[n] = True
    f(str(n), 1, 1)
    vistied[n] = False