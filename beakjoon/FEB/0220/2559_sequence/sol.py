# import sys
# sys.stdin = open('input.txt', 'r')
# #########################################
#
# T = int(input())   # Test case 개수를 받아오는 코드
# for tc in range(1, T+1):
"""
며칠 동안의 온도의 합이 가장 큰 값을 알아보고자 한다.
10일간의 온도가 주어졌을 때, 모든 연속적인 이틀간의 온도합에서의 최대값
"""
# N: arr의 길이, K: 구간합 길이
N, K = map(int, input().split())
# arr: 온도가 들어있는 배열
arr = list(map(int, input().split()))
# 개초딩 선언: 아무튼 너보다 작음
high_temp = -float('inf')
"""
배열을 항상 갱신하기 보다 과거에서 현재로 넘어올때 한자리씩 바꾸기
일부러 처음 생성할 때 K개 구간을 다 설정하는게 아니라
for 문 진입하자마자 K개의 구간을 만들 수 있도록 설정
"""
prev_temp = sum(arr[:K-1])
for i in range(N-K+1):
    # prev_temp에서는 구간합의 첫번째 숫자를 제거한 상태에서 돌아온다.
    # 그렇기 때문에 다음 구간합에 사용할 숫자를 추가한다.
    prev_temp += arr[i+K-1]
    # 최대값 갱신
    if high_temp < prev_temp:
        high_temp = prev_temp
    # 구간합의 가장 앞에 있는 숫자를 제거 -> 다음 구간합을 계산하기 위함
    prev_temp -= arr[i]
print(high_temp)
