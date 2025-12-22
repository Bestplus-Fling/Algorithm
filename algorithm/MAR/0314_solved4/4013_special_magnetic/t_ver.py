import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
#####################################

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    magnet_list = [deque(list(map(int, input().split()))) for _ in range(4)]
    rotate_info_list = [list(map(int, input().split())) for _ in range(K)]
    score_sum = 0


    def rotate_magent(mag, rot):
        # mag: 자석 번호, rot: 회전해야하는 방향, vit: 방문 여부 및 회전 방향
        if visited[mag] != 0:
            return

        visited[mag] = rot

        if mag == 0:
            if magnet_list[mag][2] != magnet_list[mag+1][6]:
                rotate_magent(mag+1, -rot)
        elif mag == 4:
            if magnet_list[mag-1][2] != magnet_list[mag][6]:
                rotate_magent(mag-1, -rot)
        elif mag == 1 or mag == 2:
            if magnet_list[mag][2] != magnet_list[mag+1][6]:
                rotate_magent(mag+1, -rot)
            if magnet_list[mag][6] != magnet_list[mag-1][2]:
                rotate_magent(mag-1, -rot)


    # 주어진 rotate_info_list(회전 정보)에 따라서 각 자석을 회전
    for rotate_info in rotate_info_list:
        magnet_num, rotate_dir = rotate_info

        # 방문처리 + 각 자석이 어떤 방향으로 회전할 지 저장하는 용도
        visited = [0] * 4

        # 자석을 돌리는 함수
        rotate_magent(magnet_num-1, rotate_dir)

        for i, v in enumerate(visited):
            if v != 0:
                magnet_list[i].rotate(v)

    score_list = [1, 2, 4, 8]
    for i in range(4):
        if magnet_list[i][0]:
            score_sum += score_list[i]

    print(f"#{tc}", score_sum)