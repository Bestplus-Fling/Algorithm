import sys
sys.stdin = open('input.txt', 'r')


def carrot():
    C_cnt = [0] * 31
    for n in range(N):
        C_cnt[Ci[n]] += 1
    min_diff = 1e10
    for i in range(1, 30):
        for j in range(i + 1, 31):
            small = 0
            medium = 0
            large = 0
            for s in range(i):
                small += C_cnt[s]
            for m in range(i, j):
                medium += C_cnt[m]
            for l in range(j, 31):
                large += C_cnt[l]
            if 0 < small <= N // 2 and 0 < medium <= N // 2 and 0 < large <= N // 2:
                diff = max(small, medium, large) - min(small, medium, large)
                if diff < min_diff:
                    min_diff = diff
    if min_diff == 1e10:
        return -1
    return min_diff

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    Ci = list(map(int, input().split()))
    print(f'#{t} {carrot()}')