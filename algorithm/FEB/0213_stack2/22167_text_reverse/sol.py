import sys
sys.stdin = open('input.txt', 'r')
#########################################


def reverse_text(txt, n = -1):
    if n == -len(txt):
        return txt[0]
    return txt[n] + reverse_text(txt, n-1)


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    text = input()
    print(reverse_text(text))
