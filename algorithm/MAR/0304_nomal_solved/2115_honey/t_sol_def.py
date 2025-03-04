import sys
import itertools
sys.stdin = open('input.txt', 'r')
#####################################

"""
일꾼 1과 일꾼 2의 벌통의 개수(M) 만틈 선택을 하고(모든 경우에 대해서),
그 선택한 벌통의 부분집합을 구하고, 각 부분집합들의 최대 이익을 구하고, 거기서 최대 수익을 찾자
"""


def cal_square_sum(num_list):
    if sum(num_list) > C:
        return 0
    return sum(num ** 2 for num in num_list)


T = int(input())
for tc in range(1, T+1):
    # N = 벌통의 크기, M = 벌통의 개수, C = 꿀을 채취할 수 있는 최대 양
    N, M, C = list(map(int, input().split()))
    honey_matrix = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0

    # 일꾼 1이 전체적으로 순회를 한다.
    # 단, 벌통의 개수(M) 직전까지만 순회를 한다.
    for fst_i in range(N):  # 첫 번째 일꾼의 i(행)
        for fst_j in range(N-M+1):  # 첫 번째 일꾼의 j(열), 꿀통은 열로 연속되어야 한다.
            # 슬라이싱을 이용해서 첫 번째 일꾼이 선택한 꿀통만 가져온다.
            fst_select_honey_list = honey_matrix[fst_i][fst_j: fst_j + M]

            # 가져온 꿀통에서 최대 이익을 구해야 한다.
            # 부분집합을 구한 다음에, 거기서 최대 이익을 구한다.
            fst_select_honey_max = 0
            # 부분집합 => 모든 조합의 경우의 수
            for select_cnt in range(1, M+1):
                comb = itertools.combinations(fst_select_honey_list, select_cnt)
                max_honey_list = list(map(cal_square_sum, comb))
                fst_select_honey_max = max(fst_select_honey_max, max(max_honey_list))
        # 두 번째 일꾼이 벌통을 골랐을 경우
        # 첫 번째 일꾼이 고른 같은 행, 그 이후 열부터 고를 수 있다.
        for snd_i in range(fst_i, N):
            for snd_j in range(0, N-M+1):   # M 만큼 선택했을 때 인덱스가 겹치지 않게 설정
                # 같은 행, 두 번째 일꾼의 열이 첫 번째 일꾼의 열보다 작으면 skip
                if snd_i == fst_i and snd_j < fst_j + M: continue
                snd_select_honey_list = honey_matrix[snd_i][snd_j:snd_j + M]

                # 가져온 꿀통에서 최대 이익을 구해야 한다.
                # 부분집합을 구한 다음에, 거기서 최대 이익을 구한다.
                snd_select_honey_max = 0
                # 부분집합 => 모든 조합의 경우의 수
                for select_cnt in range(1, M + 1):
                    comb = itertools.combinations(snd_select_honey_list, select_cnt)
                    max_honey_list = list(map(cal_square_sum, comb))
                    snd_select_honey_max = max(snd_select_honey_max, max(max_honey_list))
                max_sum = max(max_sum, fst_select_honey_max + snd_select_honey_max)

    print(f'#{tc} {max_sum}')
