import sys
sys.stdin = open('input.txt', 'r')
#########################################

"""
호석이 씹새끼
N의 배수인 양을 센다 kN번 양
이전에 셌던 번호들의 각 자리수에서 0에서 9까지의
모든 숫자를 보는 것은 최소 몇 번 양을 센 시점일까
"""

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    mul = 1
    nums = []
    while True:
        temp = str(N*mul)
        for num in temp:
            if nums.count(num) == 0:
                nums.append(num)
        if len(nums) == 10:
            break
        mul += 1
    print(f'#{tc}', N*mul)