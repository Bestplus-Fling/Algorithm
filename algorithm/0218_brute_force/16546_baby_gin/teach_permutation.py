import sys
sys.stdin = open('input.txt', 'r')
#########################################


from itertools import permutations


# 숫자가 1씩 순증하는지 확인
def is_run(target):
    # target 의 길이는 3으로 상정하고 함수를 작성
    return (target[0] + 1 == target[1]) and (target[1] + 1 == target[2])


def is_triplet(target):
    # 방법 1. 직접 카운트
    # count = 0
    # for card in target:
    #     if target[0] == card:
    #         count += 1
    # return count == 3

    # 방법 2. set 의 특성 이용
    return len(set(target)) == 1


def is_babygin(target):
    num1 = target[:3]
    num2 = target[3:]

    # run 이나 triplet 이면 result 는 0이 아닌 1이 들어간다
    result1 = is_run(num1) + is_triplet(num1)   # 앞 숫자에 대한 run/triplet 확인
    result2 = is_run(num2) + is_triplet(num2)   # 뒤 숫자에 대한 run/triplet 확인

    return (result1 + result2) == 2     # result1, result2 둘 다 조건에 부합하면 결과는 2가 출력


T = int(input())  # Test case 개수를 받아오는 코드
for tc in range(1, T + 1):
    card_list = list(map(int, input().strip()))

    result = 'false'
    for target in permutations(card_list):
        if is_babygin(target):
            result = 'true'
            break
    print(f'#{tc} {result}')

