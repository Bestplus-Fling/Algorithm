# 첫번째로 줄은 선 학생은 무조건 0번 번호를 받는다.

N = int(input())
arr = list(map(int, input().split()))
result = []
for i in range(N):
    if not result:
        result.append(i+1)
        continue
    result.insert(len(result) - arr[i], i+1)
print(*result)