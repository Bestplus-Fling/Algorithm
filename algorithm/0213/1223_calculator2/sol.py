import sys
sys.stdin = open('input.txt', 'r')
#########################################


def in_post_fix(fix_l):
    mul_stack, add_stack = [], []

    for i in range(list_len-1, -1, -1):
        token = fix_l[i]

        if operator == '*' and token.isnumeric():
            mul_stack.append(int(token))
        if operator == '+':
            temp = 1
            while mul_stack:
                val = mul_stack.pop()
                temp *= val
            add_stack.append(temp)
        if token in ['+', '*']:
            operator = token
        # if token.isnumeric():
        #     if mul_stack:
        #         if operator == '*':
        #             temp = mul_stack.pop()
        #             temp = int(token) * temp
        #             mul_stack.append(temp)
        #             continue
        #         elif operator == '+':
        #             val = mul_stack.pop()
        #             val = int(token) + val
        #             # print(temp)
        #             mul_stack.append(temp)
        #             continue
        #         else:
        #             continue
        #     else:
        #         mul_stack.append(int(token))
        #         continue
        # else:
        #     operator = token
        #     if not mul_stack and operator == '+':
        #         mul_stack.append(temp)
        #     continue
    return mul_stack.pop()


T = 10 # int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    list_len = int(input())
    infix_list = input()
    print(in_post_fix(infix_list))
    # print(f'#{tc} {in_post_fix(list_len, infix_list)}')
    break
