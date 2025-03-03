import sys
sys.stdin = open('input.txt', 'r')
#########################################

"""
한 복도에는 1 이상 100 이하의 정수로 구분되는 100개의 버튼이 존재
버튼 K는 복도의 시작점에서 K미터 떨어짐, 두 로봇의 시작점은 버튼 1
매 1초마다, 로봇은 복도의 양 방향 중 하나로 1m 이동하거나
자기 위치에 있는 버튼을 누르거나 아무것도 하지 않는다.
"""


from collections import deque


def select_button():
    lgc_lst, _O, _B = [], [], []
    for i in range(int(N)):
        button = buttons[i]
        lgc_lst.append((button[0], int(button[1:])))
        if button[0] == 'B':
            _B.append((button[0], int(button[1:])))
        else:
            _O.append((button[0], int(button[1:])))

    return lgc_lst, _B, _O


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, *input_button = input().split()
    buttons = [''.join(input_button[_:_ + 2]) for _ in range(0, int(N) * 2 - 1, 2)]
    # B랑 O를 나눠서 리스트에 저장
    logic_list, B_list, O_list = select_button()
    logic_list, B_list, O_list = deque(logic_list), deque(B_list), deque(O_list)
    print(logic_list, B_list, O_list)
    """
    시간의 흐름을 똑같이 가기
    현재 위치가 버튼이면 카운팅하고 대기
        만약 버튼에 위치에 동시에 도달하면, O를 우선적으로 누르고 대기
    현재 위치가 버튼이 아니면 이동
    """
    time = 0
    B_way, O_way = 1, 1
    # 버튼을 누른 횟수 확인
    while logic_list:
        who_mov_now = logic_list[0][0]
        if B_list:
            B_point = B_list[0][1]
        if O_list:
            O_point = O_list[0][1]
        # 현재 로직이 O가 움직여야 한다면
        if who_mov_now == 'O':
            # 이동할 버튼위치와 현재 위치가 같다면
            # 버튼 누른 횟수 증가, 이동할 위치 갱신
            if O_point == O_way:
                O_list.popleft()
                logic_list.popleft()
        elif who_mov_now == 'B':
            if B_point == B_way:
                B_list.popleft()
                logic_list.popleft()
            # 아직 버튼에 도착 못하면 계속 이동
        # 다음 버튼 이동 위치가 현재 위치보다 큰 수라면 앞으로 이동
        if O_point > O_way:
            O_way += 1
        # 아니라면 뒤로 이동
        elif O_point < O_way:
            O_way -= 1
        if B_point > B_way:
            B_way += 1
        elif B_point < B_way:
            B_way -= 1
        time += 1
    print(f'#{tc} {time}')
