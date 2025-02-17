import sys
sys.stdin = open('input.txt', 'r')
#########################################


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    C_list = list(map(int, input().split()))
    max_cnt = []
    for i in range(N):
        cnt = 1
        for j in range(i, N-1):
            if C_list[j] < C_list[j + 1]:
                cnt += 1
            else:
                break
        max_cnt.append(cnt)
    print(f'#{tc} {max(max_cnt)}')
