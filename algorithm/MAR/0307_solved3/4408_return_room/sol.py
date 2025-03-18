import sys
sys.stdin = open('test.txt', 'r')
#####################################

room = [[i for i in range(1, 400, 2)], [i for i in range(2, 401, 2)]]


def check():
    visited = [False] * 400


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    students = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda tpl: tpl[1])
    ans_a = 1
    for i in range(N-1):
        start = students[i + 1][0]
        end = students[i + 1][1] + 1
        direction = 1
        if start > end:
            direction = -1
            end -= 2
        if students[i][1] in range(start, end, direction):
            ans_a += 1
    print(f'#{tc}', ans_a)
