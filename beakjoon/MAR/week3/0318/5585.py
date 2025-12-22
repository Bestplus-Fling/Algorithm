import sys
sys.stdin = open('5585.txt', 'r')
#########################################
coin = [500, 100, 50, 10, 5, 1]
pay = 1000 - int(sys.stdin.readline())
idx, ans = 0, 0

while idx < 6:
    ans = pay // coin[idx]
    if ans == 0:
        idx += 1
        continue
    pay -= coin[idx] * ans
    ans += ans
print(ans)
