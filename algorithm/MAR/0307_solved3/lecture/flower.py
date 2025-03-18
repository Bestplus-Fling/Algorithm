import sys
sys.stdin = open('flower.txt', 'r')
#####################################

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 방법 1
    # date = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda tpl: tpl[1])
    date = [tuple(map(int, input().split())) for _ in range(N)]
    # start = date[0][0]
    # end = date[-1][-1]
    ans_a = [0] * 100001
    # print(start, end)
    # idx = 0
    for i in range(N):
        st, ed = date[i]
        for j in range(st, ed):
            if not ans_a[j]:
                ans_a[j] = 1

    print(ans_a.count(1))

    # # 방법 2
    # for i in range(N):
    #     a, b = map(int, input().split())
    #     for j in range(a, b):
    #         ans[j] = 1



