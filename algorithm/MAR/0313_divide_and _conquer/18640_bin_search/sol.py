import sys
sys.stdin = open('input.txt', 'r')
#####################################
"""
정렬한 상태로 리스트 A 에 저장
리스트 B 에 저장된 M개의 정수에 대해 A에 들어 있는 수인지 이진 탐색을 통해 한다.
전체 탐색 구간의 시작과 끝 인덱스 = l, r
중심원소의 인덱스 m = (l+r)//2
이진탐색의 왼쪽 구간은 l 부터, m-1
이진탐색의 오른쪽 구간은 m+1부터 r

이때 B에 속한 어떤 수가 A에 들어있으면서,
동시에 탐색 과정에서 양쪽 구간을 번갈아 선택하게 되는 숫자의 개수를 확인

이때 m에 찾는 원소가 있는 경우 방향을 따지지 않는다
"""


def div():
    l, r = 0, N-1
    c = 0
    while l <= r:
        m = (l+r) // 2
        if arr[m] == b:
            return 1
        if arr[m] > b:
            r = m - 1
            if c == -1:
                return 0
            c = -1
        else:
            l = m + 1
            if c == 1:
                return 0
            c = +1
    return 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    B = list((map(int, input().split())))
    ans_a = 0
    arr.sort()
    for b in B:
        if div():
            ans_a += 1
    print(f'#{tc}', ans_a)

"""
1. B에 속한 어떤 수가 A에 들어있으면서
2. 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수를 확인

"""