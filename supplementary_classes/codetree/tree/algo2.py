import sys
sys.stdin = open("input2_2.txt")


n, m = map(int, input().split())
a = list(map(int, input().split()))

# M 개의 비어있는 의자, 순서대로 1번부터 M번 번호
# 사람들이 앉고자 하는 의자에 대한 정보 ai
# ai = 1 이상, M 이하 / i번째 사람은 1 이상 ai 이하 의자에만 앉고 싶다
# 1번 사람부터 순서대로 규칙에 맞게 앉는다.
# 최초로 앉지 못하는 사람이 생기면 종료


def f():
    global t
    while t in s:
        t -= 1
        if t <= 0:
            return 'a'
    return 1


s = set()

for i in range(n):
    t = a[i]
    if t in s:
        if f() == 'a':
            break
    s.add(t)
print(len(s))


# def check():
#     # print(a[cnt])
#     for j in range(a[cnt]):
#         if arr[j] != 0:
#             continue
#         return j
#     return 'a'
#
#
# arr = [0] * (m+1)
# cnt = 0
# for i in range(n):
#     if arr[a[cnt]]:
#         temp = check()
#         if temp != 'a':
#             arr[temp] = 1
#             cnt += 1
#             continue
#         else:
#             break
#     arr[a[cnt]] = 1
#     cnt += 1
# print(cnt)