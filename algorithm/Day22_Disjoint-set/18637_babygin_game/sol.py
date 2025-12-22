import sys
sys.stdin = open("input.txt", "r")


def check(card):
    for k in range(10):
        if card[k] >= 3:    # triplet
            return True
        if 1 <= k < 9:  # run
            if card[k-1] and card[k] and card[k+1]:
                return True


def play():
    Flag = False
    for i in range(0, N, 2):
        if i == 6:
            Flag = True
        a[card_list[i]] += 1
        if Flag and check(a):
            return 1
        b[card_list[i + 1]] += 1
        if Flag and check(b):
            return 2
    return 0


T = int(input())
N = 12
for tc in range(1, T+1):
    card_list = list(map(int, input().split()))
    a, b = [0] * 10, [0] * 10
    print(f'#{tc}', play())

