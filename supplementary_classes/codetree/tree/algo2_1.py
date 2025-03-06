import sys
sys.stdin = open("input2_3.txt")


n, m = map(int, input().split())
a = list(map(int, input().split()))

# M 개의 비어있는 의자, 순서대로 1번부터 M번 번호
# 사람들이 앉고자 하는 의자에 대한 정보 ai
# ai = 1 이상, M 이하 / i번째 사람은 1 이상 ai 이하 의자에만 앉고 싶다
# 1번 사람부터 순서대로 규칙에 맞게 앉는다.
# 최초로 앉지 못하는 사람이 생기면 종료

arr = [0] * (m+1)
ans = 0
for i in range(n):
    if not arr[a[i]]:
        arr[a[i]] = 1
        continue
    idx = a[i]
    while arr[idx]:
        idx -= 1
        if idx == 0:
            break
    if idx <= 0:
        ans = i
        break
    arr[idx] = 1
print(ans)

