import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: 19532
# 작성 코드 시작

# def solve():
#     for x in range(-999, 1000):
#         for y in range(-999, 1000):
#             exp1 = (a * x) + (b * y) == c
#             exp2 = (d * x) + (e * y) == f
#             if exp1 and exp2:
#                 print(x, y)
#                 return
cal = lambda w, x, y, z: (w * x) - (y * z)

def solve():
    x = cal(c, e, b, f) // cal(a, e, b, d)
    y = cal(c, d, a, f) // cal(b, d, a, e)
    print(x, y)


a, b, c, d, e, f = map(int, input().split())
solve()


