import sys
from collections import defaultdict
sys.stdin = open('input.txt', 'r')
#####################################

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 버스 노선의 정류장 범위
    bus_routes = [list(map(int, input().split())) for _ in range(N)]
    # 몇 개의 노선이 지나가는 지 확인해야 하는 정류장 개수
    P = int(input())
    p_list = [int(input()) for _ in range(P)]

    # 딕셔너를 활용
    result = defaultdict(int)

    # 주어진 버스 노선을 순회, 각 버스 노선마다 주어진 정류장들이 지나가는 지 확인
    # 지나가면 + 1
    for bus_route in bus_routes:
        # 주어진 정류장들을 지나가는 확인
        for bus_stop in set(p_list):
            if bus_route[0] <= bus_stop <= bus_route[1]:
                result[bus_stop] += 1
    answer = []
    for bus_stop in p_list:
        answer.append(result[bus_stop])

    print(f'#{tc} {answer}')
