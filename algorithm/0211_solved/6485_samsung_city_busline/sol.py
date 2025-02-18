import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    # 첫 번째 테스트케이스
    # 버스 노선 개수
    N = int(input())
    # 각 버스 노선이 정차하는 정류장 범위
    bus_list = [list(map(int, input().split())) for _ in range(N)]
    # 버스 정류장 개수
    P = int(input())
    stop_num = [int(input()) for _ in range(P)]
    cnt_bus = [0] * P
    # 버스 노선 하나씩 불러오기
    for i in range(N):
        # 버스 정류장 번호 확인
        for j in range(P):
            for k in range(bus_list[i][0], bus_list[i][1]+1):
                if k == stop_num[j]:
                    cnt_bus[j] += 1
                    break

    print(f'#{tc} {" ".join(map(str, cnt_bus))}')
