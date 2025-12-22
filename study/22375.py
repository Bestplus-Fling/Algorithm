import sys
sys.stdin = open('22375.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    default = list(input().split())
    change = list(input().split())
    ans_a = 0
    for i in range(N):
        # 만약에 check_bit랑 default가 다르면, 전체 순회, 반전
        if default[i] == change[i]:
            continue
        ans_a += 1
        for j in range(i, N):
            default[j] = '1' if default[j] == '0' else '0'
    print(f'#{tc}', ans_a)
