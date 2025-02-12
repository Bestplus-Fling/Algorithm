def check_match(expression):
    stack = []
    matching_dict = {')': '(', '}': '{', ']': '['}

    for char in expression:
        # 열린 괄호를 만나면 => 스택에 적재
        if char in matching_dict.values():
            stack.append(char)

        # 닫힌 괄호흘 만나면 짝을 확인
        elif char in matching_dict.keys():
            if not stack: # 스택이 비어있다면?
                return False
            # if len(stack) == 0:
            # 스택에 가장 마지막 원소의 열린 괄호와 닫힌 괄호의 짝이 다르면
            if stack[-1] != matching_dict[char]:
                return False
            stack.pop()

        # 올바른 짝이 입력됐다면 스택이 공란이기 때문에 True, 남아있으면 False
    return not stack

examples = ["(a(b)", "a(b)c", "a{b(c[d]e}f)"]
for ex in examples:
    if check_match(ex):
        print(f"{ex} 는 올바른 괄호")
    else:
        print(f"{ex} 는 올바르지 않은 괄호")