import sys
sys.stdin = open('9205.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    away = []
    for i in range(N+2):
        x, y = map(int, input().split())
        away.append([x, y])
    print(away)
