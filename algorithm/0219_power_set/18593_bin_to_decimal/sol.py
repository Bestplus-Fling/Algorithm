import sys
sys.stdin = open('input.txt', 'r')
#########################################

from pprint import pprint

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    # 2진수로 이루어진 행의 개수를 입력
    N = int(input())
    # 2진수로 이루어진 2차원 리스트를 한 줄로 입력
    arr = []
    for _ in range(N):
        arr.extend(list(map(int, input().strip())))
    # arr 에 있는 2진수 배열을 7자리씩 끊어서 저장
    matrix, temp = [], []
    for i in range(N * 10):
        temp.append(arr[i])
        if len(temp) == 7:
            matrix.append(temp)
            temp = []
    # 7자리로 끊은 2진수를 2 ** j 위치를 확인해서 모든 값을 더한 후 result 에 저장
    result = []
    for _list in matrix:
        temp = 0
        for j in range(7):
            temp += (2 ** j) * _list[-(j+1)]
        result.append(temp)
    print(f"#{tc}", *result)
