import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    # 버스 노선 수 입력
    N = int(input())
    # 각 버스 노선의 시/종점 입력
    bus_list = [list(map(int, input().split())) for _ in range(N)]
    # 버스 정류장의 수 입력
    P = int(input())
    # 버스 정류장 수 만큼 배열을 생성 => 버스가 지나다니는 정류장 위치를 count++
    stp = [0] * P
    for j in range(P):
        # 버스정류장의 번호(위치) 입력
        C = int(input())
        for i in range(N):
            # 버스 정류장이 버스 노선에 포함되어 있다면 해당 정류장 위치 ++
            if C in range(bus_list[i][0], bus_list[i][1]+1):
                stp[j] += 1
    print(f'#{tc} {" ".join(map(str, stp))}')
