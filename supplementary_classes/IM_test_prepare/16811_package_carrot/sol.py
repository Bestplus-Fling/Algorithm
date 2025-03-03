import sys
sys.stdin = open('input.txt', 'r')
#########################################


from collections import deque

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    carrot_list = list(map(int, input().split()))
    deque_carrot = deque(sorted(carrot_list))

    len_over = N // 2

    dict_size = {}
    for sz in carrot_list:
        dict_size[sz] = dict_size.get(sz, 0) + 1
    print(dict_size)

    if max(dict_size.values()) > len_over:
        print(f'#{tc}', -1)
        continue

    carrot_box = []

    box_len = [0] * 3
    if N % 3 == 1:
        box_len[0] = (N//3) + 1
        box_len[1] = box_len[2] = (N//3)
    elif N % 3 == 2:
        box_len[0] = box_len[1] = (N // 3) + 1
        box_len[2] = (N // 3)
    else:
        box_len[0] = box_len[1] = box_len[2] = (N // 3)
    # max_box = 0
    for idx in range(3):
        box = []
        evenly = len(deque_carrot) // (3 - idx)
        while deque_carrot:
            if box:
                if deque_carrot[0] != box[-1]:
                    if idx != 2:
                        if len(box) + dict_size[deque_carrot[0]] > len(deque_carrot) - dict_size[deque_carrot[0]]:
                            break
                    if len(box) >= evenly or len(box) > box_len[idx]:
                        break
            box.append(deque_carrot.popleft())
        carrot_box.append(box)
        # if max_box < len(box):
        #     max_box = len(box)
    # if max_box > len_over:
    #     print(f'#{tc}', -1)
    #     continue

    max_len, min_len = 0, len_over + 1
    for box in carrot_box:
        ch = len(box)
        if len(box) == 0 or len(box) > len_over:
            TF = -1
            break
        if max_len < ch:
            max_len = ch
        if min_len > ch:
            min_len = ch
        TF = max_len - min_len
    print(carrot_box)
    # print(dict_size)
    print(f'#{tc} {TF}')


        # while deque_carrot:
        #     # 박스가 0 이상이고
        #     if box:
        #         # 현재 당근과 박스 마지막 당근이 일치하지 않고
        #         if box[-1] != deque_carrot[0]:
        #             # 한 박스에 담길 당근보다 많이 담겼다면 종료
        #             if len(box) >= len_over:
        #                 break
        #             # 균등 분배해야 되는 경우 종료
        #             if carrot_boxs[-1] != box and len(box) >= len(deque_carrot):
        #                 break
        #     box.append(deque_carrot.popleft())
