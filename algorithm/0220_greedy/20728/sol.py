import sys
sys.stdin = open('input.txt', 'r')
#########################################
"""
첫 번째 예제: 주머니 2개를 고르는 방법은 
{1, 2}, {1, 3}, {2, 3}이 있다. 각각의 (최대) – (최소) 값은 1, 2, 1이다. 이 중 최솟값은 1이다.

두 번째 예제: 무조건 모든 주머니를 나눠줘야 한다.
"""
"""
사탕이 담긴 N개의 주머니
이 중 i 번째 주머니에는 사탕이 ai개 들어있다.
이 주머니 중 정확히 K개를 선택하여 나누어 준다
공정성을 위해 나눠 준 주머니 가운데 사탕의 개수가 가장 많은 것과 가장 적은 것의 사탕 개수 차이를
최소화한다
"""

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 사탕의 개수를 오름차순으로 정렬
    arr = sorted(list(map(int, input().split())))
    result_min = float('inf')
    # 주머니를 다 줘야 하는 경우 최대 최소만 구해서 뺀다.
    if N == K:
        result_min = arr[K-1] - arr[0]
    # 아닐 경우 조합에서 최대 최소의 차를 확인
    else:
        for i in range(N-K+1):
            # K개의 사탕 주머니를 가지는 변수 선언
            temp = arr[i:i+K]
            # 사탕 주머니의 최대값과 최소값의 차가 최소값보다 작을 때 갱신
            ot = temp[K - 1] - temp[0]
            if ot > result_min:
                continue
            result_min = temp[K - 1] - temp[0]
    print(f'#{tc}', result_min)

