X, Y = map(int, input().split())


# F(i): i를 각 자리수로 쪼갠 list를 정렬 후 반환
def F(i):
    result = []
    while (i > 0):
        result.append(i % 10)
        i //= 10

    return sorted(result)


cnt = 0
# X ~ Y 까지 모든 경우에 대해
for i in range(X, Y + 1):
    # 자리수를 쪼개서
    digits = F(i)
    # 흥미로운 수인지 확인
    if len(set(digits)) == 2 and (digits[0] != digits[1] or digits[-1] != digits[-2]):
        cnt += 1

print(cnt)
