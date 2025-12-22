def black_jack(idx=0, num_sum=0, cnt=0):
    global result
    if (idx == N and cnt != 3) or num_sum > M:
        return
    if cnt == 3 and num_sum <= M:
        result = max(result, num_sum)
        return
    black_jack(idx+1, num_sum+arr[idx], cnt+1)
    black_jack(idx+1, num_sum, cnt)


N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
black_jack()
print(result)