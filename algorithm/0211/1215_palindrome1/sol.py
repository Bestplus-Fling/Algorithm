import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = 10 # int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    F = 8
    word_list = [input() for _ in range(F)]
    cir_list = list(zip(*word_list[::-1]))
    sum_val = 0
    for i in range(F):
        for j in range(F):
            cnt = 0
            if 0 <= j+N-1 < F:
                temp1 = word_list[i][j:j+N:]
                temp2 = cir_list[i][j:j+N]
                if int(temp1[::] == temp1[::-1]):
                    cnt += 1
                if int(temp2[::] == temp2[::-1]):
                    cnt += 1
            sum_val += cnt
    print(f'#{tc} {sum_val}')