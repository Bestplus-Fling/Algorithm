import sys
sys.stdin = open('1182.txt', 'r')
#########################################

N, S = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0


def sets(i, snum, cnt):
    global ans
    if i == N:
        if snum == S and cnt:
            ans += 1
        return
    sets(i+1, snum+nums[i], cnt+1)
    sets(i+1, snum, cnt)


sets(0, 0, 0)
print(ans)
