import sys
sys.stdin = open('input.txt', 'r')
#####################################


for tc in range(int(input())):
    N = int(input())
    bus_line = [tuple(map(int, input().split())) for _ in range(N)]
    P = int(input())
    ans = [0] * P
    for idx in range(P):
        C = int(input())
        for start, end in bus_line:
            if start <= C <= end:
                ans[idx] += 1
    print(f'#{tc+1}', *ans)
