N = int(input())
arr = list(map(int, input().split()))
search_num = int(input())
cnt = 0
for num in arr:
    if search_num == num:
        cnt += 1
print(cnt)