"""
M과 N이 주어질 때 m 이상 n 이하의 자연수 중 완전제곱수인 것들을 모두 골라
그 합을 구하고 그중 최솟값을 찾는 프로그램을 작성
"""

M, N = int(input()), int(input())
now = 1
while True:
    if now * now >= M:
        break
    now += 1

sum_ans = 0
min_ans = float('inf')
for i in range(M, N+1):
    if i // now == now and i % now == 0:
        sum_ans += i
        min_ans = min(min_ans, i)
        now += 1

if sum_ans:
    print(sum_ans)
    print(min_ans)
else:
    print(-1)
