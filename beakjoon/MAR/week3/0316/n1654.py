import sys
sys.stdin = open('input/1654.txt', 'r')
#########################################

K, N = map(int, input().split())
# K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력
lan_list = [int(input()) for _ in range(K)]
# 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력
length = sum(lan_list) // N
print(length)