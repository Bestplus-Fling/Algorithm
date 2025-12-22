import sys
sys.stdin = open("input.txt", "r")


def search():
    # 1: 2진수 합 차 두개 경우(binary[b]가 0인지 1인지에 따라서 값을 변경)
    for b in range(len_b):
        bk = 2**b
        if binary[-1-b] == '0':
            check_b = int_b + bk
        else:
            check_b = int_b - bk

        for t in range(len_t):          # 2: 3진수 합 차(ternary[t]가
            tk = 3**t
            if ternary[-1-t] == '0':    # 0일 경우 (+1, +2)
                check_t1 = int_t + tk
                check_t2 = int_t + tk * 2
            elif ternary[-1-t] == '1':  # 1일 경우(-1, +1)
                check_t1 = int_t - tk
                check_t2 = int_t + tk
            else:                       # 2일 경우(-1, -2)
                check_t1 = int_t - tk
                check_t2 = int_t - tk * 2
            if check_b == check_t1 or check_b == check_t2:
                return check_b


T = int(input())
for tc in range(1, T+1):
    binary = input()
    ternary = input()

    len_b = len(binary)
    len_t = len(ternary)

    int_b, int_t = int(binary, 2), int(ternary, 3)

    print(f'#{tc}', search())
