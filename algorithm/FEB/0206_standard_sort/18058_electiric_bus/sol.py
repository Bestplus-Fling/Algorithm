import sys
sys.stdin = open('input.txt', 'r')
#########################################
'''
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서,
중간에 충전기가 설치된 정류장을 만들기로 했다.
버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고,
한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
충전기가 설치된 M개의 정류장 번호가 주어질 때,
최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다.
출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
 
[예시]
다음은 K = 3, N = 10, M = 5, 충전기가 설치된 정류장이 1, 3, 5, 7, 9인 경우의 예이다.

[입력]
첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )
 
[출력]
#과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.
'''
'''
1. 현재 위치 + 이동 가능 거리가 종점에 못미칠 때
1.1 현재 위치(idx)에서 이동 가능한 거리(mov_point)만큼 순회했을 때 이동 가능한 충전소가 존재할 때(in)
1.1.1 가장 먼 거리의 충전소 index를 저장(stp_sign)(마지막에 저장되는 위치가 가장 먼 충전소) 
    ex) 현재 위치 0, 이동 가능 거리 3일때 (정류장 + i) in staging_area가 True면
        정류장 + i 값을 stp_sign에 저장
1.1.2 stp_sign이 staging_area에 없거나, 
1.2.1 이동 가능 거리가 0이 아니고 현재 정류장이 stp_sign에 도달하지 못했을 때(!=) mov_count 1씩 감소
1.2.1.1 만약 이동 가능 거리가 0일 경우 충전 횟수 0으로 초기화 후 break 
1.2.2 현재 정류장이 stp_sign과 일치할 때 mov_count를 K로 초기화, 충전 횟수(stage_count) 증가, 1.1로 재귀

2. 현재 위치 + 이동 가능 거리에 종점이 포함될 때
2.1 for문 break, 충전횟수 출력 
'''
T = int(input())   # Test case 개수를 받아오는 코드(노선 수)
for tc in range(1, T+1):
    """
    '''
    입력: 
    5256_binomial coefficient = 한 번 충전으로 이동 가능한 정류장 수
    n = 종점 정류장 위치
    m = 충전소가 있는 정류장의 수
    staging_area = 충전소가 있는 정류장의 idx 목록
    '''
    K, N, M = map(int, input().split())
    staging_area = list(map(int, input().split()))
    # pass_count : 충전소 리스트 idx, mov_point : 이동 가능한 정류장 수
    pass_count, mov_point = 0, K
    # stage_count : 버스 충전 횟수
    stage_count = 0
    # 멈춰서 충전하는 정류소 저장
    stp_sign = 0
    # 안되는거: 테스트케이스 2번에서 충전소 위치가 범위 안에 없으면 break
    for bus_stop in range(N):
        print(f'현재 정류장{bus_stop}, 이동 가능거리{mov_point}, '
              f'가장 가까운 충전소 위치{staging_area[pass_count]}, 충전 횟수{stage_count}')
        # if mov_point == 0:
        #     break
        # 현재 위치에서 이동 가능한 정류장 수를 더해도 종점에 다다를 수 없으면
        if bus_stop + mov_point < N:
            # 이동 가능한 범위 안에서 가장 먼 충전소가 있는지 확인
            if bus_stop + mov_point >= staging_area[pass_count]:
                # 남은 이동 가능 정류장 수를 순회하면서 이동 가능한 범위에서 가장 멀리 있는 충전소 확인
                for idx in range(1, mov_point):
                    if bus_stop + idx < N and bus_stop + idx + 1 in staging_area:
                        stp_sign = staging_area[pass_count]
                #디버깅용
                if tc == 2 and bus_stop > 1:
                    print(stp_sign)
                # 목표한 위치의 충전소에 도달할때 까지 이동 거리 감소

                if stp_sign != bus_stop:
                    mov_point -= 1
                    # continue
                elif stp_sign == bus_stop:
                    mov_point = K
                    stage_count += 1
        # else:
        #     mov_point -= 1
        if bus_stop == staging_area[pass_count]:
            pass_count += 1
        # if stp_sign != staging_area[pass_count]:
        #     stage_count = 0
        #     break
        # if mov_point == 0 and bus:
        # if bus_stop + mov_point < staging_area[pass_count] and staging_area[pass_count] == bus_stop:
        #     mov_point = K
    """
    K, N, M = map(int, input().split())
    staging_area = list(map(int, input().split()))
    mov_point, stp_sign, stage_count = K, 0, 0
    for bus_stop in range(N):
        if tc == 2:
            print(f'이동해야 할 충전소{stp_sign}, 현재 위치{bus_stop}, '
              f'이동 가능 거리{mov_point} 충전 횟수{stage_count}')
        if bus_stop != 0 and mov_point == 0 and bus_stop != stp_sign:
            stage_count = 0
            break
        if bus_stop + mov_point < N:
            # for문으로 현재 위치부터 이동 가능 거리 내에 충전소가 존재하는지 확인
            for ind in range(0, mov_point+1):
                if bus_stop + ind in staging_area:
                    stp_sign = bus_stop + ind
            if mov_point != 0 and bus_stop != stp_sign:
                mov_point -= 1
            if bus_stop == stp_sign:
                # print('charging')
                mov_point = K - 1
                stage_count += 1
        else:
            break
    print(f'#{tc} {stage_count}')
