import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = 10 # int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):

    # 찾아야 하는 회문의 길이 입력
    N = int(input())
    # 하드코딩 방지용(배열은 항상 8 X 8)
    F = 8

    # 글자판 입력
    word_list = [input() for _ in range(F)]
    # 입력한 글자판을 90도 회전 => 세로 회문 확인
    cir_list = list(zip(*word_list[::-1]))
    print(cir_list)
    break
    # 회문의 개수 확인
    # sum_val = 0
    # for i in range(F):
    #     for j in range(F):
    #         cnt = 0
    #         # j 위치에서 j부터 회문 길이(j+N-1)가 인덱스를 벗어나면 탐색 X
    #         if 0 <= j+N-1 < F:
    #             # 회문 길이만큼 슬라이싱 후 확인
    #             temp1 = word_list[i][j:j+N]
    #             temp2 = cir_list[i][j:j+N]
    #             if int(temp1[::] == temp1[::-1]):
    #                 cnt += 1
    #             if int(temp2[::] == temp2[::-1]):
    #                 cnt += 1
    #         sum_val += cnt
    # print(f'#{tc} {sum_val}')