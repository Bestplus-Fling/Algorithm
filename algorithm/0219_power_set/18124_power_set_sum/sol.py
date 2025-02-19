import sys
sys.stdin = open('input.txt', 'r')
#########################################
"""
10개의 정수를 입력 받아 부분 집합의 합이 0이 되는 것이 존재하는지를 계산
만약 합이 존재하면 1, 그렇지 않으면 0
"""


def power_set(idx, num_sum, cnt):
    global count
    if cnt != 0 and num_sum == 0:
        count = True
    if idx == 10:
        return

    power_set(idx + 1, num_sum + arr[idx], cnt + 1)
    power_set(idx + 1, num_sum, cnt)




T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    count = False
    power_set(0, 0, 0)
    print(f'#{tc} {1 if count else 0}')
