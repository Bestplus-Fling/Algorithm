n = int(input())
B, c1, c2 = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    B.append(num)
    c1.append(cnt1)
    c2.append(cnt2)

# Write your code here!
# 카운트 가능한 경우의 수를 탐색
# 많이 맞은 자리의 숫자를 먼저 확인
# 327의 경우 경우의 수는 32x, x27, 3x7이고
# 123의 경우 자리까지 맞은 숫자가 1, 위치는 다르지만 포함된 숫자가 1

answer = 0
# A가 가능한 후보를 만든다.
for A in range(111, 1000):
    a1 = A // 100
    a2 = (A // 10) % 10
    a3 = (A // 1) % 10
    if a1 == 0 or a2 == 0 or a3 == 0:
        continue
    if a1 == a2 or a2 == a3 or a1 == a3:
        continue
    # A의 후보가 정해졌을 때, B의 물음에 모두 합당한지 확인한다.
    is_answer = True
    for i in range(n):
        b1 = (B[i] // 100) % 10
        b2 = (B[i] // 10) % 10
        b3 = (B[i] // 1) % 10
        if (c1[i] != int(b1 == a1) + int(b2 == a2) + int(b3 == a3)):
            is_answer = False
            break
        # 겹친 개수
        overlap = 6 - len(set([a1, a2, a3, b1, b2, b3]))
        if (c2[i] != overlap - c1[i]):
            is_answer = False
            break
    if (is_answer):
        answer += 1
print(answer)
