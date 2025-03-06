import bisect

N, M = map(int, input().split())
arr = [
    int(input())
    for _ in range(N)
]

# 정렬 해놓고
arr = sorted(arr)

# 정답이 될 수 있는 후보군
candidates = []

# elem 에 대한 쌍을 찾을 때 elem+M 이상 최솟값 찾기
for elem in arr:
    # elem + M 이상 되는 최소값 찾기
    idx = bisect.bisect_right(arr, elem+M-1)
    if idx == len(arr):
        # 없다
        continue
    else:
        candidates.append(arr[idx] - elem)
if candidates:
    # 가능한 차이값이 있을 때는 가장 작은 차이값
    print(sorted(candidates)[0])
else:
    # 가능한 차이값이 없을때는 -1
    print(-1)