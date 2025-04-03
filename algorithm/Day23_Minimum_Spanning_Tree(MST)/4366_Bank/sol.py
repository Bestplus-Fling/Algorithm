import sys
sys.stdin = open("input.txt", "r")


def search(dif):
    for b in range(len_b):
        bk = 2 ** b
        case = dif - bk
        for t in range(len_t):
            tk = 3 ** t
            tki = case // tk
            if tki > 2: continue

            if case % tk == 0:
                return bk, case


T = int(input())
for tc in range(1, T+1):
    binary = input()
    ternary = input()

    len_b = len(binary)
    len_t = len(ternary)

    int_b, int_t = int(binary, 2), int(ternary, 3)
    dv = abs(int_b - int_t)
    bb, tt = search(dv)
    if int_b > int_t:
        ans_b = int_b - bb
        ans_t = int_t + tt
    else:
        ans_b = int_b + bb
        ans_t = int_t - tt
    print(f'#{tc}', ans_b)
