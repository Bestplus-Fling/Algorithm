import sys
sys.stdin = open('input.txt', 'r')
#####################################

"""
원자들이 움직일 수 있는 좌표 범위에 제한은 없다
원자들은 동시에 1초에 이동 방향으로 1만큼 이동한다
원자들은 2개 이상의 원자들이 서로 충돌할 경우 보유한 에너지를 방출, 바로 소멸
이때 방출하는 에너지의 총합을 구한다.
"""

d = {0: 1, 1: 0, 2: 3, 3: 2}

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    vit = [False] * N
    for i in range(N):
        x, y, dist, e = map(int, input().split())
        x, y = x*2, y*2
        arr.append([y, x, dist, e])
    result = 0
    for i in range(N):
        if vit[i]:
            continue
        x1, y1, d1, e1 = arr[i]
        for j in range(N):
            if j == i or vit[j]:
                continue
            x2, y2, d2, e2 = arr[j]
            #
            if d[d1] == d2:
                if d[d1] == d2 and (x1 <= x2 or x1 >= x2 or y1 <= y2 or y1 >= y2):
                    result += e1 + e2
                    vit[i], vit[j] = True, True
                break
    print(result)