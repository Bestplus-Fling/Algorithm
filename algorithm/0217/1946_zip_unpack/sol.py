import sys
sys.stdin = open('input.txt', 'r')
#########################################
# from collections import deque


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    # 알파벳과 숫자 쌍의 개수를 입력
    N = int(input())
    # 알파벳과 숫자쌍을 튜플 형태로 저장
    zip_list = [tuple(input().split()) for _ in range(N)]
    # 최종 출력되는 문자열을 저장
    char_list = []
    # 임시로 문자열을 합치고, 문자열이 10이 되면 char_list 에 값을 넘긴다.
    temp_list = []
    for char, len_char in zip_list:
        for _ in range(int(len_char)):
            # 알파벳을 숫자만큼 저장하다가
            temp_list.append(char)
            # temp_list 가 10이 되면 char_list 에 저장하고
            if len(temp_list) == 10:
                char_list.append(temp_list)
                # 현재까지 temp_list 의 정보를 삭제한다.
                temp_list = []
    # for 문 종료 후 temp_list 가 남아있기 때문에 마지막으로 한번 더 저장
    char_list.append(temp_list)
    # 최종 출력 형태를 만족할 수 있도록 for 문으로 출력
    print(f'#{tc}')
    for x in range(len(char_list)):
        print(''.join(char_list[x]))
