import sys
sys.stdin = open('input.txt', 'r')
#########################################
"""
0시부터 다음날 0시 이전까지 A 도크의 사용신청을 확인, 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록
최대 몇 대의 화물차가 이용할 수 있는지 확인
"""
# 1. 종료시간을 기준으로 정렬
# 2. 가장 짧은 작업시간을 가진 작업을 먼저 실행 / 횟수 count
# 3. 종료한 시간을 기점으로 시작할 수 있는 작업이 있다면 2번으로 이동
T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    # 도크 사용 종료 시점을 기준으로 오름차순 정렬
    timeline = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda tpl: tpl[1])
    t, idx, cnt = 0, 0, 0
    # 24시를 넘어가거나 모든 사용신청 내역을 확인하면 while 문 종료
    while t <= 24:
        if idx == N:
            break
        # 현재 시간을 기준으로 사용신청한 내용이 있다면
        if timeline[idx][0] == t:
            # count / 시간을 도크 사용 종료 시점으로 갱신 / 다음 신청내용을 확인
            cnt += 1
            t = timeline[idx][1]
            idx += 1
            continue
        # 현재 확인중인 신청내역의 시작시간이 이미 지났다면 다음 신청내역을 확인
        elif timeline[idx][0] < t:
            idx += 1
            continue
        # 시간이 흐르는 조건
        # 1. 도크 사용 후
        # 2. 지금 시간이 현재 확인중인 신청 내역의 시작시간에 미치지 못했을 때
        t += 1
    print(f'#{tc}', cnt)
