import sys
sys.stdin = open('input.txt', 'r')
#########################################

'''
원재 썰어버리기 프로젝트
내장함수 대신 수제작 함수 사용하기
split 안쓰고 스택으로 쌓아서 저장
문자인 숫자를 숫자로 바꾸고
그 다음 숫자가 그 전에 숫자보다 작다면 차를 더한다.'''
def max_arr(x):
    max_num, max_idx = 0, -1
    for o in range(x, N):
        if max_num < val_list[o]:
            max_num = val_list[o]
            max_idx = o

    return max_idx


def slicing(tpl):
    idx = 0
    comp_list = []
    temp_num = []
    while len(tpl) != idx:
        if tpl[idx] == ' ':
            comp_list.append(int(''.join(temp_num)))
            temp_num.clear()
            idx += 1
            continue
        temp_num.append(temp_list[idx])
        idx += 1
    comp_list.append(int(''.join(temp_num)))
    return comp_list



T = int(input())  # Test case 개수를 받아오는 코드
for tc in range(1, T + 1):
    N = int(input())
    temp_list = input()
    val_list = slicing(temp_list)
    # print(val_list)
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
