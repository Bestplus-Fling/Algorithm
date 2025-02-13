import sys
sys.stdin = open('input.txt', 'r')
#########################################

def multiplex(bot, end_num):
    if end_num == 0:
        return 1
    else:
        return bot * multiplex(bot, end_num - 1)

T = 10 # int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    bot, end_num = map(int, input().split())
    print(f'#{N} {multiplex(bot, end_num)}')
    pass
