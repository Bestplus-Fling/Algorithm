import sys
sys.stdin = open('input.txt', 'r')
#####################################
"""
손해를 보지 않으면서 홈방범 서비스를 가장 많은 집들에 제공하는 서비스 영역을 찾고
홈 방범 서비스를 제공 받는 집들의 수를 출력
M = 하나의 집이 지불하는 방범비용
"""


# 함수 1: 다이아몬드 탐색
def diamond(dx, dy, st, ed):
    # 집 개수 확인
    count = 0
    for i in range(_len):
        x = dx + i
        if 0 <= x < N:
            for j in range(st, ed):
                y = dy + j
                # 좌표가 음수일 경우도 있어서, 범위 안에 들어왔을 때랑,
                # 집이 있을 때만 동작할 수 있도록 설정
                if not (0 <= y < N) or not town[x][y]:
                    continue
                count += 1
        # 다이아몬드 크기 증가/감소
        if i < c:
            st -= 1
            ed += 1
        else:
            st += 1
            ed -= 1
    return count


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    town = [list(map(int, input().split())) for _ in range(N)]
    ans_a = 0
    house = 0
    for a in range(N):
        house += town[a].count(1)
    # 다이아몬드 만들기
    for k in range(1, N*2):
        # 지불해야 하는 이용료 공식
        payment = (k * k) + ((k - 1) * (k - 1))
        # 총 주택수보다 지불 비용이 커지는 시점에서 종료
        if house * M < payment:
            break
        # 다이아몬드를 만들기 위한 길이를 확인(항상 홀수여야 한다)
        _len = (k * 2) - 1
        # 다이아몬드의 중심점을 확인
        c = _len // 2

        # 다이아몬드의 중심점을 0~N-1 사이에서 순회할 수 있도록 했음
        for ni in range(-c, N+c):
            for nj in range(-c, N+c):
                temp = diamond(ni, nj, c, c+1)
                cost = temp * M
                """
                # 가장 많은 주택에 공급할 수 있는 조건
                1. 현재 ans에 저장된 주택 수보다 temp가 더 많을 때
                2. 서비스 이용료가 수익보다 많은 시점(=손해가 아닐 때)
                """
                if temp > ans_a and cost-payment >= 0:
                    ans_a = temp
    print(f'#{tc}', ans_a)
