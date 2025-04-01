import sys
sys.stdin = open("input.txt", "r")


def subset(start, num_sum, num_list=[]):
    global result
    # 이미 목표값을 초과한 경우 제외
    if num_sum > K:
        return

    if num_sum == K:    # 목표값 달성시 +1
        result += 1
    for i in range(start, N):
        num_list.append(data[i])
        subset(i+1, num_sum+data[i], num_list)
        num_list.pop()


T = int(input())
for tc in range(1, T+1):
    # 배열의 길이 N, 목표값 K
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    result = 0
    subset(0, 0)
    print(f'#{tc}', result)
