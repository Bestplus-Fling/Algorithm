import sys
sys.stdin = open("14501.txt")


def f(date, pys):
    global max_pay
    if date >= N:
        max_pay = max(max_pay, pys)
        return
    pass_pay = pys
    # print(f'{date+1}일 상담 미선택')
    f(date+1, pass_pay)
    if date+schedule[date]-1 < N:
        pass_pay += pay[date]
    # print(f'{date+1}일 상담 선택 {pass_pay}')
    f(date+schedule[date], pass_pay)


N = int(input())
schedule = []
pay = []
for i in range(N):
    t1, t2 = map(int, input().split())
    schedule.append(t1)
    pay.append(t2)
# print(schedule, pay)
max_pay = 0
f(0, 0)
print(max_pay)
