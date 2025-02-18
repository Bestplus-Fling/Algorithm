import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = 10 # int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    # 입력 : N(건물의 개수) / arr(건물의 높이)
    N = int(input())
    arr = list(map(int, input().split()))
    # result = 0
    # for i in range(2, N-2):
    #     slice_arr = arr[i-2:i+3]
    #     mid_t = slice_arr[2]
    #     cnt, next_high_t = 0, 0
    #     for j in range(5):
    #         if j != 2 and mid_t > slice_arr[j]:
    #             cnt += 1
    #             if next_high_t < slice_arr[j]:
    #                 next_high_t = slice_arr[j]
    #     if cnt == 4:
    #         result += mid_t - next_high_t
    # print(f'#{tc} {result}')
    building_list = arr

    total = 0 # 조망권을 누적하기 위한 변수
    for idx in range(N):
        if not building_list[idx]: #빌딩이 없다면 skip!
            continue

        #빌딩이 존재
        # 현재 위치 = building_list[idx]
        # 왼쪽 두 칸 = building_lsit[idx -2]
        # 왼쪽 한 칸 = building_lsit[idx -1]
        # 오른쪽 한 칸 = building_lsit[idx +1]
        # 오른쪽 두 칸 = building_lsit[idx +2]

        # 주변 빌딩 중 가장 높은 빌딩을 찾자
        max_height = 0
        for delta in [-2, -1, 1, 2]:
            if 0 <= idx+delta < N-1:
                if max_height < building_list[idx + delta]: # 주변 빌딩 높이
                    max_height = building_list[idx + delta]

            #building_list[idx + delta] # 주변 빌딩 높이

        # print(max_height)
        # 조망권이 있다는 것은 현재 빌딩 보다 max_height가 더 작아야 함
        if building_list[idx] > max_height:
            total += (building_list[idx] - max_height)
    print(f'#{tc} {total}')