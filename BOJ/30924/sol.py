# 문제 번호: 30924
# 작성 코드 시작
from random import choice

def query(c):
    u = set(range(1, 10001))

    while u:
        x = choice(list(u))

        print(f"? {c} {x}", flush=True)

        resp = int(input())
        if resp == 1:
            return x
        else:
            u.remove(x)


a = query("A")
b = query("B")
print(f"! {a + b}")