import sys
sys.stdin = open('input.txt', 'r')
#####################################

"""
자석의 개수는 4, 각 자석은 8개의 날을 가지고 있다.
하나의 자석이 1칸 회전될 때, 붙어 있는 자석은 서로 붙어 있는 날의 자성이 다를 때만
반대 방향으로 1칸 회전
자석을 회전시키는 방향은 시계방향이 1, 반시계 방향이 -1로 주어진다.
날의 자성은 0이 N극, 1이 S극
각 자석의 날 자성정보는 빨간색의 화살표 위치의 날부터 시계방향 순서로 제시된다.
1번 자석
"""

# 점수 획득표 => index 0번 자리일 때 기준
"""
1번 자석 N극 0점, S극 1점
2번 자석 N극 0점, S극 2점
3번 자석 N극 0점, S극 4점
4번 자석 N극 0점, S극 8점
"""
from pprint import pprint
from collections import deque


def cw(_list, i):
    temp = [_list.pop()]
    # print(_list)
    temp1 = temp + _list
    # print(temp1)
    arr[i] = temp1


def ccw(_list, i):
    queue = deque(_list)
    temp = queue.popleft()
    queue.append(temp)
    temp1 = list(queue)
    arr[i] = temp1


T = int(input())
for tc in range(1, T+1):
    K = int(input())
    arr = [list(input().split()) for _ in range(4)]
    rot = [list(map(int, input().split())) for _ in range(K)]
    # pprint(arr)
    ans_a = 0
    # s: 자석 번호 => s-1로 시작, cw => 회전방향
    for s, c in rot:
        idx = s-1
        # 자기 자리 회전
        if c == 1:         # 7번 -> 0번(pop)
            cw(arr[idx], idx)
            pass
        else:               # 0번 -> 7번(popleft)
            ccw(arr[idx], idx)
            pass
        # 극이 다르면
        # n과 p가 각각 4 이상, 0 미만될때 while 종료
        p, n = idx-1, s
        pr = -c
        nr = -c
        while p >= 0 or n < 4:
            # pprint(arr)
            # print(p, n)
            # print(f'회전방향 prev{pr}, next{nr}')
            if p >= 0:
                # prev 는 prev + 1 의 [6]를 기준으로 [2]랑 비교
                # 극성이 같은 순간, prev~0 까지 회전 금지
                if arr[p][2] == arr[p+1][6-pr]:
                    p = -1
                else:
                    if pr == 1:
                        cw(arr[p], p)
                    else:
                        ccw(arr[p], p)

                    pr = -pr
                    p -= 1

            if n < 4:
                # next 는 next - 1 의 [2]를 기준으로 [6]랑 비교
                # 극성이 같은 순간, next ~ 4 까지 회전 금지
                if arr[n][6] == arr[n-1][2-nr]:
                    n = 4
                else:
                    if nr == 1:
                        cw(arr[n], n)
                    else:
                        ccw(arr[n], n)
                    nr = -nr
                    n += 1

    for j in range(4):
        if arr[j][0] == '1':
            ans_a += 2 ** j
    print(f'#{tc}', ans_a)
