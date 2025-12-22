import sys
sys.stdin = open('input.txt', 'r')
#########################################


def power_set(idx=0, f_sum=0, w_sum=0):
    global min_work
    # 종료 조건
    # 2. 최소 노동력(현재 저장된 노동력) 보다 클때 종료
    if min_work < w_sum:
        return
    # 1. idx == N 종료
    # 과일의 합이 Xkg 이상이여야 한다.
    if idx >= N:
        if f_sum >= X:
            min_work = min(min_work, w_sum)
        return
    # 선택을 했을 때
    power_set(idx+1, f_sum + fruits[idx], w_sum + works[idx])
    # 선택을 하지 않았을 때
    power_set(idx+1, f_sum, w_sum)
    pass


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, X = map(int, input().split())
    fruits = list(map(int, input().split()))
    works = list(map(int, input().split()))
    min_work = float('inf')
    # 최소 노동력을 만족할 때 min_work를 갱신
    power_set()
    print(f'#{tc}', min_work if min_work != float('inf') else -1)
