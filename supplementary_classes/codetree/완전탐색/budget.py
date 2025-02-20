N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

ans = 0
# 반값 할인을 누구에게 할지 모든 경우에 대해 탐색
for discount in range(N):
    # discount 해줄 친구에게 할인
    P[discount] //= 2

    new_P = sorted(P[:])    # 복사

    # 예산 안에서 선물 가능한 최대 인원 구하기(Greedy)
    total, cnt = 0, 0
    for money in new_P:
        if total + money <= B:
            total += money
            cnt += 1
        else:
            break
    ans = max(ans, cnt)

    # 할일했을 걸 원상복구
    P[discount] *= 2

print(ans)