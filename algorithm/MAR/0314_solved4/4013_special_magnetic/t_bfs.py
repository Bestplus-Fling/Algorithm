import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
#####################################

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
        queue = deque([[magnet_num-1, rotate_dir]])

        while queue:
            mag_idx, rotate = queue.popleft()
            visited[mag_idx] = True

            if mag_idx != N-1:  # 마지막 톱니바퀴가 아니라면, 모두 오른쪽자석과 비교한다.
                if magnet_list[mag_idx][RIGHT_POS] != magnet_list[mag_idx+1][LEFT_POS]:
                    if not visited[mag_idx+1]:  # 방문한 적 없으면
                        queue.append([mag_idx+1, -rotate])
            if mag_idx != 0:
                if magnet_list[mag_idx][LEFT_POS] != magnet_list[mag_idx-1][RIGHT_POS]:
                    if not visited[mag_idx-1]:
                        queue.append([mag_idx-1, -rotate])
            if rotate == 1:
                magnet_list[mag_idx].rotate(1)
            else:
                magnet_list[mag_idx].rotate(-1)
    for i in range(N):
        if magnet_list[i][0]:
            score_sum += 2 ** i
    print(f"#{tc}", score_sum)