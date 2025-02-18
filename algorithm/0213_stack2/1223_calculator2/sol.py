import sys
sys.stdin = open('input.txt', 'r')
#########################################


def in_post_fix():
    op_dict = {'+': 1, '*': 2}
    stack, postfix = [], []
    for char in infix_list:
        # 숫자는 바로 출력
        if char.isnumeric():
            postfix.append(int(char))
        # 연산자일 때
        else:
            # 스택에 값이 있고 스택에 있는 연산자가 현재 연산자보다 우선순위가 높다면
            # 우선순위가 같은 연산자가 나올때까지 pop한다음 자기 자신을 스택에 push
            while stack and op_dict[stack[-1]] >= op_dict[char]:
                postfix.append(stack.pop())
            stack.append(char)
    # for문 종료 후 스택에 남은 연산자를 출력
    while stack:
        postfix.append(stack.pop())

    # 후위표기식으로 변경해서 계산
    return calculate_posfix(postfix)


def calculate_posfix(postfix):
    stack = []

    for token in postfix:
        # 더하기
        if token == '+':
            val2 = stack.pop()
            val1 = stack.pop()
            stack.append(val1 + val2)
        # 곱하기
        elif token == '*':
            val2 = stack.pop()
            val1 = stack.pop()
            stack.append(val1 * val2)
        # 숫자는 stack에 push
        else:
            stack.append(token)
    # 마지막 연산된 숫자를 pop해서 return
    return stack.pop()


T = 10  # int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    list_len = int(input())
    infix_list = input()
    print(f'#{tc} {in_post_fix()}')
