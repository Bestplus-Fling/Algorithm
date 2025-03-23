# 스타트 팀과 링크 팀의 시너지 최소값을 출력
import sys
sys.stdin = open("14889.txt")
from itertools import combinations


def f(p):
    c = 0
    for i in range(M):
        x = p[i]
        for j in range(M):
            if i == j: continue
            y = p[j]
            c += arr[x][y]
    return c


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
M = N // 2
player = [i for i in range(N)]
select = list(combinations(player, M))
ans = float('inf')
for k in range(len(select)//2):
    start = f(select[k])
    link = f(select[-(k+1)])
    ans = min(ans, abs(start-link))
print(ans)
