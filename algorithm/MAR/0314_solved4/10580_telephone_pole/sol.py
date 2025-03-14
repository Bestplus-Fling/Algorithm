import sys
sys.stdin = open('input.txt', 'r')
#####################################

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    line = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for S, E in line:
        if S == E:
            continue
        for i in range(N):
            if line[i] == (S, E):
                continue
            cs, ce = line[i]
            if S < cs and ce < E:
                ans += 1
    print(f'#{tc}', ans)