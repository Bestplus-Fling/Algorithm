N = int(input())
arr = list(map(int, input().split()))
search_num = int(input())
ans = 0
for num in arr:
    if search_num == num:
        ans += 1
print(ans)