import sys
sys.stdin = open("input.txt", "r")
dx = [-1, 1, 1, -1]
dy = [1, 1, -1, -1]

dic = {
    0: 2,
    1: 3,
    2: 0,
    3: 1,
}


def f(x, y, dir, dessert, check, cnt=0):
    global result
    """
    :param x: 현재 x좌표 
    :param y: 현재 y좌표
    :param dir: 현재 진행방향(0: 우상, 1: 우하, 2: 좌하, 3:좌상) 
    :param dessert: 여태까지 드신 디저트 종류
    :param check: 진행방향 체크(visited)
    :param cnt: 먹은 디저트의 수
    :return: 
    """
    if (x, y) == (i, j):    # 시작 좌표 위치로 돌아왔을 때
        if cnt > 1:    # 4. 하나의 카페에서 디저트를 먹는 것도 안 된다.
            result = max(cnt, result)
            return
    # 3. 카페 투어 중에 같은 숫자의 디저트를 팔고 있는 카페가 있으면 안 된다.
    if data[x][y] in dessert:
        return
    for idx, dxy in enumerate(zip(dx, dy)):
        # 5. 왔던 길을 다시 돌아가는 것도 안 된다.
        if cnt != 0:
            if dic[dir] == idx: continue    # 마주보는 방향으로 이동 금지
            # 이미 진행한 방향으로 이동하는 것도 안된다.
            # 하지만 현재 진행 방향이랑 같다면 상관 없다.
            if check[idx] and idx != dir: continue

        px, py = dxy
        nx, ny = x + px, y + py
        # 2. 카페 투어를 하는 도중 해당 지역을 벗어나면 안 된다.
        if not(0 <= nx < N and 0 <= ny < N): continue
        check[idx] = True
        f(nx, ny, idx, dessert+[data[x][y]], check, cnt+1)
        check[idx] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 1. 대각선 방향으로 움직이고 사각형 모양을 그리며 출발한 카페로 돌아와야 한다.
    data = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    for i in range(N):
        for j in range(N):
            f(i, j, 0, [], [False] * 4)
    print(f'#{tc}', result)
