import sys
sys.stdin = open('input.txt', 'r')
#########################################


def search(work):
    dic = {')': '(', ']': '[', '}': '{'}
    stc = []
    for txt in work:
        # 열린 괄호(value)일 경우
        if txt in dic.values():
            # 스택에 저장
            stc.append(txt)
            continue
        # 닫힌 괄호(key)일 경우
        if txt in dic.keys():
            # 스택 top과 현재 key의 value가 일치할 때 제거
            if dic[txt] == stc[-1]:
                stc.pop()
            # 쌍이 안맞으면 0을 반환
            else:
                return 0
    if not stc:
        return 1
    else:
        return 0


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    word = input()
    print(f'#{tc} {search(word)}')
