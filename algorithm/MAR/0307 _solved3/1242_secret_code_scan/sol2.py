import sys
sys.stdin = open('input.txt', 'r')
#########################################
"""
1. 입력을 받는다.
2. strip으로 0을 제거한 상태에서 16진수 한자리씩 2진수로 변환해서 4자리를 차곡차곡 쌓는다.
"""


def hex_bin(hb, index):
    for num in hb:
        temp = bin(int(num, 16))[2::]
        temp = temp.zfill(4)
        print(temp)
        save_bin[index] += [temp]
    pass


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().strip('0') for _ in range(N)]
    save_bin = [[''] for _ in range(M)]
    idx = 0
    for _hex in set(arr):
        if _hex:
            print(_hex)
            hex_bin(_hex, idx)
            idx += 1
    bin_list = []
    while idx != 0:
        idx -= 1
        temp1 = list(''.join(save_bin[idx]))
        while temp1[-1] == '0':
            temp1.pop()
        temp1 = ''.join(temp1)
        temp1 = temp1.zfill()
        bin_list.append(temp1)
    print(bin_list[0], len(bin_list[0]))

    break