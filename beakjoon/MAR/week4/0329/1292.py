import sys
sys.stdin = open("1292.txt")

s, e = map(int, input().split())
ans = 0
nums = []
for i in range(1, 46):
    nums.extend([i]*i)
for i in range(s, e+1):
    ans += nums[i-1]
print(ans)
