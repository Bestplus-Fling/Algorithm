import sys
sys.stdin = open('input.txt', 'r')
#########################################

from collections import deque

T = int(input())  # Test case 개수
for tc in range(1, T + 1):
    N = int(input())
    carrot_list = list(map(int, input().split()))

    # N // 2 기준 계산
    len_over = N // 2

    # 각 크기별 당근 개수 확인
    carrot_count = {}
    for carrot in carrot_list:
        carrot_count[carrot] = carrot_count.get(carrot, 0) + 1

    # (1) 한 상자에 N//2 초과하는 경우 -1
    if max(carrot_count.values()) > len_over:
        print(f'#{tc} -1')
        continue

    # (2) 상자 크기 결정
    box_size = [N // 3] * 3
    if N % 3 == 1:
        box_size[0] += 1
    elif N % 3 == 2:
        box_size[0] += 1
        box_size[1] += 1

    # (3) 당근 크기별로 정렬 (값과 개수 함께 저장)
    carrot_items = deque(sorted(carrot_count.items()))

    # (4) 상자 초기화
    carrot_boxes = [[] for _ in range(3)]

    # (5) 당근 분배 (같은 당근은 반드시 같은 상자에 담기도록 수정)
    for idx in range(3):
        while carrot_items and len(carrot_boxes[idx]) < box_size[idx]:
            carrot, count = carrot_items.popleft()

            # 현재 상자에 넣을 수 있는 최대 수량
            to_add = min(count, box_size[idx] - len(carrot_boxes[idx]))

            # 상자에 추가 (같은 당근은 같은 상자에 넣음)
            carrot_boxes[idx].extend([carrot] * to_add)
            count -= to_add

            # 남은 당근 다시 큐에 삽입 (다른 상자로 분배하지 않음)
            if count > 0:
                carrot_items.appendleft((carrot, count))

    # (6) 상자 내 개수 검증
    max_len = max(len(box) for box in carrot_boxes)
    min_len = min(len(box) for box in carrot_boxes)

    # (7) 빈 상자 혹은 초과 여부 확인
    if any(len(box) == 0 or len(box) > len_over for box in carrot_boxes):
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max_len - min_len}')
