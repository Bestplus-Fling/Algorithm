import sys
sys.stdin = open('input.txt', 'r')
#########################################


def search_max(tmp_inp):
    idx = len(tmp_inp) - 1
    max_num = 0
    # 숫자들을 조합하는 스택
    num_stack = []
    result = 0
    while idx != -2:
        token = ''
        # 공백을 만나면 num_stack 에 있는 모든 숫자를 다시 합쳐서 int 형으로 반환
        if tmp_inp[idx] == ' ' or idx == -1:
            while num_stack:
                token += num_stack.pop()
            token = int(token)
            # 만약 가장 큰 값을 만나면 갱신
            if max_num < token:
                max_num = token
            # 최대값과 token 의 차를 result 에 저장
            else:
                result += max_num - token
            idx -= 1
            continue
        num_stack.append(tmp_inp[idx])
        idx -= 1

    return result


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    tmp_input = input()
    reprint = search_max(tmp_input)
    print(f'#{tc} {reprint}')
