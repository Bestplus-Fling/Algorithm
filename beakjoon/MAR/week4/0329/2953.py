import sys
# sys.stdin = open("2953.txt")

N = 5
score = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_score = 0
max_idx = 0
for i in range(N):
    sum_score = sum(score[i])
    if max_score < sum_score:
        max_idx = i + 1
        max_score = sum_score
print(max_idx, max_score)
