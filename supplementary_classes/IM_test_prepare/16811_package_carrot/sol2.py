import sys
sys.stdin = open('input.txt', 'r')
#########################################


def search_carrot():
    temp = []
    min_diff = 1e6
    carrot_dict = {}
    for _ in carrot_list:
        carrot_dict[_] = carrot_dict.get(_, 0) + 1

    for i in range(1, 30):
        for j in range(i+1, 31):
            small, medium, large = 0, 0, 0
            for s in range(i):
                small += carrot_dict.get(s, 0)
            for m in range(i, j):
                medium += carrot_dict.get(m, 0)
            for l in range(j, 31):
                large += carrot_dict.get(l, 0)
            # print(small, medium, large)
            if 0 < small <= (N // 2) and 0 < medium <= N // 2 and 0 < large <= N // 2:
                temp = max(small, medium, large) - min(small, medium, large)
                if min_diff > temp:
                    min_diff = temp
    if min_diff == 1e6:
        return -1
    return min_diff


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    carrot_list = list(sorted(list(map(int, input().split()))))
    print(f'#{tc} {search_carrot()}')







