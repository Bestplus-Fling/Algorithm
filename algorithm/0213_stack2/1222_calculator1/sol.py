import sys
sys.stdin = open('input.txt', 'r')
#########################################


def in_post_fix(infix, lenth):
    postfix_logic = []

    for i in range(lenth):
        token = infix[i]
        if token.isnumeric():
            postfix_logic.append(int(token))

        if len(postfix_logic) == 2:
            val2 = postfix_logic.pop()
            val1 = postfix_logic.pop()
            temp = val1 + val2
            postfix_logic.append(temp)

    return postfix_logic[0]


T = 10 # int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    infix_len = int(input())
    infix_logic = input()

    print(f'#{tc} {in_post_fix(infix_logic, infix_len)}')
