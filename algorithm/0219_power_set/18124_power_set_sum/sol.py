import sys
sys.stdin = open('input.txt', 'r')
#########################################
"""
10개의 정수를 입력 받아 부분 집합의 합이 0이 되는 것이 존재하는지를 계산
만약 합이 존재하면 1, 그렇지 않으면 0
"""


def power_set(idx, num_sum, cnt):
    global count
    # idx(depth)가 배열 길이(문제에서 10개의 정수만 준다고 했음)에 도달하면 종료
    if idx == 10:
        # 공집합을 제외한 나머지 집합들의 합이 0일 경우 count를 True로 변경
        if cnt != 0 and num_sum == 0:
            count = True
        return
    # 현재 arr[idx]를 선택했을 때의 경우를 탐색
    power_set(idx + 1, num_sum + arr[idx], cnt + 1)
    # 현재 arr[idx]를 선택하지 않았을 때의 경우를 탐색
    power_set(idx + 1, num_sum, cnt)




T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    count = False
    power_set(0, 0, 0)
    print(f'#{tc} {1 if count else 0}')
