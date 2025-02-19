import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = float(input())
    for i in range(1, (2**13)):
        check_bin = (bin(int(i)))[:1:-1]
        temp = 0
        for j in range(len(check_bin)):
            temp += (2 ** (-(j+1))) * int(check_bin[j])
        # print(temp)
        if temp == N:
            break
    print(f'#{tc}', check_bin if temp == N else 'overflow')
