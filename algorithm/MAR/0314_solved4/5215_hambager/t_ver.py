import sys
sys.stdin = open('input.txt', 'r')
#####################################


def dfs(depth, total_socre, total_calorie):
    global result

    if total_calorie > limit_k:
        return

    if depth == topping_cnt:
        result = max(result, total_socre)
        return

    dfs(depth+1, total_socre, total_calorie)

    dfs(depth+1, total_socre + toppings[depth][0], total_calorie + toppings[depth][1])


T = int(input())
for tc in range(1, T+1):
    topping_cnt, limit_k = map(int, input().split())
    toppings = [tuple(map(int, input().split())) for _ in range(topping_cnt)]

    result = 0
    dfs(0, 0, 0)

    print(f'#{tc}', result)