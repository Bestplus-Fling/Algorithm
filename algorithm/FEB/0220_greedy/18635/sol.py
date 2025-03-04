import sys
sys.stdin = open('input.txt', 'r')
#########################################
"""
다음 줄부터 테스트 케이스의 별로 첫 줄에 컨테이너 수 N과 트럭 수 M이, 
다음 줄에 N개의 화물이 무게 wi,
그 다음 줄에 M개 트럭의 적재용량 ti가 주어진다.
"""
"""
# N개의 컨테이너를 M대의 트럭으로 운반하려고 한다
# 트럭당 한 개의 컨테이너 운반 가능 / 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없음
# 최대 M대의 트럭이 편도로 한번만 운행
# 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물 전체 무게가 얼마인지 출력
# 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력
"""
# 1. 컨테이너 무게가 더 크면 컨테이너 shift
# 2. 조건에 부합하면 화물 무게를 result 에 합산하고 컨테이너, 트럭 shift
# 3. 트럭으로 옮길 수 있는 컨테이너가 한대도 없다면 break 후 result 0 출력
T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight_list = sorted(list(map(int, input().split())), reverse=True)
    truck_list = sorted(list(map(int, input().split())), reverse=True)
    i, j = 0, 0
    result = 0
    while i != N and j != M:
        if weight_list[i] > truck_list[j]:
            i += 1
        else:
            result += weight_list[i]
            i += 1
            j += 1
    print(f'#{tc}', result)
