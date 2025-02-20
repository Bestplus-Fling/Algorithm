N, K = map(int, input().split())
# candy = []
# pos = []
counting_array = [0] * 100

for _ in range(N):
    c, p = map(int, input().split())
    # candy.append((c, p))
    counting_array[p] += c

ans = 0
# 중심을 각 지점에 위치시킨다.
for center in range(K, 100-K):
    # 해당 중심에 대해서 -K ~ +K 위치의 바구니를 탐색
    low = max(0, center-K)  # 중심에서 가장 왼쪽
    high = min(100, center+K)   # 중심에서 가장 오른쪽

    # center를 중심으로 했을 때 얻을 수 있는 사탕 개수: result
    result = 0
    for target in range(low, high+1):
        # 정해진 위치에 대해 해당 위치에 바구니가 있는지 확인
        # for cnt, pos in candy:
        #     if pos == target:
        #         result += cnt
        result += counting_array[target]
    ans = max(result, ans)

print(ans)