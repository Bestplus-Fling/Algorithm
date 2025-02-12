import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = 10 # int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    # 상자의 개수 입력
    N = int(input())

    # 상자 높이 입력
    box_list = list(map(int, input().split()))
    # N + 1의 의미: 평탄화가 끝나고 한번 더 순회하면서 최대최소값을 확인해서 출력하기 위함
    for j in range(N+1):
        # 값을 수정하기 위해 index를 가지는 변수 선언
        max_idx = min_idx = -1
        # 상자 입력 값 0 < box <= 100이므로 최대 최소값 저장하는 변수 선언
        max_val, min_val = 0, 101

        # 박스를 순회하면서 가장 높은/가장 낮은 박스 확인
        for i in range(len(box_list)):
            if max_val < box_list[i]:
                max_val = box_list[i]
                max_idx = i
            if min_val > box_list[i]:
                min_val = box_list[i]
                min_idx = i
        # 박스 순회가 끝나면 가장 높은 박스 - 1 / 가장 낮은 박스 + 1
        if j != N:
            box_list[min_idx] += 1
            box_list[max_idx] -= 1

    print(f'#{tc} {max_val - min_val}')
