import sys
sys.stdin = open('input.txt', 'r')
#########################################


def search(work):
    dic = {')': '(', ']': '[', '}': '{'}
    stc = []
    for txt in work:
        if txt in dic.values():
            stc.append(txt)
            continue
        if txt in dic.keys():
            if txt == stc.pop():
                return 0
    if not stc:
        return 1
    else:
        return 0


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    word = input()
    print(f'#{tc} {search(word)}')
