import sys
sys.stdin = open('input.txt', 'r')
#########################################
# from collections import deque


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    zip_list = [tuple(input().split()) for _ in range(N)]
    char_list = []
    temp_list = []
    for char, len_char in zip_list:
        for _ in range(int(len_char)):
            temp_list.append(char)
            if len(temp_list) == 10:
                char_list.append(temp_list)
                temp_list = []
    char_list.append(temp_list)
    print(f'#{tc}')
    for x in range(len(char_list)):
        print(''.join(char_list[x]))
