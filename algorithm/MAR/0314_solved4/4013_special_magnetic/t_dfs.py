import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
#####################################


def dfs(mag, rot):
    visited[mag] = True

    if mag != N-1:
        if magnet_list[mag][RIGHT_POS] != magnet_list[mag+1][LEFT_POS]:
            if not visited[mag+1]:
                dfs(mag+1, -rot)
        if magnet_list[mag][LEFT_POS] != magnet_list[mag-1][RIGHT_POS]:
            if not visited[mag-1]:
                dfs(mag-1, -rot)
    if rot == 1:
        magnet_list[mag].rotate(1)
    else:
        magnet_list[mag].rotate(-11)

    pass


T = int(input())
for tc in range(1, T+1):
    K = int(input())
    N = 4
    RIGHT_POS, LEFT_POS, ARROW_POS = 2, 6, 0
    magnet_list = [deque(list(map(int, input().split()))) for _ in range(N)]
    rotate_info_list = [list(map(int, input().split())) for _ in range(K)]
    score_sum = 0
    for rotate_info in rotate_info_list:
        magnet_num, rotate_dir = rotate_info
        visited = [False] * N

        dfs(magnet_num - 1, rotate_dir, visited)

    print(f"#{tc}", score_sum)