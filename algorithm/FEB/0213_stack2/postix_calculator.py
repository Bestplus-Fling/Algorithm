def run_calculator(expr):
    stack = []
    tokens = expr.split()

    for token in tokens:
        # 피연산자는 삽입
        # 연산자면 스택에서 값 2개 pop 후 연산, 다시 삽입
        # for loop 끝나면 마지막 스택에 들어있는 값 꺼내서 출력
        if token.isnumeric():
            stack.append(int(token))

        else:
            num2 = stack.pop()
            num1 = stack.pop()

            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(num1 * num2)
            elif token == '/':
                stack.append(num1 / num2)
    return stack.pop()


posfix_expression = '3 2 5 * + 8 4 / -'
result = run_calculator(posfix_expression)
print(result)