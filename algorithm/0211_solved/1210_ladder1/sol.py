import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = 10 # int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    test_case = int(input())
    # i == 0에서 1을 찾아서 시작
    # while True:
        # 현재 위치에서 좌 우를 확인
        # 인덱스가 범위를 벗어나지 않고
            # 좌 우에 1이 있으면
            # 현재 위치를 0으로 변경
            # if copylist[i][j-1] == 1
                # copylist[i][j] = 0
                # j += 1
            # elif list[i][j+1] == 1

                #
                # 이동하면서 현재위치 숫자를 0으로 변경
            # 좌 우에 1이 없으면
                # 아래로 이동
                # 이동하면서 현재위치 숫자를 0으로 변경
