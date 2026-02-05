# 문제 번호: 30917
# 작성 코드 시작

def query(c):
    for x in range(1, 10):
        print(f"? {c} {x}", flush=True)
        resp = int(input())

        if resp == 1:
            return x

A = query("A")
B = query("B")
print(f"! {A + B}")
