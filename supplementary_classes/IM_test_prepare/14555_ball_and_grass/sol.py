import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    field = input()
    ans_a = 0
    for i in range(len(field)):
        # 열린 괄호는 무조건 +1
        # 닫힌 괄호는 인접해있으면 pass, 아니면 +1
        if field[i] == '(':
            ans_a += 1
        elif field[i] == ')' and not(field[i-1] == '('):
            ans_a += 1
    print(f'#{tc}', ans_a)

