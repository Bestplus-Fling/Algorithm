import sys
sys.stdin = open('input.txt', 'r')
#########################################


def is_babygin(count_list):

    babygin = 0
    idx = 0
    while idx < 10:
        # triplet 인지 확인
        # 해당 숫자의 개수가 3 이상이면 triplet
        if count_list[idx] >= 3:
            babygin += 1
            count_list[idx] -= 3
            continue
        # run 인지 확인
        # 해당 숫자의 갯수가 1 이상이면 가능성 있음
        if idx < 8 and count_list[idx] >= 1 and count_list[idx+1] >= 1 and count_list[idx+2] >= 1:
            # run!
            babygin += 1
            for j in range(3):
                count_list[idx+j] -= 1
            continue
        idx += 1

    return babygin == 2


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    card_list = list(map(int, input().strip()))
    # 카드 숫자의 개수를 세어서 run, triplet인지 확인

    count_list = [0] * 10   # 카드 번호별 (인덱스)로 0값 초기화
    # 카드 번호를 계수
    for i in card_list:
        count_list[i] += 1
    result = 'false'
    if is_babygin(count_list):
        result = 'ture'
    print(f'#{tc}', result)
