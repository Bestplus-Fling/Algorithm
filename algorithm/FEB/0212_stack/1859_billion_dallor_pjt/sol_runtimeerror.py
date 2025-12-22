import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    val_list = list(map(int, input().split()))
    tax_coming = 0
    for i in range(N):
        temp = 0
        if not(i+1 == N):
            for j in range(i+1, N):
                if val_list[i] < val_list[j] and temp < val_list[j] - val_list[i]:
                    temp = val_list[j] - val_list[i]
        if temp:
            tax_coming += temp
    print(f'#{tc} {tax_coming}')
