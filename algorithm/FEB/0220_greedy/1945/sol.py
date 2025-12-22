import sys
sys.stdin = open('input.txt', 'r')
#########################################

_list = [11, 7, 5, 3, 2]
T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    # 소인수 분해한 각 요소의 지수를 저장하는 변수 선언
    result = []
    for num in _list:
        # 각 소수들의 지수를 count
        temp = 0
        while True:
            # 소수로 온전히 나눌 수 있지 않을 때
            if N % (num ** (temp+1)):
                # 현재까지 count한 지수를 저장
                result.append(temp)
                # 소수로 나눈 몫을 갱신해서 다음 소수로 계산
                N = N // (num ** temp)
                break
            temp += 1
    print(f'#{tc}', *reversed(result))
