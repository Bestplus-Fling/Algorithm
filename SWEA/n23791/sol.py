import sys
sys.stdin = open('input.txt', 'r')
#####################################

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    s = [list(map(int, input().split())) for _ in range(2)]

    p = [[] for _ in range(N+1)]
    for i in range(N):
        for j in range(2):
            k = s[j][i]
            if p[k]:
                continue
            p[k] = 'B' if j else 'A'
    print(''.join(p[1:v :]))


