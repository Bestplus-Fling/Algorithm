import sys
sys.stdin = open("14501.txt")


def dfs(day, sum_pay):
    global max_pay
    if N <= day:
        max_pay = max(max_pay, sum_pay)
        return
    if day + work[day] <= N:
        dfs(day+work[day], sum_pay+payment[day])
    dfs(day+1, sum_pay)


N = int(input())
work, payment = [], []
max_pay = 0
for _ in range(N):
    d, p = map(int, input().split())
    work.append(d)
    payment.append(p)
dfs(0, 0)
print(max_pay)
