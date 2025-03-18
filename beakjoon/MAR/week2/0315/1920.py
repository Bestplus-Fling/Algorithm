import sys
sys.stdin = open("1920.txt")


def bst(num):
    l, r = 0, N-1
    while l <= r:
        m = (l+r) // 2
        if a[m] == num:
            return 1
        elif a[m] > num:
            r = m-1
        else:
            l = m+1
    return 0


N, a = int(input()), sorted(list(map(int, input().split())))
# l, r, m으로 값을 찾는다.
# 중간값을 보장하는
M, b = int(input()), list(map(int, input().split()))
F = 0
for i in b:
    print(bst(i))



