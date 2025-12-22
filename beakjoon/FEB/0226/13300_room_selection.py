# 남학생은 남학생끼리, 여학생은 여학생끼리
# 한 방에는 같은 학년만, 한 명만 배정 가능
# N : 수학여행 참여 인원
# K : 한 방에 배정 가능 인원
N, K = map(int, input().split())
arr = [[0] * 6 for _ in range(2)]
for _ in range(N):
    sex, cls = map(int, input().split())
    arr[sex][cls-1] += 1

count = 0
for i in range(2):
    for j in range(6):
        if not arr[i][j]:
            continue
        count += (arr[i][j] // K) + (1 if arr[i][j] % K > 0 else 0)
print(count)
