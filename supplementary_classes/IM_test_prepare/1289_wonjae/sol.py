import sys

sys.stdin = open('input.txt', 'r')
#########################################

"""
메모리 bit중 하나를 골라 0인지 1인지 결정하면 해당 값이 메모리의 끝까지 덮어씌우는 것
원래의 상태가 주어질 때 초기화 상태 (모든 bit가 0) 에서 원래 상태로 돌아가는데 최소 몇번 고쳐야 하는가
현재 설정된 비트가 원래 비트가 일치 = 그대로 append, 아니면 바꿔서 append
"""

T = int(input())  # Test case 개수를 받아오는 코드
for tc in range(1, T + 1):
    bit = input()
    check_bit = 0
    ans = 0
    for num in bit:
        if int(num) != check_bit:
            check_bit = 1 - check_bit
            ans += 1

    print(f'#{tc}' ,ans)
