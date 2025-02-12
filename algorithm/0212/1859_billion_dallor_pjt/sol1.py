import sys
sys.stdin = open('input.txt', 'r')
#########################################


def max_arr(x):
    max_num, max_idx = 0, -1
    for o in range(x, N):
        if max_num < val_list[o]:
            max_num = val_list[o]
            max_idx = o

    return max_idx


T = int(input())  # Test case 개수를 받아오는 코드
for tc in range(1, T + 1):
    N = int(input())
    val_list = list(map(int, input().split()))
    tax_coming = 0
    max_val = max(val_list[:])   # max_arr(0)
    stack = []
    idx = 0
    for i in range(N):
        if max_val > val_list[i]:
            stack.append(val_list[i])
            continue
        if max_val == val_list[i]:
            while stack:
                tax_coming += max_val - stack.pop()
            if i == N-1:
                continue
            max_val = max(val_list[i + 1:])
        else:
            break

    print(f'#{tc} {tax_coming}')
