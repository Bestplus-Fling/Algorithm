import sys
sys.stdin = open("1931.txt", "r")

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr = sorted(arr, key=lambda x: (x[1], x[0]))
ans, time = 0, 0
for st, ed in arr:
    if st < time:
        continue
    time = ed
    ans += 1
print(ans)