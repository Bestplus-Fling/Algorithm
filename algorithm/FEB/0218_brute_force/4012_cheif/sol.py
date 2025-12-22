import sys
sys.stdin = open('input.txt', 'r')
#########################################

"""
N개의 식재료가 있다.(짝수)
식재료들을 각각 N/2개씩 나누어 두 개의 요릐를 하려고 한다
A와 B 음식의 맛의 차이가 최소가 되도록 재료를 배분해야 한다.
식재료 i는 식재료 j와 같이 요리하게 되면 궁합이 잘 맞아 시너지 Sij가 발생
세로 i, 가로 j일때 어떤 식재료로 완성된 요리 A와 B의 최소차를 찾는다.
"""

from itertools import combinations

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    num = [_ for _ in range(N)]
    # 재료를 반 나눠서
    _list = list(combinations(num, N//2))

    _min = float('inf')
    for i in range(len(_list)):
        temp = [_ for _ in num if _ not in _list[i]]
        A_ingredient = list(combinations(_list[i], 2))
        B_ingredient = list(combinations(temp, 2))
        A_food, B_food = 0, 0
        for iA1, iA2 in A_ingredient:
            A_food += S[iA1][iA2] + S[iA2][iA1]
        for iB1, iB2 in B_ingredient:
            B_food += S[iB1][iB2] + S[iB2][iB1]
        _min = min(_min, abs(A_food - B_food))
    print(f'#{tc}', _min)


# for fA1, fA2 in combinations(_list[i], 2):
#     food_A = S[fA1][fA2] + S[fA2][fA1]
# for fB1, fB2 in combinations(temp, 2):
#     # print(fB1, fB2, end=' /')
#     food_B = S[fB1][fB2] + S[fB2][fB1]
#     # print(food_A, food_B)
# _min = min(_min, abs(food_A - food_B))
#
# print()
# food_0B = (S[_list[-1-i][0]][_list[-1-i][1]] + S[_list[-1-i][1]][_list[-1-i][0]])