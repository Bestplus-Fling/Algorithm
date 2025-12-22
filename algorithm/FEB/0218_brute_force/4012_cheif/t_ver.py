import sys
import itertools
sys.stdin = open('input.txt', 'r')
#########################################


def sum_food_synergy(food_list):
    synergy_list = itertools.combinations(food_list, 2)
    synergy_sum = 0
    for synergy in synergy_list:
        i, j = synergy
        synergy_sum += (matrix_synergy[i][j] + matrix_synergy[j][i])
    return synergy_sum


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    matrix_synergy = [list(map(int, input().split())) for _ in range(N)]
    # print(N, synergy)
    num_list = [i for i in range(N)]

    # A 요리와 B 요리는 식재료를 절반씩 나눠가저야 한다.
    # 절반씩 나눠갖는 조합을 구한다.
    food_comb_list = list(itertools.combinations(num_list, N // 2))
    res = float('inf')
    # print(food_comb_list)

    # 하나의 조합은 A 요리에 들어간다고 생각한다.
    for a_food_list in food_comb_list:
        # B 요리에 들어가는 식재료는 A에 들어가지 않은 식재료다.
        # num_list => 전체 식재료 목록
        # a_food_list => A 요리에 들어갈 식재료 목록
        b_food_list = []
        # 전체 식재료 목록을 돌면서, A 요리에 포함되지 않은 직재료들을 B 요리의 식재료로 넣는다.
        b_food_list = [num for num in num_list if num not in a_food_list]

        # 각 요리에 포함된 식재료들의 시너지를 확인
        a_synergy_sum = sum_food_synergy(a_food_list)
        b_synergy_sum = sum_food_synergy(b_food_list)
        # 두 요리의 맛 차이
        food_score = abs(a_synergy_sum - b_synergy_sum)
        res = min(res, food_score)  # 음식 맛의 차이가 기존 res 값보다 작으면 갱신
    print(f'#{tc}', res)
    # break
