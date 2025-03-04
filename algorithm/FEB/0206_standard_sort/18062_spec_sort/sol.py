import sys
sys.stdin = open('input.txt', 'r')
#########################################

'''
N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 
큰 수와 작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
 

10 1 9 2 8 3 7 4 6 5
 

주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오
'''

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 입력받은 리스트를 정렬(가장 큰수와 가장 작은 수, 그다음 큰수 작은수 순서로 정렬하기 위함)
    # 버블 정렬
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(f'#{tc}', end=' ')
    for i in range(5):
        print(arr[-i-1], arr[i], end=' ')

    print()



