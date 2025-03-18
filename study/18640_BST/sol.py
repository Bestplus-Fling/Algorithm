import sys
sys.stdin = open('input.txt', 'r')
#########################################


def bst(num, left, right):
    check = 0
    while left <= right:
        m = (left+right) // 2
        if a_list[m] == num:
            return 1
        elif a_list[m] < num:
            if check == 1:
                return 0
            check = 1
            left = m+1
        else:
            if check == -1:
                return 0
            check = -1
            right = m-1
    return 0
    pass


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a_list = sorted(list(map(int, input().split())))
    b_list = list(map(int, input().split()))
    result = 0
    for b_num in b_list:
        if bst(b_num, 0, N-1):
            result += 1
    print(f'#{tc}', result)
