import sys
sys.stdin = open('input.txt', 'r')
#####################################

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 도크를 사용하려는 시작, 종료 시간을 입력, 종료시간을 우선 오름차순 정렬
    timeline = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda tpl: tpl[1])
    # 도크 사용하는 화물차의 수, 시간 확인용 변수
    ans, time = 0, 0
    for start, end in timeline:
        # 현재 시간을 기준으로 사용시작시간이 더 크거나 같다면(사용 가능하다면)
        if time <= start:
            ans += 1    # 사용 횟수 증가
            time = end  # 시간을 도크 사용 종료시간으로 변경
    # 최종 횟수 출력
    print(f'#{tc}', ans)
    # print(timeline)
    # idx, time, ans = 0, 1, 0
    # while idx != N:
    #     start, end = timeline[idx]
    #     # print(start, end)
    #     if start == time:
    #         ans += 1
    #         idx += 1
    #         time = end
    #         continue
    #     if timeline[idx][0] < time:
    #         idx += 1
    #         continue
    #     time += 1
