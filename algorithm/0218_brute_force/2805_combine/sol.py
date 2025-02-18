import sys
sys.stdin = open('input.txt', 'r')
#########################################

'''
농장의 크기(N)은 항상 홀수
수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태만 가능
'''
T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
