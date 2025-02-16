import sys
sys.stdin = open('input.txt', 'r')
#########################################

"""
N개의 전등(1 ~ N번)
i번 스위치를 조작하면
    i ~ N번까지의 전등을 켜짐/꺼짐이 반대가 된다.

모든 전등의 현재 상태와
스위치 조작 후 상태가 주어지면
최소 몇 개의 스위치를 조작해야 하는지
[입력]
첫 줄에 테스트케이스 개수 T, 다음 줄 부터 케이스 별로 스위치 개수 N, 
다음 두 줄에 조작 전 스위치 상태 Ai와 조작 후 상태 Bi가 각각 N개씩 주어진다.
(1<=T<=10, 1<=N<=100)

[출력]
#과 케이스번호, 빈칸으로 구분된 답을 출력한다.
"""
T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    # 인덱스가 같이 이동하면서 일치하면 pass, 불일치하면 조작하면서 반전하고 cnt += 1
    N = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    for i in range()
    pass