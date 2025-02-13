import
def infix_to(expression):
    op_dict = {'+':1, '-':1, '*':2, '/':2, '(':0}
    stack = []
    postfix = []

    for ch in expression:
        # 숫자는 바로 추가
        if ch.isnumeric():
            postfix.append(ch)
        # 연산자들은 stack에 push
        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            top_token = stack.pop()
            while top_token != '(':
                postfix.append(top_token)
                top_token = stack.pop()
        else:
            while stack and op_dict[stack[-1]] >= op_dict[ch]:
                postfix.append(stack.pop())
            stack.append(ch)

        while stack:
            postfix.append(stack.pop())

        return ' '.join(postfix)


